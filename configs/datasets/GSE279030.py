def dataset_id(row):
    return "GSE279030"


def description(row):
    return (
        "DNA methylation profiling of histiocytic neoplasms (Erdheim-Chester "
        "disease, Langerhans cell histiocytosis, Rosai-Dorfman-Destombes "
        "disease) and non-neoplastic suture granuloma controls, 2024"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    title = row["Title"]
    if "Langerhans cell histiocytosis" in title:
        return "Langerhans cell histiocytosis"
    if "Erdheim-Chester" in title:
        return "Erdheim-Chester disease"
    if "Rosai-Dorfman" in title:
        return "Rosai-Dorfman-Destombes disease"
    if "suture granulomas" in title:
        return "non-neoplastic histiocytic infiltrates of suture granulomas"
    return None


def methylation_class(row):
    title = row["Title"]
    if "Langerhans cell histiocytosis" in title:
        return "LCH"
    if "Erdheim-Chester" in title:
        return "ECD"
    if "Rosai-Dorfman" in title:
        return "RDD"
    if "suture granulomas" in title:
        return "HSG"
    return None


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    value = row["disease state"]
    mapping = {
        "control, suture granulomas": "control",
        "histiocytoses": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["Sex"]
