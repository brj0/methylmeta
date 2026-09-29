def dataset_id(row):
    return "GSE261635"


def description(row):
    return (
        "Epigenome analysis of early gastric cancer with and without "
        "lymphovascular invasion"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease state"]
    mapping = {
        "ECG,LVI(+)": "early gastric cancer with lymphovascular invasion",
        "ECG,LVI(-)": "early gastric cancer without lymphovascular invasion",
    }
    return mapping[value]


def methylation_class(row):
    return "GAST_CA"


def sample_site(row):
    return "Stomach"


def primary_site(row):
    return "Stomach"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
