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


def material(row):
    value = row["treatment"]
    if "cell_culture" in value:
        return cell_line
    return None


def sex(row):
    value = row["Sex"]
    mapping = {
        "M": "male",
        "F": "female",
        None: None,
    }
    return mapping[value]


def age(row):
    return row["age"]
