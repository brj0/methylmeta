def dataset_id(row):
    return "GSE308164"


def description(row):
    return (
        "Methylation-based cellular deconvolution of triple-negative breast "
        "cancer DNA reveals a prognostic immune signature"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Triple-negative breast cancer"


def methylation_class(row):
    return "BR_CA_TN"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]
