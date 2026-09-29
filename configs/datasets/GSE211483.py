def dataset_id(row):
    return "GSE211483"


def description(row):
    return (
        "Integrated miRNA, DNA methylation and RNA expression profiling of "
        "gastroenteropancreatic and lung neuroendocrine neoplasms"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    organ = {
        "lung": "lung",
        "pancreas": "pancreas",
        "stomach": "stomach",
        "small intestine": "small intestine",
        "apendix": "appendix",
    }[row["primary.tumor"]]
    if row["tissue.type"] == "normal":
        return "Normal " + organ + " tissue"
    histology = {
        "NET": "neuroendocrine tumour",
        "NEC": "neuroendocrine carcinoma",
    }[row["Source"].split(".")[-2]]
    return histology + " of the " + organ


def methylation_class(row):
    organ = {
        "lung": "lung",
        "pancreas": "pancreas",
        "stomach": "stomach",
        "small intestine": "small intestine",
        "apendix": "appendix",
    }[row["primary.tumor"]]
    if row["tissue.type"] == "normal":
        return {
            "lung": "CTRL_LU",
            "pancreas": "CTRL_PAN",
            "stomach": "CTRL_GAST",
            "small intestine": "CTRL_SI",
            "appendix": "CTRL_APP",
        }[organ]
    histology = row["Source"].split(".")[-2]
    return {
        ("lung", "NET"): "LU_NET",
        ("lung", "NEC"): "LU_NEC",
        ("pancreas", "NET"): "PAN_NET",
        ("stomach", "NET"): "GAST_NET",
        ("small intestine", "NET"): "SI_NET",
        ("appendix", "NET"): "APP_NET",
    }.get((organ, histology))


def sample_site(row):
    return {
        "lung": "lung",
        "pancreas": "pancreas",
        "stomach": "stomach",
        "small intestine": "small intestine",
        "apendix": "appendix",
    }[row["primary.tumor"]]


def primary_site(row):
    return {
        "lung": "lung",
        "pancreas": "pancreas",
        "stomach": "stomach",
        "small intestine": "small intestine",
        "apendix": "appendix",
    }[row["primary.tumor"]]


def sample_type(row):
    return {"normal": "control", "tumor": "primary"}[row["tissue.type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return {"normal": None, "tumor": row["grade"]}[row["tissue.type"]]


def sex(row):
    return {"Female": "female", "Male": "male"}[row["gender"]]
