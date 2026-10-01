def dataset_id(row):
    return "GSE80508"


def description(row):
    return (
        "DNA methylation profiling of t(8;21)-positive and t(8;21)-negative "
        "acute myeloid leukemia and normal bone marrow"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    value = row["diagnosis"]
    mapping = {"Healthy donor": "Normal bone marrow"}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["diagnosis"]
    mapping = {
        "Healthy donor": "CTRL_MARROW",
        "t(8;21)-positive AML": "AML_RUNX1_RUNX1T1",
        "t(8;21)-negative AML": "AML",
    }
    return mapping[value]


def sample_site(row):
    return "Bone marrow"


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    mapping = {
        "Healthy donor": "control",
        "t(8;21)-positive AML": "primary",
        "t(8;21)-negative AML": "primary",
    }
    return mapping[row["diagnosis"]]


def material_type(row):
    return "blood"
