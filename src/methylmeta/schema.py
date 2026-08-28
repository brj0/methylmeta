from __future__ import annotations

from enum import StrEnum

from mepylome.dtypes import ArrayType
from pydantic import BaseModel, Field


class SampleType(StrEnum):
    control = "control"
    primary = "primary"
    metastasis = "metastasis"
    recurrence = "recurrence"


class MaterialType(StrEnum):
    tissue = "tissue"
    cell_line = "cell_line"


class Preservation(StrEnum):
    FFPE = "FFPE"
    FROZEN = "FROZEN"
    FRESH = "FRESH"


class TumorGrade(StrEnum):
    G1 = "G1"
    G2 = "G2"
    G3 = "G3"
    G4 = "G4"
    low_grade = "low-grade"
    high_grade = "high-grade"


class Sex(StrEnum):
    male = "male"
    female = "female"


class SampleMetadata(BaseModel):
    """Canonical metadata schema for a biological sample."""

    dataset_id: str = Field(
        description=(
            "Identifier of the originating dataset/cohort/study "
            "(e.g. TCGA project code, GEO accession, ArrayExpress "
            "accession, or custom cohort name)"
        ),
    )

    description: str | None = Field(
        default=None,
        description=(
            "Text description or label summarizing the dataset or cohort"
        ),
    )

    sample_id: str = Field(
        description=(
            "Unique identifier for the biological sample (often sentrix id)"
        ),
    )

    diagnosis: str | None = Field(
        default=None,
        description=(
            "Histopathological or clinical primary tumor diagnosis "
            '(e.g. "pheochromocytoma", "glioblastoma")'
        ),
    )

    methylation_class: str | None = Field(
        default=None,
        description=(
            "Methylation-based classification result "
            '(e.g. "PCC", "GBM_RTK_II", "HNSCC")'
        ),
    )

    sample_site: str | None = Field(
        default=None,
        description=(
            "Anatomical site/organ from which the material was sampled "
            "(biopsy/resection location); may be primary or "
            "metastatic/recurrent"
        ),
    )

    primary_site: str | None = Field(
        default=None,
        description=(
            "Anatomical site/organ of the original primary tumor "
            "(may differ from sample_site in advanced cases)"
        ),
    )

    sample_type: SampleType | None = Field(
        default=None,
        description=(
            "Type or origin of the tumor sample "
            "(primary vs metastatic vs recurrent lesion)"
        ),
    )

    material_type: MaterialType | None = Field(
        default=None,
        description="Biological material from which DNA was obtained",
    )

    preservation: Preservation | None = Field(
        default=None,
        description=(
            "Tissue preservation or embedding method used for the sample"
        ),
    )

    tumor_grade: TumorGrade | None = Field(
        default=None,
        description="Histological tumor grade",
    )

    sex: Sex | None = Field(
        default=None,
        description="Sex of the patient",
    )

    age: int | None = Field(
        default=None,
        description="Age in years at sampling",
    )

    array_type: ArrayType | None = Field(
        default=None,
        description=(
            "Illumina methylation array type used to generate the sample data"
        ),
    )
