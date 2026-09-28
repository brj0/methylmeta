def dataset_id(row):
    return "GSE79740"


def description(row):
    return "DNA methylation profiling of signet ring cell colorectal cancer"


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    mapping = {
        "normal": "Normal colorectum",
        "tumour": "Signet ring cell colorectal carcinoma",
    }
    return mapping[row["disease state"]]


def methylation_class(row):
    mapping = {
        "normal": "CTRL_COL",
        "tumour": "CR_CA",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    mapping = {
        "normal": "control",
        "tumour": "primary",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "Formal fixed paraffin embedded": "FFPE",
    }
    return mapping[row["Treatment-Protocol"]]
