def dataset_id(row):
    return "GSE197696"


def description(row):
    return (
        "DNA methylation profiling of myeloid/natural killer cell precursor "
        "acute leukemia (MNKPL) using the Illumina EPIC array"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    return "ALAL"


def sample_site(row):
    value = row["Source"]
    mapping = {
        "bone marrow": "bone marrow",
        "lymph node": "lymph node",
    }
    return mapping[value]


def primary_site(row):
    return "bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Sex"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]
