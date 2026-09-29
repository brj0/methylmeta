def dataset_id(row):
    return "GSE296589"


def description(row):
    return (
        "Myometrial DNA methylome of fibroid-free, fibroid and "
        "testosterone-treated patients"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Normal myometrium"


def methylation_class(row):
    return "CTRL_MYOMETR"


def sample_site(row):
    return "Uterus"


def primary_site(row):
    return "Uterus"


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def age(row):
    value = row["age"]
    if value == "Not Available":
        return None
    return float(value)
