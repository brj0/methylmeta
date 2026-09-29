def _is_normal(row):
    return row["sample_type"] == "Solid Tissue Normal"


def dataset_id(row):
    return "TCGA-PRAD"


def description(row):
    return (
        "TCGA Prostate Adenocarcinoma (PRAD), Cancer Genome Atlas Network 2015"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _is_normal(row):
        return "Normal prostate tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if _is_normal(row):
        return "CTRL_PROST"
    organ_map = {
        "Prostate gland": "prostate",
        "Bone, NOS": "bone",
        "Colon, NOS": "colon",
        "Head, face or neck, NOS": "head_neck",
        "Kidney, NOS": "kidney",
        "Lung, NOS": "lung",
        "Lymph node, NOS": "lymph_node",
        "Skin, NOS": "skin",
        "Skin of scalp and neck": "skin",
        "Skin of trunk": "skin",
        "Thorax, NOS": "thorax",
        "Thyroid gland": "thyroid",
        "Not Reported": None,
        "Unknown": None,
    }
    class_map = {
        # prostate primaries (mucinous and signet ring cell carcinoma are
        # acinar variants, no narrower prostate class is available)
        ("prostate", "Acinar cell carcinoma"): "PROS_ACIN",
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ADCA",
        ("prostate", "Adenocarcinoma with mixed subtypes"): "PROS_ADCA",
        ("prostate", "Mucinous adenocarcinoma"): "PROS_ADCA",
        ("prostate", "Signet ring cell carcinoma"): "PROS_ADCA",
        ("prostate", "Infiltrating duct carcinoma, NOS"): "PROS_DUCT",
        # prior, subsequent or synchronous primaries of the same patient
        ("head_neck", "Basal cell carcinoma, NOS"): "BCC",
        ("head_neck", "Squamous cell carcinoma, NOS"): "HNSCC",
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("skin", "Basaloid squamous cell carcinoma"): "SKIN_SCC",
        ("skin", "Squamous cell carcinoma, NOS"): "SKIN_SCC",
        ("kidney", "Clear cell carcinoma"): "RCC_CC",
        ("thorax", "Malignant melanoma, NOS"): "MEL",
        # non-Hodgkin lymphoma NOS cannot be assigned to a lymphoma subclass
        ("lymph_node", "Malignant lymphoma, non-Hodgkin, NOS"): None,
        # records without a tumor type
        ("colon", "Not Reported"): None,
        ("head_neck", "Not Reported"): None,
        ("lung", "Not Reported"): None,
        ("skin", "Not Reported"): None,
        ("thyroid", "Not Reported"): None,
        (None, "Not Reported"): None,
        (None, "Malignant melanoma, NOS"): "MEL",
    }
    classification = row["diagnoses.classification_of_tumor"]
    if classification in {"metastasis", "recurrence"}:
        # metastatic and recurrent prostate cancer keeps its organ of origin
        organ = "prostate"
    else:
        organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
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
    mapping = {"FFPE": "FFPE", "OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
