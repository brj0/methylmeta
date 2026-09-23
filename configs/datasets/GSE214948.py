def dataset_id(row):
    return "GSE214948"


def description(row):
    return "Merkel Cell Carcinomas"


def sample_id(row):
    value = row["Sample_ID"]
    if value == "NONE":
        return None
    return value


def diagnosis(row):
    return row["cell line"]


def methylation_class(row):
    value = row["Sample_ID"]
    if value == "NONE":
        return None
    return "MCC"


def material_type(row):
    value = row["cell line"]
    if value is None:
        return None
    if "tissue" in value:
        return "tissue"
    return "cell_line"


def sample_site(row):
    return row["Source"]
