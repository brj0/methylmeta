def dataset_id(row):
    return "GSE77269"


def description(row):
    return (
        "DNA methylation analysis of hepatocellular carcinoma with portal "
        "vein tumor thrombosis (GSE77269)"
    )


def sample_id(row):
    name = row["Supplementary-Data_1"].split("/")[-1]
    suffix = "_Grn.idat.gz"
    return name[: -len(suffix)]


def diagnosis(row):
    mapping = {
        "Adjacent normal": "Adjacent normal liver tissue",
        "Primary tumor": "Hepatocellular carcinoma",
        "Portal vein tumor thrombosis (PVTT)": (
            "Hepatocellular carcinoma, portal vein tumour thrombus"
        ),
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "Adjacent normal": "CTRL_LIV",
        "Primary tumor": "HCC",
        "Portal vein tumor thrombosis (PVTT)": "HCC",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    mapping = {
        "Adjacent normal": "Liver",
        "Primary tumor": "Liver",
        "Portal vein tumor thrombosis (PVTT)": "Portal vein",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return "Liver"


def sample_type(row):
    mapping = {
        "Adjacent normal": "control",
        "Primary tumor": "primary",
        "Portal vein tumor thrombosis (PVTT)": "metastasis",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
