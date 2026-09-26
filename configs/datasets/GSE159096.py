def dataset_id(row):
    return "GSE159096"


def description(row):
    return "Methylation profiling of ampullary carcinoma (AMPAC) tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "AMP_ADCA"


def sample_site(row):
    return "Ampulla of Vater"


def primary_site(row):
    return "Ampulla of Vater"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
