def dataset_id(row):
    return "GSE221029"


def description(row):
    return (
        "DNA methylation profiling of human FFPE meningioma samples "
        "(Chen, Choudhury et al.)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease"]


def methylation_class(row):
    return "MNG"


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
