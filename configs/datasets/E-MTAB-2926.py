def dataset_id(row):
    return "E-MTAB-2926"


def description(row):
    return "DLBCL and lymphoid controls"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Factor Value [clinical information]"]


def methylation_class(row):
    value = row["Description"].lower()

    if "dlbcl" in value:
        return "DLBCL"
    if "gastritis" in value:
        return "CTRL_GASTRIC"
    if "control" in value:
        return "CTRL_LYMPH"
    if "mzl" in value:
        return "MZL"

    return value


def material_type(row):
    value = row["Factor Value[material type]"].lower()

    if "paraffin" in value:
        return "tissue"
    if "frozen" in value:
        return "tissue"
    if "cell" in value:
        return "cell_line"

    return value


def preservation(row):
    value = row["Factor Value[material type]"].lower()

    if "paraffin" in value:
        return "FFPE"
    if "frozen" in value:
        return "FROZEN"
    if "cell" in value:
        return None

    return value


def sex(row):
    return row["Characteristics[sex]"]
