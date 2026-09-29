def dataset_id(row):
    return "TARGET-AML"


def description(row):
    return "TARGET pediatric acute myeloid leukemia cohort"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    controls = {
        "Blood Derived Normal": "normal blood",
        "Bone Marrow Normal": "normal bone marrow",
        "Fibroblasts from Bone Marrow Normal": (
            "normal bone marrow fibroblasts"
        ),
    }
    sample_type = row["sample_type"]
    if sample_type in controls:
        return controls[sample_type]
    return row["diagnoses.primary_diagnosis"]


def methylation_class(row):
    sample_type = row["sample_type"]
    controls = {
        "Blood Derived Normal": "CTRL_BLOOD",
        "Bone Marrow Normal": "CTRL_MARROW",
        "Fibroblasts from Bone Marrow Normal": "CTRL_MARROW",
    }
    if sample_type in controls:
        return controls[sample_type]
    mapping = {"Acute myeloid leukemia, NOS": "AML"}
    return mapping[row["diagnoses.primary_diagnosis"]]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    return row["diagnoses.tissue_or_organ_of_origin"]


def sample_type(row):
    value = row["sample_type"]
    mapping = {
        "Blood Derived Normal": "control",
        "Bone Marrow Normal": "control",
        "Fibroblasts from Bone Marrow Normal": "control",
        "Primary Blood Derived Cancer - Bone Marrow": "primary",
        "Primary Blood Derived Cancer - Peripheral Blood": "primary",
        "Recurrent Blood Derived Cancer - Bone Marrow": "recurrence",
        "Recurrent Blood Derived Cancer - Peripheral Blood": "recurrence",
    }
    return mapping[value]


def material_type(row):
    mapping = {
        "Blood Derived Normal": "blood",
        "Bone Marrow Normal": "blood",
        "Fibroblasts from Bone Marrow Normal": "cell_line",
        "Primary Blood Derived Cancer - Bone Marrow": "blood",
        "Primary Blood Derived Cancer - Peripheral Blood": "blood",
        "Recurrent Blood Derived Cancer - Bone Marrow": "blood",
        "Recurrent Blood Derived Cancer - Peripheral Blood": "blood",
    }
    return mapping[row["sample_type"]]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
