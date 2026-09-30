def dataset_id(row):
    return "GSE109402"


def description(row):
    return "Pediatric medulloblastoma proteogenomics, Archer et al. 2018"


def sample_id(row):
    return row["Sample_ID"]


def sample_site(row):
    return "Cerebellum"


def diagnosis(row):
    return row["tissue type"]


def methylation_class(row):
    mapping = {
        "WNT": "MB_WNT",
        "SHH": "MB_SHH",
        "Group 3": "MB_G3",
        "Group 4": "MB_G4",
        "Cerebellum": "CTRL_CEBM",
    }
    return mapping[row["subgroup"]]


def sample_type(row):
    mapping = {"Cerebellum": "control"}
    return mapping.get(row["subgroup"], "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "F": "female",
        "M": "male",
        "-": None,
    }
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value == "-":
        return None
    return float(value[:-1])
