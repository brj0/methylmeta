def dataset_id(row):
    return "GSE156299"


def description(row):
    return (
        "DNA methylation profiling of normal bile duct, biliary precursor "
        "lesions (IPNB/ITPN) and cholangiocarcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "IPNB - premalignant": (
            "Intraductal papillary neoplasm of the bile ducts (IPNB)"
        ),
        "ITPN - premalignant": (
            "Intraductal tubulopapillary neoplasm of the bile ducts (ITPN)"
        ),
        "ITPN-P - premalignant": (
            "Intraductal tubulopapillary neoplasm of the bile ducts (ITPN-P)"
        ),
        "bile duct control - normal": "Normal bile duct",
        "bile duct control - normal - ITPN-P": "Normal bile duct",
        "dCCA - invasive": "Distal cholangiocarcinoma, invasive",
        "iCCA - invasive": "Intrahepatic cholangiocarcinoma, invasive",
        "pCCA - invasive": "Perihilar cholangiocarcinoma, invasive",
    }
    return mapping[row["disease state"]]


def methylation_class(row):
    mapping = {
        "IPNB - premalignant": "BD_IPN",
        "ITPN - premalignant": "BD_ITPN",
        "ITPN-P - premalignant": "BD_ITPN",
        "bile duct control - normal": "CTRL_BD",
        "bile duct control - normal - ITPN-P": "CTRL_BD",
        "dCCA - invasive": "CCA_EXT",
        "iCCA - invasive": "CCA_INT",
        "pCCA - invasive": "CCA_EXT",
    }
    return mapping[row["disease state"]]


def sample_site(row):
    mapping = {
        "IPNB - premalignant": "Bile duct",
        "ITPN - premalignant": "Bile duct",
        "ITPN-P - premalignant": "Bile duct",
        "bile duct control - normal": "Bile duct",
        "bile duct control - normal - ITPN-P": "Bile duct",
        "dCCA - invasive": "Bile duct",
        "iCCA - invasive": "Liver",
        "pCCA - invasive": "Bile duct",
    }
    return mapping[row["disease state"]]


def primary_site(row):
    mapping = {
        "IPNB - premalignant": "Bile duct",
        "ITPN - premalignant": "Bile duct",
        "ITPN-P - premalignant": "Bile duct",
        "bile duct control - normal": "Bile duct",
        "bile duct control - normal - ITPN-P": "Bile duct",
        "dCCA - invasive": "Extrahepatic bile duct",
        "iCCA - invasive": "Liver",
        "pCCA - invasive": "Extrahepatic bile duct",
    }
    return mapping[row["disease state"]]


def sample_type(row):
    mapping = {
        "IPNB - premalignant": "primary",
        "ITPN - premalignant": "primary",
        "ITPN-P - premalignant": "primary",
        "bile duct control - normal": "control",
        "bile duct control - normal - ITPN-P": "control",
        "dCCA - invasive": "primary",
        "iCCA - invasive": "primary",
        "pCCA - invasive": "primary",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
