def dataset_id(row):
    return "GSE337222"


def description(row):
    return "SJMB03 phase III medulloblastoma trial, molecular subgroups"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "CONTR,_CEBM": "normal cerebellar hemisphere",
        "CONTR,_HEMI": "normal cerebral cortex",
        "CONTR,_INFLAM": "control tissue with inflammatory microenvironment",
        "MB,_G3": "medulloblastoma, group 3",
        "MB,_G4": "medulloblastoma, group 4",
        "MB,_SHH_CHL_AD": "medulloblastoma, SHH-activated",
        "MB,_SHH_INF": "medulloblastoma, SHH-activated, infant",
        "MB,_WNT": "medulloblastoma, WNT-activated",
        "PIN_T,_PPT": "pineal parenchymal tumor",
        "PLEX,_PED_B": "choroid plexus tumor, pediatric B",
    }
    return mapping[row["subgroup"]]


def methylation_class(row):
    mapping = {
        "CONTR,_CEBM": "CTRL_CEBM",
        "CONTR,_HEMI": "CTRL_HEMI",
        "CONTR,_INFLAM": "CTRL_INFLAM",
        "MB,_G3": "MB_G3",
        "MB,_G4": "MB_G4",
        "MB,_SHH_CHL_AD": "MB_SHH_CHL_AD",
        "MB,_SHH_INF": "MB_SHH_INF",
        "MB,_WNT": "MB_WNT",
        "PIN_T,_PPT": "PINE_PPT",
        "PLEX,_PED_B": "PLEX_PED_B",
    }
    return mapping[row["subgroup"]]


def sample_site(row):
    return "Brain"


def sample_type(row):
    mapping = {
        "CONTR,_CEBM": "control",
        "CONTR,_HEMI": "control",
        "CONTR,_INFLAM": "control",
        "MB,_G3": "primary",
        "MB,_G4": "primary",
        "MB,_SHH_CHL_AD": "primary",
        "MB,_SHH_INF": "primary",
        "MB,_WNT": "primary",
        "PIN_T,_PPT": "primary",
        "PLEX,_PED_B": "primary",
    }
    return mapping[row["subgroup"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
