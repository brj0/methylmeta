from __future__ import annotations

import difflib
import inspect
import logging
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from typing import Any

import polars as pl

from methylmeta.loader import load_dataset_module
from methylmeta.paths import CACHE_DIR, METADATA_OVERRIDES_DIR
from methylmeta.schema import SampleMetadata

logger = logging.getLogger(__name__)

MISSING_VALUES = {
    "",
    "--",
    "<NA>",
    "N/A",
    "NA",
    "NAN",
    "NONE",
    "NULL",
    "NaN",
    "None",
    "missing",
    "nan",
}

SEX_MAPPING = {
    "F": "female",
    "Female": "female",
    "f": "female",
    "M": "male",
    "Male": "male",
    "m": "male",
}

TUMOR_GRADE_MAPPING = {
    1: "G1",
    2: "G2",
    3: "G3",
    4: "G4",
}

CSV_NULL_VALUES = [
    "",
    "<NA>",
    "NA",
    "--",
    "NAN",
    "nan",
    "NaN",
    "N/A",
    "NULL",
    "None",
    "NONE",
]


def read_metadata(path: Path) -> pl.DataFrame:
    """Read a CSV, TSV, XLSX, or XLS metadata file."""
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return pl.read_csv(
            path,
            infer_schema_length=10000,
            null_values=CSV_NULL_VALUES,
            comment_prefix="#",
        )

    if suffix == ".tsv":
        return pl.read_csv(
            path,
            separator="\t",
            infer_schema_length=10000,
            null_values=CSV_NULL_VALUES,
            comment_prefix="#",
        )

    if suffix in {".xlsx", ".xls"}:
        return pl.read_excel(path)

    raise ValueError(f"Unsupported metadata file format: {path.suffix}")


@dataclass
class ColumnProfile:
    """Summary of one raw metadata column."""

    name: str
    dtype: str
    n_null: int
    n_unique: int
    is_constant: bool
    is_low_cardinality: bool
    sample_values: list[str]

    def __str__(self) -> str:
        # Save tokens for constant values
        if self.is_constant:
            value = self.sample_values[0] if self.sample_values else "null"
            return f"{self.name} (constant): {value!r}"
        if self.is_low_cardinality:
            values_line = (
                f"sample_values (all {self.n_unique}): {self.sample_values}"
            )
        else:
            values_line = (
                f"sample_values ({len(self.sample_values)} of "
                f"{self.n_unique}): {self.sample_values}"
            )

        lines = [
            f"name: {self.name}",
            f"dtype: {self.dtype}",
            f"n_null: {self.n_null}",
            values_line,
        ]
        return "\n".join(lines)


@dataclass
class DatasetProfile:
    """Structural summary of one dataset's raw metadata.

    This is what to look at (or hand to an agent) before writing a config -
    seeing actual column names and their value distributions beats guessing
    at what a value_mapping dict needs to contain.
    """

    dataset_id: str
    n_rows: int
    columns: list[ColumnProfile]
    source_file: Path | None = None

    def summary(self) -> str:
        lines = [
            "DATASET",
            f"dataset_id: {self.dataset_id}",
            f"source_file: {self.source_file}",
            f"n_rows: {self.n_rows}",
            f"n_columns: {len(self.columns)}",
            "",
            "COLUMNS",
        ]

        for i, column in enumerate(self.columns, start=1):
            lines.extend(
                [
                    "",
                    f"column_{i}:",
                    str(column),
                ]
            )

        return "\n".join(lines)


@dataclass
class RowError:
    """One row that failed to harmonize."""

    row_index: int
    raw_row: dict[str, Any]
    error: str


@dataclass
class HarmonizeReport:
    """Result of a dry-run test of one dataset's config against real data."""

    dataset_id: str
    total_rows: int
    ok_rows: int
    errors: list[RowError] = field(default_factory=list)
    preview: pl.DataFrame = field(default_factory=pl.DataFrame)
    config_errors: list[str] = field(default_factory=list)

    @property
    def success(self) -> bool:
        return not self.errors and not self.config_errors

    def grouped_errors(self) -> dict[str, list[RowError]]:
        """Group failures by identical error message.

        A single typo in a value_mapping dict tends to fail every row that
        contains that raw value, so this collapses e.g. 200 identical
        KeyErrors down to one group instead of 200 lines.
        """
        groups: dict[str, list[RowError]] = {}
        for err in self.errors:
            groups.setdefault(err.error, []).append(err)
        return groups

    def summary(
        self,
        max_examples: int = 2,
        max_mapping_rows: int | None = 100,
    ) -> str:
        lines = [
            f"{self.dataset_id}: {self.ok_rows}/{self.total_rows} rows OK",
        ]

        if self.config_errors:
            lines.append(f"{len(self.config_errors)} config problem(s):")
            lines.extend(f"  {msg}" for msg in self.config_errors)

        if self.errors:
            lines.append(f"{len(self.errors)} row(s) failed:")
            for error_msg, rows in self.grouped_errors().items():
                lines.append(f"  [{len(rows)}x] {error_msg}")
                for row_err in rows[:max_examples]:
                    lines.append(
                        "      e.g. row "
                        f"{row_err.row_index}: {row_err.raw_row}"
                    )
        else:
            lines.append("All rows harmonized successfully.")

        coverage = self.field_coverage()
        if coverage:
            lines.append("")
            lines.append(coverage)

        mapping = self.mapping_table(max_rows=max_mapping_rows)
        if mapping:
            lines.append("")
            lines.append(mapping)

        return "\n".join(lines)

    def field_coverage(self) -> str:
        """Per-field fill rate over the rows that harmonized.

        A field at 0 non-null values is either not defined in the config or
        always returns None - both are worth a second look, since `test()`
        passes either way.
        """
        n_rows = self.preview.height
        if n_rows == 0:
            return ""

        lines = [f"FIELD COVERAGE (non-null, of {n_rows} OK rows):"]
        for name in SampleMetadata.model_fields:
            if name in self.preview.columns:
                n_filled = n_rows - self.preview[name].null_count()
            else:
                n_filled = 0
            pct = 100 * n_filled / n_rows
            lines.append(f"  {name}: {n_filled} ({pct:.0f}%)")
        return "\n".join(lines)

    def mapping_table(self, max_rows: int | None = None) -> str:
        """Unique (diagnosis -> methylation_class) pairs with row counts.

        This is the review artifact: a compact table showing what the config
        actually produced, which is far quicker to check by eye than the
        config code. If the config defines no diagnosis, only the class
        counts are shown.
        """
        preview = self.preview
        if preview.is_empty() or "methylation_class" not in preview.columns:
            return ""

        keys = ["methylation_class"]
        if (
            "diagnosis" in preview.columns
            and preview["diagnosis"].null_count() < preview.height
        ):
            keys = ["diagnosis", "methylation_class"]

        counts = preview.group_by(keys).len().sort(keys)
        rows = list(counts.iter_rows())
        shown = rows if max_rows is None else rows[:max_rows]

        def fmt(value: object) -> str:
            return "<None>" if value is None else str(value)

        lines = [
            "MAPPING ("
            + " -> ".join(keys)
            + f"; {len(rows)} unique, count first):"
        ]
        for *values, count in shown:
            lines.append(
                f"  {count:>5}  " + " -> ".join(fmt(v) for v in values)
            )
        if len(shown) < len(rows):
            lines.append(f"  ... {len(rows) - len(shown)} more")
        return "\n".join(lines)


def unknown_config_functions(dataset: ModuleType) -> list[str]:
    """Describe public functions in a config that are not schema fields.

    The harmonizer only ever looks up functions by canonical field name, so
    a function like `material()` (meant to be `material_type()`) is silently
    ignored and its field stays empty - and every test still passes. Helpers
    are fine as long as their name starts with an underscore; functions
    imported from elsewhere are ignored.
    """
    fields = list(SampleMetadata.model_fields)
    problems = []
    for name, function in inspect.getmembers(dataset, inspect.isfunction):
        if (
            function.__module__ != dataset.__name__
            or name.startswith("_")
            or name in fields
        ):
            continue
        close = difflib.get_close_matches(name, fields, n=1, cutoff=0.6)
        hint = f" (did you mean {close[0]!r}?)" if close else ""
        problems.append(
            f"function {name}(){hint} is not a canonical field, so it would "
            "be silently ignored. Rename it, remove it, or prefix it with "
            "'_' if it is a helper."
        )
    return problems


class MetadataHarmonizer:
    """Harmonize one dataset into the canonical metadata schema."""

    def __init__(
        self,
        dataset: ModuleType,
    ) -> None:
        self.dataset = dataset
        self.config_errors = unknown_config_functions(dataset)

    def harmonize(self, raw: pl.DataFrame) -> pl.DataFrame:
        """Harmonize a raw metadata table."""
        if self.config_errors:
            raise ValueError(
                f"Invalid config {self.dataset.__name__}: "
                + "; ".join(self.config_errors)
            )

        rows = [self._harmonize_row(row) for row in raw.iter_rows(named=True)]

        if not rows:
            return pl.DataFrame()

        data = [metadata.model_dump(mode="python") for metadata in rows]

        return pl.DataFrame(data, infer_schema_length=None)

    def test(
        self, raw: pl.DataFrame, dataset_id: str = "?"
    ) -> HarmonizeReport:
        """Dry-run a config against real data, isolating failures per row.

        Unlike `harmonize()`, a single bad row (an unmapped raw value, a
        typo'd WHO acronym, a KeyError in a field function, ...) doesn't
        abort the whole dataset - it's collected and reported so every
        problem in the file surfaces in one pass instead of one-at-a-time.
        """
        ok_rows: list[SampleMetadata] = []
        errors: list[RowError] = []

        for i, row in enumerate(raw.iter_rows(named=True)):
            try:
                ok_rows.append(self._harmonize_row(row))
            except Exception as exc:  # noqa: BLE001 - report, don't crash
                errors.append(
                    RowError(
                        row_index=i,
                        raw_row=dict(row),
                        error=f"{type(exc).__name__}: {exc}",
                    )
                )

        data = [metadata.model_dump(mode="python") for metadata in ok_rows]
        preview = (
            pl.DataFrame(data, infer_schema_length=None)
            if data
            else pl.DataFrame()
        )

        return HarmonizeReport(
            dataset_id=dataset_id,
            total_rows=len(ok_rows) + len(errors),
            ok_rows=len(ok_rows),
            errors=errors,
            preview=preview,
            config_errors=list(self.config_errors),
        )

    def _harmonize_row(
        self,
        row: dict[str, Any],
    ) -> SampleMetadata:
        values: dict[str, Any] = {}

        for field_name in SampleMetadata.model_fields:
            function = getattr(self.dataset, field_name, None)

            if function is None:
                continue

            value = function(row)
            values[field_name] = self._normalize(field_name, value)

        return SampleMetadata.model_validate(values)

    @staticmethod
    def _normalize(
        field: str,
        value: Any,
    ) -> Any:
        if value is None:
            return None

        if isinstance(value, str):
            value = value.strip()

            if value in MISSING_VALUES:
                return None

        if field == "sex":
            return SEX_MAPPING.get(value, value)

        if field == "tumor_grade":
            return TUMOR_GRADE_MAPPING.get(value, value)

        return value


METADATA_EXTENSIONS = {".csv", ".tsv", ".xlsx", ".xls"}


def find_metadata_file(dataset_dir: Path) -> Path:
    """Searches and returns spreadsheed path in 'dataset_dir' if unique."""
    files = sorted(
        p
        for p in dataset_dir.iterdir()
        if p.is_file() and p.suffix.lower() in METADATA_EXTENSIONS
    )

    if len(files) != 1:
        raise ValueError(
            f"Expected exactly one metadata in {dataset_dir}, "
            f"found {len(files)}: {[p.name for p in files]}"
        )

    return files[0]


def find_metadata_override(
    overrides_dir: Path, dataset_id: str
) -> Path | None:
    """Look for a hand-curated `<dataset_id>.<ext>` spreadsheet.

    Returns None if `overrides_dir` doesn't exist or has no matching file -
    this is the common case, since most datasets' GEO/ArrayExpress sample
    sheet is fine as-is. If exactly one matching file is found, it's
    returned. Multiple matches (e.g. both a .csv and .xlsx for the same
    dataset_id) raise, same as `find_metadata_file`.
    """
    if not overrides_dir.is_dir():
        return None

    matches = sorted(
        p
        for ext in METADATA_EXTENSIONS
        for p in overrides_dir.glob(f"{dataset_id}{ext}")
        if p.is_file()
    )

    if not matches:
        return None

    if len(matches) > 1:
        raise ValueError(
            f"Expected at most one metadata override for {dataset_id!r} in "
            f"{overrides_dir}, found {len(matches)}: "
            f"{[p.name for p in matches]}"
        )

    return matches[0]


class MetadataMerger:
    """Merge harmonized metadata from multiple datasets.

    Typical usecase:

        merger = MetadataMerger(
            config_dir="/path/to/configs/datasets",
            dataset_dir="/path/to/datasets",
        )

        # 1. Figure out which of the datasets you want don't have a config yet.
        wanted = ["GSE197094", "GSE196228", "GSE999999"]
        missing = merger.missing_configs(wanted)
        # -> ["GSE999999"]  (this is what an agent should generate .py files
        # for)

        # 2. Once configs/datasets/GSE999999.py exists, merge just what you
        # want.
        df = merger.merge(dataset_ids=wanted)

        # Or, to merge everything that currently has both a config and data:
        df = merger.merge()

        # 3. If dataset_dir/<dataset_id>/ also contains IDAT files, fill in
        # array_type by reading them. This is a separate, slower step - write
        # df out as a checkpoint first if merging at scale.
        df = merger.add_array_types(df)

    `dataset_dir` is expected to contain one subdirectory per dataset_id,
    each holding both that dataset's metadata file and (optionally) its own
    IDAT files - IDATs are never looked up outside a dataset's own folder,
    since generic filenames (e.g. "sample1_Grn.idat") can collide across
    different datasets, especially ArrayExpress or private cohorts.

    Some datasets have useless GEO/ArrayExpress metadata while the real
    annotation is only in a paper spreadsheet. Put that file in
    `metadata_overrides_dir` (default `data/metadata/`) as `<dataset_id>.<ext>`
    to use it instead of the metadata in `dataset_dir`.
    """

    def __init__(
        self,
        config_dir: str | Path,
        dataset_dir: str | Path,
        metadata_overrides_dir: str | Path | None = None,
        strict: bool = True,
    ) -> None:
        self.config_dir = Path(config_dir)
        self.dataset_dir = Path(dataset_dir)
        self.strict = strict

        if metadata_overrides_dir is None:
            metadata_overrides_dir = METADATA_OVERRIDES_DIR
        self.metadata_overrides_dir = Path(metadata_overrides_dir)

    def _resolve_metadata_file(self, dataset_id: str) -> Path:
        """Pick the metadata spreadsheet to use for `dataset_id`.

        A file in `metadata_overrides_dir` named `<dataset_id>.<ext>` wins
        over whatever is sitting in that dataset's own directory under
        `dataset_dir` - this is for datasets whose GEO/ArrayExpress sample
        sheet is useless (bare patient numbers, no diagnoses) and where the
        real annotation was published as a spreadsheet on the paper's page
        instead.
        """
        override = find_metadata_override(
            self.metadata_overrides_dir, dataset_id
        )
        if override is not None:
            logger.info(
                "%s: using metadata override %s (ignoring sheet, if any, in "
                "%s)",
                dataset_id,
                override,
                self.dataset_dir / dataset_id,
            )
            return override

        return find_metadata_file(self.dataset_dir / dataset_id)

    def config_path(self, dataset_id: str) -> Path:
        """Path of the config for `dataset_id`.

        A config's filename *is* its dataset_id (`<dataset_id>.py`); this is
        enforced by `load_config`. That lets each dataset be loaded on its
        own, so one broken or half-written config can't affect the others.
        """
        return self.config_dir / f"{dataset_id}.py"

    def _has_configs(self) -> bool:
        return any(self.config_dir.glob("*.py"))

    def load_config(self, dataset_id: str) -> ModuleType:
        """Load `<config_dir>/<dataset_id>.py` and check its dataset_id."""
        path = self.config_path(dataset_id)

        if not path.is_file():
            hint = ""
            if not self._has_configs():
                hint = (
                    f" No .py files at all in {self.config_dir}: config_dir "
                    "should point at your harmonizer configs (e.g. "
                    "'configs/datasets'), not at a raw-data/download "
                    "directory - double check you haven't swapped "
                    "config_dir and dataset_dir."
                )
            raise ValueError(
                f"No config found for {dataset_id!r}: expected {path} "
                f"(see missing_configs()).{hint}"
            )

        module = load_dataset_module(path)
        actual_id = module.dataset_id(None)
        if actual_id != dataset_id:
            raise ValueError(
                f"{path.name}: dataset_id(None) returned {actual_id!r} but "
                f"the filename requires {dataset_id!r}. Rename the file or "
                "fix dataset_id()."
            )
        return module

    def available_datasets(self) -> list[str]:
        """Dataset IDs that already have a config .py file."""
        return sorted(
            p.stem
            for p in self.config_dir.glob("*.py")
            if p.name != "__init__.py"
        )

    def missing_configs(self, dataset_ids: Iterable[str]) -> list[str]:
        """Which of `dataset_ids` have no config .py file yet.

        This is the hand-off point for a future agent: whatever comes back
        here is what it needs to write configs/datasets/<id>.py for.
        """
        if not self._has_configs():
            raise ValueError(
                f"No dataset config .py files found in {self.config_dir}. "
                "config_dir should point at your harmonizer configs (e.g. "
                "'configs/datasets'), not at a raw-data/download "
                "directory - double check you haven't swapped config_dir "
                "and dataset_dir."
            )
        return [d for d in dataset_ids if not self.config_path(d).is_file()]

    def merge(
        self,
        dataset_ids: Iterable[str] | None = None,
    ) -> pl.DataFrame:
        """Harmonize and merge datasets.

        If `dataset_ids` is given, merge
        exactly those (in that order) - every one of them must already have
        a config (see `missing_configs`). If omitted, merge everything that
        currently has both a config and a data directory (skipping/erroring
        on the rest per `strict`).
        """
        if dataset_ids is not None:
            dataset_ids = list(dataset_ids)
            missing = self.missing_configs(dataset_ids)
            if missing:
                raise ValueError(
                    f"No config found for: {missing}. Generate these "
                    "configs first (see missing_configs())."
                )
        else:
            dataset_ids = self.available_datasets()

        if not dataset_ids:
            raise ValueError("No dataset IDs to merge.")

        merged: list[pl.DataFrame] = []

        for dataset_id in dataset_ids:
            dataset_path = self.dataset_dir / dataset_id

            if not dataset_path.is_dir():
                if self.strict:
                    raise FileNotFoundError(
                        f"{dataset_id}: directory not found: {dataset_path}"
                    )
                logger.warning("Skipping %s: no data directory", dataset_id)
                continue

            metadata_file = self._resolve_metadata_file(dataset_id)

            logger.info("Processing %s", dataset_id)

            dataset = self.load_config(dataset_id)
            raw = read_metadata(metadata_file)

            harmonizer = MetadataHarmonizer(dataset=dataset)
            merged.append(harmonizer.harmonize(raw))

        if not merged:
            raise ValueError("No datasets were processed.")

        result = pl.concat(merged, how="vertical_relaxed").unique(
            maintain_order=True
        )
        self._validate_unique_sample_ids(result)

        return result

    def add_array_types(
        self,
        df: pl.DataFrame,
        show_progress: bool = True,
    ) -> pl.DataFrame:
        """Fill in `array_type` by reading each sample's own IDAT header."""
        from mepylome.dtypes import ArrayType
        from mepylome.dtypes.beads import idat_basepaths

        if "dataset_id" not in df.columns or "sample_id" not in df.columns:
            raise ValueError("df must have dataset_id and sample_id columns")

        rows = df.select("dataset_id", "sample_id").iter_rows()
        if show_progress:
            try:
                from tqdm import tqdm

                rows = tqdm(
                    rows, total=df.height, desc="Computing array types"
                )
            except ImportError:
                pass

        basepaths_by_dataset: dict[str, dict[str, Path]] = {}
        array_types: list[str | None] = []

        for dataset_id, sample_id in rows:
            if dataset_id not in basepaths_by_dataset:
                dataset_path = self.dataset_dir / dataset_id
                found = (
                    idat_basepaths(dataset_path, only_valid=True)
                    if dataset_path.is_dir()
                    else []
                )
                basepaths_by_dataset[dataset_id] = {p.name: p for p in found}

            basepath = basepaths_by_dataset[dataset_id].get(sample_id)

            if basepath is None:
                array_types.append(None)
                continue

            try:
                array_types.append(str(ArrayType.from_idat(basepath)))
            except Exception:
                logger.warning(
                    "%s/%s: could not determine array type from %s",
                    dataset_id,
                    sample_id,
                    basepath,
                )
                array_types.append("invalid_array")

        return df.with_columns(pl.Series("array_type", array_types))

    def add_idat_paths(self, df: pl.DataFrame) -> pl.DataFrame:
        """Add `idat_path`: absolute IDAT basepath (no `_Grn.idat` suffix).

        Samples without a valid IDAT pair on disk get null.
        """
        from mepylome.dtypes.beads import idat_basepaths

        if "dataset_id" not in df.columns or "sample_id" not in df.columns:
            raise ValueError("df must have dataset_id and sample_id columns")

        basepaths_by_dataset: dict[str, dict[str, Path]] = {}
        paths: list[str | None] = []

        for dataset_id, sample_id in df.select(
            "dataset_id", "sample_id"
        ).iter_rows():
            if dataset_id not in basepaths_by_dataset:
                dataset_path = self.dataset_dir / dataset_id
                found = (
                    idat_basepaths(dataset_path, only_valid=True)
                    if dataset_path.is_dir()
                    else []
                )
                basepaths_by_dataset[dataset_id] = {p.name: p for p in found}

            basepath = basepaths_by_dataset[dataset_id].get(sample_id)
            paths.append(str(basepath.resolve()) if basepath else None)

        return df.with_columns(pl.Series("idat_path", paths, dtype=pl.String))

    @staticmethod
    def drop_invalid(df: pl.DataFrame) -> pl.DataFrame:
        """Drop rows without a usable IDAT pair.

        That is: no `idat_path`, or (if the column exists) `array_type` is
        `invalid_array`. Run after `add_idat_paths` / `add_array_types`.
        """
        if "idat_path" not in df.columns:
            raise ValueError("df needs an idat_path column (add_idat_paths)")

        no_idat = pl.col("idat_path").is_null()
        bad_array = (
            pl.col("array_type").eq_missing("invalid_array")
            if "array_type" in df.columns
            else pl.lit(False)
        )
        n_no_idat, n_bad = df.select(
            no_idat.sum().alias("no_idat"),
            (~no_idat & bad_array).sum().alias("bad_array"),
        ).row(0)
        logger.info(
            "Dropping %d rows without IDAT and %d with invalid array "
            "(keeping %d)",
            n_no_idat,
            n_bad,
            df.height - n_no_idat - n_bad,
        )
        return df.filter(~no_idat & ~bad_array)

    def add_purities(
        self,
        df: pl.DataFrame,
        methods: tuple[str, ...] = ("absolute", "estimate"),
        n_jobs: int | None = None,
        show_progress: bool = True,
        cache_dir: str | Path | None = None,
    ) -> pl.DataFrame:
        """Add `purity_<method>` columns (RFpurify, predicted from IDATs).

        Needs `idat_path` (see `add_idat_paths`). Results are cached per
        dataset in `<cache_dir>/<dataset_id>.json` (default:
        `CACHE_DIR/purity`, never inside the dataset folders) and reused
        across merges; the cache is ignored if the mepylome version differs.
        Samples that are missing or fail get null (and are not cached).
        """
        import json
        import os
        from concurrent.futures import ThreadPoolExecutor
        from importlib.metadata import version

        from mepylome import MethylData

        if "idat_path" not in df.columns:
            raise ValueError("df needs an idat_path column (add_idat_paths)")

        cache_dir = Path(cache_dir) if cache_dir else CACHE_DIR / "purity"
        cache_dir.mkdir(parents=True, exist_ok=True)
        columns = [f"purity_{m}" for m in methods]
        mepylome_version = version("mepylome")
        n_jobs = n_jobs or min(8, os.cpu_count() or 1)

        def predict(basepath: str) -> dict[str, float]:
            md = MethylData(file=basepath, prep="noob")
            return {
                f"purity_{m}": round(float(md.predict_purity(m).iloc[0]), 3)
                for m in methods
            }

        results: dict[tuple[str, str], dict[str, float]] = {}

        for dataset_id in df["dataset_id"].unique(maintain_order=True):
            cache_path = cache_dir / f"{dataset_id}.json"
            cache: dict[str, dict[str, float]] = {}
            if cache_path.is_file():
                stored = json.loads(cache_path.read_text())
                if stored.get("mepylome") == mepylome_version:
                    cache = stored["samples"]

            rows = df.filter(
                (pl.col("dataset_id") == dataset_id)
                & pl.col("idat_path").is_not_null()
                & pl.col("sample_id").is_not_null()
            ).select("sample_id", "idat_path")
            todo = [
                (sid, path)
                for sid, path in rows.iter_rows()
                if not all(c in cache.get(sid, {}) for c in columns)
            ]

            if todo:
                with ThreadPoolExecutor(max_workers=n_jobs) as pool:
                    futures = {
                        sid: pool.submit(predict, path) for sid, path in todo
                    }
                    items = futures.items()
                    if show_progress:
                        from tqdm import tqdm

                        items = tqdm(
                            items,
                            total=len(futures),
                            desc=f"Purity {dataset_id}",
                        )
                    for sid, future in items:
                        try:
                            cache.setdefault(sid, {}).update(future.result())
                        except Exception:
                            logger.warning(
                                "%s/%s: could not predict purity",
                                dataset_id,
                                sid,
                                exc_info=True,
                            )
                cache_path.write_text(
                    json.dumps(
                        {"mepylome": mepylome_version, "samples": cache}
                    )
                )

            for sid, _ in rows.iter_rows():
                if all(c in cache.get(sid, {}) for c in columns):
                    results[(dataset_id, sid)] = cache[sid]

        return df.with_columns(
            pl.Series(
                col,
                [
                    results.get((d, s), {}).get(col)
                    for d, s in df.select(
                        "dataset_id", "sample_id"
                    ).iter_rows()
                ],
                dtype=pl.Float64,
            )
            for col in columns
        )

    def profile(
        self,
        dataset_id: str,
        max_unique: int = 15,
        sample_size: int = 5,
    ) -> DatasetProfile:
        """Summarize a raw metadata column and value distributions.

        Deliberately doesn't require a config to exist - this is the step
        that comes *before* writing one, so you (or an agent) can see real
        column names and values instead of guessing at a value_mapping dict.

        `max_unique` is the low-cardinality threshold: columns at or under
        it are enumerable categories, so every value is kept - a config's
        mapping needs to cover all of them, not a sample. `sample_size`
        caps how many example values are kept for columns *above* that
        threshold (IDs, URLs, free text), where only enough values to see
        the pattern are useful; collecting and formatting all `max_unique`
        of them just to show `sample_size` was redundant.
        """
        metadata_file = self._resolve_metadata_file(dataset_id)

        raw = read_metadata(metadata_file)

        columns = []
        for name in raw.columns:
            column = raw[name]
            uniques = column.drop_nulls().unique().to_list()
            n_unique = len(uniques)
            is_low_cardinality = n_unique <= max_unique
            cap = max_unique if is_low_cardinality else sample_size
            sample_values = sorted(str(v) for v in uniques[:cap])
            columns.append(
                ColumnProfile(
                    name=name,
                    dtype=str(column.dtype),
                    n_null=column.null_count(),
                    n_unique=n_unique,
                    is_constant=n_unique <= 1,
                    is_low_cardinality=is_low_cardinality,
                    sample_values=sample_values,
                )
            )

        return DatasetProfile(
            dataset_id=dataset_id,
            n_rows=raw.height,
            columns=columns,
            source_file=metadata_file,
        )

    def test(
        self,
        dataset_id: str,
    ) -> HarmonizeReport:
        """Dry-run a single dataset's config against its real metadata.

        This is the fast iteration loop for writing/fixing a config: point
        it at one dataset, see exactly which rows fail and why, fix the
        config, rerun - without having to run the full multi-dataset merge.
        """
        dataset = self.load_config(dataset_id)
        metadata_file = self._resolve_metadata_file(dataset_id)
        raw = read_metadata(metadata_file)

        harmonizer = MetadataHarmonizer(dataset=dataset)
        return harmonizer.test(raw, dataset_id=dataset_id)

    def column_values(
        self,
        dataset_id: str,
        column: str,
        max_values: int = 500,
    ) -> str:
        """Full unique-value list (with counts) for one raw column."""
        raw = read_metadata(self._resolve_metadata_file(dataset_id))
        if column not in raw.columns:
            close = difflib.get_close_matches(column, raw.columns, n=3)
            hint = f" Did you mean: {close}?" if close else ""
            raise ValueError(f"No column {column!r}.{hint}")

        vc = raw[column].drop_nulls().value_counts(sort=True).head(max_values)
        total_unique = raw[column].drop_nulls().n_unique()
        lines = [
            f"{column}: {total_unique} unique non-null value(s)"
            + (
                f" (showing top {max_values} by frequency)"
                if total_unique > max_values
                else ""
            )
        ]
        for value, count in vc.iter_rows():
            lines.append(f"  {count:>6}  {value!r}")
        return "\n".join(lines)

    @staticmethod
    def _validate_unique_sample_ids(
        df: pl.DataFrame,
    ) -> None:
        expected = set(SampleMetadata.model_fields)
        actual = set(df.columns)
        if expected != actual:
            raise ValueError(
                f"Invalid metadata columns.\n"
                f"Expected: {sorted(expected)}\n"
                f"Actual: {sorted(actual)}"
            )

        duplicates = df.filter(
            pl.col("sample_id").is_not_null()
            & pl.struct("dataset_id", "sample_id").is_duplicated()
        )

        if not duplicates.is_empty():
            raise ValueError(
                f"Duplicate (dataset_id, sample_id) detected:\n{duplicates}"
            )
