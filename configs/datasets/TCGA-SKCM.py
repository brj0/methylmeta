def dataset_id(row):
    return "TCGA-SKCM"


def description(row):
    return "TCGA Skin Cutaneous Melanoma (SKCM) cohort, Akbani 2015"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal skin"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_SKIN"
    value = row["diagnoses.primary_diagnosis"]
    if value == "Squamous cell carcinoma, NOS":
        organ = row["diagnoses.tissue_or_organ_of_origin"]
        if "skin" in organ.lower():
            return "SKIN_SCC"
        return "SCC"
    mapping = {
        # cutaneous melanoma entities of this cohort
        "Malignant melanoma, NOS": "SKIN_MEL",
        "Melanoma, NOS": "SKIN_MEL",
        "Amelanotic melanoma": "SKIN_MEL",
        "Epithelioid cell melanoma": "SKIN_MEL",
        "Spindle cell melanoma, NOS": "SKIN_MEL",
        "Nodular melanoma": "MEL_NOD",
        "Superficial spreading melanoma": "MEL_SS",
        "Lentigo maligna melanoma": "MEL_CSD",
        "Acral lentiginous melanoma, malignant": "ACR_MEL",
        # non-melanoma entities (second / other primaries)
        "Basal cell carcinoma, NOS": "BCC",
        "Spindle cell nevus, NOS": "NEV_BEN",
        "Papillary urothelial carcinoma": "URO_CA",
        "Intraductal carcinoma, noninfiltrating, NOS": "DCIS",
        "Chronic myeloid leukemia, NOS": "CML",
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown": None}
    return mapping.get(value, value)


def sample_type(row):
    value = row["sample_type"]
    mapping = {
        "Primary Tumor": "primary",
        "Metastatic": "metastasis",
        "Additional Metastatic": "metastasis",
        "Solid Tissue Normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["preservation_method"]
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[value]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
