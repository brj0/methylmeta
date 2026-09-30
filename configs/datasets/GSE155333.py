def dataset_id(row):
    return "GSE155333"


def description(row):
    return "DNA methylation of T-ALL blasts and normal developing thymocytes"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease state"]
    if value == "T-ALL":
        return "T-cell acute lymphoblastic leukemia"
    return value


def methylation_class(row):
    mapping = {
        "T-ALL": "T_ALL",
        "Normal thymocytes CD34+ 4- 1-": "CTRL_THYM",
        "Normal thymocytes CD34+4+": "CTRL_THYM",
        "Normal thymocytes CD34+4-1+": "CTRL_THYM",
        "Normal thymocytes DP CD4+CD8+ (Double Positive) CD3+": "CTRL_THYM",
        "Normal thymocytes DP CD4+CD8+ (Double Positive) CD3-": "CTRL_THYM",
        "Normal thymocytes ISP CD4+ (Immature Single Positive) "
        "CD3,8,34- CD28+": "CTRL_THYM",
        "Normal thymocytes SP4+ (Single Positive) CD3+": "CTRL_THYM",
        "Normal thymocytes SP8+ (Single Positive) CD3+": "CTRL_THYM",
        "Normal thymocytes \u0263\u03b4 CD3+ CD1+": "CTRL_THYM",
        "Normal thymocytes \u0263\u03b4 CD3+ CD1-": "CTRL_THYM",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    mapping = {
        "Blast from the bone marrow": "Bone marrow",
        "Human postnatal thymus": "Thymus",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    mapping = {
        "Blast from the bone marrow": "Bone marrow",
        "Human postnatal thymus": "Thymus",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    mapping = {
        "Blast from the bone marrow": "primary",
        "Human postnatal thymus": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    mapping = {
        "Blast from the bone marrow": "blood",
        "Human postnatal thymus": "tissue",
    }
    return mapping[row["tissue"]]
