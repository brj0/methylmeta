def dataset_id(row):
    return "GSE133395"


def description(row):
    return "Acral melanoma methylome signatures (EPIGENETICS OF ALM)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "AN": "acral naevus",
        "PALM": "primary acral lentiginous melanoma",
        "NALM": "primary non-lentiginous acral melanoma",
        "MALM": "metastatic acral melanoma",
        "PCM": "primary non-acral cutaneous melanoma",
    }
    return mapping[row["cancer type"]]


def methylation_class(row):
    mapping = {
        "AN": "NEV_ACRAL",
        "PALM": "ACR_MEL",
        "NALM": "ACR_MEL",
        "MALM": "ACR_MEL",
        "PCM": "SKIN_MEL",
    }
    return mapping[row["cancer type"]]


def sample_type(row):
    mapping = {
        "AN": "control",
        "PALM": "primary",
        "NALM": "primary",
        "PCM": "primary",
        "MALM": "metastasis",
    }
    return mapping[row["cancer type"]]


def sample_site(row):
    mapping = {
        "AN": "Acral skin",
        "PALM": "Acral skin",
        "NALM": "Acral skin",
        "PCM": "Skin",
        "MALM": None,
    }
    return mapping[row["cancer type"]]


def primary_site(row):
    mapping = {
        "AN": "Acral skin",
        "PALM": "Acral skin",
        "NALM": "Acral skin",
        "PCM": "Skin",
        "MALM": "Acral skin",
    }
    return mapping[row["cancer type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
