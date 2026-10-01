def dataset_id(row):
    return "GSE307029"


def description(row):
    return "Methylation profiling of advanced small cell lung cancers and "
    "large cell neuroendocrine carcinomas from EBUS-TBNA lymph node "
    "aspirates"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue type"]
    mapping = {
        "sclc": "Small cell lung carcinoma",
        "LCNEC": "Large cell neuroendocrine carcinoma of the lung",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue type"]
    mapping = {
        "sclc": "SCLC",
        "LCNEC": "LCNEC",
    }
    return mapping[value]


def sample_type(row):
    return "metastasis"


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return "Lung"


def material_type(row):
    return "tissue"
