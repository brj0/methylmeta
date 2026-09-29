def dataset_id(row):
    return "GSE261443"


def description(row):
    return "TERT expression and clinical outcome in pulmonary carcinoids"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["histopathology"]
    mapping = {
        "typical": "typical carcinoid of the lung",
        "atypical": "atypical carcinoid of the lung",
    }
    return mapping.get(value, "carcinoid tumour of the lung")


def methylation_class(row):
    value = row["histopathology"]
    mapping = {
        "typical": "LU_NET_TYP",
        "atypical": "LU_NET_ATYP",
    }
    return mapping.get(value, "LU_NET")


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
