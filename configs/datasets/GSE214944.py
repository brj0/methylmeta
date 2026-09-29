def dataset_id(row):
    return "GSE214944"


def description(row):
    return (
        "Merkel cell carcinoma tissues and cell lines, and a pre-B-cell "
        "acute lymphoblastic leukemia cell line"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if "Merkel" in row["Title"]:
        return "Merkel cell carcinoma"
    return "B-cell acute lymphoblastic leukemia"


def methylation_class(row):
    if "Merkel" in row["Title"]:
        return "MCC"
    return "B_ALL"


def sample_site(row):
    mapping = {"cell line": None}
    return mapping.get(row["Source"], row["Source"])


def primary_site(row):
    if "Merkel" in row["Title"]:
        return "skin"
    return "bone marrow"


def sample_type(row):
    value = row["sample type"]
    if not any(char.isdigit() for char in value):
        # cell line entries carry no primary/metastasis annotation
        return None
    if value.endswith("metastasis"):
        return "metastasis"
    return "primary"


def material_type(row):
    if "cell_line" in row["Title"]:
        return "cell_line"
    return "tissue"


def sex(row):
    mapping = {
        "F": "female",
        "M": "male",
    }
    # the sex code directly follows the "gender_" prefix
    return mapping.get(row["sample type"][7])


def age(row):
    value = row["sample type"].split("_")[3]
    if not value.isdigit():
        return None
    return float(value)
