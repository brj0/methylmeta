def dataset_id(row):
    return "GSE153347"


def description(row):
    return (
        "Longitudinal DNA methylation profiling of IDH1/2-mutant acute "
        "myeloid leukemia under IDH inhibitor therapy"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["timepoint"] == "Control":
        return "normal bone marrow"
    return row["patient diagnosis"]


def methylation_class(row):
    if row["timepoint"] == "Control":
        return "CTRL_MARROW"
    mapping = {
        "IDH1/IDH2 mutant": "AML_IDH",
        "wildtype": "AML",
    }
    return mapping[row["idh1/2 genotype"]]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    mapping = {
        "BL": "primary",
        "Control": "control",
        "NR": "recurrence",
        "RES": "recurrence",
    }
    return mapping[row["timepoint"]]


def material_type(row):
    return "blood"
