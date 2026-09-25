def dataset_id(row):
    return "TARGET-CCSK"


def description(row):
    return "TARGET cohort of clear cell sarcoma of the kidney (CCSK)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnoses.primary_diagnosis"]


def methylation_class(row):
    return "REN_CCS"


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "metastasis": "metastasis",
        "recurrence": "recurrence",
        "control": "control",
        "Not Reported": None,
        "Unknown": None,
    }
    return mapping[value]


def primary_site(row):
    return "Kidney"


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {
        "Not Reported": None,
        "Unknown": None,
    }
    return mapping.get(value, value)


def material_type(row):
    return "tissue"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
