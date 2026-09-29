def dataset_id(row):
    return "GSE43091"


def description(row):
    return (
        "Genome-scale methylome profiling of hepatocellular adenomas and "
        "normal liver (Pilati et al., 2014)"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["pathological diagnosis"]


def methylation_class(row):
    mapping = {
        "non dysplastic hepatocellular adenoma": "HCA",
        "dysplastic hepatocellular adenoma": "HCA",
        "frontier hepatocellular adenoma/carcinoma": "HCA",
        "hepatocellular carcinoma developed on an adenoma": "HCC",
        "normal liver": "CTRL_LIV",
    }
    return mapping[row["pathological diagnosis"]]


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def sample_type(row):
    mapping = {
        "non dysplastic hepatocellular adenoma": "primary",
        "dysplastic hepatocellular adenoma": "primary",
        "frontier hepatocellular adenoma/carcinoma": "primary",
        "hepatocellular carcinoma developed on an adenoma": "primary",
        "normal liver": "control",
    }
    return mapping[row["pathological diagnosis"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "F": "female",
        "M": "male",
    }
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
