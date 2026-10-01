def dataset_id(row):
    return "GSE212838"


def description(row):
    return "Diffuse gliomas stratified by IDH and 1p/19q status"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["who diagnosis"]


def methylation_class(row):
    mapping = {
        "Astrocytoma, IDH-mutant grade 3": "ASTRO_IDH",
        "Astrocytoma, IDH-mutant grade 4": "ASTRO_IDH_HG",
        "Oligodendroglioma, IDH-mutant and 1p19q-codeleted grade 3": "OLIGO_IDH",
    }
    return mapping[row["who diagnosis"]]


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
    mapping = {
        "Astrocytoma, IDH-mutant grade 3": "G3",
        "Astrocytoma, IDH-mutant grade 4": "G4",
        "Oligodendroglioma, IDH-mutant and 1p19q-codeleted grade 3": "G3",
    }
    return mapping[row["who diagnosis"]]


def sex(row):
    mapping = {"f": "female", "m": "male"}
    return mapping[row["gender"]]
