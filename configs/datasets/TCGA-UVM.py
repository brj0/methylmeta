def dataset_id(row):
    return "TCGA-UVM"


def description(row):
    return "TCGA Uveal Melanoma cohort, Robertson 2017"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    # all samples are ocular primaries of this uveal melanoma cohort
    mapping = {
        "Epithelioid cell melanoma": "UVE_MEL",
        "Malignant melanoma, NOS": "UVE_MEL",
        "Mixed epithelioid and spindle cell melanoma": "UVE_MEL",
        "Spindle cell melanoma, NOS": "UVE_MEL",
        "Spindle cell melanoma, type B": "UVE_MEL",
        "Pheochromocytoma, malignant": "PHEO",
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
    return mapping.get(value, value)


def sample_type(row):
    mapping = {"Primary Tumor": "primary"}
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
