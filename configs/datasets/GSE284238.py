def dataset_id(row):
    return "GSE284238"


def description(row):
    return (
        "Epigenome-wide DNA methylation study of normal rectal background "
        "mucosa in adults with colorectal adenoma and healthy controls (2024)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease state"]
    mapping = {
        "colorectal adenoma": (
            "normal rectal mucosa of a patient with colorectal adenoma"
        ),
        "normal control": "normal rectal mucosa",
    }
    return mapping[value]


def methylation_class(row):
    return "CTRL_COL"


def sample_site(row):
    return "Rectum"


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
