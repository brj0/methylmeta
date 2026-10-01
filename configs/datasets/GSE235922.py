def dataset_id(row):
    return "GSE235922"


def description(row):
    return "Meningeal solitary fibrous tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "SFT"


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Source"]
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return mapping[value]
