def dataset_id(row):
    return "E-MTAB-13975"


def description(row):
    return (
        "IDH- and H3-wildtype high-grade glioma subgroups in teenage and "
        "young adult patients"
    )


def sample_id(row):
    value = row["Array Data File"]
    for suffix in ("_Grn.idat", "_Red.idat"):
        if value.endswith(suffix):
            return value[: -len(suffix)]
    return value


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
