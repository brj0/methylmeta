def dataset_id(row):
    return "GSE246036"


def description(row):
    return (
        "Extracranial malignant rhabdoid tumors: clinical and molecular "
        "risk factors towards an integrated model of high-risk tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "MRT"


def sample_type(row):
    # Description is "tumor sample <n>" (primary) or "tumor RR <n>" (relapse)
    mapping = {"sample": "primary", "RR": "recurrence"}
    return mapping[row["Description"].split()[1]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
