def dataset_id(row):
    return "GSE220838"


def description(row):
    return (
        "Methylation analysis of lung adenocarcinoma and its brain metastases"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Lung adenocarcinoma": "Lung adenocarcinoma",
        "Brain metastasis": "Lung adenocarcinoma brain metastasis",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "Lung adenocarcinoma": "LU_ADCA",
        "Brain metastasis": "LU_ADCA",
    }
    return mapping[row["Source"]]


def sample_site(row):
    mapping = {
        "Lung adenocarcinoma": "Lung",
        "Brain metastasis": "Brain",
    }
    return mapping[row["Source"]]


def primary_site(row):
    return "Lung"


def sample_type(row):
    mapping = {
        "Lung adenocarcinoma": "primary",
        "Brain metastasis": "metastasis",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
