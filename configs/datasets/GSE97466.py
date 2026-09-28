def dataset_id(row):
    return "GSE97466"


def description(row):
    return (
        "Prognostic classifier based on genome-wide DNA methylation profiling "
        "in well differentiated thyroid tumors (Bisarro dos Reis et al., "
        "2020)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["histology"]


def methylation_class(row):
    mapping = {
        "papillary thyroid cancer": "THYR_PTC",
        "follicullar thyroid cancer": "THYR_FTC",
        "minimally invasive follicular carcinomas": "THYR_FTC",
        "Hürthle cell carcinomas": "THYR_ONC_CA",
        "poorly differentiated thyroid carcinoma": "THYR_PDC",
        "anaplastic thyroid cancer": "THYR_ANA_CA",
        "follicular adenoma": "THYR_FOL_AD",
        "follicular adenoma/Hürthle cell": "THYR_ONC_AD",
        "nodular goiter": "THYR_FND",
        "lymphocytic thyroiditis": "CTRL_THYR",
        "non-neoplastic adjacent tissue": "CTRL_THYR",
    }
    histology = row["histology"]
    if histology == "papillary thyroid cancer":
        return "THYR_PTC_TAL" if row["variant"] == "Tall cell" else "THYR_PTC"
    return mapping[histology]


def sample_type(row):
    mapping = {
        "tumor tissue": "primary",
        "benign lesion": "primary",
        "non-neoplastic adjacent tissue": "control",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Thyroid"


def primary_site(row):
    return "Thyroid"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
