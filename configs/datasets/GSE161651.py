def dataset_id(row):
    return "GSE161651"


def description(row):
    return (
        "Upper-tract urothelial carcinomas and normal adjacent tissue "
        "profiled on Illumina EPIC arrays"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "cancer": "Upper-tract urothelial carcinoma",
        "normal": "Normal adjacent upper-tract urothelium",
    }
    return mapping[row["disease state"]]


def methylation_class(row):
    mapping = {
        "cancer": "URO_CA",
        "normal": "CTRL_URO",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    return "Upper urinary tract"


def primary_site(row):
    return "Upper urinary tract"


def sample_type(row):
    mapping = {
        "cancer": "primary",
        "normal": "control",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "F": "female",
        "M": "male",
    }
    return mapping[row["gender"]]
