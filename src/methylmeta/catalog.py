"""Static catalog of tumor classes each dataset config can produce.

Dataset configs already encode their possible `methylation_class()` outputs.
This module reads them with `ast` instead of executing them, so no metadata or
generated file is needed.

The result is intentionally an over-approximation: a class listed by a config
is included even if it happens to be absent from the actual metadata. This is
safe for deciding which datasets to download. Case counts require real data.

Collected from `methylation_class()` and functions it calls in the same file:

- string literals in `return` statements
- string literals used as dict values
- string literals assigned to variables

Dict keys and comparisons are ignored because they are raw metadata labels.
Only strings that are keys in `tumor_types.yaml` are included.

Known limitation: dynamically produced classes, such as `return row["class"]`,
cannot be detected statically.
"""

from __future__ import annotations

import ast
import csv
import difflib
import io
import json
import logging
from collections import deque
from collections.abc import Iterable, Iterator, Mapping
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from methylmeta.paths import CONFIGS_DIR
from methylmeta.vocab import all_tumor_types, get_tumor_type

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DatasetEntry:
    """What one dataset config can produce."""

    dataset_id: str
    description: str | None
    classes: frozenset[str]


@dataclass(frozen=True)
class Match:
    """A dataset that contains at least one of the wanted classes."""

    entry: DatasetEntry
    matched: frozenset[str]


# ---------------------------------------------------------------------------
# Parsing configs
# ---------------------------------------------------------------------------


def _string_literals(node: ast.AST) -> Iterator[str]:
    """Yield string literals that can be *produced* by an expression.

    Skips comparisons, subscript keys and dict keys: those are raw sheet
    values being looked at, not values being returned.
    """
    if isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            yield node.value
    elif isinstance(node, ast.Compare):
        return
    elif isinstance(node, ast.Subscript):
        yield from _string_literals(node.value)
    elif isinstance(node, ast.Dict):
        for value in node.values:
            yield from _string_literals(value)
    else:
        for child in ast.iter_child_nodes(node):
            yield from _string_literals(child)


def _function_literals(function: ast.FunctionDef) -> Iterator[str]:
    """Yield candidate class strings from one function body."""
    for node in ast.walk(function):
        expression: ast.expr | None = None
        if isinstance(node, ast.Return):
            expression = node.value
        elif isinstance(node, ast.Assign | ast.AnnAssign) and isinstance(
            node.value, ast.Constant | ast.Dict | ast.IfExp
        ):
            # Assignments of calls (`value = row[..].replace("A", "B")`) are
            # string munging of raw values, not class assignment.
            expression = node.value
        if expression is not None:
            yield from _string_literals(expression)


def _called_names(function: ast.FunctionDef) -> set[str]:
    return {
        node.func.id
        for node in ast.walk(function)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }


def classes_in_source(tree: ast.Module) -> frozenset[str]:
    """Valid tumor type acronyms that `methylation_class` can return."""
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    start = functions.get("methylation_class")
    if start is None:
        return frozenset()

    seen = {"methylation_class"}
    queue = deque([start])
    literals: set[str] = set()

    while queue:
        function = queue.popleft()
        literals.update(_function_literals(function))
        for name in _called_names(function):
            if name in functions and name not in seen:
                seen.add(name)
                queue.append(functions[name])

    return frozenset(s for s in literals if get_tumor_type(s) is not None)


def _description_in_source(tree: ast.Module) -> str | None:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "description":
            for sub in ast.walk(node):
                if (
                    isinstance(sub, ast.Return)
                    and isinstance(sub.value, ast.Constant)
                    and isinstance(sub.value.value, str)
                ):
                    return sub.value.value
    return None


def parse_config(path: Path) -> DatasetEntry:
    """Statically read one `configs/datasets/<dataset_id>.py`."""
    path = Path(path)
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return DatasetEntry(
        dataset_id=path.stem,
        description=_description_in_source(tree),
        classes=classes_in_source(tree),
    )


def load_catalog(
    config_dir: str | Path = CONFIGS_DIR,
) -> dict[str, DatasetEntry]:
    """Read every dataset config in `config_dir`, keyed by dataset_id.

    A config that cannot be parsed is logged and skipped, so one
    half-written file doesn't take the whole lookup down.
    """
    config_dir = Path(config_dir)
    if not config_dir.is_dir():
        raise FileNotFoundError(f"Config directory not found: {config_dir}")

    catalog: dict[str, DatasetEntry] = {}
    for path in sorted(config_dir.glob("*.py")):
        if path.name == "__init__.py":
            continue
        try:
            catalog[path.stem] = parse_config(path)
        except (SyntaxError, ValueError, OSError) as exc:
            logger.warning("Skipping unparsable config %s: %s", path, exc)
    return catalog


# ---------------------------------------------------------------------------
# Resolving what the user asked for
# ---------------------------------------------------------------------------


@lru_cache(maxsize=1)
def _children_map() -> dict[str, tuple[str, ...]]:
    children: dict[str, list[str]] = {}
    for tumor_type in all_tumor_types():
        if tumor_type.parent:
            children.setdefault(tumor_type.parent, []).append(
                tumor_type.acronym
            )
    return {parent: tuple(kids) for parent, kids in children.items()}


def expand_descendants(acronym: str) -> frozenset[str]:
    """`acronym` plus every entry below it via `parent` in tumor_types."""
    children = _children_map()
    result = {acronym}
    queue = deque([acronym])
    while queue:
        for child in children.get(queue.popleft(), ()):
            if child not in result:
                result.add(child)
                queue.append(child)
    return frozenset(result)


def _suggest(value: str, choices: Iterable[str]) -> str:
    lookup = {choice.upper(): choice for choice in choices}
    close = difflib.get_close_matches(value.upper(), list(lookup), n=3)
    return f" Did you mean: {[lookup[c] for c in close]}?" if close else ""


def resolve_selection(
    classes: Iterable[str] = (),
    families: Iterable[str] = (),
    sites: Iterable[str] = (),
    descendants: bool = True,
) -> dict[str, frozenset[str]]:
    """Turn user-facing selectors into sets of tumor type acronyms.

    Returns {label: acronyms}, one entry per selector, so callers can tell
    which selector no dataset covers. The union of the values is what to look
    for. With `descendants`, every acronym also selects its sub-entities
    (e.g. `SKIN_MEL` selects `ACR_MEL`).

    - `classes`: tumor type acronyms from tumor_types.yaml.
    - `families`: family tags (e.g. `glioma`), exact, case-insensitive.
    - `sites`: case-insensitive substring of the tumor type's `site`.
    """
    all_types = all_tumor_types()

    def expand(acronyms: Iterable[str]) -> frozenset[str]:
        result: set[str] = set()
        for acronym in acronyms:
            result |= expand_descendants(acronym) if descendants else {acronym}
        return frozenset(result)

    selection: dict[str, frozenset[str]] = {}

    for acronym in classes:
        if get_tumor_type(acronym) is None:
            raise ValueError(
                f"Unknown methylation class {acronym!r}."
                + _suggest(acronym, (t.acronym for t in all_types))
                + " (search with `methylmeta search_vocab <text>`)"
            )
        selection[acronym] = expand([acronym])

    for family in families:
        wanted = family.lower()
        members = [
            t.acronym
            for t in all_types
            if wanted in {f.lower() for f in t.families or []}
        ]
        if not members:
            known = sorted({f for t in all_types for f in t.families or []})
            raise ValueError(
                f"Unknown family {family!r}." + _suggest(family, known)
            )
        selection[f"family:{family}"] = expand(members)

    for site in sites:
        wanted = site.lower()
        members = [
            t.acronym for t in all_types if wanted in (t.site or "").lower()
        ]
        if not members:
            known = sorted({t.site for t in all_types if t.site})
            raise ValueError(
                f"No tumor type with site containing {site!r}."
                + _suggest(site, known)
            )
        selection[f"site:{site}"] = expand(members)

    return selection


# ---------------------------------------------------------------------------
# Querying
# ---------------------------------------------------------------------------


def find_datasets(
    catalog: Mapping[str, DatasetEntry],
    wanted: Iterable[str] | None = None,
) -> list[Match]:
    """Datasets whose config can produce any of the `wanted` acronyms.

    `wanted=None` returns every dataset (with all of its classes as
    `matched`). Sorted by number of matched classes, then dataset_id.
    """
    wanted_set = None if wanted is None else frozenset(wanted)

    matches = []
    for entry in catalog.values():
        matched = (
            entry.classes if wanted_set is None else entry.classes & wanted_set
        )
        if matched or wanted_set is None:
            matches.append(Match(entry=entry, matched=matched))

    matches.sort(key=lambda m: (-len(m.matched), m.entry.dataset_id))
    return matches


def uncovered_selectors(
    selection: Mapping[str, frozenset[str]],
    matches: Iterable[Match],
) -> list[str]:
    """Labels of selectors that no dataset in `matches` covers."""
    found: set[str] = set()
    for match in matches:
        found |= match.matched
    return [
        label
        for label, acronyms in selection.items()
        if not (acronyms & found)
    ]


ROW_COLUMNS = (
    "dataset_id",
    "methylation_class",
    "name",
    "site",
    "lineage_broad",
    "families",
    "parent",
    "description",
)

OUTPUT_FORMATS = ("table", "ids", "json", "tsv")


def class_rows(
    matches: Iterable[Match],
    downloaded: Mapping[str, bool] | None = None,
) -> list[dict[str, str | None]]:
    """One row per (dataset, matched class), with tumor-type attributes.

    Long ("tidy") layout meant for `polars.DataFrame(rows)` /
    `pandas.DataFrame(rows)`. `families` is `|`-joined; `description` is the
    dataset's (repeated on each of its rows). With `downloaded`, a
    `downloaded` column ("true"/"false") is added. Sorted by dataset_id, then
    class.
    """
    rows: list[dict[str, str | None]] = []
    for match in sorted(matches, key=lambda m: m.entry.dataset_id):
        for acronym in sorted(match.matched):
            tumor_type = get_tumor_type(acronym)
            row: dict[str, str | None] = {
                "dataset_id": match.entry.dataset_id,
                "methylation_class": acronym,
                "name": tumor_type.name if tumor_type else None,
                "site": tumor_type.site if tumor_type else None,
                "lineage_broad": (
                    tumor_type.lineage_broad if tumor_type else None
                ),
                "families": (
                    "|".join(tumor_type.families or []) if tumor_type else None
                ),
                "parent": tumor_type.parent if tumor_type else None,
                "description": match.entry.description,
            }
            if downloaded is not None:
                row["downloaded"] = str(
                    downloaded[match.entry.dataset_id]
                ).lower()
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# One-call query + rendering (what `methylmeta find` does)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FindResult:
    """Outcome of `query_datasets`."""

    matches: list[Match]
    # Selectors (class, family:..., site:...) that no dataset covers.
    uncovered: list[str]
    # dataset_id -> fully downloaded? Only set when a dataset_dir was given.
    downloaded: dict[str, bool] | None = None


def _split_csv(values: Iterable[str]) -> list[str]:
    """Flatten repeated and comma-separated values."""
    return [
        v.strip() for value in values for v in value.split(",") if v.strip()
    ]


def query_datasets(
    config_dir: str | Path = CONFIGS_DIR,
    *,
    classes: Iterable[str] = (),
    families: Iterable[str] = (),
    sites: Iterable[str] = (),
    descendants: bool = True,
    dataset_dir: str | Path | None = None,
    idat: bool = False,
    missing: bool = False,
) -> FindResult:
    """Everything `methylmeta find` does, without any printing.

    `classes` and `families` items may be comma-separated; `sites` are
    substrings and taken as they are (site names can contain commas).
    Selectors are OR-ed; with none, every dataset is returned. With
    `dataset_dir`, each match gets a `downloaded` flag, and `missing=True`
    keeps only the incomplete ones.

    Raises ValueError for unknown selectors or an empty config_dir, and
    FileNotFoundError if config_dir does not exist.
    """
    if missing and dataset_dir is None:
        raise ValueError("`missing` requires `dataset_dir`.")

    catalog = load_catalog(config_dir)
    if not catalog:
        raise ValueError(
            f"No dataset configs found in {config_dir}. config_dir should "
            "point at your harmonizer configs (e.g. 'configs/datasets')."
        )

    selection = resolve_selection(
        classes=_split_csv(classes),
        families=_split_csv(families),
        sites=[s.strip() for s in sites if s.strip()],
        descendants=descendants,
    )
    wanted = frozenset().union(*selection.values()) if selection else None
    matches = find_datasets(catalog, wanted)
    uncovered = uncovered_selectors(selection, matches)

    downloaded: dict[str, bool] | None = None
    if dataset_dir is not None:
        from methylmeta.fetch import check_datasets  # needs mepylome

        statuses = check_datasets(
            [m.entry.dataset_id for m in matches],
            Path(dataset_dir).expanduser(),
            check_idat=idat,
        )
        downloaded = {s.dataset_id: s.is_complete for s in statuses}
        if missing:
            matches = [
                m for m in matches if not downloaded[m.entry.dataset_id]
            ]

    return FindResult(matches, uncovered, downloaded)


def _class_list(match: Match, max_classes: int) -> str:
    classes = sorted(match.matched)
    if max_classes and len(classes) > max_classes:
        rest = len(classes) - max_classes
        return ", ".join(classes[:max_classes]) + f", +{rest} more"
    return ", ".join(classes)


def _render_table(result: FindResult, max_classes: int) -> str:
    header = ["DATASET", "CLASSES", "DESCRIPTION"]
    if result.downloaded is not None:
        header.insert(1, "LOCAL")
    rows = []
    for match in result.matches:
        row = [match.entry.dataset_id, _class_list(match, max_classes)]
        if result.downloaded is not None:
            done = result.downloaded[match.entry.dataset_id]
            row.insert(1, "yes" if done else "no")
        row.append(match.entry.description or "")
        rows.append(row)
    if not rows:
        return ""

    # Pad every column but the (free-length) description.
    widths = [
        max(len(line[i]) for line in [header, *rows])
        for i in range(len(header) - 1)
    ]
    return "\n".join(
        "  ".join(cell.ljust(w) for cell, w in zip(line, widths, strict=False))
        + "  "
        + line[-1]
        for line in [header, *rows]
    ).rstrip()


def _render_tsv(result: FindResult) -> str:
    columns = list(ROW_COLUMNS)
    if result.downloaded is not None:
        columns.append("downloaded")
    buffer = io.StringIO()
    writer = csv.DictWriter(
        buffer, fieldnames=columns, delimiter="\t", lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(class_rows(result.matches, result.downloaded))
    return buffer.getvalue().rstrip("\n")


def _render_json(result: FindResult) -> str:
    records = []
    for match in result.matches:
        record: dict[str, object] = {
            "dataset_id": match.entry.dataset_id,
            "description": match.entry.description,
            "matched_classes": sorted(match.matched),
            "methylation_classes": sorted(match.entry.classes),
        }
        if result.downloaded is not None:
            record["downloaded"] = result.downloaded[match.entry.dataset_id]
        records.append(record)
    return json.dumps(records, indent=2)


def render(
    result: FindResult,
    output_format: str = "table",
    max_classes: int = 8,
) -> str:
    """Format a `FindResult` as text (no trailing newline; may be empty).

    - `table`: human-readable, at most `max_classes` classes per dataset
      (0 = all).
    - `ids`: one dataset_id per line, for `methylmeta fetch`.
    - `tsv`: one row per dataset/class pair (see `class_rows`), header
      always present.
    - `json`: one record per dataset with all of its classes.
    """
    if output_format == "table":
        return _render_table(result, max_classes)
    if output_format == "ids":
        return "\n".join(m.entry.dataset_id for m in result.matches)
    if output_format == "tsv":
        return _render_tsv(result)
    if output_format == "json":
        return _render_json(result)
    raise ValueError(
        f"Unknown format {output_format!r}; expected one of {OUTPUT_FORMATS}."
    )
