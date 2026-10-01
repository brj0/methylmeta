def dataset_id(row):
    return "GSE197378"


def description(row):
    return "Methylation profiling of CNS hemangioblastomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "HMB"


def sample_site(row):
    return row["location"]


def primary_site(row):
    return row["location"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
