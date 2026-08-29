from __future__ import annotations

import logging
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


class MetadataHarmonizer:
    """Harmonize one dataset into the canonical metadata schema."""

    def __init__(
        self,
        dataset: ModuleType,
        strict: bool = True,
    ) -> None:
        self.dataset = dataset
        self.strict = strict

    def harmonize(self, raw: pl.DataFrame) -> pl.DataFrame:
        """Harmonize a raw annotation table."""
        rows = [self._harmonize_row(row) for row in raw.iter_rows(named=True)]

        if not rows:
            return pl.DataFrame()

        data = [metadata.model_dump(mode="python") for metadata in rows]

        return pl.DataFrame(data, infer_schema_length=None)

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


class MetadataMerger:
    """Merge harmonized metadata from multiple datasets."""

    def __init__(
        self,
        config_dir: str | Path,
        strict: bool = True,
        idat_dir: str | Path | None = None,
    ) -> None:
        self.config_dir = Path(config_dir)
        self.strict = strict

        self.id_to_basepath: dict[str, Path] = {}

        if idat_dir is not None:
            from mepylome.dtypes.beads import idat_basepaths

            basepaths = idat_basepaths(Path(idat_dir))
            self.id_to_basepath = {p.name: p for p in basepaths}

    def merge_directory(
        self,
        input_dir: str | Path,
    ) -> pl.DataFrame:
        """Harmonize and merge all datasets in a directory."""
        input_dir = Path(input_dir)

        config_paths = sorted(self.config_dir.glob("*.py"))

        if not config_paths:
            raise ValueError(
                f"No dataset Python files found in {self.config_dir}"
            )

        merged: list[pl.DataFrame] = []

        for config_path in config_paths:
            dataset = load_dataset_module(config_path)
            dataset_id = dataset.dataset_id(None)

            dataset_dir = input_dir / dataset_id

            if not dataset_dir.is_dir():
                if self.strict:
                    raise FileNotFoundError(
                        f"{dataset_id}: directory not found: {dataset_dir}"
                    )

                logger.warning(
                    "Skipping %s: no data directory",
                    dataset_id,
                )
                continue

            annotation_file = dataset_dir / "annotation.csv"

            if not annotation_file.exists():
                if self.strict:
                    raise FileNotFoundError(
                        f"{dataset_id}: annotation.csv not found"
                    )

                logger.warning(
                    "Skipping %s: annotation.csv not found",
                    dataset_id,
                )
                continue

            logger.info("Processing %s", dataset_id)

            raw = pl.read_csv(
                annotation_file,
                infer_schema_length=10000,
                null_values=[
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
                ],
            )

            harmonizer = MetadataHarmonizer(
                dataset=dataset,
                strict=self.strict,
            )

            merged.append(harmonizer.harmonize(raw))

        if not merged:
            raise ValueError("No datasets were processed.")

        result = pl.concat(
            merged,
            how="vertical_relaxed",
        ).unique()

        self._validate_unique_sample_ids(result)

        return result

    @staticmethod
    def _validate_unique_sample_ids(
        df: pl.DataFrame,
    ) -> None:
        if "sample_id" not in df.columns:
            raise ValueError("Missing required column: sample_id")

        duplicates = df.filter(
            pl.col("sample_id").is_not_null()
            & pl.col("sample_id").is_duplicated()
        )

        if not duplicates.is_empty():
            raise ValueError(f"Duplicate sample_id detected:\n{duplicates}")
