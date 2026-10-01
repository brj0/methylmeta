def dataset_id(row):
    return "GSE297733"


def description(row):
    return "GLASS-OD primary and recurrent oligodendrogliomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    mapping = {
        "WHO grade 2": "OLIGO_IDH",
        "WHO grade 3": "OLIGO_IDH_ANA",
    }
    return mapping[row["grade"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    mapping = {
        "resection #1": "primary",
        "resection #2": "recurrence",
        "resection #3": "recurrence",
        "resection #4": "recurrence",
        "resection #5": "recurrence",
    }
    return mapping[row["resection"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {
        "WHO grade 2": "G2",
        "WHO grade 3": "G3",
    }
    return mapping[row["grade"]]


def sex(row):
    return row["Sex"]
