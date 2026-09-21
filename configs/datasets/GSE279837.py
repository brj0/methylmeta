def dataset_id(row):
    return "GSE279837"


def description(row):
    return "Soft tissue myoepithelial tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Myoepithelial Tumor"


def methylation_class(row):
    return "SG_MYO"


def sample_site(row):
    return "Soft Tissue"


def primary_site(row):
    return "Soft Tissue"


def sample_type(row):
    return "primary"


def preservation(row):
    return "FFPE"
