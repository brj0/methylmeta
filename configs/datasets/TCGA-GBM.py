def dataset_id(row):
    return "TCGA-GBM"


def description(row):
    return "TCGA Glioblastoma Multiforme (GBM), Ceccarelli 2016"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Glioblastoma": "Glioblastoma",
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping[value]


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Glioblastoma": "GBM_NOS",
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {
        "Brain, NOS": "Brain",
        "Not Reported": None,
        None: None,
    }
    return mapping[value]


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {
        "Brain, NOS": "Brain",
        "Frontal lobe": "Frontal lobe",
        "Occipital lobe": "Occipital lobe",
        "Temporal lobe": "Temporal lobe",
        "Prostate gland": "Prostate",
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping[value]


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "Prior primary": "primary",
        "recurrence": "recurrence",
        "Progression": "recurrence",
        "Unknown": None,
        "not reported": None,
        None: None,
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["preservation_method"]
    mapping = {
        "Unknown": None,
        "OCT": "FROZEN",
    }
    return mapping[value]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
