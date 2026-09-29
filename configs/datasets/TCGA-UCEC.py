def dataset_id(row):
    return "TCGA-UCEC"


def description(row):
    return (
        "TCGA Uterine Corpus Endometrial Carcinoma (UCEC), Kandoth et al. "
        "2013"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal endometrial tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None, None: None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_ENDOM"
    organ = row["diagnoses.tissue_or_organ_of_origin"]
    value = row["diagnoses.primary_diagnosis"]
    # diagnosis records of non-uterine primaries stored for these cases
    organ_class = {
        ("Breast, NOS", "Adenocarcinoma, NOS"): "BR_CA_NST",
        ("Kidney, NOS", "Clear cell carcinoma"): "RCC_CC",
        ("Lung, NOS", "Adenocarcinoma, NOS"): "LU_ADCA",
        ("Rectum, NOS", "Adenocarcinoma, NOS"): "CR_CA",
        ("Transverse colon", "Adenocarcinoma, NOS"): "CR_CA",
    }
    class_map = {
        # unspecific histology: the cohort tumour, mostly sampled elsewhere
        "Adenocarcinoma, NOS": "ENDOM_CA",
        "Adenocarcinoma with mixed subtypes": "ENDOM_MIXC",
        "Adenoid basal carcinoma": "CERV_ABC",
        "Basal cell carcinoma, NOS": "BCC",
        "Carcinoma, undifferentiated, NOS": "ENDOM_DDC",
        "Clear cell adenocarcinoma, NOS": "ENDOM_CCC",
        "Clear cell carcinoma": "ENDOM_CCC",
        "Endometrioid adenocarcinoma, NOS": "ENDOM_EC",
        "Endometrioid adenocarcinoma, secretory variant": "ENDOM_EC",
        "Infiltrating duct carcinoma, NOS": "BR_CA_NST",
        "Intraductal carcinoma, noninfiltrating, NOS": "DCIS",
        "Malignant lymphoma, small B lymphocytic, NOS": None,
        "Papillary serous cystadenocarcinoma": "ENDOM_SC",
        "Pheochromocytoma, NOS": "PHEO",
        "Serous cystadenocarcinoma, NOS": "ENDOM_SC",
        "Serous surface papillary carcinoma": "ENDOM_SC",
        "Squamous cell carcinoma, NOS": "CERV_SCC",
        "Not Reported": None,
        None: None,
    }
    if (organ, value) in organ_class:
        return organ_class[(organ, value)]
    return class_map[value]


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
    mapping = {"FFPE": "FFPE", "OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def tumor_grade(row):
    mapping = {
        "G1": "G1",
        "G2": "G2",
        "G3": "G3",
        "High Grade": "high-grade",
    }
    return mapping.get(row["diagnoses.tumor_grade"])


def sex(row):
    return "female"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
