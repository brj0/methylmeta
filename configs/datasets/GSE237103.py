def dataset_id(row):
    return "GSE237103"


def description(row):
    return (
        "DNA methylation and NGS profiling of progressive glioblastoma, "
        "EORTC-26101 trial"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Diffuse glioma, IDH-wildtype"


def methylation_class(row):
    return "GBM_NOS"


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
    return row["gender"]
