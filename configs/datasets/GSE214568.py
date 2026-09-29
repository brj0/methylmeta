def dataset_id(row):
    return "GSE214568"


def description(row):
    return (
        "Genomic characterization of DICER1-associated neoplasms "
        "uncovers novel molecular classes"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "SLCT": "Sertoli-Leydig cell tumor",
        "PINB": "Pineoblastoma",
        "MAS": "Müllerian adenosarcoma",
        "PIS DICER1": "Primary intracranial sarcoma, DICER1-mutant",
        "ERMS": "Embryonal rhabdomyosarcoma",
        "MG": "Multinodular goiter (thyroid follicular nodular disease)",
        "MEPL": "Medulloepithelioma",
        "MAS/ERMS": "Müllerian adenosarcoma / embryonal rhabdomyosarcoma",
        "PPB I": "Pleuropulmonary blastoma, type I",
        "PPB II": "Pleuropulmonary blastoma, type II",
        "PPB III": "Pleuropulmonary blastoma, type III",
        "PPB Ir": "Pleuropulmonary blastoma, regressed type Ir",
        "CN": "Cystic nephroma",
        "AS": "Anaplastic sarcoma of the kidney",
        "LGESS": "Low-grade endometrial stromal sarcoma",
        "HGESS": "High-grade endometrial stromal sarcoma",
        "PB": "Pituitary blastoma",
        "NCMH": "Nasal chondromesenchymal hamartoma",
        "PCA": "PCA",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "SLCT": "SLCT",
        "PINB": "PINE_BL",
        "MAS": "UT_ADSARC",
        "PIS DICER1": "CNS_SARC_DICER1",
        "ERMS": "RMS_EMB",
        "MG": "THYR_FND",
        "MEPL": "MEDULLOEPI",
        "MAS/ERMS": "UT_ADSARC",  # NOTE: RMS dropped
        "PPB I": "PPB",
        "PPB II": "PPB",
        "PPB III": "PPB",
        "PPB Ir": "PPB",
        "CN": "PED_CYSTNEPH",
        "AS": "REN_ANASARC",
        "LGESS": "ESS_LG",
        "HGESS": "ESS_HG",
        "PB": "PIT_BL",
        "NCMH": "NCMH",
        "PCA": "THYR_PTC",
    }
    return mapping[row["Source"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return mapping[row["tissue preparation"]]
