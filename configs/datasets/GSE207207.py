def dataset_id(row):
    return "GSE207207"


def description(row):
    return (
        "Methylation profiling of the peripheral nerve sheath tumor spectrum "
        "to identify MPNST epigenetic subgroups"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    mapping = {
        "Neurofibroma": "NFIB",
        "Cutaneous_NF": "NFIB",
        "Atypical_NF": "NFIB_ATY",
        "MPNST": "MPNST",
        "Low-Grade MPNST": "MPNST_LG",
    }
    return mapping[row["Source"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]
