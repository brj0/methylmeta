def dataset_id(row):
    return "GSE164994"


def description(row):
    return (
        "DNA methylation profiling of intracranial mesenchymal tumors with "
        "FET-CREB fusions"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Intracranial mesenchymal tumor with FET-CREB fusion"


def methylation_class(row):
    return "ICMT"


def sample_site(row):
    return row["tumor location"]


def primary_site(row):
    return row["tumor location"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["patient sex"]


def age(row):
    return float(row["patient age at dx (yrs)"])
