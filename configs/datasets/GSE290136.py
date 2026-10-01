def dataset_id(row):
    return "GSE290136"


def description(row):
    return "Methylation profiling of BRAF-altered pediatric low-grade gliomas"


def sample_id(row):
    return row["Sample_ID"]


def methylation_class(row):
    mapping = {
        "CONTR, CEBM": "CTRL_CEBM",
        "CONTR, INFLAM": "CTRL_INFLAM",
        "CONTR, REACT": "CTRL_REACT",
        "CPH, PAP": "CPH_PAP",
        "GBM, MID": "GBM_MID",
        "IHG": "IHG",
        "LGG, DIG/DIA": "LGG_DIG_DIA",
        "LGG, DNT": "LGG_DNT",
        "LGG, GG": "LGG_GG",
        "LGG, PA MID": "LGG_PA_MID",
        "LGG, PA PF": "LGG_PA_PF",
        "LGG, PA/GG ST": "LGG_PA_GG_ST",
        "MNG": "MNG",
        "PXA": "PXA",
    }
    return mapping[row["dkfz classifier"]]


def diagnosis(row):
    controls = {
        "CONTR, CEBM": "Normal cerebellar hemisphere",
        "CONTR, INFLAM": "Brain tissue with inflammatory changes",
        "CONTR, REACT": "Brain tissue with reactive changes",
    }
    return controls.get(row["dkfz classifier"], row["pathology"])


def sample_site(row):
    return row["anatomic location"]


def primary_site(row):
    return "Brain"


def sample_type(row):
    controls = {
        "CONTR, CEBM": "control",
        "CONTR, INFLAM": "control",
        "CONTR, REACT": "control",
    }
    return controls.get(row["dkfz classifier"], "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {
        "Glioblastoma": "G4",
        "High grade astrocytoma": "high-grade",
        "Low grade astrocytoma": "low-grade",
        "Anaplastic ganglioglioma": "high-grade",
        "Anaplastic pleomorphic xanthoastrocytoma": "high-grade",
    }
    return mapping.get(row["pathology"])
