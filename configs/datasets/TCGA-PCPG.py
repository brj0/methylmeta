def dataset_id(row):
    return "TCGA-PCPG"


def description(row):
    return "TCGA Pheochromocytoma and Paraganglioma (PCPG), Fishbein 2017"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal adrenal tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_ADREN"
    # organ the tumour arose in: extra-adrenal paragangliomas are recorded
    # with the region or surrounding soft tissue as their site
    organ_map = {
        "Adrenal gland, NOS": "adrenal",
        "Medulla of adrenal gland": "adrenal",
        "Cortex of adrenal gland": "adrenal",
        "Aortic body and other paraganglia": "paraganglia",
        "Carotid body": "paraganglia",
        "Retroperitoneum": "paraganglia",
        "Mediastinum, NOS": "paraganglia",
        "Thorax, NOS": "paraganglia",
        "Head, face or neck, NOS": "paraganglia",
        "Nervous system, NOS": "paraganglia",
        "Connective, subcutaneous and other soft tissues of "
        "abdomen": "paraganglia",
        "Connective, subcutaneous and other soft tissues of "
        "pelvis": "paraganglia",
        "Connective, subcutaneous and other soft tissues of "
        "thorax": "paraganglia",
        "Connective, subcutaneous and other soft tissues of "
        "trunk, NOS": "paraganglia",
        "Lymph node, NOS": "lymph_node",
        "Lung, NOS": "lung",
        "Liver": "liver",
        "Thyroid gland": "thyroid",
        "Breast, NOS": "breast",
        "Skin, NOS": "skin",
        "Upper limb, NOS": "skin",
        "Kidney, NOS": "kidney",
        "Duodenum": "small_intestine",
    }
    # one line per (organ, histology) pair seen in this dataset; pairs that
    # are not listed stay None
    class_map = {
        ("adrenal", "Pheochromocytoma, NOS"): "PHEO",
        ("adrenal", "Pheochromocytoma, malignant"): "PHEO",
        ("adrenal", "Not Reported"): None,
        ("paraganglia", "Pheochromocytoma, malignant"): "PGG",
        ("paraganglia", "Paraganglioma, NOS"): "PGG",
        ("paraganglia", "Paraganglioma, malignant"): "PGG",
        ("paraganglia", "Extra-adrenal paraganglioma, NOS"): "PGG",
        ("paraganglia", "Extra-adrenal paraganglioma, malignant"): "PGG",
        ("paraganglia", "Not Reported"): None,
        # metastases / additional tumours of a pheochromocytoma
        ("lung", "Pheochromocytoma, NOS"): "PHEO",
        ("liver", "Pheochromocytoma, NOS"): "PHEO",
        # metastases / additional tumours of a paraganglioma
        ("lymph_node", "Paraganglioma, NOS"): "PGG",
        ("lymph_node", "Extra-adrenal paraganglioma, malignant"): "PGG",
        # prior, synchronous or subsequent primaries of the same patient
        ("thyroid", "Medullary carcinoma, NOS"): "MTC",
        ("thyroid", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("breast", "Intraductal carcinoma, noninfiltrating, NOS"): "DCIS",
        ("breast", "Not Reported"): None,
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("skin", "Not Reported"): None,
        ("kidney", "Clear cell carcinoma"): "RCC_CC",
        ("small_intestine", "Carcinoid tumor, NOS"): "SI_NET",
        ("lung", "Not Reported"): None,
    }
    organ = organ_map.get(row["diagnoses.tissue_or_organ_of_origin"])
    histology = row["diagnoses.primary_diagnosis"]
    return class_map.get((organ, histology))


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
        "Additional - New Primary": "primary",
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
