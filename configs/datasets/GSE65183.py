def dataset_id(row):
    return "GSE65183"


def description(row):
    return (
        "Melanoma biopsies and cell lines before and after MAPK inhibitor "
        "treatment (2015)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Melanoma"


def methylation_class(row):
    mapping = {"melanoma": "SKIN_MEL"}
    return mapping[row["cell type"]]


def sample_type(row):
    value = row["Description"]
    mapping = {"post": "recurrence", "pre": "primary"}
    for token, outcome in mapping.items():
        if token in value:
            return outcome
    return "primary"


def material_type(row):
    mapping = {"tumor biopsy": "tissue", "tumor cell line": "cell_line"}
    return mapping[row["Source"]]


def primary_site(row):
    return "Skin"
