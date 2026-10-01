def dataset_id(row):
    return "GSE296440"


def description(row):
    return (
        "DNA methylation-based stratification of pediatric thyroid "
        "carcinoma invasiveness (CHOP cohort, 1st batch)"
    )


def sample_id(row):
    return row["Sample_ID"]


def _is_metastasis(row):
    return row["Stage"] == "Lymph.Node.Met" or "LN" in row["case_id"]


def diagnosis(row):
    if _is_metastasis(row):
        return "Metastatic thyroid carcinoma"
    return "Thyroid carcinoma"


def methylation_class(row):
    return "THYR_CA"


def sample_site(row):
    if _is_metastasis(row):
        return "Lymph node"
    return "Thyroid gland"


def primary_site(row):
    return "Thyroid gland"


def sample_type(row):
    if _is_metastasis(row):
        return "metastasis"
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
