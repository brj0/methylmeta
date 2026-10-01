def dataset_id(row):
    return "GSE285849"


def description(row):
    return (
        "Methylation profiling of disseminated pediatric low-grade glioma, "
        "97 FFPE surgical specimens"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "pediatric low-grade glioma"


def methylation_class(row):
    return "LGG"


def primary_site(row):
    return "Brain"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
