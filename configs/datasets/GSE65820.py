def dataset_id(row):
    return "GSE65820"


def description(row):
    return (
        "Whole genome characterisation of chemoresistant ovarian cancer "
        "(Patch et al., 2015)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["cell type"] == "normal":
        return "normal fallopian tube"
    return "high grade serous ovarian cancer"


def methylation_class(row):
    mapping = {
        "normal": "CTRL_TUB",
        "high grade serous ovarian cancer": "OVA_HGSC",
    }
    return mapping[row["cell type"]]


def sample_site(row):
    mapping = {
        "Ascites": None,
        "Fallopian Tube": "Fallopian tube",
        "PrimaryTumour": "Ovary",
        "Primarytumour": "Ovary",
        "TumourLocalRecurrence": None,
        "TumourMetastasisToDistantLocation": None,
        "Tumourmetastasistodistantlocation": None,
    }
    return mapping[row["tissue"]]


def primary_site(row):
    if row["cell type"] == "normal":
        return None
    return "Ovary"


def sample_type(row):
    mapping = {
        "Ascites": "primary",
        "Fallopian Tube": "control",
        "PrimaryTumour": "primary",
        "Primarytumour": "primary",
        "TumourLocalRecurrence": "recurrence",
        "TumourMetastasisToDistantLocation": "metastasis",
        "Tumourmetastasistodistantlocation": "metastasis",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    mapping = {
        "normal": None,
        "high grade serous ovarian cancer": "high-grade",
    }
    return mapping[row["cell type"]]


def sex(row):
    return "female"
