def dataset_id(row):
    return "GSE110081"


def description(row):
    return (
        "Hepatosplenic T-cell lymphoma and benign T-cell subsets "
        "(DNA methylation profiling)"
    )


def sample_id(row):
    # IDAT basenames are not available, so the GEO accession is used.
    return row["Accession"]


def diagnosis(row):
    if row["Source"] == "malignant":
        return "hepatosplenic T-cell lymphoma"
    return row["Description"].split("\n")[0]


def methylation_class(row):
    mapping = {
        "malignant": "HSTCL",
        "benign": "CTRL_BLOOD",
    }
    return mapping[row["Source"]]


def sample_type(row):
    mapping = {
        "malignant": "primary",
        "benign": "control",
    }
    return mapping[row["Source"]]


def material_type(row):
    mapping = {
        "malignant": "tissue",
        "benign": "blood",
    }
    return mapping[row["Source"]]


def preservation(row):
    return "FROZEN"
