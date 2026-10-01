def dataset_id(row):
    return "GSE293560"


def description(row):
    return (
        "Glioma methylation profiling correlated with germline and "
        "somatic alterations"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["first_glioma_histology"]


def methylation_class(row):
    histology = row["first_glioma_histology"]
    grade4 = {
        "Astrocytoma (Grades 2, 3, 4)": None,
        "Glioma": "GBM_NOS",
    }
    if str(row["first_glioma_grade"]) == "4" and histology in grade4:
        return grade4[histology]
    mapping = {
        "Astrocytoma (Grades 2, 3, 4)": None,
        "Glioma": None,
        "Gliosarcoma": "GBM_NOS",
        "Mixed Oligodendroglioma-Astrocytoma": None,
        "Oligodendroglioma": None,
    }
    return mapping[histology]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {"2": "G2", "3": "G3", "4": "G4"}
    return mapping.get(str(row["first_glioma_grade"]))


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
