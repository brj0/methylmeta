def dataset_id(row):
    return "GSE167347"


def description(row):
    return (
        "Medulloblastoma in adults: cytogenetic phenotypes identify "
        "prognostic subgroups (adult medulloblastoma cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease"]


def methylation_class(row):
    return "MB"


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
