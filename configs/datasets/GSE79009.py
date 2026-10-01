def dataset_id(row):
    return "GSE79009"


def description(row):
    return "Genomic landscape of schwannoma (Agnihotri et al., 2016)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "SCHW"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
