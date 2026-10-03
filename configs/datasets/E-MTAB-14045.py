def dataset_id(row):
    return "E-MTAB-14045"


def description(row):
    return (
        "Cutaneous melanoma and benign melanocytic nevi, with control skin "
        "samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Characteristics[disease]"]
    return "normal skin" if value is None else value


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "cutaneous melanoma": "SKIN_MEL",
        "melanocytic nevus": "NEV_BEN",
        None: "CTRL_SKIN",
    }
    return mapping[value]


def sample_type(row):
    if row["Characteristics[disease]"] is None:
        return "control"
    return "primary"


def sample_site(row):
    return "skin"


def primary_site(row):
    return "skin"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    value = row["Characteristics[age]"]
    return None if value is None else float(value)
