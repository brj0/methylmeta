def dataset_id(row):
    return "GSE178610"


def description(row):
    return (
        "Genome-wide DNA methylation profiles of endometrioid endometrial "
        "cancer tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    return "ENDOM_EC"


def sample_site(row):
    return "Endometrium"


def primary_site(row):
    return "Endometrium"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["sample type"]]
