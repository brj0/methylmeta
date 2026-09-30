def dataset_id(row):
    return "GSE114210"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of IG-MYC-positive "
        "precursor B-cell neoplasms and Burkitt lymphomas"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    # The study contrasts IG-MYC-positive neoplasms with precursor B-cell
    # phenotype against Burkitt lymphomas; EBV status is not recorded, so the
    # broader Burkitt class is used.
    mapping = {
        "Burkitt lymphoma": "BURK",
        "preBL": "B_ALL_IGHMYC",
    }
    return mapping[row["disease state"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "Cryo-preserved tumor": "FROZEN",
        "FFPE tumor": "FFPE",
    }
    return mapping[row["Source"]]


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]
