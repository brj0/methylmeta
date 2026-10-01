def dataset_id(row):
    return "GSE279982"


def description(row):
    return (
        "DNA methylation biomarkers for cervical cancer risk prediction in "
        "HIV-positive Nigerian women, 2024"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    mapping = {
        "HIV Positive with Cervical intraepithelial neoplasia": "CIN",
        "HIV Positive with Cervical intraepithelial neoplasia from abnormal "
        "tissue": "CIN",
        "HIV Positive with Cervical intraepithelial neoplasia from normal "
        "tissue": "CTRL_CERV",
        "HIV Positive without Cervical Cancer": "CTRL_CERV",
        "HIV negative Cervical Cancer": "CERV_CA",
        "HIV negative Cervical Cancer from tumor tissue": "CERV_CA",
        "HIV negative Cervical Cancer from adjacent normal tissue": (
            "CERV_CA"
        ),
        "HIV Positive Cervical Cancer": "CERV_HPVA",
        "HIV Positive Cervical Cancer from tumor tissue": "CERV_HPVA",
        "HIV Positive Cervical Cancer from adjacent normal tissue": (
            "CERV_HPVA"
        ),
    }
    return mapping[row["Description"]]


def sample_site(row):
    return "Cervix"


def primary_site(row):
    return "Cervix"


def sample_type(row):
    mapping = {
        "HIV Positive with Cervical intraepithelial neoplasia": "primary",
        "HIV Positive with Cervical intraepithelial neoplasia from abnormal "
        "tissue": "primary",
        "HIV Positive with Cervical intraepithelial neoplasia from normal "
        "tissue": "control",
        "HIV Positive without Cervical Cancer": "control",
        "HIV negative Cervical Cancer": "primary",
        "HIV negative Cervical Cancer from tumor tissue": "primary",
        "HIV negative Cervical Cancer from adjacent normal tissue": "control",
        "HIV Positive Cervical Cancer": "primary",
        "HIV Positive Cervical Cancer from tumor tissue": "primary",
        "HIV Positive Cervical Cancer from adjacent normal tissue": "control",
    }
    return mapping[row["Description"]]


def material_type(row):
    return "tissue"


def tumor_grade(row):
    mapping = {
        "CIN 1": "low-grade",
        "CIN 2": "high-grade",
        "CIN 3": "high-grade",
    }
    return mapping.get(row["colposcopy based dysplasia grade"])


def sex(row):
    return "female"


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
