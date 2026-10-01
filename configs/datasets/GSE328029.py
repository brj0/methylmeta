def dataset_id(row):
    return "GSE328029"


def description(row):
    return (
        "DNA methylation profiling of perivascular epithelioid cell "
        "neoplasms (PEComa)"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return "Perivascular epithelioid cell tumor (PEComa)"


def methylation_class(row):
    return "PEC"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
