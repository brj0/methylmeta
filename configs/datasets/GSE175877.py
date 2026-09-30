def dataset_id(row):
    return "GSE175877"


def description(row):
    return (
        "DNA methylation profiling of adult IDH-mutant diffuse "
        "lower-grade gliomas"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue brain tumor"]


def methylation_class(row):
    return "LGG"


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
