def dataset_id(row):
    return "GSE178416"


def description(row):
    return "Mucosal melanoma (cutaneous, uveal, conjunctival, normal)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["type"]
    mapping = {
        "Conjunctival melanoma": "Conjunctival Melanoma",
        "Cutaneous melanoma": "Cutaneous Melanoma",
        "Mucosal melanoma": "Mucosal Melanoma",
        "Mucosal": "Genital Melanoma",
        "Normal melanocytes": "Normal Melanocytes Cellculture",
        "Uveal melanoma": "Uveal Melanoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["type"]
    mapping = {
        "Conjunctival melanoma": "COMEL",
        "Cutaneous melanoma": "CMEL",
        "Mucosal melanoma": "MMEL",
        "Mucosal": "MMEL",
        "Normal melanocytes": "CONTR_MELANOCYTE",
        "Uveal melanoma": "UMEL",
    }
    return mapping.get(value, value)


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
