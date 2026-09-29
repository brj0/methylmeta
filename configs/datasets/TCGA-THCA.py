def dataset_id(row):
    return "TCGA-THCA"


def description(row):
    return "TCGA Thyroid Carcinoma (THCA), Agrawal 2014"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal thyroid tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_THYR"
    organ_map = {
        "Thyroid gland": "thyroid",
        "Lymph node, NOS": "lymph_node",
        "Lung, NOS": "lung",
        "Head, face or neck, NOS": "head_neck",
        "Breast, NOS": "breast",
        "Bone, NOS": "bone",
        "Skin of scalp and neck": "skin",
        "Connective, subcutaneous and other soft tissues, NOS": "soft_tissue",
        "Prostate gland": "prostate",
        "Mandible": "mandible",
        "Rectum, NOS": "rectum",
        "Brain, NOS": "brain",
        "Colon, NOS": "colon",
        "Cheek mucosa": "cheek_mucosa",
        "Unknown": "unknown",
        "Not Reported": "not_reported",
    }
    class_map = {
        ("bone", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("brain", "Astrocytoma, NOS"): "LGG",
        ("breast", "Adenocarcinoma, NOS"): "BR_CA",
        ("breast", "Intraductal carcinoma, noninfiltrating, NOS"): "DCIS",
        ("breast", "Tubular adenocarcinoma"): "BR_CA",
        ("cheek_mucosa", "Adenoid cystic carcinoma"): "ADCC",
        ("colon", "Adenocarcinoma, NOS"): "CR_CA",
        ("head_neck", "Basal cell carcinoma, NOS"): "BCC",
        ("head_neck", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("lung", "Adenocarcinoma, NOS"): None,
        ("lung", "Combined small cell carcinoma"): "SCLC",
        ("lung", "Not Reported"): None,
        ("lung", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("lung", "Papillary carcinoma, columnar cell"): "THYR_PTC",
        ("lung", "Papillary carcinoma, follicular variant"): "THYR_PTC",
        ("lymph_node", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("lymph_node", "Papillary carcinoma, columnar cell"): "THYR_PTC",
        ("mandible", "Squamous cell carcinoma, NOS"): "HNSCC",
        ("not_reported", "Not Reported"): None,
        ("not_reported", "Papillary adenocarcinoma, NOS"): None,
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ACIN",
        ("rectum", "Leiomyosarcoma, NOS"): "LMS",
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("skin", "Basaloid squamous cell carcinoma"): "SKIN_SCC",
        ("soft_tissue", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("thyroid", "Carcinoma, NOS"): "THYR_CA",
        ("thyroid", "Follicular adenocarcinoma, NOS"): "THYR_FTC",
        ("thyroid", "Nonencapsulated sclerosing carcinoma"): "THYR_PTC",
        ("thyroid", "Oxyphilic adenocarcinoma"): "THYR_ONC_CA",
        ("thyroid", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("thyroid", "Papillary carcinoma, NOS"): "THYR_PTC",
        ("thyroid", "Papillary carcinoma, columnar cell"): "THYR_PTC",
        ("thyroid", "Papillary carcinoma, follicular variant"): "THYR_PTC",
        ("thyroid", "Papillary carcinoma, oxyphilic cell"): "THYR_PTC",
        ("unknown", "Follicular carcinoma, minimally invasive"): None,
        ("unknown", "Malignant lymphoma, non-Hodgkin, NOS"): None,
        ("unknown", "Not Reported"): None,
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    histology = row["diagnoses.primary_diagnosis"]
    return class_map[(organ, histology)]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {
        "Primary Tumor": "primary",
        "Metastatic": "metastasis",
        "Solid Tissue Normal": "control",
    }
    return mapping[row["sample_type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
