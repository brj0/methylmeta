def dataset_id(row):
    return "GSE150654"


def description(row):
    return "Methylation profiles of microglandular adenosis, normal breast and breast cancer"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "breast, microglandular adenosis": "MGA",
        "breast, normal mammary glands": "CTRL_BR",
        "breast, hormone-receptor-positive breast cancer": "BR_CA_HRP",
        "breast, triple-negative breast cancer": "BR_CA_TN",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    mapping = {
        "breast, normal mammary glands": "control",
    }
    return mapping.get(row["tissue"], "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return "female"
