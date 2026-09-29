def dataset_id(row):
    return "GSE267068"


def description(row):
    return (
        "Serous borderline ovarian tumors and serous ovarian carcinomas "
        "profiled with the Infinium MethylationEPIC array"
    )


def _diagnosis_text(row):
    parts = row["Description"].replace("\\n", "\n").split("\n")
    parts = [part.strip() for part in parts if part.strip()]
    return parts[-1] if parts else None


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return _diagnosis_text(row)


def methylation_class(row):
    mapping = {
        "high-grade serous ovarian carcinoma": "OVA_HGSC",
        "low-grade serous ovarian carcinoma": "OVA_LGSC",
        "serous borderline ovarian tumor with the BRAF V600E mutation": "OVA_SER_BOT",
        "serous borderline ovarian tumor without the BRAF V600E mutation": "OVA_SER_BOT",
    }
    return mapping[_diagnosis_text(row)]


def sample_type(row):
    return "primary"


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["Source"]]


def tumor_grade(row):
    value = _diagnosis_text(row)
    if value is None:
        return None
    if "high-grade" in value:
        return "high-grade"
    if "low-grade" in value:
        return "low-grade"
    return None


def sex(row):
    return row["gender"].lower()
