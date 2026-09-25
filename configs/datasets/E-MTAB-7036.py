def dataset_id(row):
    return "E-MTAB-7036"


def description(row):
    return "Colorectal cancer methylome profiling"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"].strip()


def methylation_class(row):
    value = row["Characteristics[sampling site]"]
    mapping = {
        "neoplasm": "CR_CA",
        "normal tissue adjacent to neoplasm": "CTRL_COL",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "colon"


def sample_type(row):
    value = row["Characteristics[sampling site]"]
    mapping = {
        "neoplasm": "primary",
        "normal tissue adjacent to neoplasm": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"male": "male", "female": "female"}
    return mapping[row["Characteristics[sex]"]]


def age(row):
    return float(row["Characteristics[age]"])
