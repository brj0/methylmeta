def dataset_id(row):
    return "GSE89803"


def description(row):
    return "Bile duct tumor and normal methylation profiles (Jusakul 2017)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "bile duct tumor": "Cholangiocarcinoma",
        "bile duct normal": "Normal bile duct",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "bile duct tumor": "CCA",
        "bile duct normal": "CTRL_BD",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    mapping = {
        "bile duct tumor": "primary",
        "bile duct normal": "control",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Bile duct"


def primary_site(row):
    return "Bile duct"


def material_type(row):
    return "tissue"
