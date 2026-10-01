def dataset_id(row):
    return "GSE254031"


def description(row):
    return (
        "DNA methylation profiling of papillary tumors of the pineal region "
        "(PTPR)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Papillary tumor of the pineal region"


def methylation_class(row):
    return "PTPR"


def sample_site(row):
    return "Pineal region"


def primary_site(row):
    return "Pineal region"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return row["material"]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
