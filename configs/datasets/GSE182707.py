def dataset_id(row):
    return "GSE182707"


def description(row):
    return "DNA methylation profiles for the SIOP Ependymoma I Study"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    value = row["methylation class"]
    mapping = {
        "PFA": "EPN_PF_A",
        "PFB": "EPN_PF_B",
        "RELA": "EPN_ST_ZFTA",
        "YAP": "EPN_ST_YAP1",
    }
    return mapping[value]


def sample_site(row):
    value = row["tumour location"]
    mapping = {
        "PF": "Posterior fossa",
        "ST": "Supratentorial",
    }
    return mapping[value]


def primary_site(row):
    return sample_site(row)


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["who grade"]
    mapping = {
        "II": "G2",
        "III": "G3",
    }
    return mapping[value]
