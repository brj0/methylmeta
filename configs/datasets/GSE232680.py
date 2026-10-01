def dataset_id(row):
    return "GSE232680"


def description(row):
    return (
        "DNA methylation profiling of low- and high-grade pseudomyxoma "
        "peritonei and normal colon mucosa"
    )


def sample_id(row):
    return row["Source"]


def diagnosis(row):
    # "Low grade pseudomyxoma peritonei\nSAMPLE 3" or "Normal colon mucosa"
    return row["Description"].split("\n")[0]


def methylation_class(row):
    mapping = {
        "Normal": "CTRL_COL",
        "pseudomyxoma peritonei": "APP_MUC_NEO",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    mapping = {
        "Normal": "Colon",
        "pseudomyxoma peritonei": "Peritoneum",
    }
    return mapping[row["disease state"]]


def primary_site(row):
    mapping = {
        "Normal": "Colon",
        "pseudomyxoma peritonei": "Appendix",
    }
    return mapping[row["disease state"]]


def sample_type(row):
    mapping = {
        "Normal": "control",
        "pseudomyxoma peritonei": "primary",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Femal": "female",
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]
