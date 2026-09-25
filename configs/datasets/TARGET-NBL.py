def dataset_id(row):
    return "TARGET-NBL"


def description(row):
    return "TARGET cohort of neuroblastoma (NBL), Pugh 2013"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnoses.primary_diagnosis"]


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Neuroblastoma, NOS": "NBL",
        "Ganglioneuroblastoma": "GNBL",
        None: None,
    }
    return mapping[value]


def sample_type(row):
    if row["diagnoses.primary_diagnosis"] is None:
        return "control"
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "recurrence": "recurrence",
        "metastasis": "metastasis",
        "control": "control",
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping[value]


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {
        "Unknown": None,
        "Unknown primary site": None,
    }
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def material_type(row):
    return "tissue"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
