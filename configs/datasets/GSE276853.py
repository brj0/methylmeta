def dataset_id(row):
    return "GSE276853"


def description(row):
    return (
        "Germinal center-derived B-cell lymphomas (FL, DLBCL, FL-DLBCL) "
        "from the ICGC MMML-Seq cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "DLBCL, cryo-preserved": "Diffuse large B-cell lymphoma",
        "FL, cryo-preserved": "Follicular lymphoma",
        "FL-DLBCL, cryo-preserved": (
            "Follicular lymphoma with diffuse large B-cell lymphoma"
        ),
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "DLBCL, cryo-preserved": "DLBCL",
        "FL, cryo-preserved": "FL",
        "FL-DLBCL, cryo-preserved": "DLBCL",
    }
    return mapping[value]


def sample_site(row):
    return row["Source"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
