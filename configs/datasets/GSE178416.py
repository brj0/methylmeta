def dataset_id(row):
    return "GSE178416"


def description(row):
    return "Mucosal melanoma (cutaneous, uveal, conjunctival, normal)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["type"]


def methylation_class(row):
    value = row["type"]
    mapping = {
        "Conjunctival melanoma": "CONJ_MEL",
        "Cutaneous melanoma": "SKIN_MEL",
        "Mucosal melanoma": "MUC_MEL",
        "Mucosal": "MUC_MEL",
        "Normal melanocytes": "CTRL_MELCYT",
        "Uveal melanoma": "UVE_MEL",
    }
    return mapping[value]


def material_type(row):
    value = row["exact anatomic site"]
    if value == "Melanocytes":
        return "cell_line"
    return "tissue"


def sample_site(row):
    return row["exact anatomic site"]


def primary_site(row):
    return row["exact anatomic site"]


def preservation(row):
    return "FFPE"
