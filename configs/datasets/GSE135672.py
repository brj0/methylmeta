def dataset_id(row):
    return "GSE135672"


def description(row):
    return "Ameloblastoma vs. Dental Follicle (normal controls)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "ameloblastoma": "Ameloblastoma",
        "Dental follicle": "Control Tissue Dental Follicle",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "ameloblastoma": "AMBL",
        "Dental follicle": "CDFOLLICLE",
    }
    return mapping[value]


def sample_site(row):
    return "Jaw / Oral"


def primary_site(row):
    return "Jaw / Oral"


def sex(row):
    return row["gender"]
