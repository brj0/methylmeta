def dataset_id(row):
    return "GSE315451"


def description(row):
    return (
        "Blood-based epigenetic instability in aging and disease, MDS/CML "
        "diagnosis samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease"]
    mapping = {
        "CML": "Chronic myeloid leukemia",
        "MDS": "Myelodysplastic syndrome",
    }
    return mapping[value]


def methylation_class(row):
    value = row["disease"]
    mapping = {
        "CML": "CML",
        "MDS": "MDS",
    }
    return mapping[value]


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def sex(row):
    value = row["Sex"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
