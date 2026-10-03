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
        "ACC": "ACICC",
        "ADCCA": "ADCC",
        "BC": "SG_BC_ADCA",
        "BC_AD": "SG_BC_AD",
        "CADC": "SG_CRIB_ADCA",
        "CCC": "SG_HYAL_CCC",
        "C_AD": "SG_CANL_AD",
        "EPMYOC": "SG_EPIMYO_CA",
        "IDC": "SG_INTRA_CA",
        "MC": "MEC",
        "MSADC": "SG_MSECR_ADCA",
        "MYOCA": "SG_MYOEP_CA",
        "MYO_PA": "PLEO_MYO",
        "NOR": "CTRL_SG",
        "ONCO": "SG_ONC",
        "P_ADC": "SG_POLYM_ADCA",
        "SCA": "SG_SECR_CA",
        "SDCA": "SDC",
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
