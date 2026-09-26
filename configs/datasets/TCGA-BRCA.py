def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    if not barcode:
        return None
    return barcode.split("-")[-1][:2]


def _is_normal(row):
    return _sample_type_code(row) in {"10", "11", "12", "13", "14"}


def dataset_id(row):
    return "TCGA-BRCA"


def description(row):
    return "TCGA Breast Invasive Carcinoma (BRCA), TCGA Network 2012"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _is_normal(row):
        return "Normal breast tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None, None: None}
    return mapping.get(value, value)


def methylation_class(row):
    if _is_normal(row):
        return "CTRL_BR"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Infiltrating duct carcinoma, NOS": "BR_CA_NST",
        "Lobular carcinoma, NOS": "BR_CA_LOB",
        "Infiltrating duct and lobular carcinoma": "BR_CA",
        "Infiltrating duct mixed with other types of carcinoma": "BR_CA",
        "Infiltrating lobular mixed with other types of carcinoma": "BR_CA",
        "Metaplastic carcinoma, NOS": "BR_CA_META",
        "Mucinous adenocarcinoma": "BR_CA_MUC",
        "Medullary carcinoma, NOS": "BR_CA_NST",
        "Intraductal papillary adenocarcinoma with invasion": (
            "BR_CA_INV_PAP"
        ),
        "Invasive micropapillary carcinoma": "BR_CA_MICROPAP",
        "Paget disease and infiltrating duct carcinoma of breast": (
            "BR_CA_NST"
        ),
        "Intraductal carcinoma, noninfiltrating, NOS": "DCIS",
        "Ductal carcinoma in situ, NOS": "DCIS",
        "Lobular carcinoma in situ, NOS": "LCIS",
        "Pleomorphic carcinoma": "BR_CA",
        "Clear cell carcinoma": "BR_CA",
        "Papillary carcinoma, NOS": "BR_CA_INV_PAP",
        "Adenocarcinoma, NOS": "BR_CA",
        "Carcinoma, NOS": "BR_CA",
        "Basal cell carcinoma, NOS": "BCC",
        "Myelodysplastic syndrome, NOS": "MDS",
        "Phyllodes tumor, malignant": "PHYT_MAL",
        "Tubular adenocarcinoma": "BR_CA_TUB",
        "Cribriform carcinoma, NOS": "BR_CA_CRIB",
        "Adenoid cystic carcinoma": "BR_ADCC",
        "Large cell neuroendocrine carcinoma": "BR_NEC",
        "Apocrine adenocarcinoma": "BR_CA_APOCRINE",
        "Not Reported": None,
        None: None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Breast, NOS": "Breast", "Not Reported": None, None: None}
    return mapping[value]


def primary_site(row):
    value = row["diagnoses.primary_diagnosis"]
    return {
        "Basal cell carcinoma, NOS": "Skin",
        "Myelodysplastic syndrome, NOS": None,
        "Not Reported": None,
        None: None,
    }.get(value, "Breast")


def sample_type(row):
    mapping = {
        "01": "primary",
        "02": "recurrence",
        "05": "primary",
        "06": "metastasis",
        "07": "metastasis",
        "10": "control",
        "11": "control",
        "12": "control",
        "13": "control",
        "14": "control",
    }
    return mapping.get(_sample_type_code(row))


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
