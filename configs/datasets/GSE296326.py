def dataset_id(row):
    return "GSE296326"


def description(row):
    return "Post-eradication gastric cancer and noncancerous gastric mucosa"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Tumor": "Gastric carcinoma",
        "Noncancerous gastric mucosa": "Noncancerous gastric mucosa",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "Tumor": "GAST_CA",
        "Noncancerous gastric mucosa": "CTRL_GAST",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Stomach"


def primary_site(row):
    return "Stomach"


def sample_type(row):
    mapping = {
        "Tumor": "primary",
        "Noncancerous gastric mucosa": "control",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["Sex"]]
