def dataset_id(row):
    return "GSE248618"


def description(row):
    return (
        "Intratumoral heterogeneity in posterior fossa type A (PF-EPN-A) "
        "ependymoma: DNA methylation profiles of high and low cell density "
        "tumor areas and routine diagnostics"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Posterior fossa ependymoma type A (PF-EPN-A)"


def methylation_class(row):
    return "EPN_PF_A"


def sample_site(row):
    return "Posterior fossa"


def primary_site(row):
    return "Posterior fossa"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
