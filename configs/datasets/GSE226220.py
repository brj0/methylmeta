def dataset_id(row):
    return "GSE226220"


def description(row):
    return (
        "Pediatric CNS embryonal tumor with rhabdoid features and a "
        "ZNF532-NUTM1 fusion, methylation profiling of a single case"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "CNS_EMB_NEC"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
