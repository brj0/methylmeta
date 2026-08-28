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
        "ACC": "ADCCA",
        "ADC": "SNAD",
        "ALV RMS": "RMS_ALV",
        "BP SSARC": "BSNS",
        "CTRL": "CSINONASAL",
        "EMB RMS": "RMS_EMB",
        "LECA": "LEC",
        "MELA": "MMEL",
        "PIT AD": "PITAD",
        "RHB MEN": "MEN",
        "SCC": "SNSCC",
        "SMARCB1": "SNC_SMARCB1",
        "NEC-like IDH2": "NECIDH2",
        "NEC-like SMARCA4 ARID1A": "SNNEC_SMARCA4",
        None: None,
        "Unknown": None,
    }

    base = row["methylation class"]

    # For test samples, there is no methylation diagnosis.
    if "Test_set" in row["Title"] and row["predicted class"] is not None:
        base = row["predicted class"]

    return mapping.get(base, base)
