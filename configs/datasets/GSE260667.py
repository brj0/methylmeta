def dataset_id(row):
    return "GSE260667"


def description(row):
    return (
        "Methylome analysis of nodal marginal zone lymphoma (nMZoL) and "
        "nodal diffuse large B-cell lymphoma (nDLBCL)"
    )


def _cohort(row):
    value = row["Description"] or row["Title"]
    if "nDLBCL" in value:
        return "nDLBCL"
    if "nMZoL" in value:
        return "nMZoL"
    return None


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "nMZoL": "Nodal marginal zone lymphoma",
        "nDLBCL": "Diffuse large B-cell lymphoma, NOS",
    }
    return mapping.get(_cohort(row))


def methylation_class(row):
    mapping = {
        "nMZoL": "NMZL",
        "nDLBCL": "DLBCL",
    }
    return mapping.get(_cohort(row))


def sample_site(row):
    return "Lymph node"


def primary_site(row):
    return "Lymph node"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping.get(row["gender"])


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
