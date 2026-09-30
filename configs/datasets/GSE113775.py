def dataset_id(row):
    return "GSE113775"


def description(row):
    return (
        "DNA methylation of an esophageal neuroendocrine carcinoma and "
        "the matched normal esophagus"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "tumor": "esophageal neuroendocrine carcinoma",
        "normal": "normal esophagus tissue",
    }
    return mapping[row["disease state"]]


def methylation_class(row):
    mapping = {
        "tumor": "ESO_NEC",
        "normal": "CTRL_ESO",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    mapping = {
        "tumor": "primary",
        "normal": "control",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def sex(row):
    return row["gender"]
