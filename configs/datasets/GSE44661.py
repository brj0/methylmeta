def dataset_id(row):
    return "GSE44661"


def description(row):
    return (
        "DNA methylation analysis of melanoma progression to brain metastasis"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    mapping = {
        "melanocytes": "CTRL_MELCYT",
        "primary melanoma": "SKIN_MEL",
        "melanoma lymph node metastasis": "SKIN_MEL",
        "melanoma brain metastasis": "SKIN_MEL",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    mapping = {
        "melanocytes": "skin",
        "primary melanoma": "skin",
        "melanoma lymph node metastasis": "lymph node",
        "melanoma brain metastasis": "brain",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    if row["tissue"] == "melanocytes":
        return None
    return "skin"


def sample_type(row):
    mapping = {
        "melanocytes": "control",
        "primary melanoma": "primary",
        "melanoma lymph node metastasis": "metastasis",
        "melanoma brain metastasis": "metastasis",
    }
    return mapping[row["tissue"]]


def material_type(row):
    mapping = {
        "Cell line": "cell_line",
        "Cell line derived from patient.": "cell_line",
        "Tissue": "tissue",
    }
    return mapping[row["Description"].splitlines()[-1]]


def preservation(row):
    mapping = {
        "Cell line": None,
        "Cell line derived from patient.": None,
        "Tissue": "FFPE",
    }
    return mapping[row["Description"].splitlines()[-1]]
