def dataset_id(row):
    return "GSE205331"


def description(row):
    return "Skull base chordoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease"]
    mapping = {
        "chordoma": "Chordoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["disease"]
    mapping = {
        "chordoma": "CHORD",
    }
    return mapping[value]


def sample_site(row):
    return "Skull Base"


def primary_site(row):
    return "Skull Base"


def sample_type(row):
    return "primary"


def sex(row):
    return row["Sex"]
