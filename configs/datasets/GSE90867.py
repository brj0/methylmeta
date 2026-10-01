def dataset_id(row):
    return "GSE90867"


def description(row):
    return (
        "Adrenal aldosterone- and cortisol-producing adenomas, "
        "KCNJ5 mutation status"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "ADREN_CORT_AD"


def sample_site(row):
    return "Adrenal gland"


def primary_site(row):
    return "Adrenal gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
