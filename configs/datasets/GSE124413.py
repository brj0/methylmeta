def dataset_id(row):
    return "GSE124413"


def description(row):
    return "Methylation analysis of childhood acute myeloid leukemia (AML)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "AML, pre-treatment": "acute myeloid leukemia",
        "Bone marrow, normal": "normal bone marrow",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "AML, pre-treatment": "AML",
        "Bone marrow, normal": "CTRL_MARROW",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Bone marrow"


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    mapping = {
        "AML, pre-treatment": "primary",
        "Bone marrow, normal": "control",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "blood"


def preservation(row):
    return "FROZEN"


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping.get(value, value)


def age(row):
    value = row["age at diagnosis (days)"]
    if value is None:
        return None
    return float(value) / 365.25
