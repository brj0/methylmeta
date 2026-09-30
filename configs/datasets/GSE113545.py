def dataset_id(row):
    return "GSE113545"


def description(row):
    return (
        "Cytosine methylation analysis of adult mixed phenotype acute "
        "leukemia (MPAL) bone marrow samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "mixed phenotype acute leukemia"


def methylation_class(row):
    return "ALAL"


def sample_site(row):
    return "bone marrow"


def primary_site(row):
    return "bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"
