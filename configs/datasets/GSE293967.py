def dataset_id(row):
    return "GSE293967"


def description(row):
    return "Pleomorphic Adenoma vs Carcinoma ex Pleomorphic Adenoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Description"]
    mapping = {
        "Carcinoma NOS ex PA": "Carcinoma ex Pleomorphic Adenoma, Not Otherwise Specified",
        "PA": "Pleomorphic Adenoma",
        "adenoid cystic carcinoma ex PA": "Adenoid Cystic Carcinoma ex Pleomorphic Adenoma",
        "epithelial/myoepithelial carcinoma ex PA": "Epithelial-Myoepithelial Carcinoma ex Pleomorphic Adenoma",
        "myoepithelial carcinoma ex PA": "Myoepithelial Carcinoma ex Pleomorphic Adenoma",
        "salivary duct carcinoma ex PA": "Salivary Duct Carcinoma ex Pleomorphic Adenoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Description"]
    mapping = {
        "Carcinoma NOS ex PA": "CXPA",
        "PA": "PLEO_AD",
        "adenoid cystic carcinoma ex PA": "ADCC",
        "epithelial/myoepithelial carcinoma ex PA": "EMC",
        "myoepithelial carcinoma ex PA": "SG_MYOEP_CA",
        "salivary duct carcinoma ex PA": "SDC",
    }
    return mapping[value]


def sample_site(row):
    value = row["localisation"]
    mapping = {
        "salivary gland; Parotid": "Parotid Gland",
        "salivary gland; Sub-maxillary": "Submandibular Gland",
        "salivary gland; Sub-mandibular": "Submandibular Gland",
        "salivary gland; Cervical": "Cervical Salivary Gland",
        "salivary gland; Para-pharyngeal": "Parapharyngeal Space",
        "salivary gland; Peri-mandibular": "Perimandibular",
        "salivary gland; Unknown": "Salivary Gland (unspecified)",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["Sex"]
