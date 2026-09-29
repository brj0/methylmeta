def dataset_id(row):
    return "GSE66836"


def description(row):
    return (
        "Genome-wide DNA methylation signature in lung adenocarcinomas has "
        "prognostic impact (Karlsson et al., 2015)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    mapping = {
        "lung adenocarcinoma": "LU_ADCA",
        "normal lung": "CTRL_LU",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    mapping = {
        "Normal": "control",
        "Tumor": "primary",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]
