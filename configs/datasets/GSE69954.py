def dataset_id(row):
    return "GSE69954"


def description(row):
    return (
        "Nordic pediatric T-cell acute lymphoblastic leukemia cohort "
        "(NOPHO-ALL2008)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "T-cell acute lymphoblastic leukemia"


def methylation_class(row):
    return "T_ALL"


def sample_site(row):
    mapping = {
        "T-ALL bone marrow Sample": "bone marrow",
        "T-ALL peripheral blood Sample": "peripheral blood",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return "bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"
