def dataset_id(row):
    return "GSE157397"


def description(row):
    return (
        "Germline-driven replication repair-deficient high-grade gliomas "
        "exhibit unique hypomethylation patterns"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    # Histology labels are cohort abbreviations; expand them for readability.
    mapping = {
        "AA": "Anaplastic astrocytoma",
        "AO": "Anaplastic oligodendroglioma",
        "Anaplastic PXA": "Anaplastic pleomorphic xanthoastrocytoma",
        "GBM": "Glioblastoma",
        "GBM/MB": "Glioblastoma / medulloblastoma",
        "HGG": "High-grade glioma",
        "PNET/GBM": "Primitive neuroectodermal tumour / glioblastoma",
        "PXA": "Pleomorphic xanthoastrocytoma",
    }
    value = row["histology"]
    return mapping.get(value, value)


def methylation_class(row):
    # Only the histological diagnosis is available per sample, so the
    # broadest matching CNS methylation class is used.
    mapping = {
        "AA": "ASTRO_IDH_HG",
        "AO": "OLIGO_IDH_ANA",
        "Anaplastic PXA": "PXA",
        "GBM": "GBM_NOS",
        "GBM/MB": "GBM_NOS",
        "HGG": "GBM_NOS",
        "PNET/GBM": "GBM_NOS",
        "PXA": "PXA",
    }
    return mapping[row["histology"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    mapping = {"P": "primary", "R": "recurrence"}
    return mapping[row["primary (p) or recurrent (r)"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Fresh Frozen": "FROZEN"}
    return mapping[row["tissue source"]]


def sex(row):
    mapping = {"F": "female", "M": "male", "U": None}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age at diagnosis"])
