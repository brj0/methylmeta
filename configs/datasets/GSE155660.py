def dataset_id(row):
    return "GSE155660"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of paediatric primary "
        "intracranial sarcoma (FFPE tumour tissue, Peru)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["histology"]


def methylation_class(row):
    return "CNS_SARC_DICER1"


def sample_site(row):
    return row["localization"]


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["Sex"]
    mapping = {
        "f": "female",
        "m": "male",
    }
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value.split(" ")[0])
