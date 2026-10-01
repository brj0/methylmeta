def dataset_id(row):
    return "GSE209668"


def description(row):
    return (
        "Integrated proteogenomic analysis of medulloblastoma progression "
        "(DNA methylation)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "medulloblastoma"


def methylation_class(row):
    return "MB"


def sample_type(row):
    mapping = {"primary": "primary", "recurrent": "recurrence"}
    return mapping[row["type"]]


def material_type(row):
    return "tissue"
