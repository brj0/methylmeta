def dataset_id(row):
    return "GSE198656"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of gliomas arising in the "
        "setting of neurofibromatosis type 1"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Description"]
    return value.split("\n")[0].split("\\n")[0].strip()


def methylation_class(row):
    # TODO: Use the study metadata
    return None


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
    value = row["patient age"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
