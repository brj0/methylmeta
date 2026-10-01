def dataset_id(row):
    return "GSE303580"


def description(row):
    return "Wilms tumour and matched non-neoplastic kidney DNA methylation profiles"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue type"]
    mapping = {
        "Wilms tumor": "Wilms tumor",
        "Non neoplastic kidney control": "Non-neoplastic kidney",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue type"]
    mapping = {
        "Wilms tumor": "WILMS",
        "Non neoplastic kidney control": "CTRL_REN",
    }
    return mapping[value]


def sample_type(row):
    value = row["tissue type"]
    mapping = {
        "Wilms tumor": "primary",
        "Non neoplastic kidney control": "control",
    }
    return mapping[value]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return "Kidney"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Sex"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]
