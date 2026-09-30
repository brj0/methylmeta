def dataset_id(row):
    return "GSE136791"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of endometrial endometrioid "
        "adenocarcinoma and endometrial hyperplasia tissues"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["tissue"] == "Hyperplasia":
        return "Endometrial hyperplasia"
    return row["patient diagnosis"]


def methylation_class(row):
    mapping = {
        "Carcinoma": "ENDOM_EC",
        "Hyperplasia": "EMH",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return row["anatomical site"]


def primary_site(row):
    return row["anatomical site"]


def sample_type(row):
    mapping = {
        "Carcinoma": "primary",
        "Hyperplasia": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def sex(row):
    return "female"
