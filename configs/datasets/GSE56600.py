def dataset_id(row):
    return "GSE56600"


def description(row):
    return "Methylation data of pediatric B-cell acute leukemias"


def sample_id(row):
    return row["Title"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    value = row["cytogenetics"]
    mapping = {
        "ETV6/RUNX1": "B_ALL_ETV6_RUNX1",
        "MLL": "B_ALL_KMT2A",
        "TCF3/PBX1": "B_ALL_TCF3_PBX1",
        "hyperdiploid": "B_ALL_HYPERDIP",
        "others": "B_ALL",
        "unknown": "B_ALL",
    }
    return mapping[value]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def sex(row):
    value = row["gender"]
    if value is None:
        return None
    mapping = {"F": "female", "M": "male"}
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
