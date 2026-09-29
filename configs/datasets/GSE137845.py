def dataset_id(row):
    return "GSE137845"


def description(row):
    return (
        "Glioma patient surgical samples with corresponding patient-derived "
        "xenografts and cell lines"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "glioma"


def methylation_class(row):
    # Only "glioma" is recorded (no grade or histology), which is not a
    # vocabulary entity, so neither GBM_NOS nor LGG is supported.
    return None


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "cell line": "cell_line",
        "patient sample": "tissue",
        "xenograft": "tissue",
    }
    return mapping[row["Source"]]


def preservation(row):
    mapping = {
        "cell line": "FRESH",
        "patient sample": "FROZEN",
        "xenograft": "FROZEN",
    }
    return mapping[row["Source"]]
