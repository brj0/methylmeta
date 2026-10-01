def dataset_id(row):
    return "GSE85212"


def description(row):
    return (
        "DNA methylation profiling of 763 primary medulloblastoma samples "
        "(Cavalli et al., 2017)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "WNT": "MB_WNT",
        "SHH": "MB_SHH",
        "Group3": "MB_G3",
        "Group4": "MB_G4",
    }
    return mapping[row["subgroup"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    mapping = {
        "primary tumor": "primary",
    }
    return mapping[row["type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "Fresh frozen": "FROZEN",
    }
    return mapping[row["Source"]]
