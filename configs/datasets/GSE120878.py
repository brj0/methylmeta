def dataset_id(row):
    return "GSE120878"


def description(row):
    return (
        "Identification of a robust methylation classifier for cutaneous "
        "melanoma diagnosis (primary invasive melanomas and nevi)"
    )


def sample_id(row):
    # GEO idat file names embed the channel, e.g.
    # 'GSM3417546_melanocytic_Grn_228' -> 'GSM3417546_melanocytic_228'
    value = row["Sample_ID"]
    return value.replace("_Grn", "").replace("_Red", "")


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "primary invasive melanoma": "SKIN_MEL",
        "nevus": "NEV_BEN",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Skin"


def primary_site(row):
    return "Skin"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
