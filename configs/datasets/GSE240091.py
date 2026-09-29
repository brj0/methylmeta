def dataset_id(row):
    return "GSE240091"


def description(row):
    return "Growing teratoma tissues from non-seminomatous germ cell tumors"


def sample_id(row):
    # NOTE: This repo has wrong idat file endings (green.idat / red.idat)
    return row["Sample_ID"].removesuffix("_green")


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "TER_PP"


def primary_site(row):
    return "Testis"


def material_type(row):
    return "tissue"
