def dataset_id(row):
    return "GSE174625"


def description(row):
    return (
        "Congenital pulmonary malformations, pleuropulmonary blastoma and "
        "healthy lung tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "CPAM 1": "congenital pulmonary airway malformation, type 1",
        "CPAM 2": "congenital pulmonary airway malformation, type 2",
        "CPAM 3": "congenital pulmonary airway malformation, type 3",
        "ELS": "extralobar bronchopulmonary sequestration",
        "ILS": "intralobar bronchopulmonary sequestration",
        "PPB": "pleuropulmonary blastoma",
        "healthy": "healthy lung tissue",
    }
    return mapping[row["histological type"]]


def methylation_class(row):
    mapping = {
        "CPAM 1": None,
        "CPAM 2": None,
        "CPAM 3": None,
        "ELS": None,
        "ILS": None,
        "PPB": "PPB",
        "healthy": "CTRL_LU",
    }
    return mapping[row["histological type"]]


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    mapping = {
        "normal": "control",
        "malformed": "primary",
        "cancer": "primary",
    }
    return mapping[row["disease_state"]]


def material_type(row):
    return "tissue"


def sex(row):
    return row["Sex"]


def age(row):
    return float(row["age"])
