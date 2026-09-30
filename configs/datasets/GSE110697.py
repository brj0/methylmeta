def dataset_id(row):
    return "GSE110697"


def description(row):
    return (
        "Wilms tumor patient-derived xenografts and corresponding primary "
        "tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "WILMS"


def sample_type(row):
    # primary tumors and their patient-derived xenografts
    return "primary"


def primary_site(row):
    return "Kidney"


def sample_site(row):
    value = row["Source"]
    mapping = {
        # resected primary Wilms tumor
        "Tumor resection": "Kidney",
        # heterotopic xenograft, site of growth not reported
        "Xenograft": None,
    }
    return mapping[value]


def material_type(row):
    return "tissue"
