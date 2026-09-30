def dataset_id(row):
    return "GSE127857"


def description(row):
    return "DNA methylation profiling of gastric cancer and precursor lesions"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Tumor biopsy intestinal subtype": "Gastric adenocarcinoma, intestinal type",
        "Tumor biopsy diffuse subtype": "Gastric adenocarcinoma, diffuse type",
        "Intestinal metaplasia_complete subtype": "Complete intestinal metaplasia",
        "Intestinal metaplasia_incomplete subtype": "Incomplete intestinal metaplasia",
        "Multifocal chronic atrohic gastritis": "Multifocal chronic atrophic gastritis",
        "Normal gastric mucosa": "Normal gastric mucosa",
        "Normal paired_adyacent  to tumor": "Normal gastric mucosa adjacent to tumor",
        "non atrophic gastritis": "Non-atrophic gastritis",
    }
    return mapping[row["sample type"]]


def methylation_class(row):
    # No vocabulary term exists for intestinal metaplasia or atrophic
    # gastritis; the non-neoplastic gastric samples of this study are the
    # gastric control class.
    mapping = {
        "Tumor biopsy intestinal subtype": "GAST_ADCA",
        "Tumor biopsy diffuse subtype": "GAST_ADCA",
        "Intestinal metaplasia_complete subtype": "GAST_IM",
        "Intestinal metaplasia_incomplete subtype": "GAST_IM",
        "Multifocal chronic atrohic gastritis": "CTRL_GAST",
        "Normal gastric mucosa": "CTRL_GAST",
        "Normal paired_adyacent  to tumor": "CTRL_GAST",
        "non atrophic gastritis": "CTRL_GAST",
    }
    return mapping[row["sample type"]]


def sample_site(row):
    return "Stomach"


def primary_site(row):
    return "Stomach"


def sample_type(row):
    mapping = {
        "Tumor biopsy intestinal subtype": "primary",
        "Tumor biopsy diffuse subtype": "primary",
        "Intestinal metaplasia_complete subtype": "control",
        "Intestinal metaplasia_incomplete subtype": "control",
        "Multifocal chronic atrohic gastritis": "control",
        "Normal gastric mucosa": "control",
        "Normal paired_adyacent  to tumor": "control",
        "non atrophic gastritis": "control",
    }
    return mapping[row["sample type"]]


def material_type(row):
    return "tissue"
