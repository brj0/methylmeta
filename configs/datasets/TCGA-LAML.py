def dataset_id(row):
    return "TCGA-LAML"


def description(row):
    return "TCGA Acute Myeloid Leukemia (LAML), Ley 2013"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnoses.primary_diagnosis"]


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Acute megakaryoblastic leukaemia": "AMKL",
        "Acute monocytic leukemia": "AMOL",
        "Acute myeloid leukemia, M6 type": "AEL",
        "Acute myeloid leukemia, NOS": "AML",
        "Acute myeloid leukemia, minimal differentiation": "AML_MIN_DIFF",
        "Acute myeloid leukemia with maturation": "AML_WITH_MAT",
        "Acute myeloid leukemia without maturation": "AML_NO_MAT",
        "Acute myelomonocytic leukemia": "AMML",
        "Acute promyelocytic leukaemia, t(15;17)(q22;q11-12)": (
            "AML_PML_RARA"
        ),
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
