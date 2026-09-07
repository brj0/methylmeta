def dataset_id(row):
    return "GSE320217"


def description(row):
    return "Methylome profiling of cartilage tumors: a promising new diagnostic tool?"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["who_diagnosis"]
    mapping = {
        "ACT": "Atypical cartilaginous tumor",
    }
    return mapping.get(value, value)


def methylation_class(row):
    value = row["methylation_class"]
    mapping = {
        "CC": "CSA_CC",
        "IDH_MUT_1": "CSA_IDH_MUT",
        "IDH_MUT_2": "CSA_IDH_MUT",
        "IDH_MUT_3": "CSA_IDH_MUT",
        "IDH_MUT_SB": "CSA_SB",
        "IDH_MUT_CONT": "CSA_IDH_MUT",
        "IDH_WT_1": "CSA_IDH_WT",
        "IDH_WT_2": "CSA_IDH_WT",
    }
    return mapping[value]


def sample_site(row):
    return row["tumor_site"]


def primary_site(row):
    if row["subdiagnosis"] == "Metastasis":
        return None
    return row["tumor_site"]


def sample_type(row):
    if row["subdiagnosis"] == "Metastasis":
        return "metastasis"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "KRYO": "FROZEN",
    }
    return mapping[row["tissue"]]


def tumor_grade(row):
    value = row["grade"]
    mapping = {
        "G0": None,
        "GX": None,
    }
    return mapping.get(value, value)


def sex(row):
    return row["gender"]


def age(row):
    value = row["age"]
    return value
