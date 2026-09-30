def dataset_id(row):
    return "GSE138221"


def description(row):
    return "Methylation profiling of desmoplastic myxoid tumors of the pineal region"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"].split("\n")[0].strip()


def methylation_class(row):
    return "DMT_SMARCB1"


def sample_site(row):
    return "Pineal region"


def primary_site(row):
    return "Pineal region"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
