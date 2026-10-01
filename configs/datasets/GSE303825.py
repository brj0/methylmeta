def dataset_id(row):
    return "GSE303825"


def description(row):
    return (
        "Identification and validation of liquid biopsy-based methylation "
        "biomarkers for germ cell tumor subtypes"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    histology = {
        "GER": "germinoma",
        "MIX": "mixed germ cell tumor",
        "SE": "seminoma",
        "TE": "teratoma",
        "YST": "yolk sac tumor",
    }
    return histology[row["histology"]]


def methylation_class(row):
    organs = {
        "CNS": "cns",
        "Mediastinum": "mediastinum",
        "Ovary": "ovary",
        "Retroperitoneum": "retroperitoneum",
        "Sacrum": "sacrum",
        "Testis": "testis",
    }
    classes = {
        # germinoma of the CNS is the only organ-specific germinoma class
        ("cns", "GER"): "CNS_GERMI",
        # germ cell tumours outside the gonads and the CNS have no
        # site-specific class, so the organ-agnostic mixed (MGCT) and
        # teratoma (TER) classes are used; teratoma maturity (mature vs
        # immature) is not recorded either, so TER is used throughout
        ("cns", "MIX"): "MGCT",
        ("cns", "TE"): "TER",
        ("mediastinum", "TE"): "TER",
        ("retroperitoneum", "TE"): "TER",
        ("sacrum", "MIX"): "MGCT",
        ("sacrum", "TE"): "TER",
        ("mediastinum", "YST"): "YST",
        ("ovary", "MIX"): "OVA_MGCT",
        ("ovary", "TE"): "TER",
        ("ovary", "YST"): "OVA_YST",
        ("testis", "MIX"): "TES_MGCT",
        ("testis", "SE"): "SEMIN",
        ("testis", "TE"): "TER",
        ("testis", "YST"): "YST",
    }
    organ = organs[row["location"]]
    return classes[(organ, row["histology"])]


def sample_site(row):
    return row["location"]


def primary_site(row):
    return row["location"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
        "Unknown": None,
    }
    return mapping[row["material"]]


def sex(row):
    return row["Sex"].lower()


def age(row):
    value = row["age"]
    if value == "Unknown":
        return None
    return float(value)
