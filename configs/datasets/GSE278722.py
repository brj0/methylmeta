def dataset_id(row):
    return "GSE278722"


def description(row):
    return (
        "Methylation profiling of FFPE metaplastic breast cancer regions "
        "enriched for single morphological components"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    morph = {
        "NST": "non-special type (NST) component",
        "Spindle": "spindle cell component",
        "Chondroid": "chondroid component",
        "Squamous": "squamous component",
    }
    return "Metaplastic breast carcinoma, " + morph[row["group"]]


def methylation_class(row):
    return "BR_CA_META"


def sample_type(row):
    return "primary"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
