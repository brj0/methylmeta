def dataset_id(row):
    return "GSE160958"


def description(row):
    return "DNA methylation profiling of embryonal tumors with multilayered rosettes (ETMR)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Embryonal tumor with multilayered rosettes"


def methylation_class(row):
    return "ETMR"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"Frozen": "FROZEN"}
    return mapping[row["tissue preparation"]]
