def dataset_id(row):
    return "GSE135017"


def description(row):
    return "Epigenome analysis of pediatric low-grade glioma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "pediatric low-grade glioma": "LGG",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return "low-grade"
