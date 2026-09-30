def dataset_id(row):
    return "E-MTAB-6708"


def description(row):
    return "Methylation profiling of malignant rhabdoid tumours"


def sample_id(row):
    suffixes = ("_Grn.idat.gz", "_Red.idat.gz", "_Grn.idat", "_Red.idat")
    name = row["Array Data File"].strip()
    for suffix in suffixes:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def diagnosis(row):
    return row["Characteristics[phenotype]"]


def methylation_class(row):
    phenotype = row["Characteristics[phenotype]"]
    if phenotype == "atypical teratoid rhabdoid tumor":
        return "ATRT"
    site = row["Characteristics[organism part]"]
    mapping = {
        "kidney": "REN_MRT",
        "not available": "MRT",
    }
    return mapping.get(site, "ERT")


def sample_site(row):
    mapping = {"not available": None}
    value = row["Characteristics[organism part]"]
    return mapping.get(value, value)


def primary_site(row):
    mapping = {"not available": None}
    value = row["Characteristics[organism part]"]
    return mapping.get(value, value)


def sample_type(row):
    mapping = {"neoplasm": "primary"}
    return mapping[row["Characteristics[sampling site]"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "frozen specimen": "FROZEN",
        "paraffin specimen": "FFPE",
    }
    return mapping[row["Characteristics[specimen with known storage state]"]]


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    value = row["Characteristics[age]"].strip()
    if not value or value.lower() == "not available":
        return None
    return float(value)
