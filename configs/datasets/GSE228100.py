def dataset_id(row):
    return "GSE228100"


def description(row):
    return (
        "Pediatric low-grade glioma cohort from the LOGGIC Core BioClinical "
        "Data Bank profiled by DNA methylation"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumor subgroup"]


def methylation_class(row):
    return "LGG"


def sample_site(row):
    return row["location"]


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
