def dataset_id(row):
    return "GSE223546"


def description(row):
    return (
        "Pediatric-type high-grade neuroepithelial tumors with CIC gene "
        "fusion share a common DNA methylation signature"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "HGNET_NOS"


def sample_site(row):
    return "Central nervous system"


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["tissue preparation"]
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return mapping[value]


def tumor_grade(row):
    return "high-grade"
