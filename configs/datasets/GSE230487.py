def dataset_id(row):
    return "GSE230487"


def description(row):
    return (
        "Methylation profiling of blastic plasmacytoid dendritic cell neoplasm"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Blastic plasmacytoid dendritic cell neoplasm"


def methylation_class(row):
    return "BPDCN"


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["primary location"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]


def age(row):
    return float(row["age"])
