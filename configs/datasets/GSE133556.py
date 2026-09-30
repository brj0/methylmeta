def dataset_id(row):
    return "GSE133556"


def description(row):
    return (
        "High grade serous ovarian cancer and normal fallopian tube controls "
        "profiled by EPIC methylation array (Reyes et al. 2019)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "High grade serous ovarian cancer": "High grade serous ovarian cancer",
        "Normal Fallopian tube control": "Normal fallopian tube",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "High grade serous ovarian cancer": "OVA_HGSC",
        "Normal Fallopian tube control": "CTRL_TUB",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    mapping = {
        "High grade serous ovarian cancer": "Ovary",
        "Normal Fallopian tube control": "Fallopian tube",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    mapping = {
        "High grade serous ovarian cancer": "Ovary",
        "Normal Fallopian tube control": "Fallopian tube",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    mapping = {
        "High grade serous ovarian cancer": "primary",
        "Normal Fallopian tube control": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    mapping = {
        "High grade serous ovarian cancer": "high-grade",
        "Normal Fallopian tube control": None,
    }
    return mapping[row["tissue"]]


def sex(row):
    return "female"
