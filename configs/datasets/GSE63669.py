def dataset_id(row):
    return "GSE63669"


def description(row):
    return "DNA methylation of matched primary-metastases medulloblastomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["cell type"]


def methylation_class(row):
    return "MB"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    mapping = {
        "primary": "primary",
        "metastasis": "metastasis",
    }
    return mapping[row["tumor type"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping.get(row["Sex"])


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
