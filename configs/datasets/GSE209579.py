def dataset_id(row):
    return "GSE209579"


def description(row):
    return (
        "Early postoperative treatment versus initial observation in CNS WHO "
        "grade 2 and 3 oligodendroglioma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {"oligodendroglioma": "OLIGO_IDH"}
    return mapping[row["tissue"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
