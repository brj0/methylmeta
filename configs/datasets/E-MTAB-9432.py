def dataset_id(row):
    return "E-MTAB-9432"


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
        "diagnostic": "primary",
        "relapse": "recurrence",
    }
    return mapping[staging]


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"]
    mapping = {
        "female": "female",
        "male": "male",
    }
    return mapping[value]


def age(row):
    return float(row["Characteristics[age]"])
