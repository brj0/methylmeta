def dataset_id(row):
    return "TARGET-RT"


def description(row):
    return "TARGET cohort of pediatric malignant rhabdoid tumors"


def _site(value):
    mapping = {
        "Kidney, NOS": "Kidney",
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping.get(value, value)


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnoses.primary_diagnosis"]


def methylation_class(row):
    return "MRT"


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "recurrence": "recurrence",
        "metastasis": "metastasis",
        "control": "control",
        "Not Reported": None,
        "Unknown": None,
    }
    return mapping.get(value)


def sample_site(row):
    return _site(row["diagnoses.tissue_or_organ_of_origin"])


def primary_site(row):
    return _site(row["diagnoses.tissue_or_organ_of_origin"])


def material_type(row):
    return "tissue"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
