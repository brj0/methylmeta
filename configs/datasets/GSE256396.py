def _is_control(row):
    return row["disease"] == "Healthy control" or row["mdsdiag"] == "CTRL"


def dataset_id(row):
    return "GSE256396"


def description(row):
    return (
        "Somatic mutations and DNA methylation identify a subgroup of poor "
        "prognosis within lower risk myelodysplastic syndromes"
    )


def sample_id(row):
    value = row["Sample_ID"]
    if value:
        return value
    return row["Accession"]


def diagnosis(row):
    if _is_control(row):
        return "Healthy control bone marrow"
    mapping = {
        "5q-Syndrome": "MDS with isolated 5q deletion",
        "CMML-1": "Chronic myelomonocytic leukemia-1",
        "MDS-U": "Myelodysplastic syndrome, unclassifiable",
        "RA": "Refractory anemia",
        "RAEB-1": "Refractory anemia with excess blasts-1",
        "RARS": "Refractory anemia with ring sideroblasts",
        "RCMD": "Refractory cytopenia with multilineage dysplasia",
        "RCMD-RS": "RCMD with ring sideroblasts",
    }
    return mapping[row["mdsdiag"]]


def methylation_class(row):
    if _is_control(row):
        return "CTRL_MARROW"
    mapping = {
        "5q-Syndrome": "MDS_LB_5Q",
        "CMML-1": "CMML",
        "MDS-U": "MDS",
        "RA": "MDS_LB",
        "RAEB-1": "MDS_IB",
        "RARS": "MDS_LB",
        "RCMD": "MDS_LB",
        "RCMD-RS": "MDS_LB",
    }
    return mapping[row["mdsdiag"]]


def sample_site(row):
    return "Bone marrow"


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    if _is_control(row):
        return "control"
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male", None: None}
    return mapping[row["gender"]]
