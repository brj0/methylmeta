def dataset_id(row):
    return "GSE121930"


def description(row):
    return (
        "DNA methylation analysis of esophageal squamous cell carcinoma (ESCC)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "ESCC tissue": "esophageal squamous cell carcinoma",
        "normal esophagus tissue": "normal esophagus",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue status"]
    mapping = {
        "tumor": "ESO_SCC",
        "normal": "CTRL_ESO",
    }
    return mapping[value]


def sample_site(row):
    return "Esophagus"


def primary_site(row):
    return "Esophagus"


def sample_type(row):
    value = row["tissue status"]
    mapping = {
        "tumor": "primary",
        "normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def sex(row):
    value = row["gender"]
    mapping = {
        "Male": "male",
        "Female": "female",
    }
    return mapping[value]
