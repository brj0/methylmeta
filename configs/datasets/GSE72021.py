def dataset_id(row):
    return "GSE72021"


def description(row):
    return (
        "Epithelial ovarian carcinoma cohort: intra-gene DNA methylation "
        "variability as a prognostic marker in women's cancers"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "clear cell": "Clear cell carcinoma",
        "endometrioid": "Endometrioid carcinoma",
        "mucinous": "Mucinous carcinoma",
        "serous": "Serous carcinoma",
        "undifferentiated": "Undifferentiated carcinoma",
    }
    return mapping[row["histology"]]


def methylation_class(row):
    mapping = {
        "clear cell": "OVA_CCC",
        "endometrioid": "OVA_ENDOID_CA",
        "mucinous": "OVA_MUC_CA",
        "serous": "OVA_HGSC",
        "undifferentiated": "OVA_UNDIFF_CA",
    }
    return mapping[row["histology"]]


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["grade"]
    if value is None:
        return None
    mapping = {
        "1": "G1",
        "2": "G2",
        "3": "G3",
        "1.0": "G1",
        "2.0": "G2",
        "3.0": "G3",
    }
    return mapping.get(str(value))


def sex(row):
    return "female"
