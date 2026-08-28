def dataset_id(row):
    return "GSE197094"


def description(row):
    return "Schwannoma"


def sample_id(row):
    return row["Sample_ID"]


def sex(row):
    return row["patient sex"]


def sample_site(row):
    return row["tumor location"]


def primary_site(row):
    return row["tumor location"]


def diagnosis(row):
    value = row["oncogenic driver"]
    mapping = {
        "SOX10-mutant": "Schwannoma SOX10-mutant",
        "NF2-mutant": "Schwannoma NF2-mutant",
        "HTRA1-fused": "Schwannoma HTRA1-fused",
    }
    return mapping[value]


def methylation_class(row):
    return "SCHW"


def sample_type(row):
    return "primary"


def preservation(row):
    return "FFPE"
