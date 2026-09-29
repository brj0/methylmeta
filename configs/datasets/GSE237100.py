def dataset_id(row):
    return "GSE237100"


def description(row):
    return (
        "Matched peripheral blood and tumor immune microenvironment "
        "profiles in bladder cancer"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Tumor": "Urothelial carcinoma of the bladder",
        "Blood": "Normal peripheral blood leukocytes",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "Tumor": "URO_CA",
        "Blood": "CTRL_BLOOD",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    mapping = {
        "Tumor": "Bladder",
        "Blood": "Blood",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return "Bladder"


def sample_type(row):
    mapping = {
        "Tumor": "primary",
        "Blood": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    mapping = {
        "Tumor": "tissue",
        "Blood": "blood",
    }
    return mapping[row["tissue"]]


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
