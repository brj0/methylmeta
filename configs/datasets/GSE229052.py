def dataset_id(row):
    return "GSE229052"


def description(row):
    return (
        "Diagnostic bone marrow samples from pediatric Hispanic patients "
        "with B-cell acute lymphoblastic leukemia"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "B-cell acute lymphoblastic leukemia"


def methylation_class(row):
    return "B_ALL"


def sample_site(row):
    return "Bone marrow"


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def preservation(row):
    return "FRESH"
