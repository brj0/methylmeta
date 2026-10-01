def dataset_id(row):
    return "GSE37362"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of TET2 mutant and wild type "
        "diffuse large B-cell lymphoma biopsies"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return "diffuse large B-cell lymphoma"


def methylation_class(row):
    return "DLBCL"


def sample_site(row):
    return "Lymphoid tissue"


def primary_site(row):
    return "Lymphoid tissue"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
