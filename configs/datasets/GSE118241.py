def dataset_id(row):
    return "GSE118241"


def description(row):
    return (
        "Genome-wide enhancer-related DNA methylation in myelofibrosis "
        "patients and healthy controls"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    if row["disease state"] == "control":
        return "normal " + row["cell type"].lower()
    mapping = {
        "primary MF": "primary myelofibrosis",
        "MFI post-ET": "myelofibrosis post-essential thrombocythemia",
        "MFI post-PV": "myelofibrosis post-polycythemia vera",
    }
    return mapping[row["status"]]


def methylation_class(row):
    if row["disease state"] == "control":
        mapping = {
            "Bone marrow cells": "CTRL_MARROW",
            "Granulocytes from peripheral blood": "CTRL_BLOOD",
            "Peripheral blood cells": "CTRL_BLOOD",
        }
        return mapping[row["cell type"]]
    # MFI post-ET / post-PV are secondary myelofibrosis; the vocabulary has
    # no class for those, so the broader MPN_NOS is used.
    mapping = {
        "primary MF": "PMF",
        "MFI post-ET": "MPN_NOS",
        "MFI post-PV": "MPN_NOS",
    }
    return mapping[row["status"]]


def sample_site(row):
    mapping = {
        "Bone marrow cells": "Bone marrow",
        "Granulocytes from peripheral blood": "Peripheral blood",
        "Peripheral blood cells": "Peripheral blood",
    }
    return mapping[row["cell type"]]


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    if row["disease state"] == "control":
        return "control"
    return "primary"


def material_type(row):
    return "blood"
