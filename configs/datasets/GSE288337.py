def dataset_id(row):
    return "GSE288337"


def description(row):
    return (
        "Central neurocytoma DNA methylation profiling (primary and "
        "recurrent intraventricular brain tumors)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "central neurocytoma"


def methylation_class(row):
    return "CNEUROCYT"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    value = row["tumor_stage"]
    mapping = {
        "primary_tumor": "primary",
        "first_recurrence": "recurrence",
        "second_recurrence": "recurrence",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
