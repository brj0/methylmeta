def dataset_id(row):
    return "GSE289061"


def description(row):
    return "Ewing sarcoma cell lines profiled at early and late passages"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease"]


def methylation_class(row):
    return "EWS"


def sample_type(row):
    return "primary"


def material_type(row):
    return "cell_line"
