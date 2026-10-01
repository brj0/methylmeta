def dataset_id(row):
    return "GSE262765"


def description(row):
    return (
        "Methylomes of serous ovarian tumors of diverse aggressiveness, "
        "Szafron et al. 2024"
    )


def _diagnosis(row):
    return row["Description"].split("\n")[0].strip()


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return _diagnosis(row)


def methylation_class(row):
    mapping = {
        "high-grade serous ovarian carcinoma": "OVA_HGSC",
        "low-grade serous ovarian carcinoma": "OVA_LGSC",
        "serous borderline ovarian tumor with the BRAF V600E mutation": (
            "OVA_SER_BOT"
        ),
        "serous borderline ovarian tumor without the BRAF V600E mutation": (
            "OVA_SER_BOT"
        ),
    }
    return mapping[_diagnosis(row)]


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["Source"]]


def tumor_grade(row):
    mapping = {
        "high-grade serous ovarian carcinoma": "high-grade",
        "low-grade serous ovarian carcinoma": "low-grade",
    }
    return mapping.get(_diagnosis(row))


def sex(row):
    return "female"
