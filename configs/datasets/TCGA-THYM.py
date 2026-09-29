def dataset_id(row):
    return "TCGA-THYM"


def description(row):
    return "TCGA Thymoma (THYM), Radovich et al. 2018"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal thymus"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_THYM"
    mapping = {
        "Thymoma, type A, NOS": "THYMO_A",
        "Thymoma, type A, malignant": "THYMO_A",
        "Thymoma, type AB, NOS": "THYMO_AB",
        "Thymoma, type AB, malignant": "THYMO_AB",
        "Thymoma, type B1, NOS": "THYMO_B1",
        "Thymoma, type B1, malignant": "THYMO_B1",
        "Thymoma, type B2, NOS": "THYMO_B2",
        "Thymoma, type B2, malignant": "THYMO_B2",
        "Thymoma, type B3, malignant": "THYMO_B3",
        "Thymic carcinoma, NOS": "THYM_CA",
        # a few rows carry a prior/subsequent primary of the same patient
        # instead of the thymic tumour (basal cell carcinoma, head and neck)
        "Basal cell carcinoma, NOS": "BCC",
        "Not Reported": None,
    }
    return mapping[row["diagnoses.primary_diagnosis"]]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


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
        "Solid Tissue Normal": "control",
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
