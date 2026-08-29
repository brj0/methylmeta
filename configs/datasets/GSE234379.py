def dataset_id(row):
    return "GSE234379"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    if row["hpv status"] == "Negative" and "carcinoma" in row["Source"]:
        return "HNSCC_HPV_NEG"
    elif row["hpv status"] == "Positive" and "carcinoma" in row["Source"]:
        return "HNSCC_HPV_POS"
    else:
        return "CONTR_HN"


def sample_site(row):
    return row["Source"]


def sample_type(row):
    return "primary"


def sex(row):
    return row["gender"]


def age(row):
    return row["age"]
