def dataset_id(row):
    return "GSE131013"


def description(row):
    return (
        "Healthy, adjacent normal and tumor colon methylation profiles "
        "(COLONOMICS project, 2019)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Tumor": "colorectal adenocarcinoma",
        "Normal": "adjacent normal colon mucosa",
        "Mucosa": "normal colon mucosa",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "Tumor": "CR_CA",
        "Normal": "CTRL_COL",
        "Mucosa": "CTRL_COL",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Colon"


def primary_site(row):
    return "Colon"


def sample_type(row):
    mapping = {
        "Tumor": "primary",
        "Normal": "control",
        "Mucosa": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Male": "male", "Female": "female"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
