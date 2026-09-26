def dataset_id(row):
    return "GSE179175"


def description(row):
    return "DNA methylation profiling of pediatric adrenocortical tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["histopathological classification"]
    mapping = {
        "Adenoma": "Adrenal cortical adenoma",
        "Carcinoma": "Adrenal cortical carcinoma",
        "Uncertain malignant potential": (
            "Adrenal cortical tumor of uncertain malignant potential"
        ),
        "Unavailable": "Pediatric adrenocortical tumor",
    }
    return mapping[value]


def methylation_class(row):
    value = row["histopathological classification"]
    mapping = {
        "Adenoma": "ADREN_CORT_AD",
        "Carcinoma": "ADREN_CORT_CA",
        # Vague category
        "Uncertain malignant potential": "ADREN_CORT_AD",
        "Unavailable": None,
    }
    return mapping[value]


def sample_site(row):
    return "Adrenal gland"


def primary_site(row):
    return "Adrenal gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]


def age(row):
    value = row["age (years)"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
