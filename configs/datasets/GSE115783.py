def dataset_id(row):
    return "GSE115783"


def description(row):
    return (
        "DNA methylation profiling of nonfunctioning pituitary adenomas "
        "and normal pituitary"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    if row["tissue"] == "healthy pituitary":
        return "CTRL_ADENOPIT"
    # hormone-defined subtype of the nonfunctioning adenomas; plurihormonal
    # and null cell adenomas have no specific reference class, so they stay NOS
    mapping = {
        "Gonadotroph": "PIT_AD_FSH_LH",
        "Multihormonal": "PIT_AD",
        "Null cell adenoma": "PIT_AD",
        "-": None,
    }
    return mapping[row["tumor type"]]


def sample_site(row):
    return "Pituitary gland"


def primary_site(row):
    return "Pituitary gland"


def sample_type(row):
    mapping = {
        "healthy pituitary": "control",
        "nonfunctioning pituitary adenoma": "primary",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male", "-": None}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value == "-":
        return None
    return float(value)
