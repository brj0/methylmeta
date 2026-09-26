def dataset_id(row):
    return "GSE163372"


def description(row):
    return (
        "DNA methylation of matched normal kidney, Wilms tumor and "
        "metastatic lung samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Wilms tumor": "Wilms tumor, blastemal component",
        "metastatic tissue": "metastatic Wilms tumor (lung)",
        "normal kidney": "normal kidney cortex",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "Wilms tumor": "WILMS",
        "metastatic tissue": "WILMS",
        "normal kidney": "CTRL_REN",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    mapping = {
        "Wilms tumor": "Kidney",
        "metastatic tissue": "Lung",
        "normal kidney": "Kidney",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return "Kidney"


def sample_type(row):
    mapping = {
        "Wilms tumor": "primary",
        "metastatic tissue": "metastasis",
        "normal kidney": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
