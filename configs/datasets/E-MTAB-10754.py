def dataset_id(row):
    return "E-MTAB-10754"


def description(row):
    return "Methylation profiling of primary medulloblastoma tumours"


def sample_id(row):
    return row["Source Name"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "Grp3": "MB_G3",
        "Grp4": "MB_G4",
    }
    return mapping[row["Characteristics[cohort]"]]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "": None,
        "female": "female",
        "male": "male",
    }
    return mapping[row["Characteristics[sex]"].strip()]


def age(row):
    value = row["Characteristics[age]"].strip()
    if not value:
        return None
    return float(value)
