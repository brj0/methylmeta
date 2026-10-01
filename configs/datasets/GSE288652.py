def dataset_id(row):
    return "GSE288652"


def description(row):
    return (
        "Genome-wide DNA methylation of colon low-grade and high-grade "
        "adenomas"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    mapping = {
        "high-grade colon adenoma": "CR_AD_HG",
        "low-grade colon adenoma": "CR_AD_LG",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return "Colon"


def primary_site(row):
    return "Colon"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {
        "high-grade colon adenoma": "high-grade",
        "low-grade colon adenoma": "low-grade",
    }
    return mapping[row["disease state"]]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
