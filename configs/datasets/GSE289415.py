def dataset_id(row):
    return "GSE289415"


def description(row):
    return (
        "Two epitypes of IGHV unmutated chronic lymphocytic leukemia with "
        "distinct B-cell epigenetic imprinting (Charalampopoulou 2025)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["genotype"]


def methylation_class(row):
    return "CLL_IGHV_UNMUT"


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"
