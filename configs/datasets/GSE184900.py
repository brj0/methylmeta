def dataset_id(row):
    return "GSE184900"


def description(row):
    return (
        "Comprehensive profiling of myxopapillary ependymomas identifies a "
        "distinct molecular subtype with relapsing disease"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "myxopapillary ependymoma"


def methylation_class(row):
    return "EPN_MPE"


def sample_site(row):
    return row["localization"]


def primary_site(row):
    return "Spinal cord"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return mapping[row["material"]]


def sex(row):
    return row["Sex"]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
