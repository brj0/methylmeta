def dataset_id(row):
    return "GSE228091"


def description(row):
    return (
        "Paired primary and relapsed atypical teratoid/rhabdoid "
        "tumors (AT/RT) profiled by DNA methylation"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Atypical teratoid/rhabdoid tumor"


def methylation_class(row):
    mapping = {
        "MYC": "ATRT_MYC",
        "SHH-1A": "ATRT_SHH",
        "SHH-1B": "ATRT_SHH",
        "SHH-2": "ATRT_SHH",
        "SMARCA4": "ATRT",
        "TYR": "ATRT_TYR",
    }
    return mapping[row["molecular_subtype"]]


def sample_type(row):
    mapping = {"Primary": "primary", "Recurrence": "recurrence"}
    return mapping[row["disease_ status"]]


def sample_site(row):
    return row["localization"]


def primary_site(row):
    return "Central nervous system"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "KRYO": "FROZEN"}
    return mapping[row["conservation_ type"]]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age_ onset_ years"]
    if value is None:
        return None
    return float(value)
