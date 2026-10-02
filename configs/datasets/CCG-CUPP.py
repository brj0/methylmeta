def dataset_id(row):
    return "CCG-CUPP"


def description(row):
    return "Metastatic carcinoma of unknown primary cohort"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    _HISTOLOGY = {
        "Cholangiocarcinoma": "CCA",
        "Desmoplastic small round cell tumor": "DSRCT",
        "Squamous cell carcinoma, NOS": "SCC",
        "Squamous cell carcinoma, metastatic, NOS": "SCC",
    }
    histology = row["diagnoses.primary_diagnosis"]
    return _HISTOLOGY.get(histology)


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {
        "Not Reported": None,
        "Unknown": None,
        "Unknown primary site": None,
    }
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "metastasis": "metastasis",
        "Progression": "recurrence",
        "Subsequent Primary": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["preservation_method"]]


def age(row):
    value = row["diagnoses.age_at_diagnosis"]
    if value is None:
        return None
    return round(float(value) / 365.25, 1)
