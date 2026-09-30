def dataset_id(row):
    return "GSE102119"


def description(row):
    return (
        "Methylomic signatures of platinum re-sensitization in ovarian cancer: "
        "recurrent ovarian tumors and malignant ascites before and after "
        "guadecitabine treatment"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "human ovarian cancer tissue": "Ovarian cancer",
        "human ovarian cancer ascites fluid": "Ovarian cancer (malignant ascites)",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    return "OVA_CA"


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "recurrence"


def material_type(row):
    return "tissue"


def sex(row):
    return "female"
