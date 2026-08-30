from __future__ import annotations

from enum import StrEnum
from functools import lru_cache

import yaml
from mepylome.dtypes import ArrayType
from pydantic import BaseModel, Field, field_validator

from methylmeta.paths import TUMOR_TYPES_PATH


@lru_cache(maxsize=1)
def load_valid_methylation_classes() -> frozenset[str]:
    """Return the set of WHO-standard acronyms defined in tumor_types.yaml.

    This is the single source of truth for `methylation_class`: any value
    assigned in a dataset config must be a key in tumor_types.yaml.
    """
    with TUMOR_TYPES_PATH.open() as f:
        tumor_types = yaml.safe_load(f)["tumor_types"]
    return frozenset(tumor_types)


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

    sample_id: str | None = Field(
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

    age: float | None = Field(
        default=None,
        description="Age in years at sampling",
    )

    array_type: ArrayType | None = Field(
        default=None,
        description=(
            "Illumina methylation array type used to generate the sample data"
        ),
    )

    @field_validator("methylation_class")
    @classmethod
    def validate_methylation_class(cls, value: str | None) -> str | None:
        if value is None:
            return value

        valid = load_valid_methylation_classes()

        if value not in valid:
            raise ValueError(
                f"methylation_class {value!r} is not a WHO acronym defined "
                "in data/tumor_types.yaml. Add it there first if it is a "
                "genuinely new entity, or fix the dataset config if it's a "
                "typo/legacy acronym."
            )

        return value


def describe_fields() -> str:
    """Render every canonical field's name, type, and description.

    Pulled live from SampleMetadata rather than duplicated by hand
    elsewhere (e.g. in the config-writing spec), so it can't drift out of
    sync when a field is added, renamed, or redescribed.
    """
    import typing

    lines = []
    for name, info in SampleMetadata.model_fields.items():
        annotation = info.annotation
        args = [a for a in typing.get_args(annotation) if a is not type(None)]
        display_type = args[0] if len(args) == 1 else annotation
        type_name = getattr(display_type, "__name__", str(display_type))

        required = " (required)" if info.is_required() else ""
        lines.append(
            f"{name}: {type_name}{required} - {info.description or ''}"
        )
    return "\n".join(lines)
