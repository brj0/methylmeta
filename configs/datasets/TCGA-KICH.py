def dataset_id(row):
    return "TCGA-KICH"


def description(row):
    return "Kidney chromophobe renal cell carcinoma cohort, Davis 2014"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Renal cell carcinoma, chromophobe type": "RCC_CP",
        "Adenocarcinoma, NOS": "RCC",
        "Carcinoma, NOS": "RCC",
        "Melanoma, NOS": "MEL",
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    if value in {None, "Not Reported"}:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    if value in {None, "Not Reported"}:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "Prior primary": "primary",
        "Synchronous primary": "primary",
        "metastasis": "metastasis",
        "recurrence": "recurrence",
        "not reported": None,
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
