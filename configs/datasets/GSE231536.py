def dataset_id(row):
    return "GSE231536"


def description(row):
    return (
        "DNA methylation profiling of human retina tissue from post-mortem "
        "donors, including controls and age-related macular degeneration cases"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "retina"


def methylation_class(row):
    # non-tumorous retina tissue; eye is the most specific control organ
    return "CTRL_EYE"


def sample_site(row):
    return "retina"


def primary_site(row):
    return "retina"


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
