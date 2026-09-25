def dataset_id(row):
    return "GSE132399"


def description(row):
    return "Hepatoblastoma and fetal liver methylation profiling"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "Tumor": "Hepatoblastoma",
        "Non tumor": "non-tumor liver",
        "Fetal liver": "fetal liver",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Tumor": "HEPBL",
        "Non tumor": "CTRL_LIV",
        "Fetal liver": "CTRL_LIV",
    }
    return mapping[value]


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def sample_type(row):
    value = row["Source"]
    mapping = {
        "Tumor": "primary",
        "Non tumor": "control",
        "Fetal liver": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def sex(row):
    value = row["gender"]
    mapping = {
        "F": "female",
        "M": "male",
        None: None,
    }
    return mapping[value]
