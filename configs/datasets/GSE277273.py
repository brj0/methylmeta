def dataset_id(row):
    return "GSE277273"


def description(row):
    return (
        "Epigenetic study of normal skin, actinic keratosis and cutaneous "
        "squamous cell carcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Normal": "normal skin",
        "AK": "actinic keratosis",
        "cSCC": "cutaneous squamous cell carcinoma",
    }
    return mapping[row["cell type"]]


def methylation_class(row):
    mapping = {
        "Normal": "CTRL_SKIN",
        "AK": "SKIN_AK",
        "cSCC": "SKIN_SCC",
    }
    return mapping[row["cell type"]]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return "skin"


def sample_type(row):
    mapping = {
        "Normal": "control",
        "AK": "primary",
        "cSCC": "primary",
    }
    return mapping[row["cell type"]]


def material_type(row):
    return "tissue"
