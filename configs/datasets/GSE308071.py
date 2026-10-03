def dataset_id(row):
    return "GSE308071"


def description(row):
    return (
        "DNA methylation profiling of intracranial mesenchymal tumors with "
        "FET-CREB fusion (ICMT)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Intracranial mesenchymal tumor with FET-CREB fusion"


def methylation_class(row):
    return "ICMT"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return row["material"]


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
