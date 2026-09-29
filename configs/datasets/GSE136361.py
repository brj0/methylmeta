def dataset_id(row):
    return "GSE136361"


def description(row):
    return "Isomorphic diffuse glioma, MYB/MYBL1-altered (Wefers et al., 2020)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Isomorphic diffuse glioma"


def methylation_class(row):
    return "LGG_MYB"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
