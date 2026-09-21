def dataset_id(row):
    return "GSE221745"


def description(row):
    return "Bone marrow and peripheral blood with GATA2 deficiency"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Bone Marrow, GATA2 mutant": "MDS_LOW",
        "Bone Marrow, wild type genotype": "CONTR_MARROW",
        "Peripheral Blood, GATA2 mutant": "MDS_LOW",
        "Peripheral Blood, wild type genotype": "CONTR_BLOOD",
    }
    return mapping[value]


def sample_site(row):
    value = row["Source"]
    mapping = {
        "Bone Marrow, GATA2 mutant": "Bone marrow",
        "Bone Marrow, wild type genotype": "Bone marrow",
        "Peripheral Blood, GATA2 mutant": "Peripheral Blood",
        "Peripheral Blood, wild type genotype": "Peripheral Blood",
    }
    return mapping[value]


def sample_type(row):
    value = row["Source"]
    mapping = {
        "Bone Marrow, GATA2 mutant": "primary",
        "Bone Marrow, wild type genotype": "control",
        "Peripheral Blood, GATA2 mutant": "primary",
        "Peripheral Blood, wild type genotype": "control",
    }
    return mapping[value]


def sex(row):
    return row['""sex""']


def age(row):
    return row['""age""']
