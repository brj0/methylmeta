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
        "5p5q_class": "SG_MYOEP_5P5Q",
        "ACC": "SG_ACICC",
        "ADCCA": "ADCC",
        "BC": "BCAC",
        "BC_AD": "BCA",
        "CADC": "SG_CRIB_CA",
        "CCC": "HCCC",
        "C_AD": "SG_CAN_AD",
        "EPMYOC": "EMC",
        "IDC": "SG_IDCA",
        "MC": "MEC",
        "MSADC": "MSA",
        "MYOCA": "SG_MYOEP_CA",
        "MYO_PA": "PLEO_AD_MYO",
        "NOR": "CTRL_SG",
        "ONCO": "SG_ONCO",
        "P_ADC": "PMA",
        "SCA": "SG_SECR_CA",
        "SDCA": "SDC",
        "SPA": "SSPA",
        "WARTH": "WARTH",
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
