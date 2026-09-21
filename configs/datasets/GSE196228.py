def dataset_id(row):
    return "GSE196228"


def description(row):
    return "Sinonasal Tumors, Jurmeister 2022"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["initial diagnosis"]


def primary_site(row):
    value = row["localization"]
    mapping = {"k. A.": None}
    return mapping.get(value, value)


def sample_site(row):
    value = row["localization"]
    mapping = {"k. A.": None}
    return mapping.get(value, value)


def sex(row):
    return row["gender"]


def age(row):
    return row["age"]


def preservation(row):
    return "FFPE"


def methylation_class(row):
    mapping = {
        "ACC": "ADCC",
        "ADC": "SNAD",
        "ALV RMS": "RMS_ALV",
        "BP SSARC": "BSNS",
        "CPH": "SINO_GPC",
        "CTRL": "CTRL_SINO",
        "EMB RMS": "RMS_EMB",
        "EWS": "EWS",
        "GPC": "SINO_GPC",
        "LECA": "LEC",
        "MCC": "MCC",
        "MELA": "MEL_MUC",
        "NEC-like IDH2": "NECIDH2",
        "NEC-like SMARCA4 ARID1A": "SNNEC_SMARCA4",
        "NUT": "NUT",
        "ONB": "ONB",
        "PIT AD": "PITAD",
        "RHB MEN": "MNG",
        "SCC": "SN_SCC",
        "SMARCB1": "SMARCB1",
        "SNUC": "SNUC",
        "Unknown": None,
        None: None,
    }

    value = row["methylation class"]

    # For test samples, there is no methylation diagnosis.
    if "Test_set" in row["Title"] and row["predicted class"] is not None:
        value = row["predicted class"]

    return mapping[value]
