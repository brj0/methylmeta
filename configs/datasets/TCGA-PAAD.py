def dataset_id(row):
    return "TCGA-PAAD"


def description(row):
    return "TCGA Pancreatic Adenocarcinoma (PAAD), Raphael et al. 2017"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal pancreas tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_PAN"
    # sites carried by metastasis or recurrence records (Liver, Lung, Lymph
    # node, Peritoneum, Retroperitoneum) are not listed here; the organ of
    # origin of those records is the cohort organ (pancreas)
    organ_map = {
        "Head of pancreas": "pancreas",
        "Body of pancreas": "pancreas",
        "Tail of pancreas": "pancreas",
        "Pancreas, NOS": "pancreas",
        "Overlapping lesion of pancreas": "pancreas",
        # missing site: fall back to the cohort organ
        "Not Reported": "pancreas",
        "Breast, NOS": "breast",
        "Head, face or neck, NOS": "head_neck",
        "Pituitary gland": "pituitary",
        "Prostate gland": "prostate",
        "Skin, NOS": "skin",
        "Skin of upper limb and shoulder": "skin",
        "Upper limb, NOS": "skin",
    }
    class_map = {
        ("pancreas", "Infiltrating duct carcinoma, NOS"): "PDAC",
        ("pancreas", "Adenocarcinoma, NOS"): "PAN_CA",
        ("pancreas", "Adenocarcinoma with mixed subtypes"): "PAN_CA",
        ("pancreas", "Mucinous adenocarcinoma"): "PAN_CA",
        ("pancreas", "Neuroendocrine carcinoma, NOS"): "PAN_NEC",
        # no pancreatic entity for an undifferentiated carcinoma
        ("pancreas", "Carcinoma, undifferentiated, NOS"): None,
        # prior or subsequent primaries of the same patient
        ("breast", "Infiltrating duct carcinoma, NOS"): "BR_CA_NST",
        ("breast", "Intraductal carcinoma, noninfiltrating, NOS"): "DCIS",
        ("breast", "Not Reported"): None,
        ("head_neck", "Basaloid squamous cell carcinoma"): "HN_SCC",
        ("pituitary", "Adenoma, NOS"): "PIT_AD",
        ("prostate", "Neoplasm, malignant"): None,
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("skin", "Malignant melanoma, NOS"): "MEL",
        ("skin", "Not Reported"): None,
    }
    classification = row["diagnoses.classification_of_tumor"]
    if classification in {"metastasis", "recurrence"}:
        organ = "pancreas"
    else:
        organ = organ_map.get(row["diagnoses.tissue_or_organ_of_origin"])
    return class_map.get((organ, row["diagnoses.primary_diagnosis"]))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None}
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
    return float(value)
