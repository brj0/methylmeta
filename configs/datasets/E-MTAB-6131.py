def dataset_id(row):
    return "E-MTAB-6131"


def description(row):
    return "Multi-omics molecular profiling of primary prostate adenocarcinoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[sampling site]"]


def methylation_class(row):
    value = row["Characteristics[sampling site]"]
    mapping = {
        "neoplasm": "PROS_ADCA",
        "normal tissue adjacent to tumour": "CTRL_PROS",
    }
    return mapping[value]


def sample_site(row):
    return "Prostate"


def primary_site(row):
    return "Prostate"


def sample_type(row):
    value = row["Characteristics[sampling site]"]
    mapping = {
        "neoplasm": "primary",
        "normal tissue adjacent to tumour": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["Characteristics[isup class]"]
    mapping = {
        "ISUP Class 1": "ISUP 1",
        "ISUP Class 2": "ISUP 2",
        "ISUP Class 3": "ISUP 3",
        "ISUP Class 4": "ISUP 4",
        "ISUP Class 5": "ISUP 5",
        "not available": None,
    }
    return mapping[value]


def sex(row):
    return "male"


def age(row):
    return float(row["Characteristics[age]"])
