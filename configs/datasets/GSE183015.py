def dataset_id(row):
    return "GSE183015"


def description(row):
    return (
        "DNA methylation profiling of prostate tumors, benign prostate tissue "
        "and buffy coat from men with prostate cancer"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        ("buffy coat", "normal"): "Normal blood (buffy coat)",
        ("prostate tissue", "cancer"): "Prostate adenocarcinoma",
        ("prostate tissue", "normal"): "Normal prostate tissue",
    }
    return mapping[(row["tissue"], row["sample type"])]


def methylation_class(row):
    mapping = {
        ("buffy coat", "normal"): "CTRL_BLOOD",
        ("prostate tissue", "cancer"): "PROS_ADCA",
        ("prostate tissue", "normal"): "CTRL_PROS",
    }
    return mapping[(row["tissue"], row["sample type"])]


def sample_site(row):
    mapping = {"prostate tissue": "Prostate", "buffy coat": "Blood"}
    return mapping[row["tissue"]]


def primary_site(row):
    return "Prostate"


def sample_type(row):
    mapping = {"cancer": "primary", "normal": "control"}
    return mapping[row["sample type"]]


def material_type(row):
    mapping = {"prostate tissue": "tissue", "buffy coat": "blood"}
    return mapping[row["tissue"]]


def preservation(row):
    mapping = {"prostate tissue": "FFPE", "buffy coat": None}
    return mapping[row["tissue"]]


def tumor_grade(row):
    mapping = {
        "3+3 T4": "Gleason 6",
        "3+4": "Gleason 7",
        "3+4 T5": "Gleason 7",
        "4+3": "Gleason 7",
        "4+3 T5": "Gleason 7",
        "4+4": "Gleason 8",
        "4+5": "Gleason 9",
        "5+4": "Gleason 9",
        "5+5 T4": "Gleason 10",
    }
    return mapping[row["gleason score"]]


def sex(row):
    return "male"


def age(row):
    return float(row["age"])
