def dataset_id(row):
    return "GSE255554"


def description(row):
    return (
        "Epigenomic landscape of homologous recombination deficient "
        "triple-negative breast cancer"
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
    mapping = {
        "TRUE": "FFPE",
        "FALSE": "FFPE",
        "Not applicable (fresh frozen)": "FROZEN",
    }
    return mapping[row["macrodissected"]]


def age(row):
    return float(row["ageatdx"])
