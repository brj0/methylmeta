def dataset_id(row):
    return "GSE290457"


def description(row):
    return (
        "Malignant peripheral nerve sheath tumors treated with surgical "
        "resection and postoperative radiation"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Malignant peripheral nerve sheath tumor"


def methylation_class(row):
    return "MPNST"


def sample_site(row):
    return "Peripheral nerve"


def primary_site(row):
    return "Peripheral nerve"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]
