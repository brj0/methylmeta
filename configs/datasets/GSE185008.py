def dataset_id(row):
    return "GSE185008"


def description(row):
    return "DNA methylation profiling of ovarian clear cell carcinoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["histology"]


def methylation_class(row):
    return "OVA_CCC"


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return row["gender"].lower()
