def dataset_id(row):
    return "GSE143843"


def description(row):
    return (
        "Methylome analyses of three glioblastoma cohorts reveal "
        "chemotherapy sensitivity markers within DDR genes"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Glioblastoma, IDH-wildtype"


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


def tumor_grade(row):
    return "G4"


def sex(row):
    return row["gender"]
