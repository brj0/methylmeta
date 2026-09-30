def dataset_id(row):
    return "GSE146426"


def description(row):
    return (
        "Metabolic regulation of the epigenome drives lethal infantile "
        "ependymoma (Michealraj et al., 2020)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumour type"]


def methylation_class(row):
    return "EPN_PF"


def sample_site(row):
    return "Posterior fossa"


def primary_site(row):
    return "Posterior fossa"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "tumour sample": "tissue",
        "tumour-derived line": "cell_line",
    }
    return mapping[row["sample type"]]


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value == "Unknown":
        return None
    number, unit = value.split(" ")
    if unit.startswith("month"):
        return float(number) / 12
    return float(number)
