def dataset_id(row):
    return "GSE307219"


def description(row):
    return (
        "Methylation profiling of 77 primary mismatch repair deficient "
        "gliomas (priMMRD subgroups 1-3)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "PRIMMRD"


def sample_type(row):
    return "primary"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def material_type(row):
    return "tissue"
