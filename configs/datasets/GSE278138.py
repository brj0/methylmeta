def dataset_id(row):
    return "GSE278138"


def description(row):
    return "SNSCC + Control"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "SNSCC tumor": "Sinonasal Squamous Cell Carcinoma",
        "Nasal mucosa": "Control tissue - Normal mucosa",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "SNSCC tumor": "SN_SCC",
        "Nasal mucosa": "CONTR_SINO",
    }
    return mapping[value]


def sample_site(row):
    return "Sinonasal"


def primary_site(row):
    return "Sinonasal"
