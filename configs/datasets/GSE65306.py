def dataset_id(row):
    return "GSE65306"


def description(row):
    return "Relapse neuroblastoma methylation cohort (Eleveld 2015)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    return "NBL"


def sample_type(row):
    mapping = {
        "Tumour": "primary",
        "Relapse": "recurrence",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"
