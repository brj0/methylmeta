def dataset_id(row):
    return "GSE161944"


def description(row):
    return (
        "DNA methylation profiling of diffuse midline glioma, H3 K27M "
        "mutant, with and without FGFR1/BRAF hotspot mutations"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumor entity"]


def methylation_class(row):
    mapping = {"DMG_K27M": "DMG_K27"}
    return mapping[row["methylation_class (heidelberg classifiier)"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def age(row):
    return float(row["age (years)"])
