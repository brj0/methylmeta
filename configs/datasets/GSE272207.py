def dataset_id(row):
    return "GSE272207"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of gastric cancer and adjacent "
        "normal tissue (PRKCB hypermethylation biomarker study)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "adjacent normal tissue": "CTRL_GAST",
        "gastric cancer tissue": "GAST_CA",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    mapping = {
        "adjacent normal tissue": "control",
        "gastric cancer tissue": "primary",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Stomach"


def primary_site(row):
    mapping = {
        "adjacent normal tissue": None,
        "gastric cancer tissue": "Stomach",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"
