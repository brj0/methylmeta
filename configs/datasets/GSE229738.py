def dataset_id(row):
    return "GSE229738"


def description(row):
    return (
        "Peripheral blood DNA methylation in adult-onset Still's disease "
        "compared with T cell lymphoma, sepsis, drug eruption and healthy "
        "controls"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    value = row["disease state"]
    mapping = {
        "T cell lymphoma": "TCL_NOS",
        "adult onset still's disease": None,
        "drug eruption": None,
        "normal": "CTRL_BLOOD",
        "sepsis": None,
    }
    return mapping[value]


def sample_site(row):
    return "peripheral blood"


def sample_type(row):
    value = row["disease state"]
    mapping = {
        "T cell lymphoma": "primary",
        "adult onset still's disease": "primary",
        "drug eruption": "primary",
        "normal": "control",
        "sepsis": "primary",
    }
    return mapping[value]


def material_type(row):
    return "blood"


def sex(row):
    return row["gender"]


def age(row):
    value = row["age"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
