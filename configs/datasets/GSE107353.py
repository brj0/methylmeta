def _kind(row):
    markers = {
        "colorectal cancer": "tumor",
        "normal colorectal mucosa": "normal_mucosa",
        "blood": "blood",
    }
    tissue = row["tissue"]
    for marker, kind in markers.items():
        if marker in tissue:
            return kind


def dataset_id(row):
    return "GSE107353"


def description(row):
    return "Primary constitutional MLH1 epimutations: a focal epigenetic event"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "tumor": "Colorectal cancer",
        "normal_mucosa": "Normal colorectal mucosa",
        "blood": "Blood",
    }
    return mapping[_kind(row)]


def methylation_class(row):
    mapping = {
        "tumor": "CR_CA",
        "normal_mucosa": "CTRL_COL",
        "blood": "CTRL_BLOOD",
    }
    return mapping[_kind(row)]


def sample_site(row):
    mapping = {
        "tumor": "Colorectum",
        "normal_mucosa": "Colorectum",
        "blood": "Blood",
    }
    return mapping[_kind(row)]


def sample_type(row):
    mapping = {
        "tumor": "primary",
        "normal_mucosa": "control",
        "blood": "control",
    }
    return mapping[_kind(row)]


def material_type(row):
    mapping = {
        "tumor": "tissue",
        "normal_mucosa": "tissue",
        "blood": "blood",
    }
    return mapping[_kind(row)]


def preservation(row):
    mapping = {
        "tumor": "FFPE",
        "normal_mucosa": "FFPE",
        "blood": None,
    }
    return mapping[_kind(row)]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
