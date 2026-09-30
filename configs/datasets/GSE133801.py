def dataset_id(row):
    return "GSE133801"


def description(row):
    return "DNA methylation analysis of pineal parenchymal tumors (Liu et al., 2020)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "PINE_PPT"


def sample_site(row):
    return "Pineal gland"


def primary_site(row):
    return "Pineal gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
