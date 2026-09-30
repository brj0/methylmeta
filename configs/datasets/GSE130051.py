def dataset_id(row):
    return "GSE130051"


def description(row):
    return (
        "Second-generation molecular subgrouping of medulloblastoma: "
        "international meta-analysis of Group 3 and Group 4 subtypes "
        "(Sharma 2019)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "MB_G3": "MB_G3",
        "MB_G4": "MB_G4",
    }
    return mapping[row["subgroup"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
