def dataset_id(row):
    return "E-MTAB-16831"


def description(row):
    return "Epigenetic profile of human ovarian CNS-type tumours and PNETs"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    # "ETMR non-C19CM" is a typo for "ETMR non-C19MC" in the raw annotation
    mapping = {"ETMR non-C19CM": "ETMR non-C19MC"}
    value = row["Characteristics[disease]"]
    return mapping.get(value, value)


def methylation_class(row):
    # CNS-type tumours arising in the female genital tract share one
    # methylation class, whatever the histology-based subtype label.
    return "GYN_CNS_TYPE"


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return "female"


def age(row):
    value = row["Characteristics[age]"]
    return float(value) if value is not None else None
