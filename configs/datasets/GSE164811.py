def dataset_id(row):
    return "GSE164811"


def description(row):
    return (
        "DNA methylation profiles of colorectal cancer classified into "
        "consensus molecular subtypes 2 and 3 (MATCH study)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "CR_CA"


def sample_site(row):
    value = row["tumor location"]
    mapping = {
        "Left": "Left colon",
        "Right": "Right colon",
    }
    return mapping[value]


def primary_site(row):
    return "Colon"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    value = row["differentiation grade"]
    mapping = {
        "good": "G1",
        "moderate": "G2",
        "poor": "G3",
        "unknown": None,
    }
    return mapping[value]


def sex(row):
    return row["gender"]
