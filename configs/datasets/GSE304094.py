def dataset_id(row):
    return "GSE304094"


def description(row):
    return (
        "DNA methylation profiling of primary and recurrent human "
        "meningiomas (meningioma progression, discovery cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "MNG"


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def material_type(row):
    return "tissue"
