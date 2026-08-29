def dataset_id(row):
    return "GSE214948"


def description(row):
    return "Merkel Cell Carcinomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["cell line"]


def methylation_class(row):
    value = row["cell line"]
    mapping = {
        "Merkel cell carcinoma tissue": "MCC",
    }
    return mapping[value]


def sample_site(row):
    return row["Source"]


def sex(row):
    translate = {"M": "male", "F": "female"}
    try:
        # Expect format: gender_<M/F>_age_<number>_years_<type>_...
        return translate[row["sample type"].split("_")[1]]
    except Exception:
        return None


def age(row):
    try:
        # Expect format: gender_<M/F>_age_<number>_years_<type>_...
        return int(row["sample type"].split("_")[3])
    except Exception:
        return None
