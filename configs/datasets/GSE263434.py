def dataset_id(row):
    return "GSE263434"


def description(row):
    return "Multi-omics analysis of the JGOG3025-TR2 ovarian cancer cohort"


def sample_id(row):
    return row["Sample_ID"]


def _diagnosis_value(row):
    value = row["histology_iti"]
    if value == "Other":
        return row["histology_cpr"]
    return value


def diagnosis(row):
    return _diagnosis_value(row)


def methylation_class(row):
    mapping = {
        "Serous carcinoma": "OVA_HGSC",
        "Endometrioid carcinoma": "OVA_ENDOID_CA",
        "Clear cell carcinoma": "OVA_CCC",
        "HGSC": "OVA_HGSC",
        "EndoG3": "OVA_ENDOID_CA",
    }
    return mapping[_diagnosis_value(row)]


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
