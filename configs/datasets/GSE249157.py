def dataset_id(row):
    return "GSE249157"


def description(row):
    return (
        "Epigenetic rewiring of metastatic cancer to the brain: focus on "
        "lung and colon cancers"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "BREAST DUCT invasive ca": "breast ductal invasive carcinoma",
        "COLON ADK": "colon adenocarcinoma",
        "MELANOMA": "melanoma",
        "MULTIPLE MYELOMA": "multiple myeloma",
        "NSCLC ADCA": "non-small cell lung cancer, adenocarcinoma",
        "NSCLC G3": "non-small cell lung cancer, grade 3",
        "NSCLC SCC": "non-small cell lung cancer, squamous cell carcinoma",
        "PROSTATE ADCA": "prostate adenocarcinoma",
        "SEROUS CA": "serous carcinoma",
    }
    return "Brain metastasis from " + mapping[row["metastatic site"]]


def methylation_class(row):
    mapping = {
        "BREAST DUCT invasive ca": "BR_CA_NST",
        "COLON ADK": "CR_CA",
        "MELANOMA": "MEL",
        "MULTIPLE MYELOMA": "MYELOMA",
        "NSCLC ADCA": "LU_ADCA",
        "NSCLC G3": "NSCLC",
        "NSCLC SCC": "LU_SCC",
        "PROSTATE ADCA": "PROS_ADCA",
        "SEROUS CA": "OVA_HGSC",
    }
    return mapping[row["metastatic site"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    mapping = {
        "BREAST DUCT invasive ca": "Breast",
        "COLON ADK": "Colon",
        "MELANOMA": "Skin",
        "MULTIPLE MYELOMA": "Bone marrow",
        "NSCLC ADCA": "Lung",
        "NSCLC G3": "Lung",
        "NSCLC SCC": "Lung",
        "PROSTATE ADCA": "Prostate",
        "SEROUS CA": "Ovary",
    }
    return mapping[row["metastatic site"]]


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
