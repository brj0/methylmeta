def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    return barcode.split("-")[-1][:2]


def dataset_id(row):
    return "TCGA-CHOL"


def description(row):
    return "TCGA Cholangiocarcinoma (CHOL), Farshidfar 2017"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _sample_type_code(row) == "11":
        return "Normal bile duct tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if _sample_type_code(row) == "11":
        return "CTRL_BD"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Cholangiocarcinoma": "CCA",
        "Sarcoma, NOS": "SARC_NOS",
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {
        "Biliary tract, NOS": "Biliary tract",
        "Not Reported": None,
    }
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {
        "Not Reported": None,
        "Specified parts of peritoneum": "Peritoneum",
    }
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    code = _sample_type_code(row)
    mapping = {
        "01": "primary",
        "02": "recurrence",
        "06": "metastasis",
        "11": "control",
    }
    return mapping.get(code)


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["diagnoses.tumor_grade"]
    if value in {"G1", "G2", "G3", "G4"}:
        return value
    return None


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
