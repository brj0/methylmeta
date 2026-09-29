def dataset_id(row):
    return "GSE128654"


def description(row):
    return "Matched glioblastoma tumors, BTIC cell lines and orthotopic xenografts"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnosis"]
    mapping = {
        "gbm": "Glioblastoma",
        "gbm_r": "Glioblastoma, recurrent",
        "gbm_u": "Glioblastoma",
    }
    return mapping[value]


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    value = row["diagnosis"]
    mapping = {
        "gbm": "primary",
        "gbm_r": "recurrence",
        "gbm_u": "primary",
    }
    return mapping[value]


def material_type(row):
    value = row["sample group"]
    mapping = {
        "tumor": "tissue",
        "cell": "cell_line",
        "xeno": "tissue",
    }
    return mapping[value]


def sex(row):
    value = row["Sex"]
    mapping = {
        "f": "female",
        "m": "male",
    }
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
