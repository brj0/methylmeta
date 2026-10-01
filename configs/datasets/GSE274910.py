def dataset_id(row):
    return "GSE274910"


def description(row):
    return "DNA methylation profiles in FFPE brain tumor samples"


def sample_id(row):
    filename = row["Supplementary-Data"].rsplit("/", 1)[-1]
    return filename.split("_Grn.idat")[0]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    value = row["Description"].split(", grade")[0]
    mapping = {
        "Astrocytoma, IDH-mutant": "ASTRO_IDH",
        "Ganglioglioma": "LGG_GG",
        "Glioblastoma, IDH wildtype": "GBM_NOS",
        "Oligodendroglioma, IDH-mutant and 1p/19q-codeleted": "OLIGO_IDH",
        "Pilocytic astrocytoma": "LGG",
        "Supratentorial ependymoma, NOS": "EPN",
    }
    return mapping[value]


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
        "Astrocytoma, IDH-mutant, grade 2": "G2",
        "Astrocytoma, IDH-mutant, grade 3": "G3",
        "Oligodendroglioma, IDH-mutant and 1p/19q-codeleted, grade 2": "G2",
        "Oligodendroglioma, IDH-mutant and 1p/19q-codeleted, grade 3": "G3",
    }
    return mapping.get(row["Description"])
