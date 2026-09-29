def dataset_id(row):
    return "GSE122920"


def description(row):
    return (
        "Illumina 450k/EPIC methylation profiling of malignant astrocytomas "
        "from elderly NOA-08 trial patients"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["who grade"]


def methylation_class(row):
    mapping = {
        "glioblastoma": "GBM_NOS",
        "anaplastic astrocytoma": "ASTRO_IDH_HG",
    }
    return mapping[row["who grade"]]


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
