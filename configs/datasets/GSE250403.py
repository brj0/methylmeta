def dataset_id(row):
    return "GSE250403"


def description(row):
    return (
        "Infinium MethylationEPIC profiling of primary and recurrent "
        "desmoid tumors; intra- and inter-tumor heterogeneity study"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "desmoid tumor"


def methylation_class(row):
    return "DESMOID"


def sample_site(row):
    return row["site of primary tumor"]


def primary_site(row):
    return row["site of primary tumor"]


def sample_type(row):
    if "primary" in row["Source"]:
        return "primary"
    return "recurrence"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def age(row):
    value = row["age at diagnosis"]
    if value is None:
        return None
    return float(value)
