def dataset_id(row):
    return "GSE66881"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of ALK-positive and "
        "ALK-negative anaplastic large cell lymphoma and normal "
        "CD3-positive T cells"
    )


def sample_id(row):
    return row["Title"].split("(", 1)[1].rstrip(")")


def diagnosis(row):
    mapping = {
        "ALK positive tumor": "anaplastic large cell lymphoma, ALK-positive",
        "ALK negative tumor": "anaplastic large cell lymphoma, ALK-negative",
        "isolated CD3 cells": "CD3-positive T cells from peripheral blood",
    }
    return mapping[row["cell type"]]


def methylation_class(row):
    mapping = {
        "ALK positive tumor": "ALCL_ALK_POS",
        "ALK negative tumor": "ALCL_ALK_NEG",
        "isolated CD3 cells": "CTRL_BLOOD",
    }
    return mapping[row["cell type"]]


def sample_site(row):
    mapping = {
        "frozen_tumor": None,
        "PBMC": "Peripheral blood",
    }
    return mapping[row["Source"]]


def primary_site(row):
    mapping = {
        "frozen_tumor": "Lymphoid tissue",
        "PBMC": "Blood",
    }
    return mapping[row["Source"]]


def sample_type(row):
    mapping = {
        "anaplastic large cell lymphoma": "primary",
        "control": "control",
    }
    return mapping[row["disease state"]]


def material_type(row):
    mapping = {
        "frozen_tumor": "tissue",
        "PBMC": "blood",
    }
    return mapping[row["Source"]]


def preservation(row):
    mapping = {
        "frozen_tumor": "FROZEN",
        "PBMC": None,
    }
    return mapping[row["Source"]]
