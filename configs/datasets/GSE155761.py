def dataset_id(row):
    return "GSE155761"


def description(row):
    return (
        "Methylomic landscape of fallopian tube lesions associated with "
        "ovarian high-grade serous carcinoma (Pisanic et al.)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["histology"]
    if value is None:
        return row["source_name_ch1"].split(",")[0]
    return value


def methylation_class(row):
    mapping = {
        "Adjacent Normal Fallopian Tube Epithelia": "CTRL_TUB",
        "Concomitant High Grade Serous Carcinoma Tumor": "OVA_HGSC",
        "Dormant Serous Tubal Intraepithelial Carcinoma": "STIC",
        "P53 Signature Lesion": None,
        "Serous Tubal Intraepithelial Carcinoma (STIC)": "STIC",
        "cervical mucosa from cancer-free normal control": "CTRL_CERV",
        "endometrial endometrioid carcinoma": "ENDOM_EC",
        "endometrial mucosa from cancer-free normal control": "CTRL_ENDOM",
        "fallopian tube mucosa from cancer-free normal control": "CTRL_TUB",
        "high-grade serous ovarian carcinoma": "OVA_HGSC",
        "poorly differentiated ovarian tumor": "OVA_CA",
        "uterine serous carcinoma": "ENDOM_SC",
        None: None,
    }
    return mapping[row["histology"]]


def _site(histology):
    mapping = {
        "Adjacent Normal Fallopian Tube Epithelia": "Fallopian tube",
        "Concomitant High Grade Serous Carcinoma Tumor": "Ovary",
        "Dormant Serous Tubal Intraepithelial Carcinoma": "Fallopian tube",
        "P53 Signature Lesion": "Fallopian tube",
        "Serous Tubal Intraepithelial Carcinoma (STIC)": "Fallopian tube",
        "cervical mucosa from cancer-free normal control": "Cervix",
        "endometrial endometrioid carcinoma": "Endometrium",
        "endometrial mucosa from cancer-free normal control": "Endometrium",
        "fallopian tube mucosa from cancer-free normal control": "Fallopian tube",
        "high-grade serous ovarian carcinoma": "Ovary",
        "poorly differentiated ovarian tumor": "Ovary",
        "uterine serous carcinoma": "Uterus",
        None: None,
    }
    return mapping[histology]


def sample_site(row):
    return _site(row["histology"])


def primary_site(row):
    return _site(row["histology"])


def sample_type(row):
    mapping = {
        "Adjacent Normal Fallopian Tube Epithelia": "control",
        "Concomitant High Grade Serous Carcinoma Tumor": "primary",
        "Dormant Serous Tubal Intraepithelial Carcinoma": "primary",
        "P53 Signature Lesion": "primary",
        "Serous Tubal Intraepithelial Carcinoma (STIC)": "primary",
        "cervical mucosa from cancer-free normal control": "control",
        "endometrial endometrioid carcinoma": "primary",
        "endometrial mucosa from cancer-free normal control": "control",
        "fallopian tube mucosa from cancer-free normal control": "control",
        "high-grade serous ovarian carcinoma": "primary",
        "poorly differentiated ovarian tumor": "primary",
        "uterine serous carcinoma": "primary",
        None: "primary",
    }
    return mapping[row["histology"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE tissue": "FFPE", "fresh-frozen": "FROZEN"}
    return mapping[row["tissue type"]]


def tumor_grade(row):
    mapping = {
        "1": "G1",
        "2": "G2",
        "3": "G3",
        "4": "G4",
        "no data": None,
        None: None,
    }
    return mapping[row["grade"]]


def sex(row):
    return "female"


def age(row):
    value = row["age"]
    if value is None or value == "no data":
        return None
    return float(value)
