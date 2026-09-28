def dataset_id(row):
    return "GSE202097"


def description(row):
    return "Comparative genomics of melanoma subtypes"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "MEL"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
