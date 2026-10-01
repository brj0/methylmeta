def dataset_id(row):
    return "GSE305349"


def description(row):
    return (
        "Matched primary-recurrent IDH-wildtype glioblastoma samples "
        "from the GSAM study (GSE305349)"
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
    value = row["tumor_status"]
    mapping = {
        "primary": "primary",
        "recurrence": "recurrence",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return "G4"


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
