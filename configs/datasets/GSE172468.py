def dataset_id(row):
    return "GSE172468"


def description(row):
    return (
        "DNA methylation profiling of recurrent sarcoma from patients "
        "treated with anti-PD-1 immune checkpoint inhibitors (2021)"
    )


def sample_id(row):
    return row["Sample_ID"]


def methylation_class(row):
    return "SARC_NOS"


def sample_type(row):
    return "recurrence"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
