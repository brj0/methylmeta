def dataset_id(row):
    return "GSE222933"


def description(row):
    return (
        "Pre- and post-treatment tumor needle biopsies from a phase II trial "
        "of guadecitabine plus atezolizumab in metastatic urothelial carcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Urothelial carcinoma"


def methylation_class(row):
    return "URO_CA"


def primary_site(row):
    return "Urinary tract"


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"
