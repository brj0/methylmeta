def dataset_id(row):
    return "GSE178212"


def description(row):
    return "DNA methylation analysis of esophageal squamous cell carcinoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "adjacent non-tumor": "Normal adjacent non-tumor esophageal tissue",
        "tumor": "Esophageal squamous cell carcinoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "adjacent non-tumor": "CTRL_ESO",
        "tumor": "ESO_SCC",
    }
    return mapping[value]


def sample_site(row):
    return "Esophagus"


def primary_site(row):
    return "Esophagus"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "adjacent non-tumor": "control",
        "tumor": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"
