def dataset_id(row):
    return "GSE49031"


def description(row):
    return "Pediatric ALL"


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    import pandas as pd

    values = [
        row["disease state"],
        row["immunophenotype"],
        row["subtype"],
    ]
    return " / ".join(str(x) for x in values if pd.notna(x) and str(x).strip())


def methylation_class(row):
    value = row["disease state"]

    if "normal CD3+ cells" in value:
        return "CONTR_BLOOD"
    if "normal CD19+ cells" in value:
        return "CONTR_BLOOD"
    if "pooled normal CD34+ cells" in value:
        return "CONTR_BLOOD"
    if value == "normal peripheral blood":
        return "CONTR_BLOOD"
    if value == "normal bone marrow":
        return "CMARROW"
    return None


def sample_site(row):
    return row["Source"]
