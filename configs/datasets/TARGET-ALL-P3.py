def dataset_id(row):
    return "TARGET-ALL-P3"


def description(row):
    return "TARGET pediatric acute lymphoblastic leukemia cohort (phase 3)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    if value is not None:
        return value
    controls = {
        "Bone Marrow Normal": "normal bone marrow",
        "Lymphoid Normal": "normal lymphoid tissue",
    }
    return controls.get(row["sample_type"])


def methylation_class(row):
    value = row["sample_type"]
    controls = {
        "Bone Marrow Normal": "CTRL_MARROW",
        "Lymphoid Normal": "CTRL_LYMPH",
    }
    if value in controls:
        return controls[value]
    mapping = {
        "Acute lymphocytic leukemia": "B_ALL",
        "Acute myeloid leukemia, NOS": "AML",
    }
    return mapping.get(row["diagnoses.primary_diagnosis"])


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    return row["diagnoses.tissue_or_organ_of_origin"]


def sample_type(row):
    value = row["sample_type"]
    mapping = {
        "Bone Marrow Normal": "control",
        "Lymphoid Normal": "control",
        "Primary Blood Derived Cancer - Bone Marrow": "primary",
        "Primary Blood Derived Cancer - Peripheral Blood": "primary",
        "Recurrent Blood Derived Cancer - Bone Marrow": "recurrence",
    }
    return mapping[value]


def material_type(row):
    return "blood"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
