def dataset_id(row):
    return "GSE70783"


def description(row):
    return (
        "Primary intracranial germ cell tumors and normal tissue, "
        "Fukushima 2017"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    value = row["tissue"]
    if row["disease state"] == "Normal":
        controls = {
            "Cerebral cortex": "CTRL_HEMI",
            "Pineal gland": "CTRL_PINE",
            "Neural stem cell": "CTRL_BRAIN",
            "Testis": "CTRL_TES",
            "Ovary": "CTRL_OVA",
        }
        # microdissection control samples carry a tumour label rather than
        # an organ name, so fall back to the site they were taken from
        control_site = {
            "Central nervous system": "CTRL_BRAIN",
            "Testis": "CTRL_TES",
            "Gonad": None,
        }
        return controls.get(value, control_site.get(row["location"]))
    tumors = {
        "Germinoma": "CNS_GERMI",
        "Germinoma component": "CNS_GERMI",
        "Seminoma": "SEMIN",
        "Yolk sac tumor": "YST",
        "Mature teratoma": "TER",
        "Immature teratoma": "TER",
        "Embryonal carcinoma": "EMBCA",
        "Choriocarcinoma": "CHORCA",
        "Non-germinoma component": "MGCT",
        "Germinoma, Embryonal carcinoma": "MGCT",
        "Germinoma, Yolk sac tumor": "MGCT",
        "Yolk sac tumor, Germinoma": "MGCT",
        "Immature teratoma, Germinoma": "MGCT",
        "Mature teratoma, Germinoma": "MGCT",
        "Embryonal carcinoma, Germinoma": "MGCT",
        "Choriocarcinoma, Germinoma, Immature teratoma": "MGCT",
        "Mature teratoma, Germinoma, hemangioma": "MGCT",
        "Germinoma, Immature teratoma, Choriocarcinoma, "
        "Embryonal carcinoma": "MGCT",
        "Immature teratoma, Germinoma, polyembryoma, Yolk sac tumor": "MGCT",
        "Yolk sac tumor, Embryonal carcinoma, Immature teratoma, "
        "Germinoma": "MGCT",
        "Mature teratoma, Yolk sac tumor, Embryonal carcinoma, "
        "Germinoma": "MGCT",
        "Mature teratoma, Germinoma, Yolk sac tumor, "
        "Embryonal carcinoma": "MGCT",
    }
    return tumors[value]


def sample_site(row):
    return row["location"]


def primary_site(row):
    return row["location"]


def sample_type(row):
    mapping = {"Normal": "control", "Tumor": "primary"}
    return mapping[row["disease state"]]


def material_type(row):
    mapping = {
        "Cultured cell": "cell_line",
        "FFPE": "tissue",
        "Fresh frozen": "tissue",
    }
    return mapping[row["sample type"]]


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "Fresh frozen": "FROZEN",
        "Cultured cell": None,
    }
    return mapping[row["sample type"]]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
