def dataset_id(row):
    return "GSE298677"


def description(row):
    return (
        "DNA methylation patterns of primary hepatic neuroendocrine neoplasms"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Hepatic neuroendocrine neoplasm"


def methylation_class(row):
    return "LIV_NET"


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
