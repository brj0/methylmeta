def _cohort(row):
    if row["diagnosis"] == "Healthy" or row["Title"].startswith("Control"):
        return "control"
    return "tumour"


def _control_class(row):
    mapping = {
        "blood": "CTRL_BLOOD",
        "bone marrow": "CTRL_MARROW",
    }
    return mapping[row["tissue"]]


def _cmml_patient(row):
    return row["diagnosis"] == "CMML" or row["Title"].startswith("sample_")


def dataset_id(row):
    return "GSE105420"


def description(row):
    return (
        "DNA methylation profiling of bone marrow from CMML patients and "
        "CD34+ enriched blood from healthy controls"
    )


def sample_id(row):
    value = row["Description"].split("\n")[0]
    if value.endswith("_Grn.idat"):
        return value[: -len("_Grn.idat")]
    if value.endswith("_Red.idat"):
        return value[: -len("_Red.idat")]
    return value


def diagnosis(row):
    value = row["diagnosis"]
    if value == "CMML":
        return "chronic myelomonocytic leukemia"
    if value == "Healthy":
        return "normal " + row["tissue"]
    return value


def methylation_class(row):
    if _cohort(row) == "control":
        return _control_class(row)
    if _cmml_patient(row):
        return "CMML"
    return None


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    if _cohort(row) == "control":
        return "control"
    return "primary"


def material_type(row):
    mapping = {
        "blood": "blood",
        "bone marrow": "tissue",
    }
    return mapping[row["tissue"]]


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]
