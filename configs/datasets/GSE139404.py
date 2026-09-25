def dataset_id(row):
    return "GSE139404"


def description(row):
    return (
        "Genome-wide DNA methylation profiles of low- and high-grade "
        "colorectal adenoma and adjacent normal mucosa"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease"]
    mapping = {"normal": "normal colorectal mucosa"}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["disease"]
    mapping = {
        "high-grade adenoma": "CR_AD_HG",
        "low-grade adenoma": "CR_AD_LG",
        "normal": "CTRL_COL",
    }
    return mapping[value]


def sample_site(row):
    return "Colon"


def primary_site(row):
    return "Colon"


def sample_type(row):
    value = row["disease"]
    mapping = {
        "high-grade adenoma": "primary",
        "low-grade adenoma": "primary",
        "normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["disease"]
    mapping = {
        "high-grade adenoma": "high-grade",
        "low-grade adenoma": "low-grade",
        "normal": None,
    }
    return mapping[value]


def sex(row):
    return row["gender"]


def age(row):
    return float(row["age"])
