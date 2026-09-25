def dataset_id(row):
    return "E-MTAB-13564"


def description(row):
    return (
        "Illumina EPIC methylation profiling of blood, subcutaneous and "
        "visceral adipose tissue from patients with severe obesity"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "normal " + row["Characteristics[organism part]"]


def methylation_class(row):
    value = row["Characteristics[organism part]"]
    mapping = {
        "blood": "CTRL_BLOOD",
        "subcutaneous adipose tissue": "CTRL_ADIPOSE",
        "visceral abdominal adipose tissue": "CTRL_ADIPOSE",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "control"


def material_type(row):
    value = row["Characteristics[organism part]"]
    mapping = {
        "blood": "blood",
        "subcutaneous adipose tissue": "tissue",
        "visceral abdominal adipose tissue": "tissue",
    }
    return mapping[value]


def sex(row):
    value = row["Characteristics[sex]"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]


def age(row):
    return float(row["Characteristics[age]"])
