def dataset_id(row):
    return "TCGA-LIHC"


def description(row):
    return (
        "TCGA Liver Hepatocellular Carcinoma (LIHC), Cancer Genome Atlas "
        "Research Network 2017"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal liver tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_LIV"
    organ_map = {
        "Adrenal gland, NOS": "adrenal",
        "Bladder, NOS": "bladder",
        "Bone, NOS": "bone",
        "Breast, NOS": "breast",
        "Cecum": "colon",
        "Colon, NOS": "colon",
        "Endometrium": "uterus",
        "Hypopharynx, NOS": "head_neck",
        "Kidney, NOS": "kidney",
        "Liver": "liver",
        "Lung, NOS": "lung",
        # missing site: fall back to the cohort organ
        "Not Reported": "liver",
        "Prostate gland": "prostate",
        "Rib, sternum, clavicle and associated joints": "bone",
        "Skin of other and unspecified parts of face": "skin",
        "Skin, NOS": "skin",
        "Small intestine, NOS": "intestine",
        "Stomach, NOS": "stomach",
        "Upper limb, NOS": "other",
        "Uterus, NOS": "uterus",
    }
    class_map = {
        ("adrenal", "Hepatocellular carcinoma, NOS"): "HCC",
        ("bladder", "Not Reported"): None,
        ("bone", "Hepatocellular carcinoma, NOS"): "HCC",
        ("breast", "Not Reported"): None,
        ("colon", "Adenocarcinoma, NOS"): "CR_CA",
        ("colon", "Not Reported"): None,
        ("head_neck", "Squamous cell carcinoma, NOS"): "LAR_SCC",
        ("intestine", "Hepatocellular carcinoma, NOS"): "HCC",
        ("kidney", "Nephroblastoma, NOS"): "WILMS",
        # clear cell adenocarcinoma of the liver is not distinguishable
        ("liver", "Clear cell adenocarcinoma, NOS"): None,
        (
            "liver",
            "Combined hepatocellular carcinoma and cholangiocarcinoma",
        ): "CHC_UPLC",
        ("liver", "Hepatocellular carcinoma, NOS"): "HCC",
        ("liver", "Hepatocellular carcinoma, clear cell type"): "HCC",
        ("liver", "Hepatocellular carcinoma, fibrolamellar"): "HCC",
        ("liver", "Hepatocellular carcinoma, spindle cell variant"): "HCC",
        ("liver", "Not Reported"): None,
        # hepatocellular carcinoma is a liver entity, the recorded site of
        # these rows is a metastatic or otherwise unrelated site
        ("lung", "Hepatocellular carcinoma, NOS"): "HCC",
        ("lung", "Hepatocellular carcinoma, clear cell type"): "HCC",
        ("lung", "Neuroendocrine carcinoma, NOS"): "LU_NEC",
        ("lung", "Not Reported"): None,
        ("other", "Melanoma, NOS"): "MEL",
        ("other", "Squamous cell carcinoma, NOS"): "SCC",
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ADCA",
        ("prostate", "Not Reported"): None,
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("skin", "Squamous cell carcinoma, NOS"): "SKIN_SCC",
        ("stomach", "Tubular adenocarcinoma"): "GAST_ADCA",
        ("uterus", "Adenocarcinoma, NOS"): "ENDOM_CA",
        ("uterus", "Not Reported"): None,
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    histology = row["diagnoses.primary_diagnosis"]
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
        "Solid Tissue Normal": "control",
    }
    return mapping.get(row["sample_type"])


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def tumor_grade(row):
    value = row["diagnoses.tumor_grade"]
    mapping = {"G1": "G1", "G2": "G2", "G3": "G3", "G4": "G4", None: None}
    return mapping[value]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
