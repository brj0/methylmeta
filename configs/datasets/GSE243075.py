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
        "5p5q_class": "SG_MYOEP_CA_5P5Q",
        "ACC": "SG_ACIN_CA",
        "ADCCA": "ADCC",
        "BC": "SG_BC_CA",
        "BC_AD": "SG_BC_AD",
        "CADC": "SG_CRIB_CA",
        "CCC": "SG_HYAL_CCC",
        "C_AD": "SG_CANL_AD",
        "EPMYOC": "SG_EPMYO_CA",
        "IDC": "SG_INTRAD_CA",
        "MC": "MEC",
        "MSADC": "SG_MSECR_ADCA",
        "MYOCA": "SG_MYOEP_CA",
        "MYO_PA": "PLEO_AD_MYO",
        "NOR": "CTRL_SG",
        "ONCO": "SG_ONC",
        "P_ADC": "SG_POLYM_ADCA",
        "SCA": "SG_SECR_CA",
        "SDCA": "SG_DUCT_CA",
        "SPA": "SG_SCLP_AD",
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
