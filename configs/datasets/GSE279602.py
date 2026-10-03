def dataset_id(row):
    return "GSE279602"


def description(row):
    return (
        "DNA methylome of B-cell prolymphocytic leukemia (B-PLL) cases "
        "reveals two clinico-biological epitypes (2025)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "B-cell prolymphocytic leukemia"


def methylation_class(row):
    return "B_PLL"


def sample_site(row):
    return "Peripheral blood"


def primary_site(row):
    return "Blood"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"
