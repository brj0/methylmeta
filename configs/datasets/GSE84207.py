def dataset_id(row):
    return "GSE84207"


def description(row):
    return "Oslo2 (OSL2) breast cancer cohort (Fleischer et al. 2017)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Breast carcinoma"


def methylation_class(row):
    return "BR_CA"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return "female"
