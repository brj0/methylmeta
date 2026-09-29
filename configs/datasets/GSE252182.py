def dataset_id(row):
    return "GSE252182"


def description(row):
    return (
        "Genome-wide DNA methylation profiles of well-differentiated and "
        "dedifferentiated liposarcomas and normal adipose tissues"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "dedifferentiated liposarcomas": "dedifferentiated liposarcoma",
        "well-differentiated liposarcomas": "well-differentiated liposarcoma",
        "normal adipose tissues": "normal adipose tissue",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "dedifferentiated liposarcomas": "LPS_DD",
        "well-differentiated liposarcomas": "LPS_WD",
        "normal adipose tissues": "CTRL_ADIPOSE",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    mapping = {
        "dedifferentiated liposarcomas": "primary",
        "well-differentiated liposarcomas": "primary",
        "normal adipose tissues": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def primary_site(row):
    return "Soft tissue"
