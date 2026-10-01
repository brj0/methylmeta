def dataset_id(row):
    return "GSE93646"


def description(row):
    return (
        "Primary medulloblastoma methylation profiles (Schwalbe et al. 2017)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "CLA": "Classic medulloblastoma",
        "DN": "Desmoplastic/nodular medulloblastoma",
        "LCA": "Large cell/anaplastic medulloblastoma",
        "MBEN": "Medulloblastoma with extensive nodularity",
        "NOS": "Medulloblastoma, NOS",
    }
    return mapping[row["pathology"]]


def methylation_class(row):
    return "MB"


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age (yrs)"])
