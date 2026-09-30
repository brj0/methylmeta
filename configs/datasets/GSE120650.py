def dataset_id(row):
    return "GSE120650"


def description(row):
    return (
        "Primary neuroblastoma DNA methylation profiles, Ackermann et al. 2018"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "NBL"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
