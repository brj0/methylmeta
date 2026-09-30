def dataset_id(row):
    return "GSE168930"


def description(row):
    return (
        "Genome-wide DNA methylome analysis of human ovarian cancers "
        "(survival biomarker study)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tumour subtypes2"]
    if value is None:
        return row["tumour subtypes"]
    return value


def methylation_class(row):
    value = row["tumour subtypes2"]
    if value is None:
        # "tumour subtypes" holds the subtype code where the text is missing
        value = row["tumour subtypes"]
    mapping = {
        "serous": "OVA_HGSC",
        "clear cell": "OVA_CCC",
        "endometrioid": "OVA_ENDOID_CA",
        "mucinous": "OVA_MUC_CA",
        "seromucinous": "OVA_SM_BOT",
        "mixed clear cell and endometrioid": "OVA_CA",
        "mixed clear cell and serous": "OVA_CA",
        "mixed endoemtrioid and serous": "OVA_CA",
        "mixed endometrioid and clear cell": "OVA_CA",
        "mixed endometrioid and serous": "OVA_CA",
        "mixed endometrioid, clear cell": "OVA_CA",
        "mixed mucinous and serous": "OVA_CA",
        "mixed serous endometrioid": "OVA_CA",
        "seromucinous borderline tumour with a small focus of clear cell "
        "carcinoma and another focus of mixed endoemtrioid and mucinous "
        "tumour": "OVA_SM_BOT",
        "O1S": "OVA_HGSC",
        "O1C": "OVA_CCC",
        "O1E": "OVA_ENDOID_CA",
        "O1M": "OVA_MUC_CA",
        "O1CE": "OVA_CA",
        "O1EC": "OVA_CA",
        "O1SE": "OVA_CA",
        "O1SM": "OVA_CA",
        "O1X": "OVA_CA",
        "O16": "OVA_CA",
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


def tumor_grade(row):
    value = row["grade"]
    mapping = {
        "1": "G1",
        "2": "G2",
        "3": "G3",
        "high grade": "high-grade",
        "unknown": None,
        None: None,
    }
    return mapping[value]


def sex(row):
    return "female"


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
