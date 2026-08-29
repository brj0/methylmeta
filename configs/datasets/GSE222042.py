def dataset_id(row):
    return "GSE222042"


def description(row):
    return "Schwannoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Schwannoma"


def methylation_class(row):
    return "SCHW"


def sample_site(row):
    return "Vestibular Nerve"


def primary_site(row):
    return "Vestibular Nerve"


def sample_type(row):
    return "primary"


def preservation(row):
    value = row["tissue"]
    mapping = {
        "fresh_OR_specimen": "FROZEN",
    }
    return mapping[value]


def sex(row):
    return row["Sex"]


def age(row):
    return row["age"]
