def dataset_id(row):
    return "GSE171424"


def description(row):
    return "Methylation array profiling of small B-cell lymphomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    value = row["disease subtype"]
    mapping = {
        "BCL, favor MZL": "MZL",
        "CLL/SLL": "CLL",
        "EMZL": "MALT",
        "FL": "FL",
        "MCL": "MCL",
        "MZL": "MZL",
        "NMZL": "NMZL",
        "SBCL, favor CLL/SLL": "CLL",
        "SBCL, favor SLL": "CLL",
        "SMZL": "SMZL",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
