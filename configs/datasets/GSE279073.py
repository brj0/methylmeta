def dataset_id(row):
    return "GSE279073"


def description(row):
    return (
        "Longitudinal DNA methylation profiling of IDH-wildtype glioblastoma "
        "initial and recurrent surgical specimens (UCSF, 2024)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "IDH-wildtype glioblastoma"


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    value = row["tumor category"]
    mapping = {
        "initial": "primary",
        "recurrent": "recurrence",
        "recurrent2": "recurrence",
        "recurrent3": "recurrence",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return "G4"
