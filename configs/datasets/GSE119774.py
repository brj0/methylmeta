def dataset_id(row):
    return "GSE119774"


def description(row):
    return (
        "Chromatin landscapes of glioblastoma, glioblastoma stem cell "
        "models and neural stem cells, Mack 2019"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["cell type"]
    mapping = {
        "primary glioblastomas": "Glioblastoma",
        "glioblastoma stem cell model": "Glioblastoma stem cell model",
        "neural stem cells": "Normal neural stem cells",
    }
    return mapping[value]


def methylation_class(row):
    value = row["cell type"]
    mapping = {
        "primary glioblastomas": "GBM_NOS",
        "glioblastoma stem cell model": "GBM_NOS",
        "neural stem cells": "CTRL_BRAIN_GBM",
    }
    return mapping[value]


def sample_site(row):
    return "Brain"


def primary_site(row):
    if row["cell type"] == "neural stem cells":
        return None
    return "Brain"


def sample_type(row):
    value = row["cell type"]
    mapping = {
        "primary glioblastomas": "primary",
        "glioblastoma stem cell model": "primary",
        "neural stem cells": "control",
    }
    return mapping[value]


def material_type(row):
    value = row["cell type"]
    mapping = {
        "primary glioblastomas": "tissue",
        "glioblastoma stem cell model": "cell_line",
        "neural stem cells": "cell_line",
    }
    return mapping[value]
