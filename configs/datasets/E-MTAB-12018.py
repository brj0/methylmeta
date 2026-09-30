def dataset_id(row):
    return "E-MTAB-12018"


def description(row):
    return (
        "DNA methylation profiling of chronic lymphocytic leukaemia (CLL) "
        "subsets: unmutated CLL and mutated CLL"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[clinical information]"]
    mapping = {
        "muted B cell": "CLL_IGHV_MUT",
        "unmuted B cell": "CLL_IGHV_UNMUT",
    }
    return mapping[value]


def sample_site(row):
    return "blood"


def primary_site(row):
    return "blood"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def sex(row):
    return row["Characteristics[sex]"]
