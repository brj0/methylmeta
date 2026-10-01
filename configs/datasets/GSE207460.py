def dataset_id(row):
    return "GSE207460"


def description(row):
    return (
        "Breast cancer biopsies before, during and after neoadjuvant "
        "chemotherapy with or without bevacizumab"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


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
