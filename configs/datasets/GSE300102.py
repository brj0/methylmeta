def dataset_id(row):
    return "GSE300102"


def description(row):
    return (
        "FET-rearranged soft tissue myoepithelial tumors span a broad "
        "clinicopathologic and molecular spectrum"
    )


def sample_id(row):
    filename = row["Supplementary-Data"].rsplit("/", 1)[-1]
    return filename.split("_Grn.idat")[0]


def diagnosis(row):
    return row["histology"]


def methylation_class(row):
    fusion_class = {
        "EWSR1::KLF15": "MYOEP_KLF15",
        "EWSR1::KLF17": "MYOEP_KLF17",
        "FUS::KLF17": "MYOEP_KLF17",
        "EWSR1::KLF5": "MYOEP_TUM",
        "EWSR1::PBX1": "MYOEP_PBX",
        "EWSR1::PBX3": "MYOEP_PBX",
        "EWSR1::POU5F1": "MYOEP_POU5F1",
        "SS18::POU5F1": "MYOEP_POU5F1",
        "EWSR1::ZNF444": "MYOEP_TUM",
        "EWSR1::NFATC2": "SARC_NFATC2",
        "FUS::NFATC2": "SARC_NFATC2",
        "TRPS1::PLAG1": "MYOEP_TUM",
        "NCALD::PLAG1": "MYOEP_TUM",
        "YWHAZ::PLAG1": "MYOEP_TUM",
        "PLAG1-rearranged": "MYOEP_TUM",
        "PLAG1 IHC": "MYOEP_TUM",
    }
    if row["histology"] == "cutaneous PLAG1-rearranged mixed tumor":
        return "SKIN_PLAG1"
    return fusion_class[row["genotype"]]


def sample_site(row):
    return row["site"]


def primary_site(row):
    return row["site"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
