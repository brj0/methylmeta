def dataset_id(row):
    return "E-MTAB-15074"


def description(row):
    return (
        "Pediatric CNS tumors (medulloblastoma and ependymoma) profiled in a "
        "Brazilian public healthcare setting"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    site = row["Characteristics[organism part]"]
    disease = row["Characteristics[disease]"]
    mapping = {
        ("cerebellum", "desmoplastic medulloblastoma"): "MB",
        ("cerebellum", "ependymoma"): "EPN_PF",
        ("cerebellum", "medulloblastoma"): "MB",
        ("cerebellum", "medulloblastoma with extensive nodularity"): "MB",
        ("intracranial", "ependymoma"): "EPN",
        ("posterior fossa", "anaplastic ependymoma"): "EPN_PF",
        ("posterior fossa", "ependymoma"): "EPN_PF",
        ("posterior fossa", "medulloblastoma"): "MB",
    }
    return mapping[(site, disease)]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"female": "female", "male": "male"}
    return mapping[row["Characteristics[sex]"]]


def age(row):
    return float(row["Characteristics[age]"])
