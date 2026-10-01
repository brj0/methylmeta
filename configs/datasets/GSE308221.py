def dataset_id(row):
    return "GSE308221"


def description(row):
    return (
        "DNA methylation profiling of pediatric adrenocortical carcinoma "
        "(pACT)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "adrenocortical carcinoma"


def methylation_class(row):
    return "ADREN_CORT_CA"


def sample_site(row):
    return "Adrenal gland"


def primary_site(row):
    return "Adrenal gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Sex"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]


def age(row):
    value = row["age at diagnosis (years)"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
