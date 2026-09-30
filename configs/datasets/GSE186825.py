def dataset_id(row):
    return "GSE186825"


def description(row):
    return (
        "Recurrent platinum-resistant ovarian cancer treated with "
        "guadecitabine plus pembrolizumab"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Ovarian cancer"


def methylation_class(row):
    return "OVA_CA"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    mapping = {
        "Baseline (control)": "recurrence",
        "Treated": "recurrence",
    }
    return mapping[row["sample type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
