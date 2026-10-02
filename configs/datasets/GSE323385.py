def dataset_id(row):
    return "GSE323385"


def description(row):
    return (
        "Genome-wide DNA methylation of tumor and benign prostate tissues "
        "from African American men"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Normal": "normal prostate tissue",
        "Cancer": "prostate adenocarcinoma",
    }
    return mapping[row["disease state"]]


def methylation_class(row):
    mapping = {
        "Normal": "CTRL_PROS",
        "Cancer": "PROS_ADCA",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return "Prostate"


def sample_type(row):
    mapping = {
        "Normal": "control",
        "Cancer": "primary",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    mapping = {
        "0": None,
        # Gleason score 5 has no matching enum value; it is grade group 1
        "2+3": "ISUP 1",
        "3+2": "Gleason 6",
        "3+3": "Gleason 6",
        "3+4": "Gleason 7",
        "4+3": "Gleason 7",
        "4+4": "Gleason 8",
        "4+5": "Gleason 9",
        "5+5": "Gleason 10",
    }
    return mapping[row["gleason"]]


def sex(row):
    return "male"


def age(row):
    value = row["age@dx"]
    if value == "#N/A!":
        return None
    return float(value)
