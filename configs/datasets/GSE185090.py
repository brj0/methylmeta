def dataset_id(row):
    return "GSE185090"


def description(row):
    return (
        "DNA methylation-based classification of malformations of cortical "
        "development in the human brain"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    return "CTRL_BRAIN"


def sample_site(row):
    mapping = {"Cortex": "Cerebral cortex"}
    return mapping[row["Source"]]


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
