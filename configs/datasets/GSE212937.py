def dataset_id(row):
    return "GSE212937"


def description(row):
    return "Healthy blood controls"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Blood, chemotherapy-related AML": "AML",
        "Blood, de novo AML": "AML",
        "Blood, healthy control": "CONTR_BLOOD",
        "Blood, radiotherapy-related AML": "AML",
        "Blood, therapy-related AML": "AML",
    }
    return mapping[value]


def sample_site(row):
    return "Blood"


def sample_type(row):
    value = row["Source"]
    mapping = {
        "Blood, chemotherapy-related AML": "primary",
        "Blood, de novo AML": "primary",
        "Blood, healthy control": "control",
        "Blood, radiotherapy-related AML": "primary",
        "Blood, therapy-related AML": "primary",
    }
    return mapping[value]


def sex(row):
    return row["gender"]


def age(row):
    return row["age"]
