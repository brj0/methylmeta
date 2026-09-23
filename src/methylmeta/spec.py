"""The dataset-config contract, as an importable string.

Anything that writes configs/datasets/<dataset_id>.py files - a human or,
later, a pydantic-ai agent - needs to follow this exact contract.
"""

from methylmeta.schema import describe_fields

_TEMPLATE = """\
A dataset config is a single Python file at configs/datasets/<dataset_id>.py.
It contains plain top-level functions, one per canonical field, each with
the signature:

    def <field_name>(row: dict) -> value | None

`row` is one row of the raw metadata file (annotation.csv/tsv/xlsx) as a dict
(column name -> raw value; missing values are already None). Every function is
called once per row; there is no shared state and no shared imports needed
beyond the file itself. If needed an import can be put inside the function.

Function names must be exactly a canonical field name (below). Any other
public function is reported by test() as a config error, because the harmonizer
would silently ignore it (e.g. `material` instead of `material_type`). Helper
functions are allowed if their name starts with an underscore. The filename
must equal the dataset_id: configs/datasets/<dataset_id>.py.

Required function:
    dataset_id(row) -> str
        Constant identifier for this dataset (e.g. a GEO/ArrayExpress
        accession, TCGA project code, or a custom cohort name). Called once
        with row=None to identify the dataset, so it must not touch row.

Optional function:
    description(row) -> str
        One-line human-readable label for the dataset/cohort. If a public
        GEO/ArrayExpress study description is available (the agent exposes this
        as get_study_description), the study title is a good source for this.

Canonical fields (define a function for any that apply; omit entirely if a
dataset has no data for that field):

{fields}

Five idioms cover almost every case - pick the simplest one that fits:

1. Direct passthrough - the raw column already IS the value:

    def sample_id(row):
        return row["Sample_ID"]

2. Exact value mapping, strict — a raw column needs translating via a
   lookup dict. This field is important, but raw metadata may be missing,
   invalid, or represented across multiple rows for the same sample. Every
   relevant raw row must still be processed; do not filter rows.

   Use plain dict indexing (mapping[value]) when the expected raw values can be
   explicitly enumerated, so an unmapped raw value fails loudly with a clear
   KeyError instead of silently passing through. Samples for which
   methylation_class cannot be determined may later be filtered by downstream
   processing.

   Do not assume that one raw metadata row always corresponds to exactly one
   sample. Multiple rows may occasionally contribute metadata for the same
   sample.

    def methylation_class(row):
        value = row["Factor Value[clinical information]"]
        mapping = {{
            "HPV related HNSCC": "HNSCC_HPVA",
            "non HPV related HNSCC": "HNSCC_HPVI",
        }}
        return mapping[value]

3. Exact value mapping, with fallback - use mapping.get(value, default) instead
   when unmapped/placeholder raw values should pass through unchanged (or
   become None) rather than raise:

    def sample_site(row):
        value = row["tissue_1"]
        mapping = {{"--": None}}
        return mapping.get(value, value)

4. Constant - every sample in this dataset has the same value:

    def sample_site(row):
        return "Cerebellopontine angle"

5. Full-text diagnosis - preserve the complete raw diagnosis (often the
   histological diagnosis) without converting it to a WHO acronym. Prefer the
   raw diagnosis column that contains the most specific and complete diagnostic
   text. This value may later be used to determine methylation_class or as a
   control column.

    def diagnosis(row):
        return row["histological diagnosis"]

For anything that doesn't fit a dict lookup (free-text fields needing substring
matching, values computed from multiple columns, etc.), write a plain function
with normal Python control flow - if/elif, string containment checks (`"foo" in
value.lower()`), whatever is clearest. Do NOT use regex; substring/equality
checks are strongly preferred for readability. Do NOT implement row
filtering/exclusion inside a config - every row in the metadata file is
harmonized; if some rows are genuinely invalid, filtering happens upstream of
methylmeta, not inside a config. Prefer direct indexing (`row["column"]`) over
`row.get("column")` when the column is expected to exist. Direct indexing fails
loudly on incorrect column names and makes configs easier to review. Use
`row.get()` only when a column is genuinely optional or its absence is expected
or there are too many different entries that bloat the code of the dictionary
map.

Hard constraint: methylation_class must be a valid WHO acronym - a key that
already exists in tumor_types.yaml. This is enforced by validation
(SampleMetadata rejects anything else), so if a genuinely new tumor entity
doesn't have an acronym yet, that has to be added to tumor_types.yaml first
(with name/site/lineage/who_volume) rather than invented ad hoc in a config.
Use methylmeta.vocab.search_tumor_types(diagnosis_text) to find the right
acronym for a given raw diagnosis string instead of guessing. If there is
really no valid methylation class (for example if the row does not correspond
to a methylaton array) you can set the class to None'.

Workflow for writing/fixing a config:
    1. merger.profile(dataset_id) - see the real columns and their value
       distributions before writing any mapping logic.
    2. For a public GEO/ArrayExpress dataset, check the study's public
       title/summary/design for context on what the raw columns likely mean
       (the agent exposes this as get_study_description).
    3. Write configs/datasets/<dataset_id>.py per the idioms above.
    4. merger.test(dataset_id) - dry-run against the real metadata file; every
       failing row is reported with its exact error, without one bad row hiding
       the rest. Iterate until report.success is True.
    5. Once every dataset you want passes test(), merger.merge(dataset_ids)
       does the real multi-dataset merge.
"""

CONFIG_SPEC = _TEMPLATE.format(
    fields="\n".join(f"    {line}" for line in describe_fields().splitlines())
)
AGENT_CONFIG_SPEC = (
    CONFIG_SPEC.partition("\nWorkflow for writing/fixing a config:")[
        0
    ].rstrip()
    + "\n"
)
