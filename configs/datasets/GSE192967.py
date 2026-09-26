def dataset_id(row):
    return "GSE192967"


def description(row):
    return (
        "DNA methylation profiling of ovarian adult and juvenile granulosa "
        "cell tumors (2022)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "Genomic DNA from ovarian adult granulosa cell tumors": (
            "Adult granulosa cell tumor"
        ),
        "Genomic DNA from ovarian juvenile granulosa cell tumors": (
            "Juvenile granulosa cell tumor"
        ),
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Genomic DNA from ovarian adult granulosa cell tumors": "GRAN_ADULT",
        "Genomic DNA from ovarian juvenile granulosa cell tumors": "GRAN_JUV",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return "female"
