def dataset_id(row):
    return "GSE75153"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of human medulloblastoma "
        "molecular subgroups"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    # SHH A (child/adult) and SHH B (infant) cannot be told apart without age,
    # so the broad medulloblastoma class is used for SHH.
    mapping = {
        "Group 3": "MB_G3",
        "Group 4": "MB_G4",
        "WNT": "MB_WNT",
        "SHH": "MB_SHH",
    }
    return mapping[row["molecular subtype"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
