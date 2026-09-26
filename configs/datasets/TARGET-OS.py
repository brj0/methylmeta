def dataset_id(row):
    return "TARGET-OS"


def description(row):
    return "TARGET cohort of pediatric osteosarcoma (OS), Chen 2014"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnoses.primary_diagnosis"]


def methylation_class(row):
    return "OS"


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {
        "Not Reported": None,
        "Unknown": None,
    }
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {
        "Not Reported": None,
        "Unknown": None,
    }
    return mapping.get(value, "Bone")


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
    return mapping[value]


def material_type(row):
    return "tissue"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
