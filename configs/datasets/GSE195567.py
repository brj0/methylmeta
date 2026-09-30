def dataset_id(row):
    return "GSE195567"


def description(row):
    return (
        "DNA methylation profiling of high-grade gliomas with pleomorphic "
        "and pseudopapillary features (HPAP)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "HGG_PPF"


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return "high-grade"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["sex predicted"]]


def age(row):
    if row["age"] is None:
        return None
    return float(row["age"])
