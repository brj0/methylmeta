def dataset_id(row):
    return "GSE336418"


def description(row):
    return (
        "DNA methylation profiling of ATRT patient samples and SMARCB1-"
        "inducible I2A rhabdoid tumor cell line models"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["cell type"]
    mapping = {
        "Rhabdoid tumor": "Atypical teratoid/rhabdoid tumor",
        "Rhabdoid tumor cells": "Atypical teratoid/rhabdoid tumor cell line",
        "Meningioangiomatosis tumor": "Meningioangiomatosis",
    }
    return mapping[value]


def methylation_class(row):
    value = row["cell type"]
    mapping = {
        "Rhabdoid tumor": "ATRT",
        "Rhabdoid tumor cells": "ATRT",
        "Meningioangiomatosis tumor": None,
    }
    return mapping[value]


def sample_site(row):
    return "Central nervous system"


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    value = row["Source"]
    mapping = {
        "DNA from ATRT tumor patient": "tissue",
        "DNA from meningioangiomatosis tumor patient": "tissue",
        "I2A cells, DMSO-treated, control": "cell_line",
        "I2A cells, DNMT3A-knockout cells": "cell_line",
        "I2A cells, DNMT3B-knockout cells": "cell_line",
        "I2A cells, SMARCB1-positive, day 10 of reexpression": "cell_line",
        "I2A cells, SMARCB1-positive, day 14 of reexpression": "cell_line",
        "I2A cells, control": "cell_line",
    }
    return mapping[value]
