from __future__ import annotations

import logging
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from typing import Any

import polars as pl

from methylmeta.loader import load_dataset_module
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
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return pl.read_csv(
            path,
            infer_schema_length=10000,
            null_values=CSV_NULL_VALUES,
        )

    if suffix == ".tsv":
        return pl.read_csv(
            path,
            separator="\t",
            infer_schema_length=10000,
            null_values=CSV_NULL_VALUES,
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
        lines = [
            f"name: {self.name}",
            f"dtype: {self.dtype}",
            f"n_null: {self.n_null}",
            f"n_unique: {self.n_unique}",
            f"is_constant: {self.is_constant}",
            f"is_low_cardinality: {self.is_low_cardinality}",
            f"sample_values: {self.sample_values}",
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

    def summary(self) -> str:
        lines = [
            "DATASET",
            f"dataset_id: {self.dataset_id}",
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

    @property
    def success(self) -> bool:
        return not self.errors

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

    def summary(self, max_examples: int = 2) -> str:
        lines = [
            f"{self.dataset_id}: {self.ok_rows}/{self.total_rows} rows OK",
        ]

        if self.errors:
            lines.append(f"{len(self.errors)} row(s) failed:")
            for error_msg, rows in self.grouped_errors().items():
                lines.append(f"  [{len(rows)}x] {error_msg}")
                for row_err in rows[:max_examples]:
                    lines.append(
                        f"      e.g. row {row_err.row_index}: {row_err.raw_row}"
                    )
        else:
            lines.append("All rows harmonized successfully.")

        return "\n".join(lines)


class MetadataHarmonizer:
    """Harmonize one dataset into the canonical metadata schema."""

    def __init__(
        self,
        dataset: ModuleType,
    ) -> None:
        self.dataset = dataset

    def harmonize(self, raw: pl.DataFrame) -> pl.DataFrame:
        """Harmonize a raw metadata table."""
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


def find_metadata_file(dataset_dir: Path) -> Path:
    extensions = {".csv", ".tsv", ".xlsx", ".xls"}

    files = sorted(
        p
        for p in dataset_dir.iterdir()
        if p.is_file() and p.suffix.lower() in extensions
    )

    if len(files) != 1:
        raise ValueError(
            f"Expected exactly one metadata in {dataset_dir}, "
            f"found {len(files)}: {[p.name for p in files]}"
        )

    return files[0]


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
        # -> ["GSE999999"]  (this is what an agent should generate .py files for)

        # 2. Once configs/datasets/GSE999999.py exists, merge just what you want.
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
    """

    def __init__(
        self,
        config_dir: str | Path,
        dataset_dir: str | Path,
        strict: bool = True,
    ) -> None:
        self.config_dir = Path(config_dir)
        self.dataset_dir = Path(dataset_dir)
        self.strict = strict

        self._id_to_config: dict[str, Path] | None = None

    def _index_configs(self) -> dict[str, Path]:
        """Build (once) the dataset_id -> config .py path index.

        A dataset's identity is whatever `dataset_id(row)` returns, not its
        filename, so every config has to be loaded once to build this index.
        """
        if self._id_to_config is not None:
            return self._id_to_config

        config_paths = sorted(self.config_dir.glob("*.py"))

        if not config_paths:
            raise ValueError(
                f"No dataset config .py files found in {self.config_dir}. "
                "config_dir should point at your harmonizer configs (e.g. "
                "'configs/datasets'), not at a raw-data/download directory "
                "- double check you haven't swapped config_dir and dataset_dir."
            )

        index: dict[str, Path] = {}
        for config_path in config_paths:
            dataset = load_dataset_module(config_path)
            dataset_id = dataset.dataset_id(None)

            if dataset_id in index:
                raise ValueError(
                    f"Duplicate dataset_id {dataset_id!r}: "
                    f"{index[dataset_id]} and {config_path}"
                )
            index[dataset_id] = config_path

        self._id_to_config = index
        return index

    def available_datasets(self) -> list[str]:
        """Dataset IDs that already have a config .py file."""
        return sorted(self._index_configs())

    def missing_configs(self, dataset_ids: Iterable[str]) -> list[str]:
        """Which of `dataset_ids` have no config .py file yet.

        This is the hand-off point for a future agent: whatever comes back
        here is what it needs to write configs/datasets/<id>.py for.
        """
        index = self._index_configs()
        return [d for d in dataset_ids if d not in index]

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
        index = self._index_configs()

        if dataset_ids is not None:
            dataset_ids = list(dataset_ids)
            missing = [d for d in dataset_ids if d not in index]
            if missing:
                raise ValueError(
                    f"No config found for: {missing}. Generate these "
                    "configs first (see missing_configs())."
                )
        else:
            dataset_ids = sorted(index)

        if not dataset_ids:
            raise ValueError("No dataset IDs to merge.")

        merged: list[pl.DataFrame] = []

        for dataset_id in dataset_ids:
            config_path = index[dataset_id]
            dataset_path = self.dataset_dir / dataset_id

            if not dataset_path.is_dir():
                if self.strict:
                    raise FileNotFoundError(
                        f"{dataset_id}: directory not found: {dataset_path}"
                    )
                logger.warning("Skipping %s: no data directory", dataset_id)
                continue

            metadata_file = find_metadata_file(dataset_path)

            logger.info("Processing %s", dataset_id)

            dataset = load_dataset_module(config_path)
            raw = read_metadata(metadata_file)

            harmonizer = MetadataHarmonizer(dataset=dataset)
            merged.append(harmonizer.harmonize(raw))

        if not merged:
            raise ValueError("No datasets were processed.")

        result = pl.concat(merged, how="vertical_relaxed").unique()
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
                basepaths_by_dataset[dataset_id] = {
                    p.name: p for p in found
                }

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

    def profile(
        self,
        dataset_id: str,
        max_unique: int = 15,
    ) -> DatasetProfile:
        """Summarize a raw metadata column and value distributions.

        Deliberately doesn't require a config to exist - this is the step
        that comes *before* writing one, so you (or an agent) can see real
        column names and values instead of guessing at a value_mapping dict.
        """
        metadata_file = find_metadata_file(self.dataset_dir / dataset_id)

        raw = read_metadata(metadata_file)

        columns = []
        for name in raw.columns:
            column = raw[name]
            uniques = column.drop_nulls().unique().to_list()
            n_unique = len(uniques)
            is_low_cardinality = n_unique <= max_unique
            sample_values = sorted(str(v) for v in uniques[:max_unique])
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
            dataset_id=dataset_id, n_rows=raw.height, columns=columns
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
        index = self._index_configs()
        if dataset_id not in index:
            raise ValueError(
                f"No config found for {dataset_id!r} (see missing_configs())."
            )

        metadata_file = find_metadata_file(self.dataset_dir / dataset_id)

        dataset = load_dataset_module(index[dataset_id])
        raw = read_metadata(metadata_file)

        harmonizer = MetadataHarmonizer(dataset=dataset)
        return harmonizer.test(raw, dataset_id=dataset_id)

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
                "Duplicate (dataset_id, sample_id) detected:\n"
                f"{duplicates}"
            )
