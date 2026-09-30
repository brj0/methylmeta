def dataset_id(row):
    return "GSE185041"


def description(row):
    return (
        "DNA methylation profiling of posterior pituitary tumors: pituicytoma, "
        "granular cell tumor and spindle cell oncocytoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["histology"]


def methylation_class(row):
    return "PIT_SCO_GCT"


def sample_site(row):
    return "Pituitary gland"


def primary_site(row):
    return "Pituitary gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"f": "female", "m": "male"}
    return mapping[row["gender"]]
