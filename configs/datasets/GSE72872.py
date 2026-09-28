def dataset_id(row):
    return "GSE72872"


def description(row):
    return (
        "Methylome and transcriptome of esophageal adenocarcinoma (EAC) "
        "with Barrett's esophagus, normal squamous and gastric tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Tumour": "Esophageal adenocarcinoma",
        "BE": "Barrett's esophagus",
        "Normal": "Normal esophageal squamous epithelium adjacent to tumor",
        "Stomach": "Normal gastric mucosa",
        "Control": "Normal esophageal squamous epithelium",
        "GERD": "Normal esophageal squamous epithelium, reflux disease",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "Tumour": "ESO_ADCA",
        "BE": "BARRETT",
        "Normal": "CTRL_ESO",
        "Stomach": "CTRL_GAST",
        "Control": "CTRL_ESO",
        "GERD": "CTRL_ESO",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    if row["tissue"] == "Stomach":
        return "Stomach"
    return "Esophagus"


def primary_site(row):
    return sample_site(row)


def sample_type(row):
    mapping = {
        "Tumour": "primary",
        "BE": "primary",
        "Normal": "control",
        "Stomach": "control",
        "Control": "control",
        "GERD": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"
