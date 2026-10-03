def dataset_id(row):
    return "GSE155353"


def description(row):
    return (
        "Genome-wide DNA methylation analysis of non-cancerous and "
        "pancreatic ductal adenocarcinoma tissue samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Description"]
    mapping = {
        "Pamcreatic ductal adenocarcinoma": (
            "pancreatic ductal adenocarcinoma"
        ),
        "Non-cancerous pancreatic tissue": "non-cancerous pancreatic tissue",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Description"]
    mapping = {
        "Pamcreatic ductal adenocarcinoma": "PDAC",
        "Non-cancerous pancreatic tissue": "CTRL_PAN",
    }
    return mapping[value]


def sample_site(row):
    return "Pancreas"


def primary_site(row):
    return "Pancreas"


def sample_type(row):
    value = row["Description"]
    mapping = {
        "Pamcreatic ductal adenocarcinoma": "primary",
        "Non-cancerous pancreatic tissue": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]


def age(row):
    value = row["age"]
    mapping = {
        "20-29": 24.5,
        "30-39": 34.5,
        "40-49": 44.5,
        "50-59": 54.5,
        "60-69": 64.5,
        "70-79": 74.5,
        "80-89": 84.5,
    }
    return mapping[value]
