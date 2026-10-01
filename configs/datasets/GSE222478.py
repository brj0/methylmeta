def dataset_id(row):
    return "GSE222478"


def description(row):
    return (
        "Multiomic profiling of medulloblastoma reveals subtype-specific "
        "targetable alterations at the proteome and N-glycan level "
        "(methylation cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "medulloblastoma"


def methylation_class(row):
    value = row["Description"]
    mapping = {
        "GR3 sample": "MB_G3",
        "GR4 sample": "MB_G4",
        "SHH sample": "MB_SHH",
        "SHH p53 sample": "MB_SHH",
        "WNT sample": "MB_WNT",
    }
    return mapping[value]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]
