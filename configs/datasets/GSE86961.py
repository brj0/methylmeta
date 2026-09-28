def dataset_id(row):
    return "GSE86961"


def description(row):
    return (
        "Integrated data analysis reveals distinct drivers and pathways "
        "disrupted by DNA methylation in papillary thyroid carcinomas"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["tissue type"] == "non-neoplastic adjacent tissue":
        return "non-neoplastic adjacent thyroid tissue"
    variant = row["variant"]
    if variant == "No Info":
        return "papillary thyroid carcinoma"
    return f"papillary thyroid carcinoma, {variant} variant"


def methylation_class(row):
    if row["tissue type"] == "non-neoplastic adjacent tissue":
        return "CTRL_THYR"
    mapping = {
        "Classic": "THYR_PTC",
        "Follicular": "THYR_PTC",
        "Folicular + oncocític": "THYR_PTC",
        "Mucossecretor + classic": "THYR_PTC",
        "Tall Cell": "THYR_PTC_TAL",
        "No Info": "THYR_PTC",
    }
    return mapping[row["variant"]]


def sample_type(row):
    mapping = {
        "tumor tissue": "primary",
        "non-neoplastic adjacent tissue": "control",
    }
    return mapping[row["tissue type"]]


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
