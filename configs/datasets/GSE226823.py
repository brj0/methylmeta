def dataset_id(row):
    return "GSE226823"


def description(row):
    return (
        "DNA methylation of endometriosis-related ovarian carcinoma "
        "histotypes (clear cell, endometrioid and high-grade serous)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["histology"]
    mapping = {
        "CCOC": "Clear cell ovarian carcinoma",
        "ENOC": "Endometrioid ovarian carcinoma",
        "HGSC": "High-grade serous ovarian carcinoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["histology"]
    mapping = {
        "CCOC": "OVA_CCC",
        "ENOC": "OVA_ENDOID_CA",
        "HGSC": "OVA_HGSC",
    }
    return mapping[value]


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
