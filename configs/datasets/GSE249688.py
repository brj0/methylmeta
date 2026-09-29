def dataset_id(row):
    return "GSE249688"


def description(row):
    return (
        "DNA methylation profiling of carcinomas for the identification of "
        "sites of origin in carcinoma of unknown primary"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumor type"]


def methylation_class(row):
    mapping = {
        "adenocarcinoma (ddx: upper GI or pancreatobiliary)": None,
        "breast adenocarcinoma": "BR_CA",
        "colorecatal carcinoma": "CR_CA",
        "Endometrioid endometrial adenocarcinoma": "ENDOM_EC",
        "esophageal adenocarcinoma": "ESO_ADCA",
        "high-grade neoplasm (likely prostate origin)": "PROS_ADCA",
        "high-grade serous adenocarcinoma of the ovary": "OVA_HGSC",
        "lung adenocarcinoma": "LU_ADCA",
        "lung mucinous adenocarcinoma": "LU_MUC_ADCA",
        "Medullary Thyroid": "MTC",
        "pleomorphic dermal sarcoma": "PDS",
        "poorly differentiated carcinoma (ddx: gastrointestinal, "
        "pacreatobiliary or gastrointestinal-type gynecological "
        "carcinoma)": None,
        "poorly differentiated carcinoma (unknown origin)": None,
        "poorly differentiated carcinoma c/w lung primary": "NSCLC",
        "Prostate adenocarcinoma": "PROS_ADCA",
        "renal carcinoma (favor papillary renal cell carcinoma)": "RCC_PAP",
        "renal clear cell carcinoma": "RCC_CC",
        "rencal cell carcinoma, TFE-3+": "RCC_TFE3",
        "?breast adenocarcinoma": "BR_CA",
    }
    return mapping[row["tumor type"]]


def primary_site(row):
    mapping = {
        "adenocarcinoma (ddx: upper GI or pancreatobiliary)": None,
        "breast adenocarcinoma": "Breast",
        "colorecatal carcinoma": "Colorectum",
        "Endometrioid endometrial adenocarcinoma": "Uterus",
        "esophageal adenocarcinoma": "Esophagus",
        "high-grade neoplasm (likely prostate origin)": "Prostate",
        "high-grade serous adenocarcinoma of the ovary": "Ovary",
        "lung adenocarcinoma": "Lung",
        "lung mucinous adenocarcinoma": "Lung",
        "Medullary Thyroid": "Thyroid",
        "pleomorphic dermal sarcoma": "Skin",
        "poorly differentiated carcinoma (ddx: gastrointestinal, "
        "pacreatobiliary or gastrointestinal-type gynecological "
        "carcinoma)": None,
        "poorly differentiated carcinoma (unknown origin)": None,
        "poorly differentiated carcinoma c/w lung primary": "Lung",
        "Prostate adenocarcinoma": "Prostate",
        "renal carcinoma (favor papillary renal cell carcinoma)": "Kidney",
        "renal clear cell carcinoma": "Kidney",
        "rencal cell carcinoma, TFE-3+": "Kidney",
        "?breast adenocarcinoma": "Breast",
    }
    return mapping[row["tumor type"]]


def sample_site(row):
    mapping = {
        "Brain Metastasis": "Brain",
        "Breast Tumor": "Breast",
        "Gynecological Tumor": "Gynecological tract",
        "Kidney Tumor": "Kidney",
        "Thyroid Tumor": "Thyroid",
    }
    return mapping[row["Source"]]


def sample_type(row):
    mapping = {"Brain Metastasis": "metastasis"}
    return mapping.get(row["Source"], "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
