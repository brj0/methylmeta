"""The dataset-config contract, as an importable string.

Anything that writes configs/datasets/<dataset_id>.py files - a human or,
later, a pydantic-ai agent - needs to follow this exact contract.
"""

from methylmeta.schema import describe_fields

_TEMPLATE = '''\
A dataset config is a single Python file at configs/datasets/<dataset_id>.py.
It contains plain top-level functions, one per canonical field, each with
the signature:

    def <field_name>(row: dict) -> value | None

`row` is one row of the raw metadata file (annotation.csv/tsv/xlsx) as a
dict (column name -> raw value; missing values are already None). Every
function is called once per row; there is no shared state and no imports
needed beyond the file itself.

Required function:
    dataset_id(row) -> str
        Constant identifier for this dataset (e.g. a GEO/ArrayExpress
        accession, TCGA project code, or a custom cohort name). Called once
        with row=None to identify the dataset, so it must not touch row.

Optional function:
    description(row) -> str
        One-line human-readable label for the dataset/cohort.

Canonical fields (define a function for any that apply; omit entirely if a
dataset has no data for that field):

{fields}

Four idioms cover almost every case - pick the simplest one that fits:

1. Direct passthrough - the raw column already IS the value:

    def sample_id(row):
        return row["Sample_ID"]

2. Exact value mapping, strict - a raw column needs translating via a
   lookup dict, and every raw value is expected to be covered. Use plain
   dict indexing (mapping[value]) so an unmapped raw value fails loudly
   with a clear KeyError instead of silently passing through:

    def methylation_class(row):
        value = row["Factor Value[clinical information]"]
        mapping = {{
            "HPV related HNSCC": "HNSCC_HPV_POS",
            "non HPV related HNSCC": "HNSCC_HPV_NEG",
        }}
        return mapping[value]

3. Exact value mapping, with fallback - use mapping.get(value, default)
   instead when unmapped/placeholder raw values should pass through
   unchanged (or become None) rather than raise:

    def sample_site(row):
        value = row["tissue_1"]
        mapping = {{"--": None}}
        return mapping.get(value, value)

4. Constant - every sample in this dataset has the same value:

    def sample_site(row):
        return "Cerebellopontine angle"

For anything that doesn't fit a dict lookup (free-text fields needing
substring matching, values computed from multiple columns, etc.), write a
plain function with normal Python control flow - if/elif, string
containment checks (`"foo" in value.lower()`), whatever is clearest. Do
NOT use regex; substring/equality checks are strongly preferred for
readability. Do NOT implement row filtering/exclusion inside a config -
every row in the metadata file is harmonized; if some rows are genuinely
invalid, filtering happens upstream of methylmeta, not inside a config.

Hard constraint: methylation_class must be a valid WHO acronym - a key
that already exists in tumor_types.yaml. This is enforced by validation
(SampleMetadata rejects anything else), so if a genuinely new tumor entity
doesn't have an acronym yet, that has to be added to tumor_types.yaml
first (with name/site/lineage/who_volume) rather than invented ad hoc in
a config. Use methylmeta.vocab.search_tumor_types(diagnosis_text) to find
the right acronym for a given raw diagnosis string instead of guessing.

Workflow for writing/fixing a config:
    1. merger.profile(dataset_id) - see the real columns and their value
       distributions before writing any mapping logic.
    2. Write configs/datasets/<dataset_id>.py per the idioms above.
    3. merger.test(dataset_id) - dry-run against the real metadata file;
       every failing row is reported with its exact error, without one bad
       row hiding the rest. Iterate until report.success is True.
    4. Once every dataset you want passes test(), merger.merge(dataset_ids)
       does the real multi-dataset merge.
'''

CONFIG_SPEC = _TEMPLATE.format(
    fields="\n".join(f"    {line}" for line in describe_fields().splitlines())
)
