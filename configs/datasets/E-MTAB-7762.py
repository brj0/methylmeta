def dataset_id(row):
    return "E-MTAB-7762"


def description(row):
    return "Human pituitary adenomas DNA methylation profiling"


def sample_id(row):
    # Raw values are IDAT file names, e.g. 'P031_Grn.idat'.
    value = row["Sample_ID"]
    for suffix in ("_Grn.idat", "_Red.idat"):
        if value.endswith(suffix):
            return value[: -len(suffix)]
    return value


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    # Granulation status of the STH / plurihormonal tumors is not recorded,
    # so only the NOS class can be assigned for those.
    classes = {
        "corticotroph": "PIT_AD_ACTH",
        "gonadtroph": "PIT_AD_FSH_LH",
        "mammotroph": "PIT_AD_PRL",
        "thyrotroph": "PIT_AD_TSH",
        "somatotroph": "PIT_AD",
        "Mixed_GH-PRL": "PIT_AD",
        "Null-cell": "PIT_AD",
        "Plurihormonal_PIT-1": "PIT_AD",
    }
    return classes[row["Characteristics[cell type]"]]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "pituitary gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    return float(value)
