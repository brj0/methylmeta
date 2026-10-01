def dataset_id(row):
    return "GSE70460"


def description(row):
    return (
        "Atypical teratoid/rhabdoid tumors of the central nervous system "
        "(Johann et al. 2016)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Atypical teratoid/rhabdoid tumor"


def methylation_class(row):
    return "ATRT"


def sample_site(row):
    mapping = {
        "supratentorial": "Supratentorial",
        "infratentorial": "Infratentorial",
    }
    return mapping.get(row["localization within the brain"])


def primary_site(row):
    mapping = {
        "supratentorial": "Supratentorial",
        "infratentorial": "Infratentorial",
    }
    return mapping.get(row["localization within the brain"])


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "male": "male",
        "female": "female",
        "M": "male",
        "F": "female",
    }
    value = row["gender"]
    if value is None:
        value = row["tissue_1"]
    return mapping.get(value)


def age(row):
    value = row["age at diagnosis"]
    if value is None:
        return None
    return float(value)
