def dataset_id(row):
    return "GSE92580"


def description(row):
    return (
        "Validation of the Illumina MethylationEPIC BeadChip on "
        "fresh-frozen and FFPE paediatric brain tumour samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return None


def sample_site(row):
    return "brain"


def primary_site(row):
    return "brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    title = row["Title"]
    if "FFPE" in title:
        return "FFPE"
    return "FROZEN"
