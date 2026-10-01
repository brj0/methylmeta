def dataset_id(row):
    return "GSE89181"


def description(row):
    return (
        "DNA methylation patterns in Barrett's esophagus, dysplastic "
        "Barrett's, and esophageal adenocarcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["histology"]
    mapping = {
        "BE": "Barrett's esophagus",
        "FBE": "Barrett's esophagus",
        "Cardia": "Gastric cardia mucosa",
        "Fundus": "Gastric fundus mucosa",
        "carditis": "Carditis of the gastric cardia",
        "SQ": "Normal esophageal squamous mucosa",
        "EAC": "Esophageal adenocarcinoma",
        "LGD": "Low-grade dysplasia in Barrett's esophagus",
        "HGD": "High-grade dysplasia in Barrett's esophagus",
        "HGD/Ca": "High-grade dysplasia with carcinoma in Barrett's esophagus",
    }
    return mapping[value]


def methylation_class(row):
    value = row["histology"]
    mapping = {
        "BE": "BARRETT",
        "FBE": "BARRETT",
        "Cardia": "CTRL_GAST",
        "Fundus": "CTRL_GAST",
        "carditis": "CTRL_GAST",
        "SQ": "CTRL_ESO",
        "EAC": "ESO_ADCA",
        "LGD": "BARRETT_DYS",
        "HGD": "BARRETT_DYS",
        "HGD/Ca": "BARRETT_DYS",
    }
    return mapping[value]


def sample_site(row):
    value = row["histology"]
    mapping = {
        "Cardia": "Stomach",
        "Fundus": "Stomach",
        "carditis": "Stomach",
    }
    return mapping.get(value, "Esophagus")


def primary_site(row):
    return "Esophagus"


def sample_type(row):
    value = row["histology"]
    mapping = {
        "Cardia": "control",
        "Fundus": "control",
        "carditis": "control",
        "SQ": "control",
    }
    return mapping.get(value, "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping.get(row["gender"])


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
