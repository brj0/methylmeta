def dataset_id(row):
    return "GSE200647"


def description(row):
    return (
        "DNA methylation profiling of glioblastoma and ganglioglioma samples "
        "with FGFR3-TACC3 fusions"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "GBM": "Glioblastoma",
        "GBM-F3T3-O": "Glioblastoma, FGFR3-TACC3 fusion",
        "GBM-G34": "Glioblastoma, G34-mutant",
        "Ganglioglioma": "Ganglioglioma",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "GBM": "GBM_NOS",
        "GBM-F3T3-O": "DG_F3T3_O",
        "GBM-G34": "DHG_G34",
        "Ganglioglioma": "LGG_GG",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return row["material"]


def sex(row):
    mapping = {"Male": "male", "Female": "female", None: None}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
