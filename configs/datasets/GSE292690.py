def dataset_id(row):
    return "GSE292690"


def description(row):
    return (
        "DNA methylation epitypes of Burkitt lymphoma with distinct "
        "molecular and clinical features"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    if value == "Cell line":
        return "Burkitt lymphoma cell line " + row["cell line"]
    mapping = {
        "Burkitt lymphoma biopsy": "Burkitt lymphoma",
        "Normal centroblasts": "Normal centroblasts",
    }
    return mapping[value]


def methylation_class(row):
    mapping = {
        "Tumour": "BURK",
        "Cell line": "BURK",
        "Normal centroblasts": "CTRL_LYMPH",
    }
    return mapping[row["Source"]]


def sample_type(row):
    mapping = {
        "Tumour": "primary",
        "Cell line": None,
        "Normal centroblasts": "control",
    }
    return mapping[row["Source"]]


def material_type(row):
    mapping = {
        "Tumour": "tissue",
        "Cell line": "cell_line",
        "Normal centroblasts": "tissue",
    }
    return mapping[row["Source"]]
