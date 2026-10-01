def dataset_id(row):
    return "GSE312914"


def description(row):
    return (
        "DNA methylation-based stratification of pediatric thyroid "
        "carcinoma invasiveness"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Thyroid carcinoma"


def methylation_class(row):
    return "THYR_CA"


def sample_site(row):
    mapping = {"Primary": "Thyroid", "Lymph.Node.Met": "Lymph node"}
    return mapping[row["Stage"]]


def primary_site(row):
    return "Thyroid"


def sample_type(row):
    mapping = {"Primary": "primary", "Lymph.Node.Met": "metastasis"}
    return mapping[row["Stage"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
