def dataset_id(row):
    return "GSE136790"


def description(row):
    return "Epigenome analysis of uterine and ovarian carcinosarcoma tissues"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["patient diagnosis"]


def methylation_class(row):
    value = row["patient diagnosis"]
    mapping = {
        "uterine carcinosarcoma": "UCS",
        "ovarian carcinosarcoma": "OVA_CSARC",
    }
    return mapping[value]


def sample_site(row):
    return row["anatomical site"]


def primary_site(row):
    return row["anatomical site"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return "female"
