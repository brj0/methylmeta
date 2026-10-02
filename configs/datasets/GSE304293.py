def dataset_id(row):
    return "GSE304293"


def description(row):
    return (
        "Methylation reprogramming associated with aggressive prostate "
        "cancer and ancestral disparities"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease state"]
    mapping = {"Unknown": None}
    return mapping.get(value, value)


def methylation_class(row):
    mapping = {
        "Non-tumour prostate tissue": "CTRL_PROS",
        "Prostate tumour": "PROS_ADCA",
        "Presumably prostate tumour": "PROS_ADCA",
        "Unknown": None,
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return "Prostate"


def primary_site(row):
    return "Prostate"


def sample_type(row):
    mapping = {
        "Non-tumour prostate tissue": "control",
        "Prostate tumour": "primary",
        "Presumably prostate tumour": "primary",
        "Unknown": None,
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return row["Sex"].lower()
