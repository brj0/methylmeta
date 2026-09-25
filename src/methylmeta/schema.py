from __future__ import annotations

import typing
from enum import Enum, StrEnum
from functools import lru_cache
from typing import Any

import yaml
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
    blood = "blood"


class Preservation(StrEnum):
    FFPE = "FFPE"
    FROZEN = "FROZEN"
    FRESH = "FRESH"


class TumorGrade(StrEnum):
    G0 = "G0"
    G1 = "G1"
    G2 = "G2"
    G3 = "G3"
    G4 = "G4"
    low_grade = "low-grade"
    high_grade = "high-grade"
    gleason_6 = "Gleason 6"
    gleason_7 = "Gleason 7"
    gleason_8 = "Gleason 8"
    gleason_9 = "Gleason 9"
    gleason_10 = "Gleason 10"
    isup_1 = "ISUP 1"
    isup_2 = "ISUP 2"
    isup_3 = "ISUP 3"
    isup_4 = "ISUP 4"
    isup_5 = "ISUP 5"


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
            "Short description of the dataset or cohort. Include the first "
            "author and publication year when known."
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
            '(e.g. "PCC", "GBM_RTK2", "HNSCC")'
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
            "Type or origin of the tumor sample: one of control, primary, "
            "metastasis, recurrence"
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


def _unwrap_field_type(annotation: object) -> Any:
    """Strip an `X | None` annotation down to the bare underlying type."""
    args = [a for a in typing.get_args(annotation) if a is not type(None)]
    return args[0] if len(args) == 1 else annotation


@lru_cache(maxsize=1)
def enum_valued_fields() -> dict[str, type[Enum]]:
    """Return {field_name: EnumClass} for every enum-typed SampleMetadata.

    field. This is the single source of truth for "which canonical fields
    are constrained to a fixed vocabulary, and what that vocabulary is" -
    used both to describe the fields to the config-writing agent and to
    statically validate generated configs before they touch real data.
    """
    fields: dict[str, type[Enum]] = {}
    for name, info in SampleMetadata.model_fields.items():
        display_type = _unwrap_field_type(info.annotation)
        if isinstance(display_type, type) and issubclass(display_type, Enum):
            fields[name] = display_type
    return fields


def describe_fields() -> str:
    """Render every canonical field's name, type, and description.

    Pulled live from SampleMetadata rather than duplicated by hand
    elsewhere (e.g. in the config-writing spec), so it can't drift out of
    sync when a field is added, renamed, or redescribed.
    """
    lines = []
    for name, info in SampleMetadata.model_fields.items():
        annotation = info.annotation
        args = [a for a in typing.get_args(annotation) if a is not type(None)]
        display_type = args[0] if len(args) == 1 else annotation
        type_name = getattr(display_type, "__name__", str(display_type))

        if isinstance(display_type, type) and issubclass(display_type, Enum):
            choices = ", ".join(repr(m.value) for m in display_type)
            type_name = f"{type_name} ({choices})"

        required = " (required)" if info.is_required() else ""
        lines.append(
            f"{name}: {type_name}{required} - {info.description or ''}"
        )
    return "\n".join(lines)
