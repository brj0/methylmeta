def dataset_id(row):
    return "GSE242089"


def description(row):
    return (
        "Re-analysis of primary atypical teratoid/rhabdoid tumors (ATRT) "
        "by EPIC DNA methylation profiling (Lobon Iglesias, 2023)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Atypical teratoid/rhabdoid tumor"


def methylation_class(row):
    return "ATRT"


def sample_site(row):
    return row["anatomic location"]


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def age(row):
    return float(row["age at diagnosis"])
