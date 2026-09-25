def dataset_id(row):
    return "GSE146003"


def description(row):
    return "Global DNA methylation patterns in primary anaplastic thyroid cancer"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "anaplastic thyroid cancer sample": "anaplastic thyroid cancer",
        "normal thyroid tissue": "normal thyroid tissue",
    }
    return mapping.get(value, value)


def methylation_class(row):
    mapping = {
        "anaplastic thyroid cancer sample": "THYR_ANA_CA",
        "normal thyroid tissue": "CTRL_THYR",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Thyroid"


def primary_site(row):
    if row["tissue"] == "normal thyroid tissue":
        return None
    return "Thyroid"


def sample_type(row):
    mapping = {
        "anaplastic thyroid cancer sample": "primary",
        "normal thyroid tissue": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
