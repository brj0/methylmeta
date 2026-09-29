def dataset_id(row):
    return "GSE214180"


def description(row):
    return (
        "Methylation profiling of dedifferentiated chondrosarcoma "
        "(DDCS) components"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["sample type"]
    mapping = {
        "Dedifferentiated component": "Dedifferentiated chondrosarcoma",
        "Well-differentiated component": "Well-differentiated chondrosarcoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["sample type"]
    mapping = {
        "Dedifferentiated component": "CSA_DD",
        "Well-differentiated component": "CSA",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return row["Source"]
