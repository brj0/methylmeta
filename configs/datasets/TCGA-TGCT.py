def dataset_id(row):
    return "TCGA-TGCT"


def description(row):
    return "TCGA Testicular Germ Cell Tumors (TGCT), Shen 2018"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    # every tumour in this cohort is a germ cell tumour of the testis, so
    # the class follows from the diagnosis alone; metastases retain the
    # organ of origin
    mapping = {
        "Seminoma, NOS": "SEMIN",
        "Embryonal carcinoma, NOS": "TES_EMB_CA",
        "Yolk sac tumor": "YST",
        "Teratoma, benign": "TES_MAT_TER",
        "Teratoma, malignant, NOS": "TER_POST",
        # teratocarcinoma (embryonal carcinoma + teratoma) is a mixed
        # germ cell tumour in the current WHO classification
        "Teratocarcinoma": "TES_MGCT",
        "Mixed germ cell tumor": "TES_MGCT",
        # germ cell tumour recorded without a seminoma component
        "Germ cell tumor, NOS": None,
        "Not Reported": None,
    }
    return mapping[row["diagnoses.primary_diagnosis"]]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {
        "Primary Tumor": "primary",
        "Additional - New Primary": "primary",
    }
    return mapping[row["sample_type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
