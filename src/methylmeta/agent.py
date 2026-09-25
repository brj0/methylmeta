from __future__ import annotations

import ast
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from mepylome.dtypes.beads import idat_basepaths
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext, UsageLimits, capture_run_messages
from pydantic_ai.messages import (
    ModelMessage,
    ModelMessagesTypeAdapter,
    ModelRequest,
    ModelResponse,
    TextPart,
    ThinkingPart,
    ToolCallPart,
    ToolReturnPart,
)
from pydantic_ai.usage import RunUsage

from methylmeta.loader import load_dataset_module
from methylmeta.merger import MetadataMerger
from methylmeta.paths import PROJECT_ROOT
from methylmeta.schema import enum_valued_fields
from methylmeta.spec import AGENT_CONFIG_SPEC
from methylmeta.study_info import fetch_study_description
from methylmeta.vocab import search_tumor_types

_MAX_IDAT_BASENAMES_SHOWN = 15
_MAX_MAPPING_ROWS_SHOWN = 40

_AGENT_WORKFLOW = """\
You are a metadata harmonizer agent for Illumina methylation microarray
datasets. Your sole task is to create or repair exactly one
`configs/datasets/<dataset_id>.py` configuration file. The configuration must
correctly harmonize the real dataset and pass `methylmeta.test()`.

WORKFLOW (follow this order):
1. Call get_profile first. Never guess column names or values. get_profile
   shows some columns in full: "(all N)" lists every value, "(constant)" shows
   the single value. For any other column, call column_values(column="...") to
   see every value. Do this for any "(K of N)" column whose values you map or
   branch on - most importantly those feeding methylation_class. Whether to
   read a column in full is a judgement call: weigh the number of distinct
   values against how much that column matters. For columns with very many
   values that you only pass through or lightly transform (free text, ids,
   numerics), the sample is usually enough - skip those. Never call
   column_values more than once for the same column. Avoid unnecessary calls;
   they waste tokens. Critical for if/elif: a missed value doesn't raise, it
   silently hits the else branch and test_config still passes.
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
   methylation_class. You can batch related diagnosis terms into one call.
   Never invent a WHO acronym. Choose the most specific methylation class
   supported by the available diagnosis, molecular, immunohistochemical, and
   study context. If the available evidence supports a specific subclass,
   always use that subclass. If the evidence is ambiguous or insufficient to
   distinguish a subclass, use the broader class. Do not infer a subclass from
   a feature when the available context does not support that For normal or
   control tissue, use the most specific organ-specific control methylation
   class available in the vocabulary when the organ is known. Control classes
   use the CTRL_<organ> naming convention, where <organ> is the vocabulary's
   established organ abbreviation.
7. Write the smallest clear config possible. Prefer direct passthrough, exact
   mappings, constants, and simple if/elif logic.
8. Call test_config after every write. Fix all failures you can. Also read
   the FIELD COVERAGE and MAPPING sections of its output: passing does not
   mean correct. A field at 0% is either missing or always None, and every
   raw diagnosis must map to a sensible methylation_class.
9. Stop only when test_config reports success, or when a remaining problem
   genuinely requires human judgement.

Only define functions named exactly like canonical fields (plus dataset_id and
description). Any other public function name is reported by test_config as a
failure because the harmonizer would silently ignore it (e.g. `material`
instead of `material_type`). Avoid helper functions. Prefer small, redundant
mappings directly inside the relevant field functions. If a helper is genuinely
necessary or leads to much better readable code, its name must start with _.

**IMPORTANT:** Every raw metadata row must be harmonized. Some raw metadata
values may be incorrect, inconsistent, malformed, or otherwise invalid. Do not
filter, skip, or drop rows because of invalid metadata; harmonize every row as
far as possible. Rows may be removed later by downstream validation or
quality-control steps. Do not add row filtering. Do not use regex. Do not
create new WHO acronyms. Do not change methylmeta source code or
`tumor_types.yaml`.
Use explicit handling for controlled vocabularies. If a mapping is used,
**never use `mapping.get(...)` when `mapping[value]` provides the same behavior
with the same amount of code**. Prefer direct indexing whenever possible. For
`methylation_class`, if you use a mapping, use `mapping[value]` when all
expected values are covered. `mapping.get(value, literal_fallback)` is
acceptable when an explicit fallback is needed. **Never use `mapping.get(value,
value)` for methylation_class**. For other finite controlled vocabularies,
follow the same rule: prefer `mapping[value]`; `.get(value, literal_fallback)`
is acceptable when it provides necessary fallback handling. For open-ended
fields such as `diagnosis`, use the cleanest approach. `mapping.get(value,
value)` is acceptable when preserving the raw value is intentional. In all
cases, preserve the row and map unexpected values to an explicit, schema-valid
fallback rather than raising an error or silently returning the original value.
If an unexpected raw value is encountered, preserve the row and harmonize it as
far as possible using an explicit, schema-valid fallback rather than raising an
error or silently returning the original value.
For any field with a listed enum, the returned value must match one of the
listed literals exactly — do not paraphrase, abbreviate, or use a synonym. When
returning Python code, follow PEP 8 formatting and keep lines to a maximum of
79 characters. The generated config must pass `ruff check` - this is checked
automatically after every write, and any violation is reported back to you with
the exact rule, so you don't need to recall Ruff's rules ahead of time.
Avoid unnesessary / obvious comments.

The config contract is:

{config_spec}
"""


def _format_trace(messages: list[ModelMessage]) -> str:
    """Render a run's messages as a human-readable reasoning trace.

    Walks every request/response pair in order and prints, for each
    step: the model's own text/thinking output (its reasoning before
    acting), each tool call it made with its arguments, and each tool's
    return value. This is the same information the agent itself saw -
    it's what to read to understand *why* it wrote what it wrote, or
    where it went off track.
    """
    lines: list[str] = []
    for message in messages:
        if isinstance(message, ModelRequest):
            for part in message.parts:
                if isinstance(part, ToolReturnPart):
                    lines.append(f"[tool result] {part.tool_name}:")
                    lines.append(str(part.content))
                    lines.append("")
        elif isinstance(message, ModelResponse):
            for part in message.parts:
                if isinstance(part, ThinkingPart):
                    lines.append("[thinking]")
                    lines.append(part.content)
                    lines.append("")
                elif isinstance(part, TextPart):
                    lines.append("[model]")
                    lines.append(part.content)
                    lines.append("")
                elif isinstance(part, ToolCallPart):
                    lines.append(f"[tool call] {part.tool_name}({part.args})")
                    lines.append("")
    return "\n".join(lines)


def _write_trace_log(
    log_dir: Path, dataset_id: str, messages: list[ModelMessage]
) -> None:
    """Persist a run's full message trace for later review.

    Writes two files per run, timestamped so repeated runs on the same
    dataset don't overwrite each other's traces:
      - `<dataset_id>_<timestamp>.log`: a readable trace (see
        _format_trace) - what to skim to see the agent's reasoning,
        tool calls, and tool results in order.
      - `<dataset_id>_<timestamp>.json`: the same run as pydantic-ai's
        own message format, losslessly. Reload it with
        `ModelMessagesTypeAdapter.validate_json(...)` to feed back into
        `agent.run(..., message_history=...)` for debugging or to
        build a regression/eval set from real runs.
    Never raises: a logging failure should not take down a run that
    otherwise succeeded, so any error here is written to stderr instead.
    """
    try:
        log_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        stem = log_dir / f"{dataset_id}_{stamp}"
        stem.with_suffix(".log").write_text(
            _format_trace(messages), encoding="utf-8"
        )
        stem.with_suffix(".json").write_bytes(
            ModelMessagesTypeAdapter.dump_json(messages, indent=2)
        )
    except Exception as exc:  # noqa: BLE001
        import sys

        print(f"WARNING: could not write trace log: {exc}", file=sys.stderr)


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
    wrote_this_run: bool = False


def _config_path(deps: AgentDeps) -> Path:
    return deps.config_dir / f"{deps.dataset_id}.py"


def _clean_code(source: str) -> str:
    """Remove a Markdown code fence if the model returned one."""
    source = source.strip()
    match = re.fullmatch(r"```(?:python|py)?\s*(.*?)```", source, re.DOTALL)
    return match.group(1).strip() if match else source


def _literal_string_values(func: ast.FunctionDef) -> set[str]:
    """Collect string literals a function might *return*, statically.

    Covers the two idioms the config spec teaches: a bare `return "..."`
    and a `mapping = {...}` dict whose *values* are returned via
    `mapping[value]` or `mapping.get(value, default)`. This is a
    heuristic, not a full data-flow analysis: it can't see through values
    built from other functions or computed at runtime. It deliberately
    excludes anything that is clearly raw *input* rather than canonical
    *output*, so it doesn't flag the config's own column names as bad
    enum values:
      - the docstring (first statement, if a bare string constant)
      - dict-literal keys (`{"raw value": ...}` - the raw side)
      - subscript indices (`row["Column Name"]`, `mapping["key"]`)
      - the first positional arg of a `.get(...)` call (the lookup key
        in both `row.get("Column")` and `mapping.get(value, default)`)
    """
    excluded_ids = set()

    for node in ast.walk(func):
        if isinstance(node, ast.Dict):
            for key in node.keys:
                if isinstance(key, ast.Constant) and isinstance(
                    key.value, str
                ):
                    excluded_ids.add(id(key))
        elif isinstance(node, ast.Subscript):
            index = node.slice
            if isinstance(index, ast.Constant) and isinstance(
                index.value, str
            ):
                excluded_ids.add(id(index))
        elif (
            isinstance(node, ast.Call)  # noqa: PLR0916
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "get"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            excluded_ids.add(id(node.args[0]))

    docstring_id = None
    if (
        func.body
        and isinstance(func.body[0], ast.Expr)
        and isinstance(func.body[0].value, ast.Constant)
        and isinstance(func.body[0].value.value, str)
    ):
        docstring_id = id(func.body[0].value)

    values = set()
    for node in ast.walk(func):
        if not (
            isinstance(node, ast.Constant) and isinstance(node.value, str)
        ):
            continue
        if id(node) in excluded_ids or id(node) is docstring_id:
            continue
        values.add(node.value)
    return values


def _validate_enum_literals(tree: ast.Module) -> list[str]:
    """Catch invalid enum values before real data is touched.

    For example, detect a config that returns "recurrent" for `sample_type`
    (the real enum member is "recurrence") or "fresh frozen" for `preservation`
    (the real enum member is "FROZEN"). Runs statically on the generated
    source, so it's instant and free compared to a full `test_config` cycle
    over the actual metadata file.
    """
    enum_fields = enum_valued_fields()
    errors = []
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        enum_cls = enum_fields.get(node.name)
        if enum_cls is None:
            continue

        valid = {member.value for member in enum_cls}
        bad = sorted(_literal_string_values(node) - valid)
        if bad:
            bad_repr = ", ".join(repr(v) for v in bad)
            valid_repr = ", ".join(repr(v) for v in sorted(valid))
            errors.append(
                f"{node.name}() returns {bad_repr}, which "
                f"{'are' if len(bad) > 1 else 'is'} not valid "
                f"{enum_cls.__name__} value(s). Valid values are: "
                f"{valid_repr}."
            )
    return errors


def _run_ruff_check(source: str, dataset_id: str) -> list[str]:
    """Run `ruff check` on generated config source, statically and fast.

    Runs against a virtual path (`configs/datasets/<dataset_id>.py`, fed
    via stdin - nothing touches disk) so ruff's own per-file-ignores for
    that glob (see pyproject.toml: ANN/D/E501 relaxed for dataset
    configs) apply exactly as they would for the real file. This replaces
    asking the agent to recall style rules from prose - it either passes
    the project's actual linter or it doesn't.

    Returns a list of one-line violation strings (empty if clean, or if
    ruff itself isn't available/times out - a missing linter shouldn't
    block config writing, only a config that violates it should).
    """
    virtual_path = f"configs/datasets/{dataset_id}.py"
    try:
        result = subprocess.run(
            [
                "ruff",
                "check",
                "--stdin-filename",
                virtual_path,
                "--output-format",
                "concise",
                "--no-fix",
                "-",
            ],
            input=source,
            capture_output=True,
            text=True,
            timeout=10,
            cwd=PROJECT_ROOT,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return []

    # returncode 0 = clean, 1 = violations found, anything else means ruff
    # itself failed (bad invocation, crashed, etc.) - don't surface that
    # as if it were a config problem.
    if result.returncode != 1:
        return []
    return [line for line in result.stdout.strip().splitlines() if line]


def _validate_config_source(source: str, dataset_id: str) -> str:
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

    enum_errors = _validate_enum_literals(tree)
    if enum_errors:
        raise ValueError(" ".join(enum_errors))

    source += "\n"
    ruff_errors = _run_ruff_check(source, dataset_id)
    if ruff_errors:
        raise ValueError("ruff check failed:\n" + "\n".join(ruff_errors))

    return source


def create_agent(
    model: str,
) -> Agent[AgentDeps, AgentResult]:
    """Create the Pydantic AI metadata-config agent."""
    agent: Agent[AgentDeps, AgentResult] = Agent(
        model=model,
        deps_type=AgentDeps,
        output_type=AgentResult,
        retries=2,
        instructions=_AGENT_WORKFLOW.format(config_spec=AGENT_CONFIG_SPEC),
    )

    @agent.tool
    def get_profile(ctx: RunContext[AgentDeps]) -> str:
        """Inspect real columns and values before writing config."""
        profile = ctx.deps.merger.profile(ctx.deps.dataset_id)
        return profile.summary()

    @agent.tool
    def column_values(
        ctx: RunContext[AgentDeps],
        column: str,
        max_values: int = 300,
    ) -> str:
        """Return every unique value of one raw column, with counts.

        For a "(K of N)" column in get_profile whose values you map or
        branch on - most importantly whatever feeds methylation_class.
        Refuses low-cardinality columns (get_profile already showed every
        value) and columns with too many values to list safely - see
        merger.column_values for why. Never call this more than once for
        the same column.
        """
        try:
            return ctx.deps.merger.column_values(
                ctx.deps.dataset_id, column, max_values=max_values
            )
        except Exception as exc:  # noqa: BLE001
            return f"{type(exc).__name__}: {exc}"

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
    def search_tumor_vocabulary(queries: list[str]) -> str:
        """Search WHO tumor vocabulary for methylation class candidates.

        Pass multiple diagnosis synonyms/candidates at once (e.g.
        ["chondrosarcoma", "chondroblastoma"]) instead of calling repeatedly.
        """
        parts = []
        for q in queries:
            results = search_tumor_types(q, limit=10)
            parts.append(
                f"query: {q!r}\n"
                + ("\n".join(str(r) for r in results) or "No matches.")
            )
        return "\n\n".join(parts)

    @agent.tool
    def test_config(ctx: RunContext[AgentDeps]) -> str:
        """Run the real harmonizer test and return all grouped failures."""
        try:
            report = ctx.deps.merger.test(ctx.deps.dataset_id)
        except Exception as exc:  # noqa: BLE001
            return f"CONFIG TEST COULD NOT RUN: {type(exc).__name__}: {exc}"

        return report.summary(
            max_examples=3,
            max_mapping_rows=_MAX_MAPPING_ROWS_SHOWN,
        )

    @agent.tool
    def write_config(ctx: RunContext[AgentDeps], source: str) -> str:
        """Validate and write the selected dataset config only."""
        if not ctx.deps.allow_write:
            return (
                "WRITE DISABLED. You may inspect and test, but do not "
                "attempt another write."
            )

        path = _config_path(ctx.deps)
        if (
            path.exists()
            and not ctx.deps.force
            and not ctx.deps.wrote_this_run
        ):
            return (
                f"WRITE REFUSED: {path} already exists and --force was "
                "not given. "
                "Read and test the existing config instead."
            )

        try:
            source = _validate_config_source(source, ctx.deps.dataset_id)
        except ValueError as exc:
            return f"WRITE REFUSED: {exc}"

        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            backup = path.with_suffix(path.suffix + ".bak")
            shutil.copy2(path, backup)

        path.write_text(source, encoding="utf-8")
        ctx.deps.wrote_this_run = True

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
    request_limit: int = 80,
    tool_calls_limit: int = 200,
    log_dir: str | Path | None = None,
) -> AgentResult:
    """Run the metadata agent for one dataset.

    If `log_dir` is given, the full run trace (model reasoning, tool
    calls, and tool results, in order) is written there as a readable
    `.log` file plus a lossless `.json` file, whether or not the run
    ultimately succeeds - see `_write_trace_log`.
    """
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

    with capture_run_messages() as messages:
        try:
            result = agent.run_sync(
                user_prompt,
                deps=deps,
                usage_limits=UsageLimits(
                    request_limit=request_limit,
                    tool_calls_limit=tool_calls_limit,
                ),
            )
        finally:
            if log_dir is not None:
                _write_trace_log(Path(log_dir), dataset_id, messages)

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
