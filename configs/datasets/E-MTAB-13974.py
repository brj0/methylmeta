def dataset_id(row):
    return "E-MTAB-13974"


def description(row):
    return (
        "IDH- and H3-wildtype high-grade glioma subgroups in teenage and "
        "young adult patients (HERBY / pHGG META cohorts)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def tumor_grade(row):
    return "high-grade"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    value = row["Characteristics[age]"]
    return None if value is None else float(value)
