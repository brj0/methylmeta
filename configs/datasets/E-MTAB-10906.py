def dataset_id(row):
    return "E-MTAB-10906"


def description(row):
    return "Follicular thyroid adenomas, carcinomas and benign nodules"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "Follicular Variant Thyroid Gland Papillary Carcinoma": "THYR_PTC",
        "follicular thyroid carcinoma": "THYR_FTC",
        "thyroid adenoma": "THYR_FOL_AD",
        "thyroid nodule": "THYR_FND",
    }
    return mapping[value]


def sample_site(row):
    return "thyroid gland"


def primary_site(row):
    return "thyroid gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    return float(row["Characteristics[age]"])
