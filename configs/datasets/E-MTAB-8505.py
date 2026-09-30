def dataset_id(row):
    return "E-MTAB-8505"


def description(row):
    return (
        "Methylome landscape of infant B-cell precursor acute lymphoblastic "
        "leukemia (iB-ALL)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Characteristics[disease]"]
    if value == "normal":
        sites = {"bone marrow": "bone marrow", "liver": "liver"}
        return "normal " + sites[row["Characteristics[organism part]"]]
    return value


def methylation_class(row):
    keys = {
        "childhood B acute lymphoblastic leukemia": row[
            "Characteristics[clinical history]"
        ],
        "normal": row["Characteristics[organism part]"],
    }
    mapping = {
        "MLL-AF4": "B_ALL_KMT2A",
        "MLL-AF9": "B_ALL_KMT2A",
        "non MLL": "B_ALL",
        "bone marrow": "CTRL_MARROW",
        "liver": "CTRL_LIV",
    }
    return mapping[keys[row["Characteristics[disease]"]]]


def sample_site(row):
    sites = {"bone marrow": "Bone marrow", "liver": "Liver"}
    return sites[row["Characteristics[organism part]"]]


def primary_site(row):
    if row["Characteristics[disease]"] == "normal":
        sites = {"bone marrow": "Bone marrow", "liver": "Liver"}
        return sites[row["Characteristics[organism part]"]]
    return "Bone marrow"


def sample_type(row):
    mapping = {
        "childhood B acute lymphoblastic leukemia": "primary",
        "normal": "control",
    }
    return mapping[row["Characteristics[disease]"]]


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"].strip().lower()
    mapping = {
        "female": "female",
        "male": "male",
        "not applicable": None,
        "not available": None,
    }
    return mapping[value]


def age(row):
    value = str(row["Characteristics[age]"]).strip()
    unit = str(row["Unit[time unit]"]).strip()
    try:
        years = float(value)
    except ValueError:
        return None
    if unit == "month":
        return years / 12
    if unit == "week":
        return years / 52
    return None
