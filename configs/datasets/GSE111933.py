def dataset_id(row):
    return "GSE111933"


def description(row):
    return (
        "DNA methylation analysis of non-cancerous urothelium and "
        "corresponding urothelial carcinoma tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "non-cancerous urothelium obtained from patient with "
        "urothelial carcinomas": "CTRL_URO",
        "cancerous tissue obtained from patient with "
        "urothelial carcinomas": "URO_CA",
    }
    return mapping.get(value)


def sample_site(row):
    return "Urinary tract"


def primary_site(row):
    return "Urinary tract"


def sample_type(row):
    value = row["Source"]
    mapping = {
        "non-cancerous urothelium obtained from patient with "
        "urothelial carcinomas": "control",
        "cancerous tissue obtained from patient with "
        "urothelial carcinomas": "primary",
    }
    return mapping.get(value, "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
