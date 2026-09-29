def dataset_id(row):
    return "GSE267015"


def description(row):
    return "Retinoblastoma tumors and cell lines (Ryl et al., 2024)"


def sample_id(row):
    value = row["Sample_ID"]
    if value:
        return value
    return row["Title"]


def diagnosis(row):
    value = row["Description"]
    if "\n" in value:
        return value.split("\n")[0]
    if "\\n" in value:
        return value.split("\\n")[0]
    return value


def methylation_class(row):
    return "RB"


def sample_type(row):
    mapping = {
        "retinoblastoma cell line": None,
        "retinoblastoma tumor, primary": "primary",
        "retinoblastoma tumor, relapse": "recurrence",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Eye"


def primary_site(row):
    return "Eye"


def material_type(row):
    mapping = {
        "retinoblastoma cell line": "cell_line",
        "retinoblastoma tumor, primary": "tissue",
        "retinoblastoma tumor, relapse": "tissue",
    }
    return mapping[row["Source"]]


def preservation(row):
    mapping = {
        "retinoblastoma cell line": None,
        "retinoblastoma tumor, primary": "FROZEN",
        "retinoblastoma tumor, relapse": "FROZEN",
    }
    return mapping[row["Source"]]
