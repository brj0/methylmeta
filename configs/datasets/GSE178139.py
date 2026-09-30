def dataset_id(row):
    return "GSE178139"


def description(row):
    return (
        "DNA methylation signatures differentiating meningiomas from normal "
        "dura"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "meningioma": "Meningioma",
        "dura": "Normal dura mater",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "meningioma": "MNG",
        "dura": "CTRL_DURA",
    }
    return mapping[value]


def sample_site(row):
    value = row["Source"]
    mapping = {
        "meningioma": "Meninges",
        "dura": "Dura mater",
    }
    return mapping[value]


def primary_site(row):
    return "Meninges"


def sample_type(row):
    value = row["Source"]
    mapping = {
        "meningioma": "primary",
        "dura": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["who grade"]
    mapping = {
        "I": "G1",
        "II": "G2",
        "dura": None,
    }
    return mapping[value]


def sex(row):
    return row["Sex"].lower()


def age(row):
    return float(row["age"])
