def dataset_id(row):
    return "GSE128784"


def description(row):
    return "Whole genome methylation profiling of sclerodermiform basal cell carcinoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tumor type"]
    mapping = {"sclerodermiform": "Skerodermiform basal cell carinoma"}
    return mapping[value]


def methylation_class(row):
    value = row["tumor type"]
    mapping = {"sclerodermiform": "BCC_SCLER"}
    return mapping[value]


def sample_site(row):
    return "Skin"


def primary_site(row):
    return "Skin"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Sex"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]
