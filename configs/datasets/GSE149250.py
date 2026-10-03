def dataset_id(row):
    return "GSE149250"


def description(row):
    return (
        "Pancreatic ductal adenocarcinoma and non-tumoral pancreas "
        "methylome profiling"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "PDAC sample": "pancreatic ductal adenocarcinoma",
        "PT sample": "non-tumoral pancreatic tissue",
    }
    return mapping[row["Description"]]


def methylation_class(row):
    mapping = {
        "PDAC sample": "PDAC",
        "PT sample": "CTRL_PAN",
    }
    return mapping[row["Description"]]


def sample_site(row):
    return "Pancreas"


def primary_site(row):
    return "Pancreas"


def sample_type(row):
    mapping = {
        "PDAC sample": "primary",
        "PT sample": "control",
    }
    return mapping[row["Description"]]


def material_type(row):
    return "tissue"


def tumor_grade(row):
    mapping = {"0": None, "G2": "G2", "G3": "G3"}
    return mapping[row["histologic_grade"]]


def sex(row):
    return row["gender"]


def age(row):
    return float(row["age"])
