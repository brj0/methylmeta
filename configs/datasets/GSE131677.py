def dataset_id(row):
    return "GSE131677"


def description(row):
    return (
        "Epigenome analysis of relapse and relapse-free T-cell "
        "lymphoblastic lymphoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "T_ALL_NOS"


def sample_type(row):
    value = row["disease state"]
    mapping = {
        "Relapse T-LBL": "recurrence",
        "Relapse-free T-LBL": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"
