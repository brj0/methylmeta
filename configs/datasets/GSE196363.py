def dataset_id(row):
    return "GSE196363"


def description(row):
    return "DNA methylation of cell-free DNA from retinoblastoma aqueous humor"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Retinoblastoma"


def methylation_class(row):
    return "RB"


def sample_site(row):
    if "aqueous humor" in row["Source"].lower():
        return "Aqueous humor"
    return "Eye"


def primary_site(row):
    return "Eye"


def sample_type(row):
    return "primary"
