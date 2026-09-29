def dataset_id(row):
    return "GSE270084"


def description(row):
    return (
        "Genome-wide methylation patterns in primary uveal melanoma "
        "(MethylSig-UM epigenomic prognostic signature)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "UVE_MEL"


def sample_site(row):
    return "Uvea"


def primary_site(row):
    return "Uvea"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
