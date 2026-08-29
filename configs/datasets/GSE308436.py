def dataset_id(row):
    return "GSE308436"


def description(row):
    return "Sacral Chordoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "CHORD"


def sample_site(row):
    return row["Source"]


def sex(row):
    return row["Sex"]
