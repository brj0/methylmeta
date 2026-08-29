def dataset_id(row):
    return "GSE243075"


def description(row):
    return "Salivary Gland Tumors, Jurmeister 2024"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    value = row["methylation class"]
    mapping = {
        "5p5q_class": "SBMC5P5Q",
        "ACC": "SACC",
        "BC_AD": "BC_AD",
        "BC": "SBCAD",
        "CADC": "SCADC",
        "CCC": "HCCC",
        "C_AD": "SCA",
        "SCA": "SSC",
        "EPMYOC": "EMC",
        "IDC": "SIDC",
        "MC": "MEC",
        "MSADC": "SMSAD",
        "MYOCA": "SMYOC",
        "MYO_PA": "MYO_PA",
        "NOR": "CONTR_SALIVARY",
        "ONCO": "SONCO",
        "P_ADC": "PAD",
        "SDCA": "SDC",
        "SPA": "SSPA",
    }
    return mapping[value]


def sample_site(row):
    return row["location"]


def primary_site(row):
    return row["location"]


def preservation(row):
    value = row["Source"]
    mapping = {
        "Surgigcal resection specimen, FFPE": "FFPE",
    }
    return mapping[value]
