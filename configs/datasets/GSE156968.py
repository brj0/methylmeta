def dataset_id(row):
    return "GSE156968"


def description(row):
    return (
        "DNA methylation profiling of flash frozen breast tumors from "
        "American women of African and European ancestry (2021)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Breast tumor"


def methylation_class(row):
    return "BR_CA"


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
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
