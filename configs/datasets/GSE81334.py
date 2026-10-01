def dataset_id(row):
    return "GSE81334"


def description(row):
    return (
        "Genome-wide methylation analysis of Barrett's esophagus and "
        "esophageal adenocarcinoma subtypes"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    mapping = {
        "Esophageal adenocarcinoma": "Esophageal adenocarcinoma",
        "Squamous tissue": "Normal esophageal squamous epithelium",
        "nondysplastic Barrett's sample from Barrett's patient": (
            "Nondysplastic Barrett's esophagus"
        ),
        "nondysplastic Barrett's sample from Esophageal Adenocarcinoma "
        "patient": "Nondysplastic Barrett's esophagus",
    }
    return mapping[row["Description"]]


def methylation_class(row):
    mapping = {
        "Esophageal adenocarcinoma": "ESO_ADCA",
        "Squamous tissue": "CTRL_ESO",
        "nondysplastic Barrett's sample from Barrett's patient": "BARRETT",
        "nondysplastic Barrett's sample from Esophageal Adenocarcinoma "
        "patient": "BARRETT",
    }
    return mapping[row["Description"]]


def sample_site(row):
    return "Esophagus"


def primary_site(row):
    return "Esophagus"


def sample_type(row):
    mapping = {
        "Esophageal adenocarcinoma": "primary",
        "Squamous tissue": "control",
        "nondysplastic Barrett's sample from Barrett's patient": "primary",
        "nondysplastic Barrett's sample from Esophageal Adenocarcinoma "
        "patient": "primary",
    }
    return mapping[row["Description"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
