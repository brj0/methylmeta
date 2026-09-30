def dataset_id(row):
    return "GSE172081"


def description(row):
    return "DNA methylation profiling of FGFR2-fused low-grade neuroepithelial tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    return "PLNTY"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["patient sex"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]


def age(row):
    return float(row["patient age at dx (yrs)"])
