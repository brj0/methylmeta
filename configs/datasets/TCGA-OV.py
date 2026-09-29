def dataset_id(row):
    return "TCGA-OV"


def description(row):
    return "TCGA Ovarian Serous Cystadenocarcinoma (OV), Bell et al. 2011"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal ovarian tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Unknown": None, None: None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_OVA"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Papillary serous cystadenocarcinoma": "OVA_HGSC",
        "Serous cystadenocarcinoma, NOS": "OVA_HGSC",
        "Serous surface papillary carcinoma": "OVA_HGSC",
        "Unknown": None,
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
        "Primary Tumor": "primary",
        "Recurrent Tumor": "recurrence",
        "Solid Tissue Normal": "control",
    }
    return mapping[row["sample_type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def tumor_grade(row):
    value = row["diagnoses.tumor_grade"]
    mapping = {"G1": "G1", "G2": "G2", "G3": "G3", "G4": "G4"}
    return mapping.get(value)


def sex(row):
    return "female"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
