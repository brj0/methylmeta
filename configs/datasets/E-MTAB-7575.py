def dataset_id(row):
    return "E-MTAB-7575"


def description(row):
    return (
        "DNA methylation analysis over time in chronic lymphocytic leukemia "
        "cases treated with chemoimmunotherapy"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Characteristics[disease]"]
    if value == "normal":
        return "normal blood"
    return "chronic lymphocytic leukemia"


def methylation_class(row):
    value = row["Factor Value[disease]"]
    mapping = {
        "chronic lymphocytic leukemia": "CLL",
        "normal": "CTRL_BLOOD",
    }
    return mapping[value]


def sample_type(row):
    value = row["Characteristics[clinical history]"]
    mapping = {
        "healthy donor": "control",
        "pre-treatment": "primary",
        "post-relapse": "recurrence",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def material_type(row):
    return "blood"


def sex(row):
    value = row["Characteristics[sex]"]
    mapping = {
        "female": "female",
        "male": "male",
        "na": None,
        "not available": None,
    }
    return mapping[value]


def age(row):
    value = row["Characteristics[age]"]
    if not value.strip().isdigit():
        return None
    return float(value)
