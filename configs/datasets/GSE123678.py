def dataset_id(row):
    return "GSE123678"


def description(row):
    return (
        "HM450K DNA methylation profiling of normal brain and glioma samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["disease"] == "healthy control":
        return "normal brain tissue"
    grade_labels = {
        "GBM": "glioblastoma",
        "Grade II": "grade II glioma",
        "Grade IIII": "grade III glioma",
    }
    idh_labels = {
        "IDHmut": "IDH-mutant",
        "IDHwt": "IDH-wildtype",
    }
    grade = grade_labels[row["gliomas classification"].split(": ")[1]]
    idh = idh_labels[row["gliomas classification_1"].split(": ")[1]]
    return f"{grade} ({idh})"


def methylation_class(row):
    mapping = {
        ("grade: GBM", "IDH statut: IDHwt"): "GBM_NOS",
        ("grade: Grade IIII", "IDH statut: IDHwt"): "GBM_NOS",
        ("grade: Grade II", "IDH statut: IDHmut"): "LGG",
        ("grade: Grade IIII", "IDH statut: IDHmut"): "LGG",
        ("grade: not applicable", "IDH statut: not applicable"): "CTRL_BRAIN",
    }
    key = (row["gliomas classification"], row["gliomas classification_1"])
    return mapping[key]


def sample_site(row):
    value = row["Source"]
    mapping = {
        "DNA from  frontal cortex": "Frontal cortex",
        "DNA from corpus callosum": "Corpus callosum",
        "DNA from Glioma sample": "Brain",
    }
    return mapping[value]


def primary_site(row):
    return "Brain"


def sample_type(row):
    value = row["disease"]
    mapping = {
        "glioma sample": "primary",
        "healthy control": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    value = row["gliomas classification"]
    mapping = {
        "grade: GBM": "G4",
        "grade: Grade IIII": "G3",
        "grade: Grade II": "G2",
        "grade: not applicable": None,
    }
    return mapping[value]


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]
