def dataset_id(row):
    return "GSE152519"


def description(row):
    return (
        "Methylation profiles of primary myelofibrosis with and without "
        "progression to myelofibrosis"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "primary myelofibrosis"


def methylation_class(row):
    return "PMF"


def sample_site(row):
    return "bone marrow"


def primary_site(row):
    return "bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
