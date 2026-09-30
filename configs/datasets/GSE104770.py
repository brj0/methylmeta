def dataset_id(row):
    return "GSE104770"


def description(row):
    return "Global methylation patterns in primary plasma cell leukemia (pPCL)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["pc dyscrasia"]


def methylation_class(row):
    return "MYELOMA"


def sample_site(row):
    return "Bone marrow"


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
