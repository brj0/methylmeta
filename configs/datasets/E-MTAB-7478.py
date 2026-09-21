def dataset_id(row):
    return "E-MTAB-7478"


def description(row):
    return "HNSCC"


def sample_id(row):
    suffix = len("_Grn.idat")
    return row["Sample_ID"][:-suffix]


def diagnosis(row):
    return row["Factor Value[clinical information]"]


def methylation_class(row):
    value = row["Factor Value[clinical information]"]
    mapping = {
        "HPV related HNSCC": "HNSCC_HPVA",
        "non HPV related HNSCC": "HNSCC_HPVI",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    return row["Characteristics[age]"]
