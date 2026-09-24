def dataset_id(row):
    return "E-MTAB-7854"


def description(row):
    return (
        "DNA methylation changes in advanced sessile serrated adenomas "
        "preceding progression to dysplasia"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "sessile serrated adenoma": "SSL",
        "dysplastic sessile serrated adenoma": "SSL_DYS",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"]
    mapping = {
        "female": "female",
        "male": "male",
        "not available": None,
    }
    return mapping.get(value)


def age(row):
    return float(row["Characteristics[age]"])
