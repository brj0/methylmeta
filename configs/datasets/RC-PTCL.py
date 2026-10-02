def dataset_id(row):
    return "RC-PTCL"


def description(row):
    return "Peripheral T-cell lymphoma cohort with clinical annotations"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    if value == "Clear cell carcinoma":
        if row["diagnoses.tissue_or_organ_of_origin"] == "Kidney, NOS":
            return "RCC_CC"
        return None
    mapping = {
        "Adult T-cell leukemia/lymphoma (HTLV-1 positive) (includes all "
        "variants)": "HTLV1_ATL",
        "Anaplastic large cell lymphoma, ALK negative": "ALCL_ALK_NEG",
        "Angioimmunoblastic T-cell lymphoma": "AITL",
        "Extranodal NK/T-cell lymphoma, nasal type": "ENKTL",
        "Hepatosplenic T-cell lymphoma": "HSTCL",
        "Hodgkin lymphoma, NOS": "HODG_CL",
        "Mature T-cell lymphoma, NOS": "PTCL",
        "Myeloid leukemia, NOS": "AML",
        "Not Reported": None,
        "Peripheral T-cell lymphoma, NOS": "PTCL",
        "Prolymphocytic leukemia, T-cell type": "TPLL",
        "Renal cell carcinoma, NOS": "RCC",
        "T-cell large granular lymphocytic leukemia": "TLGLL",
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown primary site": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "Prior primary": "primary",
        "Subsequent Primary": "primary",
        "Synchronous primary": "primary",
        "Progression": "recurrence",
        "recurrence": "recurrence",
    }
    return mapping[value]


def material_type(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Blood": "blood"}
    return mapping.get(value, "tissue")


def preservation(row):
    value = row["preservation_method"]
    mapping = {"Frozen": "FROZEN"}
    return mapping[value]


def age(row):
    value = row["diagnoses.age_at_diagnosis"]
    if value is None:
        return None
    return round(float(value) / 365.25, 1)
