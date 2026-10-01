def dataset_id(row):
    return "GSE207998"


def description(row):
    return (
        "DNA methylation of 123 triple negative breast cancer tissues for "
        "non-invasive detection using liquid biopsy"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "triple negative breast cancer"


def methylation_class(row):
    return "BR_CA_TN"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"Female": "female"}
    return mapping[row["gender"]]
