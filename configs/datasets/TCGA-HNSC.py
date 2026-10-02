def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    if not barcode:
        return None
    return barcode.split("-")[-1][:2]


def dataset_id(row):
    return "TCGA-HNSC"


def description(row):
    return (
        "TCGA Head and Neck Squamous Cell Carcinoma (HNSC), "
        "Cancer Genome Atlas Network 2015"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _sample_type_code(row) == "11":
        return "Normal head and neck tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None, None: None}
    return mapping.get(value, value)


def methylation_class(row):
    if _sample_type_code(row) == "11":
        return "CTRL_HN"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Squamous cell carcinoma, NOS": "HN_SCC",
        "Squamous cell carcinoma, keratinizing, NOS": "HN_SCC",
        "Squamous cell carcinoma, large cell, nonkeratinizing, NOS": "HN_SCC",
        "Squamous cell carcinoma, spindle cell": "HN_SCC",
        "Basaloid squamous cell carcinoma": "HN_SCC",
        "Basal cell carcinoma, NOS": "BCC",
        "Follicular lymphoma, NOS": "FL",
        "Clear cell carcinoma": "RCC_CC",
        "Adenocarcinoma, NOS": None,
        "Papillary adenocarcinoma, NOS": None,
        "Papillary carcinoma, follicular variant": "THYR_PTC",
        "Not Reported": None,
        None: None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None, None: None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown": None, None: None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {
        "01": "primary",
        "02": "recurrence",
        "06": "metastasis",
        "11": "control",
    }
    return mapping.get(_sample_type_code(row))


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["diagnoses.tumor_grade"]
    mapping = {
        "G1": "G1",
        "G2": "G2",
        "G3": "G3",
        "G4": "G4",
        "GX": None,
        None: None,
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
