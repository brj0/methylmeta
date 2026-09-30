def dataset_id(row):
    return "E-MTAB-7263"


def description(row):
    return (
        "Methylation profiling of cartilage tumors, a multi-omics "
        "chondrosarcoma cohort with IDH mutation data"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    grade = row["Characteristics[tumor grading]"]
    if grade == "dedifferentiated":
        return "CSA_DD"
    if grade == "benign":
        return None
    idh1 = row["Characteristics[idh1.aamut]"]
    idh2 = row["Characteristics[idh2.aamut]"]
    if idh1 is None and idh2 is None:
        return "CSA"
    if idh1 or idh2:
        return "CSA_IDH_MUT"
    return "CSA_IDH_WT"


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["Characteristics[tumor grading]"]
    if value is None:
        return None
    mapping = {
        "G1": "G1",
        "G2": "G2",
        "G3": "G3",
        "benign": "G0",
        "dedifferentiated": None,
        "SimplifiedHistologyHighestGrade": None,
    }
    return mapping[value]
