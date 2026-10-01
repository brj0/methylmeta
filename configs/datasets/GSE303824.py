def dataset_id(row):
    return "GSE303824"


def description(row):
    return (
        "Identification and validation of liquid biopsy-based methylation "
        "biomarkers for germ cell tumor subtypes"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["cell line"] is not None:
        # germ cell tumour cell lines, with the subtype they derive from
        cell_lines = {
            "2102EP (EC)": "embryonal carcinoma",
            "JAR (Chc)": "choriocarcinoma",
            "JEG-3 (Chc)": "choriocarcinoma",
            "NCCIT (EC)": "embryonal carcinoma",
            "NOY-1 (YST)": "yolk sac tumor",
            "NT2 (EC)": "embryonal carcinoma",
            "TCam-2 (Se)": "seminoma",
        }
        return cell_lines[row["cell line"]]
    histology = {
        "EC": "embryonal carcinoma",
        "MIX": "mixed germ cell tumor",
        "SE": "seminoma",
        "YST": "yolk sac tumor",
    }
    return histology[row["histology"]]


def methylation_class(row):
    if row["cell line"] is not None:
        cell_lines = {
            "2102EP (EC)": "TES_EMB_CA",
            "JAR (Chc)": "CHORCA",
            "JEG-3 (Chc)": "CHORCA",
            "NCCIT (EC)": "TES_EMB_CA",
            "NOY-1 (YST)": "YST",
            "NT2 (EC)": "TES_EMB_CA",
            "TCam-2 (Se)": "SEMIN",
        }
        return cell_lines[row["cell line"]]
    organs = {
        "Ovary": "ovary",
        "Ovotestis": "ovotestis",
        "Testis": "testis",
    }
    classes = {
        ("ovary", "EC"): "OVA_EMBCA",
        ("ovary", "MIX"): "OVA_MGCT",
        ("ovary", "SE"): "DYSGERM",
        ("ovary", "YST"): "OVA_YST",
        ("ovotestis", "EC"): "EMBCA",
        ("ovotestis", "MIX"): "MGCT",
        ("ovotestis", "SE"): "SEMIN",
        ("ovotestis", "YST"): "YST",
        ("testis", "EC"): "TES_EMB_CA",
        ("testis", "MIX"): "TES_MGCT",
        ("testis", "SE"): "SEMIN",
        ("testis", "YST"): "YST",
    }
    organ = organs[row["location"]]
    return classes[(organ, row["histology"])]


def sample_site(row):
    return row["location"]


def primary_site(row):
    return row["location"]


def sample_type(row):
    if row["cell line"] is not None:
        # a cell line is not a patient tumour sample
        return None
    return "primary"


def material_type(row):
    if row["cell line"] is not None:
        return "cell_line"
    return "tissue"


def preservation(row):
    if row["material"] is None:
        return None
    preservation = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return preservation[row["material"]]


def sex(row):
    value = row["Sex"]
    if value is None:
        return None
    return value.lower()


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
