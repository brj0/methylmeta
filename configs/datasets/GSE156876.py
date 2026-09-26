def dataset_id(row):
    return "GSE156876"


def description(row):
    return (
        "DNA methylation profiling of formalin-fixed paraffin-embedded uveal "
        "melanoma tumours linked to histopathology, metastasis and survival"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    morphology = {
        "Epi": "epithelioid",
        "Spi": "spindle",
        "Mix": "mixed epithelioid and spindle",
    }
    return "Uveal melanoma ({})".format(morphology[row["histology"]])


def methylation_class(row):
    return "UVE_MEL"


def sample_site(row):
    return "Uvea"


def primary_site(row):
    return "Uvea"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]
