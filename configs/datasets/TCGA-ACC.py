def dataset_id(row):
    return "TCGA-ACC"


def description(row):
    return "TCGA Adrenocortical Carcinoma (ACC), Zheng 2016"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Adrenal cortical carcinoma": "ADREN_CORT_CA",
        "Osteosarcoma, NOS": "OS_CONV",
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    if value == "Not Reported":
        return None
    if value == "Cortex of adrenal gland":
        return "Adrenal gland"
    return value.replace(", NOS", "")


def primary_site(row):
    return "Adrenal gland"


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "Prior primary": "primary",
        "Subsequent Primary": "primary",
        "Synchronous primary": "primary",
        "metastasis": "metastasis",
        "recurrence": "recurrence",
    }
    return mapping[value]


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
