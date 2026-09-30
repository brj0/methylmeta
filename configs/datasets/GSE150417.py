def dataset_id(row):
    return "GSE150417"


def description(row):
    return (
        "Genome-wide DNA methylation analysis along the progression of "
        "gastric marginal zone B-cell lymphoma of MALT type"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "small cell MALT lymphoma": "ENMZL_MALT",
        "large cell MALT lymphoma": "ENMZL_MALT",
        "composite lymphomas including both the large and small-cell "
        "components": "ENMZL_MALT",
        "small cell component of composite lymphoma": "ENMZL_MALT",
        "large cell component of composite lymphoma": "ENMZL_MALT",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Stomach"


def primary_site(row):
    return "Stomach"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "cryopreserved": "FROZEN"}
    return mapping[row["tissue type"]]


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
