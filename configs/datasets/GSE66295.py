def dataset_id(row):
    return "GSE66295"


def description(row):
    return (
        "Small cell lung carcinoma cell lines, patient-derived xenografts "
        "and patient tumors (Mohammad et al. 2015)"
    )


def sample_id(row):
    value = row["Sample_ID"]
    if value:
        return value
    return row["Accession"]


def diagnosis(row):
    return "Small cell lung carcinoma"


def methylation_class(row):
    return "SCLC"


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "SCLC cell line": "cell_line",
        "SCLC patient derived xenograft": "tissue",
        "SCLC patient tumor": "tissue",
    }
    return mapping[row["Source"]]
