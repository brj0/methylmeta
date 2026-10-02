def dataset_id(row):
    return "GSE323379"


def description(row):
    return (
        "Genome-wide DNA methylation of prostate adenocarcinoma, benign "
        "prostatic hyperplasia and metastatic disease in African American men"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    state = row["disease state"]
    if state == "Normal":
        return "normal prostate tissue"
    if state == "Tumor":
        return "metastatic prostate adenocarcinoma"
    return row["diagnosis"]


def methylation_class(row):
    mapping = {
        "Normal": "CTRL_PROS",
        "Benign": "CTRL_PROS",
        "Tumor&Normal": "PROS_ADCA",
        "Tumor": "PROS_ADCA",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return "Prostate"


def sample_type(row):
    mapping = {
        "Normal": "control",
        "Benign": "control",
        "Tumor&Normal": "primary",
        "Tumor": "metastasis",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {
        "0": None,
        "Benign": None,
        "7 (4+3), Tertiary Gleason 5 also present": "Gleason 7",
        "Geason's score 9 (5+4), grade group 2": "Gleason 9",
        "Gleason's pattern 7 (3+4),": "Gleason 7",
        "Gleason's pattern 7 (3+4), Grade group  2": "Gleason 7",
        "Gleason's pattern 7 (3+4), Grade group 2": "Gleason 7",
        "Gleason's pattern 7 (3+4), Grade group 3": "Gleason 7",
        "Gleason's pattern 7 (3+4), grade group 2": "Gleason 7",
        "Gleason's pattern 7 (3+4), grade group 3": "Gleason 7",
        "Gleason's pattern 7 (4+3) with tertiary pattern 5, Grade group 3": (
            "Gleason 7"
        ),
        "Gleason's pattern 8 (3+5), grade group 2": "Gleason 8",
        "Gleason's pattern 8 (4+4),  grade group 2": "Gleason 8",
        "Gleason's pattern 8 (4+4), grade group 2": "Gleason 8",
    }
    return mapping[row["gleason"]]


def sex(row):
    return "male"


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
