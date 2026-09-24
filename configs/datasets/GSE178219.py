def dataset_id(row):
    return "GSE178219"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "normal tonsil": "Normal tonsillar tissue",
        "tumor": "Oropharyngeal squamous cell cancer",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "normal tonsil": "CTRL_LYMPH",
        "tumor": "HNSCC",
    }
    return mapping[value]


def sample_site(row):
    return "Oropharynx"


def primary_site(row):
    return "Oropharynx"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "normal tonsil": "control",
        "tumor": "primary",
    }
    return mapping[value]


def preservation(row):
    value = row["sample type"]
    mapping = {
        "snap-frozen": "FROZEN",
        "FFPE": "FFPE",
    }
    return mapping[value]
