def dataset_id(row):
    return "GSE289988"


def description(row):
    return (
        "Comparative DNA methylation profiling of human ALK-positive "
        "B-cell neoplasms (ALK-positive ALCL and ALK-positive LBCL, "
        "including a patient-derived xenograft)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "ALK-positive anaplastic large lymphoma": "ALCL_ALK_POS",
        "ALK-positive large B-cell lymphoma, after treatment with "
        "Crizotinib": "LBCL_ALK",
        "PDX model of a ALK-positive large B-cell lymphoma, after "
        "treatment with Crizotinib": "LBCL_ALK",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
