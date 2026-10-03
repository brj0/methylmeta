def _label(row):
    title = row["Title"].split(" ")[0]
    return "".join(ch for ch in title if not ch.isdigit()).strip("_")


def dataset_id(row):
    return "GSE53051"


def description(row):
    return "Large hypomethylated blocks in human solid tumors"


def sample_id(row):
    return row["Description"].split("\n")[0]


def diagnosis(row):
    mapping = {
        "Colon_Normal": "Normal colon tissue",
        "ColonN": "Normal colon tissue",
        "Colon_Cancer": "Colon carcinoma",
        "Colon_Adenoma": "Colon adenoma",
        "Colon_Met_Liver": "Colon carcinoma metastatic to liver",
        "Colon_Met_Lung": "Colon carcinoma metastatic to lung",
        "Mystery_Met_Lung": "Colon carcinoma metastatic to lung",
        "?Met_Lung": "Colon carcinoma metastatic to lung",
        "Lung_Normal": "Normal lung tissue",
        "Lung_Cancer": "Lung carcinoma",
        "Breast_Normal": "Normal breast tissue",
        "Breast_Cancer": "Breast carcinoma",
        "Breast_DCIS": "Ductal carcinoma in situ of the breast",
        "Pancreas_Normal": "Normal pancreas tissue",
        "PancreasN": "Normal pancreas tissue",
        "Pancreas_Cancer": "Pancreatic ductal adenocarcinoma",
        "Pancreas_IPMN": (
            "Intraductal papillary mucinous neoplasm of the pancreas"
        ),
        "Pancreas_LCC": "Large cell carcinoma of the pancreas",
        "PancreasNET": "Pancreatic neuroendocrine tumor",
        "Thyroid_Normal": "Normal thyroid tissue",
        "Thyroid_ADN": "Adenomatoid thyroid nodule",
        "Thyroid_FA": "Follicular adenoma of the thyroid",
        "Thyroid_FC": "Follicular thyroid carcinoma",
        "Thyroid_FVPTC": ("Follicular variant of papillary thyroid carcinoma"),
        "Thyroid_HA": "Hurthle cell adenoma of the thyroid",
        "Thyroid_HC": "Hurthle cell carcinoma of the thyroid",
        "Thyroid_PTC": "Papillary thyroid carcinoma",
    }
    return mapping[_label(row)]


def methylation_class(row):
    mapping = {
        "Colon_Normal": "CTRL_COL",
        "ColonN": "CTRL_COL",
        "Colon_Cancer": "CR_CA",
        "Colon_Adenoma": "CR_AD",
        "Colon_Met_Liver": "CR_CA",
        "Colon_Met_Lung": "CR_CA",
        "Mystery_Met_Lung": "CR_CA",
        "?Met_Lung": "CR_CA",
        "Lung_Normal": "CTRL_LU",
        "Lung_Cancer": "NSCLC",
        "Breast_Normal": "CTRL_BR",
        "Breast_Cancer": "BR_CA_NST",
        "Breast_DCIS": "DCIS",
        "Pancreas_Normal": "CTRL_PAN",
        "PancreasN": "CTRL_PAN",
        "Pancreas_Cancer": "PDAC",
        "Pancreas_IPMN": "IPMN",
        "Pancreas_LCC": None,
        "PancreasNET": "PAN_NET",
        "Thyroid_Normal": "CTRL_THYR",
        "Thyroid_ADN": "THYR_FND",
        "Thyroid_FA": "THYR_FOL_AD",
        "Thyroid_FC": "THYR_FTC",
        "Thyroid_FVPTC": "THYR_PTC",
        "Thyroid_HA": "THYR_ONC_AD",
        "Thyroid_HC": "THYR_ONC_CA",
        "Thyroid_PTC": "THYR_PTC",
    }
    return mapping[_label(row)]


def sample_site(row):
    organ = {
        "breast": "Breast",
        "colon": "Colon",
        "lung": "Lung",
        "pancreas": "Pancreas",
        "thyroid": "Thyroid",
    }
    biopsy_site = {
        "Colon_Met_Liver": "Liver",
        "Colon_Met_Lung": "Lung",
        "Mystery_Met_Lung": "Lung",
        "?Met_Lung": "Lung",
    }
    return biopsy_site.get(_label(row), organ[row["tissue"]])


def primary_site(row):
    mapping = {
        "breast": "Breast",
        "colon": "Colon",
        "lung": "Lung",
        "pancreas": "Pancreas",
        "thyroid": "Thyroid",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    mapping = {
        "Colon_Normal": "control",
        "ColonN": "control",
        "Lung_Normal": "control",
        "Breast_Normal": "control",
        "Pancreas_Normal": "control",
        "PancreasN": "control",
        "Thyroid_Normal": "control",
        "Colon_Met_Liver": "metastasis",
        "Colon_Met_Lung": "metastasis",
        "Mystery_Met_Lung": "metastasis",
        "?Met_Lung": "metastasis",
    }
    return mapping.get(_label(row), "primary")


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"f": "female", "m": "male", "na": None}
    return mapping[row["Sex"]]


def age(row):
    try:
        return float(row["age"])
    except (TypeError, ValueError):
        return None
