def dataset_id(row):
    return "GSE192353"


def description(row):
    return (
        "DNA methylation of uterine leiomyoma and adjacent myometrium (2022)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "Uterine leiomyoma": "Uterine leiomyoma",
        "Uterine myometrium": "Normal myometrium",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Uterine leiomyoma": "UT_LEIO",
        "Uterine myometrium": "CTRL_MYOMETR",
    }
    return mapping[value]


def sample_type(row):
    value = row["Source"]
    mapping = {
        "Uterine leiomyoma": "primary",
        "Uterine myometrium": "control",
    }
    return mapping[value]


def sample_site(row):
    return "Uterus"


def primary_site(row):
    return "Uterus"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return "female"


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
