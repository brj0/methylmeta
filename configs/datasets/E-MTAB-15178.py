def dataset_id(row):
    return "E-MTAB-15178"


def description(row):
    return "Paraganglioma and Phaechromocytoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def sex(row):
    return row["Characteristics[sex]"]


def sample_site(row):
    return row["Characteristics[organism part]"]


def age(row):
    value = row["Characteristics[age]"]
    return None if value == "unknown" else value


def tumor_grade(row):
    value = row["Factor Value[disease staging]"]
    mapping = {
        "benign": None,
        "metastasis": None,
        "not available": None,
    }
    return mapping[value]


def methylation_class(row):
    return "PGL"
