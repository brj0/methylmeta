def dataset_id(row):
    return "GSE295570"


def description(row):
    return (
        "Lung adenocarcinoma (LUAD) multicentre hospital cohorts "
        "profiled on the Infinium MethylationEPIC BeadChip"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "LU_ADCA"


def sample_site(row):
    return "lung"


def primary_site(row):
    return "lung"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age at diagnosis"])
