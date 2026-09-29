def dataset_id(row):
    return "GSE289017"


def description(row):
    return (
        "Preclinical Pediatric MATCH: orthotopic patient-derived xenografts "
        "and matched patient tumors of pediatric solid tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease_state"]


def methylation_class(row):
    value = row["disease_state"]
    mapping = {
        "ACC": "ADREN_CORT_CA",
        "CCS": "CCS",
        "CIC-rearranged sarcoma": "SARC_CIC",
        "DSRCT": "DSRCT",
        "EWS": "EWS",
        "Embryonal sarcoma": "LIV_EMB",
        "HB": "HEPBL",
        "MEL": "MEL",
        "MRT": "MRT",
        "NB": "NBL",
        "OS": "OS",
        "RB": "RB",
        "RMS": "RMS",
        "SS": "SYNSARC",
        "WT": "WILMS",
    }
    return mapping[value]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    mapping = {
        "Patient tumor": "primary",
        "Xenograft": "primary",
    }
    return mapping[row["sample type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    title = row["Title"].upper()
    if "FFPE" in title:
        return "FFPE"
    if "FROZEN" in title:
        return "FROZEN"
    if "FRESH" in title:
        return "FRESH"
    return None


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age at collection (yr)"])
