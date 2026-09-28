def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    if not barcode:
        return None
    return barcode.split("-")[-1][:2]


def dataset_id(row):
    return "TCGA-KIRC"


def description(row):
    return (
        "TCGA Kidney Renal Clear Cell Carcinoma (KIRC), TCGA Research Network "
        "2013"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _sample_type_code(row) == "11":
        return "Normal kidney tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None, None: None}
    return mapping.get(value, value)


def methylation_class(row):
    if _sample_type_code(row) == "11":
        return "CTRL_REN"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Clear cell adenocarcinoma, NOS": "RCC_CC",
        "Clear cell carcinoma": "RCC_CC",
        "Renal cell carcinoma, NOS": "RCC_NOS",
        "Adenocarcinoma, NOS": "RCC_NOS",
        "Transitional cell carcinoma": "URO_CA",
        "Transitional cell carcinoma in situ": "URO_CIS",
        "Squamous cell carcinoma, NOS": None,
        "Squamous cell carcinoma, clear cell type": None,
        "Adenosquamous carcinoma": "ASC",
        "Melanoma, NOS": "MEL",
        "Malignant melanoma, NOS": "MEL",
        "Papillary carcinoma, follicular variant": "THYR_PTC",
        "Papillary microcarcinoma": "THYR_PTC",
        "Pituitary adenoma, NOS": "PIT_AD",
        "Chronic lymphocytic leukemia": "CLL",
        "Neuroendocrine carcinoma, NOS": "NEC",
        "Carcinoid tumor, NOS": None,
        "Mucinous adenocarcinoma": None,
        "Malignant lymphoma, non-Hodgkin, NOS": None,
        "Not Reported": None,
        None: None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None, None: None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, None: None}
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
