def dataset_id(row):
    return "GSE226764"


def description(row):
    return (
        "DNA methylation pattern in somatotroph pituitary neuroendocrine "
        "tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    # densely granulated tumors do not resolve into group A or group B
    mapping = {
        "DG": "PIT_AD",
        "SG": "PIT_AD",
        None: "PIT_AD",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return "Pituitary gland"


def primary_site(row):
    return "Pituitary gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]
