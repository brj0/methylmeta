def dataset_id(row):
    return "GSE117852"


def description(row):
    return (
        "Methylation heterogeneity within human non-functional pancreatic "
        "neuroendocrine tumors (PanNETs)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "PAN_NET_NF"


def sample_site(row):
    return "Pancreas"


def primary_site(row):
    return "Pancreas"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
