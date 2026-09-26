def dataset_id(row):
    return "GSE179458"


def description(row):
    return (
        "Integrated epigenomic and genomic view on phyllodes and "
        "phyllodes-like breast tumors, Hench (2021)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tumor type"]
    mapping = {
        "BR_CA": "Breast carcinoma",
        "BR_FAD": "Fibroadenoma of the breast",
        "FA": "Fibroadenoma of the breast",
        "benign PT": "Benign phyllodes tumor",
        "PHYT_BEN": "Benign phyllodes tumor",
        "borderline PT": "Borderline phyllodes tumor",
        "PHYT_BOR": "Borderline phyllodes tumor",
        "malignant PT": "Malignant phyllodes tumor",
        "PHYT_MAL": "Malignant phyllodes tumor",
        "PT NOS": "Phyllodes tumor, NOS",
        "PHYT_NOS": "Phyllodes tumor, NOS",
        "benign or borderline PT": ("Phyllodes tumor, benign or borderline"),
        "DLBCL": "Diffuse large B-cell lymphoma",
        "AS": "Angiosarcoma",
        "DNADEG": "Degenerated DNA",
        "-": None,
    }
    return mapping[value]


def methylation_class(row):
    value = row["tumor type"]
    mapping = {
        "BR_CA": "BR_CA",
        "BR_FAD": "BR_FAD",
        "FA": "BR_FAD",
        "benign PT": "PHYT_BEN",
        "PHYT_BEN": "PHYT_BEN",
        "borderline PT": "PHYT_BOR",
        "PHYT_BOR": "PHYT_BOR",
        "malignant PT": "PHYT_MAL",
        "PHYT_MAL": "PHYT_MAL",
        "PT NOS": "PHYT_NOS",
        "PHYT_NOS": "PHYT_NOS",
        "benign or borderline PT": "PHYT_NOS",
        "DLBCL": "DLBCL",
        "AS": "ANGSARC",
        "DNADEG": "CTRL_DNA_DEG",
        "-": None,
    }
    return mapping[value]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["tissue source"]
    mapping = {
        "DNA FFPE": "FFPE",
        "DNA native": "FROZEN",
    }
    return mapping[value]


def sex(row):
    return "female"
