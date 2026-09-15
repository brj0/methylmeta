# Naming Conventions for `tumor_types.yaml`

Purpose: keep acronyms short and instantly recognizable to a pathologist at
the bench, while `who_volume` / `site` / `lineage_*` / `families` /
`parent` carry the anatomic and taxonomic detail. The acronym's only jobs
are **recognizability** and **uniqueness** — it does not need to encode
anatomy on its own, because `site` already does that. Where it *should*
encode anatomy is a biology question, not a style question — see Rule 3.

---

## 1. Preserve literature-established acronyms verbatim

If an entity already has an acronym pathologists say out loud — `IMT`,
`GIST`, `DFSP`, `MPNST`, `SFT`, `EWS`, `RMS`, `ALCL`, `DLBCL`, `HNSCC`,
`NSCLC`, `PEC` (PEComa) — use it as-is. Never decompose or "systematize"
a code that is already canonical, even if it breaks the grammar or
directionality below. This rule outranks Rules 2–6.

Reserve this for acronyms that are genuinely spoken in clinic and
pathology reports. A string that merely *looks* like a fused acronym
(e.g. an ad hoc `XYSCC` built by concatenating a site abbreviation with
`SCC`) is not automatically exempt — if it isn't something a pathologist
already says out loud, it follows the constructed-code rules below
instead.

## 2. Grammar for constructed codes (when no natural acronym exists)

```
CORE_ENTITY [ _BEHAVIOR ] [ _SITE ] [ _MOLECULAR_SUBTYPE ]
```

Examples: `LU_ADCA`, `ESO_SCC`, `RCC_CC`, `CSA_IDH_MUT`, `RCC_TFE3`,
`MEL_SS`.

- Qualifiers get more specific left → right: behavior, then organ/site
  (if not already the core entity — see Rule 3), then molecular subtype.
- This mirrors how established DKFZ/Heidelberg-style methylation
  classifiers name their classes (`GBM_RTK_I`, `MB_WNT`, `PXA`, …).
- What changes per entity family is **which axis fills `CORE_ENTITY`**
  — organ or histotype. That choice is Rule 3, and it is a biology
  question, not a preference.

## 3. Choosing the CORE_ENTITY: organ vs. histotype

The `CORE_ENTITY` slot goes to whichever axis actually predicts the
methylation cluster. Pan-cancer methylation data resolves this question
for most of the file: across TCGA, methylation clustering (like most
other -omics layers) is dominated by cell-of-origin / tissue of
origin, and that effect persists even after excluding CpG sites with
known baseline tissue-specific methylation. So the *default* is
**organ-first**, and entity-first is the exception — reserved for
histotypes with their own documented cross-organ histogenetic program.

**Default: organ is the CORE_ENTITY.** This applies whenever the
behavior suffix describes a growth pattern that many organs can
independently produce, rather than a specific lineage:

- `_ADCA` — adenocarcinoma is the default epithelial malignancy of
  almost every glandular/visceral organ; a lung adenocarcinoma and an
  esophageal adenocarcinoma share very little at the methylation level.
- `_SCC` — squamous cell carcinoma is the default epithelial malignancy
  of any squamous-lined or squamatized organ. Where SCC does split into
  molecularly distinct subgroups, it's overwhelmingly along **HPV
  status**, not organ-agnostic "squamousness" — so HPV status is
  captured as a suffix under the organ (`_HPV` / `_HPVI` / `_NOS`), not
  by decoupling `SCC` from its organ.
- `_CA` generically, when no more specific behavior suffix applies.

  Examples: `LU_ADCA`, `GAST_ADCA`, `ESO_SCC`, `LAR_SCC`, `SKIN_SCC`,
  `CERV_SCC_HPV`.

**Exception: histotype is the CORE_ENTITY** for the small set of
entities with a documented cross-organ histogenetic program — currently
**melanoma** (`MEL_*`) only. Melanocytes carry a strong lineage-intrinsic
methylation program wherever they sit, so cutaneous / acral / mucosal /
desmoplastic melanoma cluster substantially by that program rather than
by site, and the acronym should reflect that. Don't extend this
exception to a new entity family without comparable evidence — the
default is organ-first.

  Examples: `MEL_SS`, `MEL_ACR`, `MEL_MUC`, `MEL_DESMO` (site lives in
  `site:`, not the acronym).

**Exception — the organ is baked into the canonical name itself**
(`RCC`, `HCC`, `NSCLC`). Don't re-decompose these into `KIDNEY_CA` etc.
— the bare acronym already *is* the organ-specific entity.

**Exception — literature-canonical acronyms win regardless of
direction** (Rule 1 always applies first): `HNSCC`, `GIST`, `DFSP`, etc.
are never reordered or decomposed to fit the grammar above.

**Organ chapters** (all `LU_*`, all `BR_*`, … grouped together for
browsing) are now simply the natural result of the organ-first default
for `_ADCA` / `_SCC` / `_CA` — not a separate carve-out layered on top
of an entity-first default.

## 4. Only add a site/organ qualifier to an entity-first stem when it's load-bearing

This applies to the entity-first exception (currently: melanoma) and to
any other histotype-first stem. Add a site qualifier **only if the
classifier distinguishes ≥2 separate methylation classes of the same
base entity.** If a tumor occurs at many sites but you only ever have
one class for it, keep the bare acronym (e.g. `LM` for leiomyoma,
`IMT`) and let `site: Multiple` (or similar) carry the anatomy.
Organ-first entries don't need this rule — the organ is already the
first token by construction.

## 5. Fixed suffix vocabulary for tumor behavior

Use this small, closed set — don't improvise new abbreviations per
entry:

| Suffix     | Meaning          |
|------------|------------------|
| `_A`       | adenoma          |
| `_CA`      | carcinoma        |
| `_ADCA`    | adenocarcinoma (only where distinguishing from plain carcinoma matters — otherwise fold into `_CA`) |
| `_SCC`     | squamous cell carcinoma (organ-first per Rule 3, e.g. `LAR_SCC`; not needed on stems where SCC is already baked into a literature acronym, e.g. `HNSCC`) |
| `_SARC`    | sarcoma          |
| `_BL`      | blastoma         |
| `_ADSARC`  | adenosarcoma     |

Don't add `_CA` to a stem that already means carcinoma on its own
(`RCC`, `SCC`, `BCC`, `HCC` are already carcinomas — no `SCC_CA`). This
is about the bare stem, not the `_SCC` suffix used on an organ-first
entity (`LAR_SCC` is fine; `LAR_SCC_CA` would not be).

## 6. Suffix direction must be consistent within a CORE_ENTITY choice

Once Rule 3 has decided whether an entity family is organ-first or
entity-first, every member of that family follows the same direction.
Don't mix both directions for the same behavior word.

- All `_ADCA` and `_SCC` entries are organ-first: fix `ADCA_EAR` →
  `EAR_ADCA` and `ADCA_RETE` → `RETE_ADCA` so they match `ESO_ADCA`,
  `GAST_ADCA`, `LU_*_ADCA`, rather than the reverse.
- All `MEL_*` entries stay histotype-first, as they already are.

## 7. Length and character set

- Try to create short acronyms. Cap constructed codes at  **12–15 characters**.
- ALL CAPS, underscore-delimited only.
- No slashes, colons, or parentheses in codes (these have also caused
  actual YAML parse failures inside `name:` fields — quote any `name`
  value that contains `:` or other YAML-special characters).

## 8. `parent:` is the disambiguation link — use it every time a split exists

Whenever a base entity is split by site or molecular subtype, the more
specific code must set `parent:` back to the base code (or to the next
level up), e.g. `RMS_ALV` → parent `RMS`, `CSA_IDH_HR` → parent
`CSA_IDH_MUT` → parent `CSA`. This applies equally to organ-first splits,
e.g. `CERV_SCC_HPV` → parent `CERV_SCC` → parent `SCC`. Don't skip this
— it's what lets tooling reconstruct the hierarchy even though the
acronym itself stays short. If later classifier data shows an
organ-first entry actually clusters with a same-behavior entry from a
different organ (e.g. lung SCC turning out to cluster with SCC from
another site rather than with lung ADCA), re-point `parent:` — the
acronym itself does not need to change.

## 9. Populate `who_volume` / `site` rather than leaving them `null`

Since the acronym no longer needs to carry anatomy on its own, `site`
and `who_volume` have to actually be filled in for that trade-off to
pay off. Audit and backfill `null` values where the source WHO volume
is known.

## 10. Normalize spelling in `name:` fields

Entries currently mix British (haemangioma, tumour, naevus,
oesophagus) and American (hemangioma, tumor, nevus, esophagus)
spelling depending on which WHO volume they were sourced from. Pick
one standard — American is recommended, since it's already the
majority in the file — and normalize all `name:` fields to match.
This also makes future name-matching/deduplication far less error
-prone.

## 11. Audit for duplicate keys

YAML silently lets a later key overwrite an earlier one with the same
name. The file currently has at least one duplicate (`SCLC:` appears
twice — once generic with `who_volume: null`, once
`Thoracic Tumours`-specific — and the generic entry is currently
unreachable). Run a duplicate-key check as part of any cleanup pass.

---

## Quick checklist for adding a new entry

1. Does a natural/literature acronym exist that pathologists actually
   say out loud? → use it, stop here (Rule 1).
2. Otherwise, decide `CORE_ENTITY`: organ, unless the histotype has a
   documented cross-organ program (currently: melanoma only) or the
   organ is already baked into the canonical name (Rule 3).
3. Build `CORE_ENTITY_BEHAVIOR_SITE_SUBTYPE` (Rule 2), matching the
   direction every other member of that entity family already uses
   (Rule 6).
4. Only add an extra site qualifier on top of an entity-first stem if
   it actually creates a second methylation class (Rule 4).
5. Use the fixed behavior-suffix table (Rule 5).
6. Keep it ≤ ~15 chars, caps, underscores only (Rule 7).
7. Set `parent:` if this entry is a split of a broader entity (Rule 8).
8. Fill `who_volume` and `site` (Rule 9).
9. Use American spelling in `name:`, quote if it contains `:` etc.
   (Rules 10, 7).
