def dataset_id(row):
    return "TCGA-MESO"


def description(row):
    return "TCGA Malignant Pleural Mesothelioma (MESO), Hmeljak et al. 2018"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    histology = row["diagnoses.primary_diagnosis"]
    # mesothelioma subtypes are the same for every organ of the cohort
    mesothelioma = {
        "Epithelioid mesothelioma, malignant": "MESOT_EPITH",
        "Fibrous mesothelioma, malignant": "MESOT_SARC",
        "Mesothelioma, biphasic, malignant": "MESOT_BIPHASIC",
        "Mesothelioma, malignant": "MESOT",
    }
    if histology in mesothelioma:
        return mesothelioma[histology]
    organ_map = {
        "Abdomen, NOS": "abdomen",
        "Bladder, NOS": "bladder",
        "Bone, NOS": "bone",
        "Connective, subcutaneous and other soft tissues, NOS": "soft_tissue",
        "Head, face or neck, NOS": "head_neck",
        "Intrathoracic lymph nodes": "lymph_node",
        "Kidney, NOS": "kidney",
        "Lung, NOS": "lung",
        "Mediastinum, NOS": "mediastinum",
        "Not Reported": None,
        "Pleura, NOS": "pleura",
        "Prostate gland": "prostate",
        "Thorax, NOS": "thorax",
    }
    # diagnoses that name no lineage, classified by their organ of origin
    class_map = {
        ("head_neck", "Squamous cell carcinoma, NOS"): "HN_SCC",
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ADCA",
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    return class_map.get((organ, histology))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
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
        "Recurrent Tumor": "recurrence",
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
