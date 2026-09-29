def _is_normal(row):
    return "normal" in row["Title"].lower()


def dataset_id(row):
    return "GSE291073"


def description(row):
    return (
        "FH-deficient renal cell carcinoma, primary tumors and adjacent "
        "normal kidney tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _is_normal(row):
        return "Normal kidney tissue"
    return "Fumarate hydratase-deficient renal cell carcinoma"


def methylation_class(row):
    if _is_normal(row):
        return "CTRL_REN"
    return "RCC_FH"


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    if _is_normal(row):
        return "control"
    return "primary"


def material_type(row):
    return "tissue"
