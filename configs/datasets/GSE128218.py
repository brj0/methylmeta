def dataset_id(row):
    return "GSE128218"


def description(row):
    return (
        "Medulloblastoma subgroup cohort and Otx2/c-Myc cerebellar "
        "organoid xenografts (Ospedale Pediatrico Bambino Gesu)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["Title"].startswith("Primary_MB"):
        return "Medulloblastoma"
    return "Group 3 medulloblastoma-like cerebellar organoid xenograft"


def methylation_class(row):
    mapping = {
        "G3": "MB_G3",
        "G3 GM Organoids": "MB_G3",
        "G3 OM Organoids": "MB_G3",
        "G4": "MB_G4",
        "SHHA": "MB_SHH_CHL_AD",
        "SHHB": "MB_SHH_INF",
        "WNT": "MB_WNT",
    }
    return mapping[row["molecular subgroup"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value.split(" ")[0])
