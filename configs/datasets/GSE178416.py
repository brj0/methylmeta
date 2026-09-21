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
        "Conjunctival melanoma": "MEL_CONJ",
        "Cutaneous melanoma": "MEL_SKIN",
        "Mucosal melanoma": "MEL_MUC",
        "Mucosal": "MEL_MUC",
        "Normal melanocytes": "CTRL_MELCYT",
        "Uveal melanoma": "MEL_UVE",
    }
    return mapping.get(value, value)


def material_type(row):
    value = row["exact anatomic site"]
    if value == "Melanocytes":
        return "cell_line"
    return "tissue"


def sample_site(row):
    value = row["exact anatomic site"]
    mapping = {
        "Melanocytes": "Cultured Melanocytes",
        "Mouth": "Oral Cavity",
        "Nasal": "Nasal Cavity",
        "Sinus": "Sinonasal",
        "Skin": "Skin",
        "Uvea": "Uvea",
    }
    return mapping.get(value, value)


def primary_site(row):
    value = row["exact anatomic site"]
    mapping = {
        "Melanocytes": "Cultured Melanocytes",
        "Mouth": "Oral Cavity",
        "Nasal": "Nasal Cavity",
        "Sinus": "Sinonasal",
        "Skin": "Skin",
        "Uvea": "Uvea",
    }
    return mapping.get(value, value)


def preservation(row):
    return "FFPE"
