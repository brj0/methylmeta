def dataset_id(row):
    return "E-MTAB-11965"


def description(row):
    return (
        "Genome-wide methylation profiling of sporadic pancreatic "
        "neuroendocrine tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "pancreatic neuroendocrine tumor": "PAN_NET",
        "metastatic pancreatic neuroendocrine tumours": "PAN_NET",
    }
    return mapping[row["Characteristics[disease]"]]


def sample_site(row):
    return "pancreas"


def primary_site(row):
    return "pancreas"


def sample_type(row):
    mapping = {
        "pancreatic neuroendocrine tumor": "primary",
        "metastatic pancreatic neuroendocrine tumours": "metastasis",
    }
    return mapping[row["Characteristics[disease]"]]


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Characteristics[specimen with known storage state]"]
    mapping = {
        "paraffin specimen": "FFPE",
    }
    return mapping[value]


def sex(row):
    mapping = {
        "female": "female",
        "male": "male",
        "not available": None,
    }
    return mapping[row["Characteristics[sex]"]]


def age(row):
    value = row["Characteristics[age]"]
    if value == "not available":
        return None
    return float(value)
