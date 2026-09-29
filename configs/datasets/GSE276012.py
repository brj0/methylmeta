def dataset_id(row):
    return "GSE276012"


def description(row):
    return (
        "DNA methylation profiling of FFPE Ewing sarcoma samples to "
        "quantify tumour-infiltrating immune cells"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Ewing sarcoma"


def methylation_class(row):
    return "EWS"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["patient's gender_1"]
    mapping = {
        "F": "female",
        "M": "male",
    }
    return mapping[value]


def age(row):
    value = row["patient's age (years)"]
    if value is None:
        return None
    return float(value)
