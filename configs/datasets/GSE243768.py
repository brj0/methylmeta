def dataset_id(row):
    return "GSE243768"


def description(row):
    return "Medulloblastoma multiomic profiling cohort (methylome of 29 FFPE MB biopsies)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "GR3": "medulloblastoma, group 3",
        "GR4": "medulloblastoma, group 4",
        "SHH": "medulloblastoma, SHH-activated",
        "WNT": "medulloblastoma, WNT-activated",
    }
    return mapping[row["main molecular subgroup"]]


def methylation_class(row):
    mapping = {
        "GR3": "MB_G3",
        "GR4": "MB_G4",
        "SHH": "MB_SHH",
        "WNT": "MB_WNT",
    }
    return mapping[row["main molecular subgroup"]]


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
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]
