def dataset_id(row):
    return "GSE136724"


def description(row):
    return (
        "DNA methylation of chronic lymphocytic leukemia with differential "
        "response to chemotherapy"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Chronic lymphocytic leukemia"


def methylation_class(row):
    value = row["ighv_mutation_status"]
    mapping = {
        "mutated": "CLL_IGHV_MUT",
        "unmutated": "CLL_IGHV_UNMUT",
    }
    return mapping[value]


def sample_site(row):
    return "blood"


def primary_site(row):
    return "blood"


def sample_type(row):
    value = row["Source"]
    mapping = {
        "CLL, group A (del(17p) and/or TP53mut, untreated)": "primary",
        "CLL, group B (del(17p) and/or TP53mut, relapsed)": "recurrence",
        "CLL, group C (del(17p) and/or TP53mut, refractory)": "recurrence",
        "CLL, group D (no del(17p) or TP53mut, chemosensitive)": "primary",
        "CLL, group E (no del(17p) or TP53mut, refractory)": "recurrence",
    }
    return mapping[value]


def material_type(row):
    return "blood"


def sex(row):
    value = row["Sex"]
    mapping = {
        "female": "female",
        "male": "male",
        "unknown": row["predicted_sex_rnbeads_package_in_bioconductor"],
    }
    return mapping[value]


def age(row):
    value = row["age_years"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
