def dataset_id(row):
    return "GSE204943"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    value = row["sample_group"]
    mapping = {
        "1_Tumor": "HNSCC",
        "2_OPL": "OML",
        "3_Normal": "CTRL_HN",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def sex(row):
    return row["Sex"]
