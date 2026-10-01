def dataset_id(row):
    return "GSE289985"


def description(row):
    return (
        "DNA methylation profiling of human ALK-positive large B-cell "
        "lymphoma samples and the LM1 cell line"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "ALKLBCL"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "ALK-positive large B-cell lymphoma": "tissue",
        "ALK-positive large B-cell lymphoma, cell line": "cell_line",
    }
    return mapping[row["Source"]]
