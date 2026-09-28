def dataset_id(row):
    return "GSE202067"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of giant cell tumour of bone, "
        "aneurysmal bone cyst, chondroblastoma, non-ossifying fibroma, brown "
        "tumour, mesenchymal stem cells and osteoblasts"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "ABC": "aneurysmal bone cyst",
        "BT": "brown tumour of hyperparathyroidism",
        "CB": "chondroblastoma",
        "GCTB": "giant cell tumour of bone",
        "MSC": "normal mesenchymal stem cells",
        "NOF": "non-ossifying fibroma",
        "OB": "normal osteoblasts",
    }
    return mapping[row["Description"]]


def methylation_class(row):
    mapping = {
        "ABC": "ABC",
        "BT": "BROWN",
        "CB": "CHONDBL",
        "GCTB": "GCTB",
        "MSC": "CTRL_BONE",
        "NOF": "NOF",
        "OB": "CTRL_BONE",
    }
    return mapping[row["Description"]]


def sample_site(row):
    value = row["location"]
    mapping = {"-": None, "n/a": None}
    return mapping.get(value, value)


def primary_site(row):
    return "Bone"


def sample_type(row):
    mapping = {
        "normal, passage 2-3": "control",
        "primary tumour": "primary",
        "pulmonary metastasis": "metastasis",
        "recurrence": "recurrence",
    }
    return mapping[row["disease state"]]


def material_type(row):
    mapping = {
        "cell line": "cell_line",
        "cell line of GCTB1P": "cell_line",
        "cell line of GCTB2P": "cell_line",
        "cell line of GCTB3M": "cell_line",
        "cell line of GCTB3R1": "cell_line",
        "cell line of GCTB4P": "cell_line",
        "cell line of GCTB7P": "cell_line",
        "cultivated cells": "cell_line",
        "cryo-preserved fresh tissue": "tissue",
        "formalin-fixed, paraffin-embedded tissue": "tissue",
    }
    return mapping[row["sample type"]]


def preservation(row):
    value = row["sample type"]
    mapping = {
        "cryo-preserved fresh tissue": "FROZEN",
        "formalin-fixed, paraffin-embedded tissue": "FFPE",
    }
    return mapping.get(value)


def sex(row):
    return row["gender"]


def age(row):
    return row["age"]
