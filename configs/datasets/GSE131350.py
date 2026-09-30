def dataset_id(row):
    return "GSE131350"


def description(row):
    return (
        "Pediatric adrenocortical tumors, International Pediatric"
        " Adrenocortical Tumor Registry (IPACTR)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "Adrenocortial tumor": "Adrenocortical tumor",
        "Tissue Control": "Normal adrenal gland",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "Adrenocortial tumor": "ADREN_CORT_CA",
        "Tissue Control": "CTRL_ADREN",
    }
    return mapping[value]


def sample_site(row):
    return "Adrenal gland"


def primary_site(row):
    return "Adrenal gland"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "Adrenocortial tumor": "primary",
        "Tissue Control": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
