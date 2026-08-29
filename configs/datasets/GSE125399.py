def dataset_id(row):
    return "GSE125399"


def description(row):
    return "Inverted sinonasal papilloma + associated Carcinoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Description"]
    mapping = {
        "sinonasal inverted papilloma": "Inverted Sinonasal Papilloma",
        "SCC arising in SNIP": "Squamous Cell Carcinoma arising in Inverted Sinonasal Papilloma",
        "quamous cell carcinomas arising in SNIP": "Squamous Cell Carcinoma arising in Inverted Sinonasal Papilloma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["condition"]
    mapping = {
        "SCC arising in SNIP": "SNSCC",
    }
    return mapping[value]


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]
