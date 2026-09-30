def dataset_id(row):
    return "E-MTAB-14789"


def description(row):
    return (
        "Illumina Infinium HumanMethylation EPIC profiling of "
        "supratentorial ependymomas with a TEAD1::NCOA2 fusion"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "Supratentorial ependymoma, YAP1 fusion-positive": "EPN_ST_YAP1",
    }
    return mapping[row["Characteristics[disease]"]]


def sample_site(row):
    return row["Characteristics[sampling site]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"male": "male", "female": "female"}
    return mapping.get(row["Characteristics[sex]"])


def age(row):
    value = row["Characteristics[age]"]
    return float(value) if value else None
