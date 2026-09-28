def dataset_id(row):
    return "TCGA-DLBC"


def description(row):
    return (
        "TCGA Lymphoid Neoplasm Diffuse Large B-cell Lymphoma "
        "(DLBCL), Schmitz 2018"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Diffuse large B-cell lymphoma, NOS": "DLBCL",
        "Mediastinal (thymic) large B-cell lymphoma": "PMBCL",
        "Primary diffuse large B-cell lymphoma of the CNS": "CNSL",
        "Not Reported": None,
    }
    return mapping[value]


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
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "Progression": "recurrence",
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
