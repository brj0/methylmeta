def dataset_id(row):
    return "GSE328441"


def description(row):
    return (
        "Methylation profiling and alternative classification approaches in "
        "a glioma-enriched FFPE stereotaxic biopsy cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    mapping = {
        "Glioblastoma": "GBM_NOS",
        "Diffuse glioma": None,
        "Circumscribed glioma": None,
        "Embryonal tumor": "CNS_EMB_NEC",
        "Hemangioblastoma": "HMB",
        "Pineal tumor": "PINE_PPT",
        "unclassified brain lesion": None,
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["Sex"]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
