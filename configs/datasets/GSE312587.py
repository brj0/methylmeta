def dataset_id(row):
    return "GSE312587"


def description(row):
    return (
        "DNA methylation-based stratification of pediatric thyroid "
        "carcinoma invasiveness (Children's Hospital of Philadelphia)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["Stage"] == "Lymph.Node.Met":
        return "Lymph node metastasis of thyroid carcinoma"
    return "Thyroid carcinoma"


def methylation_class(row):
    return "THYR_CA"


def sample_site(row):
    mapping = {
        "Primary": "Thyroid",
        "Lymph.Node.Met": "Lymph node",
    }
    return mapping[row["Stage"]]


def primary_site(row):
    return "Thyroid"


def sample_type(row):
    mapping = {
        "Primary": "primary",
        "Lymph.Node.Met": "metastasis",
    }
    return mapping[row["Stage"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
