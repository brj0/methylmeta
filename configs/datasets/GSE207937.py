def dataset_id(row):
    return "GSE207937"


def description(row):
    return (
        "Integrating methylome and transcriptome signatures expands the "
        "molecular classification of pituitary tumors (PitNETs)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    who = row["who 2017"]
    if who is not None:
        return "Pituitary neuroendocrine tumor (PitNET), " + who
    return "Pituitary neuroendocrine tumor (PitNET)"


def methylation_class(row):
    who_class = {
        "Corticotroph": "PIT_AD_ACTH",
        "Gonadotroph": "PIT_AD_FSH_LH",
        "Somatotroph": "PIT_AD",
        "Undefined": "PIT_AD",
        "Undefined Pit1+/ SF1+": "PIT_AD",
        "Undefined tPit+/ Pit1+": "PIT_AD",
    }
    presentation_class = {
        "Acromegaly (GH-secreting)": "PIT_AD",
        "Cushing disease (ACTH-secreting)": "PIT_AD_ACTH",
        "Non-functioning PitNET": "PIT_AD",
    }
    who = row["who 2017"]
    if who is not None:
        return who_class[who]
    return presentation_class[row["clinical presentation"]]


def sample_site(row):
    return "Pituitary gland"


def primary_site(row):
    return "Pituitary gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age years"])
