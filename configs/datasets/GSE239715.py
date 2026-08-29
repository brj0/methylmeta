def dataset_id(row):
    return "GSE239715"


def description(row):
    return "Schwannoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Schwannoma (segmental Schwannomatosis, SOX10-mutant)"


def methylation_class(row):
    return "SCHW"


def sample_site(row):
    return row["tumor location"]


def primary_site(row):
    return row["tumor location"]


def preservation(row):
    value = row["Source"]
    mapping = {
        "FFPE tumor tissue of schwannoma": "FFPE",
    }
    return mapping[value]


def sex(row):
    return row["patient sex"]
