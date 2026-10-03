def dataset_id(row):
    return "GSE109904"


def description(row):
    return (
        "Methylation profiling of pediatric histiocytic sarcomas and "
        "antecedent hematologic malignancies"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "histiocytic sarcoma": "HISTSARC",
        "leukemia": "HEMA_NOS",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return row["gender"]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value.split(" ")[0])
