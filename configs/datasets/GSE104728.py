def dataset_id(row):
    return "GSE104728"


def description(row):
    return "Proteogenomic landscape of human medulloblastoma subgroups"


def sample_id(row):
    # GEO-style IDAT basename, e.g.
    # 'GSM2806749_200397860078_R01C02'
    return row["Sample_ID"]


def diagnosis(row):
    return "medulloblastoma"


def methylation_class(row):
    # SHH cannot be resolved into SHH A (child/adult) or SHH B (infant)
    # without age information, so it stays at the broader MB class.
    mapping = {
        "WNT": "MB_WNT",
        "SHH": "MB_SHH",
        "G3": "MB_G3",
        "G4": "MB_G4",
        None: "MB",
    }
    return mapping[row["tumor subgroup"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
