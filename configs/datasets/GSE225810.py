def dataset_id(row):
    return "GSE225810"


def description(row):
    return (
        "DNA methylation profiling of pediatric brain tumor tissues and "
        "matched in vitro cell cultures"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"].replace(" cells", "")


def methylation_class(row):
    tokens = row["Title"].split("_")
    subtypes = {
        "WNT": "MB_WNT",
        "SHHa": "MB_SHH_CHL_AD",
        "SHHb": "MB_SHH_INF",
        "G3": "MB_G3",
        "G4": "MB_G4",
    }
    entities = {
        "LGG": "LGG",
        "HGG": "HGG",
        "EPN": "EPN",
        "DIPG": "DMG_K27",
        "MNG": "MNG",
        "MB": "MB",
    }
    return subtypes.get(tokens[1], entities[tokens[0]])


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    mapping = {"tumor": "primary"}
    return mapping.get(row["Source"])


def material_type(row):
    mapping = {"tumor": "tissue"}
    return mapping.get(row["Source"], "cell_line")


def preservation(row):
    mapping = {
        "formalin-fixed": "FFPE",
        "frozen tissue": "FROZEN",
        "cell line": None,
    }
    return mapping[row["Description"].splitlines()[-1].strip()]
