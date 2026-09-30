def dataset_id(row):
    return "GSE117439"


def description(row):
    return (
        "DNA methylation in breast cancers: differences based on estrogen "
        "receptor status and recurrence"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return (
        "breast cancer, estrogen receptor " + row["estrogen receptor status"]
    )


def methylation_class(row):
    mapping = {"positive": "BR_CA_HRP", "negative": "BR_CA"}
    return mapping[row["estrogen receptor status"]]


def sample_site(row):
    return "breast"


def primary_site(row):
    return "breast"


def sample_type(row):
    mapping = {"primary": "primary", "second": "recurrence"}
    return mapping[row["tumor status"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"female": "female", "male": "male"}
    return mapping[row["Sex"]]
