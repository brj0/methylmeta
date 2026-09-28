def dataset_id(row):
    return "GSE68060"


def description(row):
    return (
        "Methylome profiling of serrated adenocarcinoma of the colorectum "
        "(Spanish and Finnish cohorts)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    tissue = row["tissue"]
    if tissue == "Normal":
        return "Normal colorectal mucosa"
    if tissue == "IVD":
        return "Control tissue"
    mapping = {
        "Conventional": "Colorectal adenocarcinoma, conventional type",
        "MSI": "Colorectal carcinoma, microsatellite unstable",
        "Serrated": "Serrated adenocarcinoma of the colorectum",
    }
    return mapping[row["type"]]


def methylation_class(row):
    mapping = {
        "Tumor": "CR_CA",
        "Normal": "CTRL_COL",
        "IVD": "CTRL_COL",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Colorectum"


def primary_site(row):
    return "Colorectum"


def sample_type(row):
    mapping = {
        "Tumor": "primary",
        "Normal": "control",
        "IVD": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
