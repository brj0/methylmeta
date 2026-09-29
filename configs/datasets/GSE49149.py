def dataset_id(row):
    return "GSE49149"


def description(row):
    return (
        "Genome-wide DNA methylation patterns in pancreatic ductal "
        "adenocarcinoma (PDAC)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["Source"] == "Adjacent":
        return "non-tumorous adjacent pancreatic tissue"
    return "pancreatic ductal adenocarcinoma"


def methylation_class(row):
    mapping = {
        "Tumor": "PAN_CA",
        "Adjacent": "CTRL_PAN",
    }
    return mapping[row["Source"]]


def sample_type(row):
    mapping = {
        "Tumor": "primary",
        "Adjacent": "control",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Pancreas"


def primary_site(row):
    return "Pancreas"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
