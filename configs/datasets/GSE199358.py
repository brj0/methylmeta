def dataset_id(row):
    return "GSE199358"


def description(row):
    return "Progressive hypothalamic/optic pathway pilocytic astrocytoma (850K array)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "LGG_PA_MID"


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return row["tumor grade"]


def sex(row):
    return row["Sex"]


def age(row):
    value = row["age (yr)"]
    if value is None:
        return None
    return float(value)
