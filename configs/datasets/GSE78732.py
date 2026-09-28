def dataset_id(row):
    return "GSE78732"


def description(row):
    return (
        "DNA methylation profiling of hepatoblastomas and adjacent "
        "non-tumoral differentiated livers (HM450K)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "normal": "normal differentiated liver",
        "tumor": "hepatoblastoma",
    }
    return mapping[row["Description"]]


def methylation_class(row):
    mapping = {
        "normal": "CTRL_LIV",
        "tumor": "HEPBL",
    }
    return mapping[row["Description"]]


def sample_type(row):
    mapping = {
        "normal": "control",
        "tumor": "primary",
    }
    return mapping[row["Description"]]


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"female": "female", "male": "male", "na": None}
    return mapping[row["gender"]]
