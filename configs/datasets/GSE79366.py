def dataset_id(row):
    return "GSE79366"


def description(row):
    return (
        "Spatial intratumor heterogeneity of epigenetic alterations in "
        "esophageal squamous cell carcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "esophageal squamous tumor": "esophageal squamous cell carcinoma",
        "normal epithelial tissue": "normal esophageal epithelial tissue",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "esophageal squamous tumor": "ESO_SCC",
        "normal epithelial tissue": "CTRL_ESO",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    mapping = {
        "esophageal squamous tumor": "primary",
        "normal epithelial tissue": "control",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Esophagus"


def primary_site(row):
    return "Esophagus"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
