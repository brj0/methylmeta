def dataset_id(row):
    return "GSE39279"


def description(row):
    return (
        "CURELUNG Project: primary NSCLC methylation profiling (Sandoval et "
        "al., 2013)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["source_name_ch1"]


def methylation_class(row):
    mapping = {
        "adenocarcinoma": "LU_ADCA",
        "squamous cell carcinoma": "LU_SCC",
    }
    return mapping[row["nsclc type"]]


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return row["gender"]


def age(row):
    try:
        return float(row["age"])
    except (TypeError, ValueError):
        return None
