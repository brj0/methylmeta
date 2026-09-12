from __future__ import annotations

import ast
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from mepylome.dtypes.beads import idat_basepaths
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext, UsageLimits
from pydantic_ai.usage import RunUsage

from methylmeta.loader import load_dataset_module
from methylmeta.merger import MetadataMerger
from methylmeta.schema import describe_fields
from methylmeta.spec import CONFIG_SPEC
from methylmeta.study_info import fetch_study_description
from methylmeta.vocab import search_tumor_types

_MAX_IDAT_BASENAMES_SHOWN = 15

_AGENT_WORKFLOW = """\
You are a metadata harmonizer agent for Illumina methylation microarray
datasets. Your sole task is to create or repair exactly one
`configs/datasets/<dataset_id>.py` configuration file. The configuration must
correctly harmonize the real dataset and pass `methylmeta.test()`.

WORKFLOW (follow this order):
1. Call get_profile first. Never guess raw column names or values.
2. Call list_idat_basenames. sample_id and methylation_class are by far the
   most important fields to get right - methylation_class is the primary
   classification target, and sample_id is the basename of the IDAT file pair:
   each sample has two raw files on disk, e.g. '<basename>_Grn.idat' and
   '<basename>_Red.idat' (or the same with a '.gz' suffix if gzipped), and
   sample_id must equal that shared '<basename>' exactly, with the
   _Grn/_Red.idat(.gz) part removed. Downstream code looks up each sample's raw
   IDAT file by matching sample_id exactly against this basename on disk,
   silently (no error) producing a missing array_type if it doesn't match.
   Prefer, in this order:
     (a) the exact IDAT basename shown by list_idat_basenames if you can find a
         raw column containing it (Sentrix-style, e.g. '201904410008_R06C01',
         or GEO-style 'GSM3519721_202915410036_R06C01', or TCGA-style
         '604e65e3-1510-49c0-8532-6dd5cd321779_noid');
     (b) any other raw column that is one of those exact basenames
         (list_idat_basenames tells you what to look for);
     (c) only if no such column exists (e.g. ArrayExpress datasets often give
         samples arbitrary author-assigned names with no Sentrix ID anywhere in
         the metadata) fall back to the best available row identifier.
     (d) if a raw column instead contains the full IDAT filename, e.g.
         '<basename>_Grn.idat.gz', strip the trailing _Grn/_Red.idat(.gz) part
         (plain string slicing, not regex) to get sample_id.
   Never prefer a generic row counter or author label (e.g. 'REFERENCE_SAMPLE
   1') over an actual IDAT basename that's present in another column.
3. Call get_study_description for context on the study's tumor type and design
   (title/summary from GEO or ArrayExpress). Raw columns often use
   abbreviations, cohort-specific codes, or bare numbers that only make sense
   once you know what the study actually is - use this as context, not as a
   substitute for the real columns.
4. Call list_configs to see what other datasets have been configured. Existing
   configs are manually validated examples of project conventions - call
   read_config(dataset_id=...) on one or two that look similar (same source
   archive or tumor type) to see them as templates, but never assume their raw
   column names or mappings apply to the current dataset - always confirm with
   get_profile. Read a few at most, not every config in the list.
5. If a config already exists for this dataset, call read_config (with no
   dataset_id, to read your own) and test_config before changing anything.
6. Use search_tumor_vocabulary for diagnosis text when choosing a
   methylation_class. Never invent a WHO acronym.
7. Write the smallest clear config possible. Prefer direct passthrough, exact
   mappings, constants, and simple if/elif logic.
8. Call test_config after every write. Fix all failures you can.
9. Stop only when test_config reports success, or when a remaining problem
   genuinely requires human judgement.

IMPORTANT: Every raw metadata row must be harmonized. Some raw metadata values
may be incorrect, inconsistent, malformed, or otherwise invalid. Do not filter,
skip, or drop rows because of invalid metadata; harmonize every row as far as
possible. Rows may be removed later by downstream validation or quality-control
steps. Do not add row filtering. Do not use regex. Do not create new WHO
acronyms. Do not change methylmeta source code or tumor_types.yaml.

When returning Python code, follow PEP 8 formatting and keep lines to a maximum
of 79 characters.

The config contract is:

{config_spec}

Canonical fields:
{fields}
"""


class AgentResult(BaseModel):
    """Final structured result returned by the metadata agent."""

    dataset_id: str
    success: bool
    config_path: str | None = None
    summary: str
    usage: RunUsage


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

    allowed = ast.FunctionDef
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

    return source + "\n"


def create_agent(
    model: str,
) -> Agent[AgentDeps, AgentResult]:
    """Create the Pydantic AI metadata-config agent."""
    agent: Agent[AgentDeps, AgentResult] = Agent(
        model=model,
        deps_type=AgentDeps,
        output_type=AgentResult,
        retries=2,
        instructions=_AGENT_WORKFLOW.format(
            config_spec=CONFIG_SPEC,
            fields=describe_fields(),
        ),
    )

    @agent.tool
    def get_profile(ctx: RunContext[AgentDeps]) -> str:
        """Inspect real columns and values before writing config."""
        profile = ctx.deps.merger.profile(ctx.deps.dataset_id)
        return profile.summary()

    @agent.tool
    def list_idat_basenames(ctx: RunContext[AgentDeps]) -> str:
        """List IDAT basenames found in this dataset's own directory.

        Each returned name is the shared prefix of an IDAT file pair
        (e.g. '<basename>_Grn.idat' / '<basename>_Red.idat', or the same
        with a '.gz' suffix) with that _Grn/_Red.idat(.gz) part already
        removed. sample_id must match one of these exactly, or array_type
        lookup silently fails later (see MetadataMerger.add_array_types) -
        test_config alone can't catch that, since it never touches the
        IDAT files. Only a capped sample is returned, not the full list.
        """
        dataset_path = ctx.deps.dataset_dir / ctx.deps.dataset_id
        if not dataset_path.is_dir():
            return f"No dataset directory found: {dataset_path}"

        found = idat_basepaths(dataset_path, only_valid=True)
        if not found:
            return (
                f"No IDAT files found under {dataset_path}. IDAT files "
                "were not yet downloaded in this dataset. Fall back to the "
                "best available row identifier for sample_id."
            )

        basenames = sorted(p.name for p in found)
        shown = basenames[:_MAX_IDAT_BASENAMES_SHOWN]

        lines = [
            f"{len(basenames)} IDAT basename(s) found under {dataset_path}."
        ]
        if len(shown) < len(basenames):
            lines.append(
                f"Showing the first {len(shown)} (sorted) as a sample of "
                "the naming pattern - this is not the full list:"
            )
        else:
            lines.append("All of them:")
        lines.extend(shown)
        return "\n".join(lines)

    @agent.tool
    def get_study_description(ctx: RunContext[AgentDeps]) -> str:
        """Fetch the public GEO/ArrayExpress study description summary.

        Cached to disk after the first fetch. Not available for private
        cohorts or unrecognized accessions - that's fine, it's optional
        context, not a required input.
        """
        return fetch_study_description(ctx.deps.dataset_id)

    @agent.tool
    def list_configs(ctx: RunContext[AgentDeps]) -> list[str]:
        """List existing dataset configs that can be used as examples."""
        return sorted(
            p.stem
            for p in ctx.deps.config_dir.glob("*.py")
            if p.name != "__init__.py"
        )

    @agent.tool
    def read_config(
        ctx: RunContext[AgentDeps], dataset_id: str | None = None
    ) -> str:
        """Read a dataset config's source.

        Defaults to the current dataset's own config. Pass a dataset_id
        from list_configs to read a different dataset's config instead -
        e.g. to use it as a template. Reads one config at a time; call
        again with a different dataset_id if you need to compare more
        than one.
        """
        target = dataset_id or ctx.deps.dataset_id
        path = ctx.deps.config_dir / f"{target}.py"
        if not path.exists():
            return f"No config exists yet: {path}"
        return path.read_text(encoding="utf-8")

    @agent.tool_plain
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
    metadata_overrides_dir: str | Path | None = None,
    model: str,
    prompt: str | None = None,
    allow_write: bool = True,
    force: bool = False,
    request_limit: int = 40,
    tool_calls_limit: int = 100,
) -> AgentResult:
    """Run the metadata agent for one dataset."""
    config_dir = Path(config_dir).expanduser().resolve()
    dataset_dir = Path(dataset_dir).expanduser().resolve()
    dataset_path = dataset_dir / dataset_id

    if not dataset_path.is_dir():
        raise ValueError(f"Dataset directory does not exist: {dataset_path}")

    merger = MetadataMerger(
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        metadata_overrides_dir=metadata_overrides_dir,
    )
    deps = AgentDeps(
        merger=merger,
        dataset_id=dataset_id,
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        allow_write=allow_write,
        force=force,
    )

    existing_config = _config_path(deps)
    if existing_config.exists() and not force:
        # Fail before spending a single token: write_config would refuse
        # this anyway, so there's no point paying for a run that can only
        # end in that refusal. Pass --force to actually replace it.
        return AgentResult(
            dataset_id=dataset_id,
            success=False,
            config_path=str(existing_config),
            summary=(
                f"SKIPPED: {existing_config} already exists and --force "
                "was not given. Not running the agent - pass --force to "
                "replace it, or run `methylmeta test` to check the "
                "existing config first."
            ),
            usage=RunUsage(),
        )

    agent = create_agent(model)
    user_prompt = prompt or (
        f"Create or repair the metadata config for dataset {dataset_id}. "
        "Use the available tools and finish with a passing test if possible."
    )

    result = agent.run_sync(
        user_prompt,
        deps=deps,
        usage_limits=UsageLimits(
            request_limit=request_limit,
            tool_calls_limit=tool_calls_limit,
        ),
    )

    usage = result.usage

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
        usage=usage,
    )
