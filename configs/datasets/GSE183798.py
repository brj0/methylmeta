def dataset_id(row):
    return "GSE183798"


def description(row):
    return "Tumor DNA methylation in pediatric germ cell tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Blue cell tumor": "Blue cell tumor",
        "Germinoma": "Germinoma",
        "MMGCT": "Mixed malignant germ cell tumor",
        "Teratoma": "Teratoma",
        "YST": "Yolk sac tumor",
    }
    return mapping[row["tumor histology"]]


def methylation_class(row):
    # the WHO germ cell tumour entity depends on the organ: a germinoma is a
    # CNS germinoma, a dysgerminoma or a seminoma; yolk sac tumour and mixed
    # germ cell tumours likewise have organ-specific classes. A generic
    # class is used for teratoma (maturity not reported) and for tumours in
    # organs without a matching class. (site, histology) combinations that
    # the vocabulary cannot resolve stay None.
    mapping = {
        ("Intracranial", "Germinoma"): "CNS_GERMI",
        ("Intracranial", "MMGCT"): "MGCT",
        ("Intracranial", "Teratoma"): "TER",
        ("Intracranial", "YST"): None,
        ("Intracranial", "Blue cell tumor"): None,
        ("Ovary", "Germinoma"): "DYSGERM",
        ("Ovary", "MMGCT"): "OVA_MGCT",
        ("Ovary", "Teratoma"): "TER",
        ("Ovary", "YST"): "OVA_YST",
        ("Ovary", "Blue cell tumor"): None,
        ("Testis", "Germinoma"): "SEMIN",
        ("Testis", "MMGCT"): "TES_MGCT",
        ("Testis", "Teratoma"): "TER",
        ("Testis", "YST"): "YST",
        ("Testis", "Blue cell tumor"): None,
        ("Extragonadal", "Germinoma"): None,
        ("Extragonadal", "MMGCT"): "MGCT",
        ("Extragonadal", "Teratoma"): "TER",
        ("Extragonadal", "YST"): None,
        ("Extragonadal", "Blue cell tumor"): None,
        ("Missing", "Germinoma"): None,
        ("Missing", "MMGCT"): "MGCT",
        ("Missing", "Teratoma"): "TER",
        ("Missing", "YST"): None,
        ("Missing", "Blue cell tumor"): None,
    }
    return mapping[(row["tumor location"], row["tumor histology"])]


def sample_site(row):
    value = row["tumor location"]
    mapping = {"Missing": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["tumor location"]
    mapping = {"Missing": None}
    return mapping.get(value, value)


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["tissue type"]]


def sex(row):
    mapping = {
        "male": "male",
        "female": "female",
        "GD": None,
        "missing": None,
    }
    return mapping[row["Sex"]]


def age(row):
    value = row["age at diagnosis"]
    if value is None:
        return None
    return float(value)
