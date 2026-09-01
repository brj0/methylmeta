from __future__ import annotations

import ast
import importlib.util
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

from methylmeta.loader import load_dataset_module
from methylmeta.merger import MetadataMerger
from methylmeta.schema import describe_fields
from methylmeta.spec import CONFIG_SPEC
from methylmeta.vocab import search_tumor_types

DEFAULT_AGENT_MODEL = "google:gemini-2.5-pro"


class AgentResult(BaseModel):
    """Final structured result returned by the metadata agent."""

    dataset_id: str
    success: bool
    config_path: str | None = None
    summary: str


@dataclass
class AgentDeps:
    """Runtime state exposed to the metadata agent's tools."""

    merger: MetadataMerger
    dataset_id: str
    config_dir: Path
    dataset_dir: Path
    allow_write: bool
    force: bool


def _config_path(deps: AgentDeps) -> Path:
    return deps.config_dir / f"{deps.dataset_id}.py"


def _clean_code(source: str) -> str:
    """Remove a Markdown code fence if the model returned one."""
    source = source.strip()
    match = re.fullmatch(r"```(?:python|py)?\s*(.*?)```", source, re.DOTALL)
    return match.group(1).strip() if match else source


def _validate_config_source(source: str) -> str:
    """Validate generated config source before it touches the filesystem."""
    source = _clean_code(source)
    if not source:
        raise ValueError("Generated config is empty.")

    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise ValueError(
            f"Generated config has invalid Python: {exc}"
        ) from exc

    allowed = (ast.FunctionDef, ast.AsyncFunctionDef)
    for node in tree.body:
        if not isinstance(node, allowed):
            raise ValueError(
                "Config may contain only top-level function definitions; "
                f"found {type(node).__name__}."
            )

    function_names = {
        node.name for node in tree.body if isinstance(node, allowed)
    }
    if "dataset_id" not in function_names:
        raise ValueError("Config must define dataset_id(row).")

    if any(
        isinstance(node, (ast.Import, ast.ImportFrom))
        for node in ast.walk(tree)
    ):
        raise ValueError(
            "Imports are not allowed in generated dataset configs."
        )

    return source + "\n"


def create_agent(
    model: str = DEFAULT_AGENT_MODEL,
) -> Agent[AgentDeps, AgentResult]:
    """Create the Pydantic AI metadata-config agent."""
    if Agent is None:
        raise RuntimeError(
            "The AI agent dependencies are not installed. Run "
            '`uv add "pydantic-ai-slim[google]"`.'
        )

    agent: Agent[AgentDeps, AgentResult] = Agent(
        model=model,
        deps_type=AgentDeps,
        output_type=AgentResult,
        retries=2,
        instructions=(
            "You are the methylmeta dataset metadata agent. Your job is to "
            "create or repair exactly one configs/datasets/<dataset_id>.py "
            "file so that the real dataset passes methylmeta.test().\n\n"
            "WORKFLOW (follow this order):\n"
            "1. Call get_profile first. Never guess raw column names or "
            "values.\n"
            "2. If a config already exists, call read_config and "
            "test_config.\n"
            "3. Use search_tumor_types for diagnosis text when choosing a "
            "methylation_class. Never invent a WHO acronym.\n"
            "4. Write the smallest clear config possible. Prefer direct "
            "passthrough, exact mappings, constants, and simple if/elif "
            "logic.\n"
            "5. Call test_config after every write. Fix all failures you "
            "can.\n"
            "6. Stop only when test_config reports success, or when a "
            "remaining "
            "problem genuinely requires human judgement.\n\n"
            "IMPORTANT: Every raw metadata row must be harmonized. Do not add "
            "row filtering. Do not use regex. Do not create new WHO acronyms. "
            "Do not change methylmeta source code or tumor_types.yaml.\n\n"
            "The config contract is:\n\n"
            + CONFIG_SPEC
            + "\n\nCanonical fields:\n"
            + describe_fields()
        ),
    )

    @agent.tool
    def get_profile(ctx: RunContext[AgentDeps]) -> str:
        """Inspect real columns and values before writing config."""
        profile = ctx.deps.merger.profile(ctx.deps.dataset_id)
        return profile.summary()

    @agent.tool
    def read_config(ctx: RunContext[AgentDeps]) -> str:
        """Read the current dataset config, if one exists."""
        path = _config_path(ctx.deps)
        if not path.exists():
            return f"No config exists yet: {path}"
        return path.read_text(encoding="utf-8")

    @agent.tool
    def search_tumor_vocabulary(query: str) -> str:
        """Search WHO tumor vocabulary for methylation class candidates."""
        results = search_tumor_types(query, limit=10)
        if not results:
            return "No WHO vocabulary matches found."
        return "\n".join(str(result) for result in results)

    @agent.tool
    def test_config(ctx: RunContext[AgentDeps]) -> str:
        """Run the real harmonizer test and return all grouped failures."""
        try:
            report = ctx.deps.merger.test(ctx.deps.dataset_id)
        except Exception as exc:  # noqa: BLE001
            return f"CONFIG TEST COULD NOT RUN: {type(exc).__name__}: {exc}"
        return report.summary(max_examples=3)

    @agent.tool
    def write_config(ctx: RunContext[AgentDeps], source: str) -> str:
        """Validate and write the selected dataset config only."""
        if not ctx.deps.allow_write:
            return (
                "WRITE DISABLED. You may inspect and test, but do not "
                "attempt another write."
            )

        path = _config_path(ctx.deps)
        if path.exists() and not ctx.deps.force:
            return (
                f"WRITE REFUSED: {path} already exists and --force was "
                "not given. "
                "Read and test the existing config instead."
            )

        try:
            source = _validate_config_source(source)
        except ValueError as exc:
            return f"WRITE REFUSED: {exc}"

        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            backup = path.with_suffix(path.suffix + ".bak")
            shutil.copy2(path, backup)

        path.write_text(source, encoding="utf-8")

        try:
            module = load_dataset_module(path)
            actual_id = module.dataset_id(None)
        except Exception as exc:  # noqa: BLE001
            path.unlink(missing_ok=True)
            return (
                f"WRITE REFUSED: generated config could not be loaded: {exc}"
            )

        if actual_id != ctx.deps.dataset_id:
            path.unlink(missing_ok=True)
            return (
                "WRITE REFUSED: dataset_id(None) returned "
                f"{actual_id!r}, expected {ctx.deps.dataset_id!r}."
            )

        # The merger caches its config index, so invalidate it after a write.
        ctx.deps.merger._id_to_config = None
        return f"WROTE {path}. Now call test_config."

    return agent


def run_agent(
    dataset_id: str,
    *,
    config_dir: str | Path,
    dataset_dir: str | Path,
    model: str = DEFAULT_AGENT_MODEL,
    prompt: str | None = None,
    allow_write: bool = True,
    force: bool = False,
) -> AgentResult:
    """Run the metadata agent for one dataset."""
    try:
        from pydantic_ai import UsageLimits
    except ImportError as exc:
        raise RuntimeError(
            "The AI agent dependencies are not installed. Run "
            '`uv add "pydantic-ai-slim[google]"`.'
        ) from exc

    config_dir = Path(config_dir).expanduser().resolve()
    dataset_dir = Path(dataset_dir).expanduser().resolve()
    dataset_path = dataset_dir / dataset_id

    if not dataset_path.is_dir():
        raise ValueError(f"Dataset directory does not exist: {dataset_path}")

    if not os.environ.get("GOOGLE_API_KEY"):
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Create a free Gemini API key in "
            "Google AI Studio and export it before running the agent."
        )

    merger = MetadataMerger(config_dir=config_dir, dataset_dir=dataset_dir)
    deps = AgentDeps(
        merger=merger,
        dataset_id=dataset_id,
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        allow_write=allow_write,
        force=force,
    )

    agent = create_agent(model)
    user_prompt = prompt or (
        f"Create or repair the metadata config for dataset {dataset_id}. "
        "Use the available tools and finish with a passing test if possible."
    )

    result = agent.run_sync(
        user_prompt,
        deps=deps,
        usage_limits=UsageLimits(request_limit=12, tool_calls_limit=30),
    )

    path = _config_path(deps)
    actual_success = False
    test_summary = ""
    if path.exists():
        try:
            report = merger.test(dataset_id)
            actual_success = report.success
            test_summary = report.summary(max_examples=3)
        except Exception as exc:  # noqa: BLE001 - surface the final failure
            test_summary = (
                f"Final test could not run: {type(exc).__name__}: {exc}"
            )

    summary = result.output.summary
    if test_summary:
        summary = f"{summary}\n\nFinal test:\n{test_summary}"

    return AgentResult(
        dataset_id=dataset_id,
        success=actual_success,
        config_path=str(path) if path.exists() else None,
        summary=summary,
    )
