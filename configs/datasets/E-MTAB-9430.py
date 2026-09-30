def dataset_id(row):
    return "E-MTAB-9430"


def description(row):
    return (
        "Paired diagnostic and relapsed medulloblastoma methylation profiles"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    return "MB"


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    staging = row["Characteristics[disease staging]"]
    mapping = {
        "diagnosis": "primary",
        "relapse": "recurrence",
        "relapse_2": "recurrence",
    }
    return mapping[staging]


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"]
    mapping = {
        "female": "female",
        "male": "male",
        "na": None,
        "not available": None,
    }
    return mapping[value]


def age(row):
    value = row["Characteristics[age]"]
    if value == "not available":
        return None
    return float(value)
