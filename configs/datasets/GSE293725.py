def dataset_id(row):
    return "GSE293725"


def description(row):
    return (
        "Mucinous cystic neoplasms of the pancreas and liver share a DNA "
        "methylation profile with mucinous ovarian tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["sample group"]
    mapping = {
        "MCN-P": "Mucinous cystic neoplasm of the pancreas",
        "MCN-L": "Mucinous cystic neoplasm of the liver",
        "gIPMN": "Intraductal papillary mucinous neoplasm of the pancreas",
    }
    return mapping[value]


def methylation_class(row):
    value = row["sample group"]
    mapping = {
        "MCN-P": "PAN_MCN",
        "MCN-L": "MCN",
        "gIPMN": "IPMN",
    }
    return mapping[value]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return "female"
