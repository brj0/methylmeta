def dataset_id(row):
    return "E-MTAB-11962"


def description(row):
    return "Genome-wide methylation profiling of sporadic pancreatic neuroendocrine tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pancreatic neuroendocrine tumor": "PAN_NET",
        "metastatic pancreatic neuroendocrine tumours": "PAN_NET",
    }
    return mapping[value]


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
    return "FFPE"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    return float(row["Characteristics[age]"])
