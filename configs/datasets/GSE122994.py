def dataset_id(row):
    return "GSE122994"


def description(row):
    return (
        "Illumina 450k/EPIC methylation profiling of 380 glioblastoma "
        "patients of the Heidelberg Neuro-Oncology Center (HD collective)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"tumor_DNA_FFPE": "FFPE"}
    return mapping[row["sample preparation"]]


def sex(row):
    mapping = {"female": "female", "male": "male"}
    return mapping[row["gender"]]
