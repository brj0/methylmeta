def dataset_id(row):
    return "TCGA-STAD"


def description(row):
    return "TCGA Stomach Adenocarcinoma (STAD), Cancer Genome Atlas 2014"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal stomach tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_GAST"
    organ_map = {
        "Gastric antrum": "stomach",
        "Body of stomach": "stomach",
        "Cardia, NOS": "stomach",
        "Fundus of stomach": "stomach",
        "Stomach, NOS": "stomach",
        "Lesser curvature of stomach, NOS": "stomach",
        # site missing: fall back to the cohort organ
        "Not Reported": "stomach",
        "Liver": "liver",
        "Lung, NOS": "lung",
        "Lymph node, NOS": "lymph_node",
        "Lymph nodes of head, face and neck": "lymph_node",
        "Prostate gland": "prostate",
        "Adrenal gland, NOS": "adrenal",
        "Peritoneum, NOS": "peritoneum",
        "Rib, sternum, clavicle and associated joints": "bone",
        "Kidney, NOS": "kidney",
        "Brain, NOS": "brain",
        "Bladder, NOS": "bladder",
        "Skin, NOS": "skin",
        "Skin of other and unspecified parts of face": "skin",
        "Pancreas, NOS": "pancreas",
    }
    class_map = {
        ("stomach", "Adenocarcinoma, NOS"): "GAST_ADCA",
        ("stomach", "Adenocarcinoma with mixed subtypes"): "GAST_ADCA",
        ("stomach", "Adenocarcinoma, intestinal type"): "GAST_ADCA",
        ("stomach", "Carcinoma, diffuse type"): "GAST_ADCA",
        ("stomach", "Mucinous adenocarcinoma"): "GAST_ADCA",
        ("stomach", "Papillary adenocarcinoma, NOS"): "GAST_ADCA",
        ("stomach", "Signet ring cell carcinoma"): "GAST_ADCA",
        ("stomach", "Tubular adenocarcinoma"): "GAST_ADCA",
        ("stomach", "Not Reported"): None,
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("prostate", "Not Reported"): None,
        ("kidney", "Not Reported"): None,
        ("bladder", "Not Reported"): None,
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    if row["diagnoses.classification_of_tumor"] == "metastasis":
        # metastatic gastric carcinoma: organ of origin is the stomach
        organ = "stomach"
    histology = row["diagnoses.primary_diagnosis"]
    return class_map.get((organ, histology))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None, "Stomach, NOS": "Stomach"}
    return mapping.get(value, value)


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
        "Solid Tissue Normal": "control",
    }
    return mapping[row["sample_type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def tumor_grade(row):
    mapping = {
        "G1": "G1",
        "G2": "G2",
        "G3": "G3",
        "GX": None,
        None: None,
    }
    return mapping[row["diagnoses.tumor_grade"]]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
