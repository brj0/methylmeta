def dataset_id(row):
    return "GSE174248"


def description(row):
    return (
        "IG-MYC rearranged B-cell precursor acute lymphoblastic leukaemia "
        "cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "B_ALL"


def sample_type(row):
    mapping = {"D": "primary", "R": "recurrence"}
    return mapping[row["diag_d_relapse_r"]]


def material_type(row):
    return "blood"
