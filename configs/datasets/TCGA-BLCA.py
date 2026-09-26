def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    return barcode.split("-")[-1][:2]


def dataset_id(row):
    return "TCGA-BLCA"


def description(row):
    return "TCGA Bladder Urothelial Carcinoma (BLCA), Robertson 2017"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _sample_type_code(row) == "11":
        return "Normal bladder tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if _sample_type_code(row) == "11":
        return "CTRL_BLA"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        # 8120/3 Conventional urothelial carcinoma
        "Transitional cell carcinoma": "URO_CA",
        # 8130/3 Papillary transitional cell carcinoma, WHO 4
        "Papillary transitional cell carcinoma": "URO_CA",
        "Papillary transitional cell carcinoma, non-invasive": "URO_CA_NI_PAP",
        "Carcinoma in situ, NOS": "URO_CIS",
        "Carcinoma, NOS": "URO_CA",
        "Squamous cell carcinoma, NOS": "URO_SCC",
        "Squamous cell carcinoma, clear cell type": "URO_SCC",
        "Adenocarcinoma, NOS": "URO_CA",
        "Papillary adenocarcinoma, NOS": "URO_CA",
        "Basal cell carcinoma, NOS": "BCC",
        "Gastrointestinal stromal tumor, NOS": "GIST",
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Transitional cell carcinoma": "Bladder",
        "Papillary transitional cell carcinoma": "Bladder",
        "Papillary transitional cell carcinoma, non-invasive": "Bladder",
        "Carcinoma in situ, NOS": "Bladder",
        "Carcinoma, NOS": "Bladder",
        "Squamous cell carcinoma, NOS": "Bladder",
        "Squamous cell carcinoma, clear cell type": "Bladder",
        "Adenocarcinoma, NOS": "Bladder",
        "Papillary adenocarcinoma, NOS": "Bladder",
        "Basal cell carcinoma, NOS": "Skin",
        "Gastrointestinal stromal tumor, NOS": None,
        "Not Reported": None,
    }
    return mapping[value]


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
        "High Grade": "high-grade",
        "Low Grade": "low-grade",
        "Not Reported": None,
        "Unknown": None,
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
