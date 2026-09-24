def dataset_id(row):
    return "GSE112308"


def description(row):
    return (
        "Genome-wide methylation of superficial malignant peripheral nerve "
        "sheath tumors and spindle/desmoplastic melanomas (GSE112308)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["condition"]


def methylation_class(row):
    value = row["condition"]
    mapping = {
        "desmoplastic melanoma": "MEL_DESMO",
        "superficial MPNST": "MPNST",
        None: None,
    }
    return mapping[value]


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
