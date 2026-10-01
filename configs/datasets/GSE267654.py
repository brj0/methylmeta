def dataset_id(row):
    return "GSE267654"


def description(row):
    return (
        "Primary and multiply recurrent meningiomas profiled by methylation "
        "profiling (dual institution cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "meningioma"


def methylation_class(row):
    return "MNG"


def sample_type(row):
    mapping = {
        "Primary": "primary",
        "Recurrence1": "recurrence",
        "Recurrence2": "recurrence",
    }
    return mapping[row["primary/recurrence"]]


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
