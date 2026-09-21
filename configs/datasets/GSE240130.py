def dataset_id(row):
    return "GSE240130"


def description(row):
    return "Nasal epithelium (control)"


def sample_id(row):
    return row["Sample_ID"]


def methylation_class(row):
    return "CTRL_SINO"


def sample_site(row):
    return "Nasal-Epithelial Tissue Swab"


def sex(row):
    return row["Sex"]


def age(row):
    return row["age"]
