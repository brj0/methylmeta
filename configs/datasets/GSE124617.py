def dataset_id(row):
    return "GSE124617"


def description(row):
    return "IDH Mutant Tumor Samples"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease state"]
    mapping = {
        "AML": "AML IDH Mutant",
        "Astrocytoma": "Astrocytoma IDH Mutant",
        "Cholangiocarcinoma": "Cholangiocarcinoma IDH Mutant",
        "Oligodendroglioma": "Oligodendroglioma IDH Mutant",
        "Breast Cancer": "Breast Cancer IDH Mutant",
        "SNUC": "SNUC IDH Mutant",
    }
    return mapping[value]


def methylation_class(row):
    value = row["disease state"]
    mapping = {
        "AML": "AML",
        "Astrocytoma": "ASTRO_IDH",
        "Breast Cancer": "BRCA",
        "Cholangiocarcinoma": "CCA",
        "Oligodendroglioma": "OLIGO_IDH",
        "SNUC": "NECIDH2",
    }
    return mapping[value]


def sample_site(row):
    value = row["tissue"]
    mapping = {
        "AML tissue": "Blood / Bone Marrow",
        "Astrocytoma tissue": "Brain",
        "Cholangiocarcinoma tissue": "Liver/Bile Duct",
        "Oligodendroglioma tissue": "Brain",
        "Breast Cancer tissue": "Breast",
        "SNUC tissue": "Sinonasal",
    }
    return mapping[value]


def primary_site(row):
    value = row["tissue"]
    mapping = {
        "AML tissue": "Blood / Bone Marrow",
        "Astrocytoma tissue": "Brain",
        "Cholangiocarcinoma tissue": "Liver/Bile Duct",
        "Oligodendroglioma tissue": "Brain",
        "Breast Cancer tissue": "Breast",
        "SNUC tissue": "Sinonasal",
    }
    return mapping[value]


def preservation(row):
    return "FFPE"
