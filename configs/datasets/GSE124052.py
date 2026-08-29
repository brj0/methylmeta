def dataset_id(row):
    return "GSE124052"


def description(row):
    return "SCC Lung metastases"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Title"]


def methylation_class(row):
    title = row["Title"]
    hpv_geno = row["hpv genotyping"]
    p16 = row["p16 immunohistochemistry"]
    if "lung" in title:
        return "NSCLC_SCC"
    elif p16 == "Positive" or "HPV" in hpv_geno:
        return "HNSCC_HPV_POS"
    else:
        return "HNSCC_HPV_NEG"


def sample_site(row):
    return "Lung"


def primary_site(row):
    value = row["hnsc site of origin"]
    mapping = {
        "Not applicable": "Lung",
    }
    return mapping[value]


def sample_type(row):
    title = row["Title"]
    if "lung" in title:
        return "primary"
    return "metastasis"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]


def age(row):
    return row["age"]
