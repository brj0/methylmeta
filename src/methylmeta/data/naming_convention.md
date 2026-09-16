# Naming Convention for `tumor_types.yaml`

**Audience note:** this document is an operating procedure for an AI
agent applying it across the file, with changes reviewed via git diff
afterward — not a human re-checking every entry live. So: don't stall on
ambiguity. Make the best call the available evidence supports, and where
a call is genuinely non-obvious, leave a one-line YAML comment next to
the entry explaining the reasoning, so the reviewer can spot and
second-guess it in the diff. That comment is the review mechanism — no
separate flagging field, no synonym-tracking field, no escalation step.

---

## 0. Governing principle

The unit this file is organized around is the **methylation class**, not
the WHO diagnostic entity. The two are related but not 1:1 — one
methylation class can span several WHO diagnoses, and one WHO diagnosis
can split into several methylation classes. Concretely:

- The **code** (YAML key) identifies a methylation class.
- `name`, `who_volume`, `site` describe the WHO/anatomic identity.
- `parent` links a code to the broader entity it belongs under.

The acronym's only jobs are recognizability and uniqueness. Anatomy and
taxonomy are `site:` and `parent:`'s job, not the acronym's.

---

## 1. Recognizability principle

A good acronym is one a pathologist reading it cold — no lookup table —
correctly guesses the entity behind. This matters as much as uniqueness,
and it's the tiebreaker whenever a naming choice has more than one
technically-valid option:

- Prefer letter groups that echo how the word is actually said or
  abbreviated in practice (`ADCA` reads as "adenocarcinoma"; `SCC` reads
  as "squamous cell carcinoma") over arbitrary truncations that are
  unique but don't evoke the word (a mechanical first-N-letters grab
  that happens not to collide with anything).
- This is explicitly *not* "make it longer to be safer" — a longer code
  that's still opaque doesn't help, and length has its own cost
  (Rule 8). The goal is a better-chosen short string, not a longer one.
- When two equally short candidates describe the same entity, pick the
  one closer to how it's actually pronounced or written shorthand in a
  pathology report, not the one that's alphabetically first or easiest
  to derive mechanically.

---

## 2. Decision procedure

```
STEP 1 — Literature-atomic check (Rule 1)
  Is this a token pathologists already say out loud as a single word,
  independent of any organ/behavior grammar — e.g. "GIST", "DFSP" — not
  just a code that happens to look fused?
    YES → use it verbatim, unmodified. STOP.
    NO  → continue.

STEP 2 — Choose CORE_ENTITY axis (Rule 3)
  Is the organ already baked into an existing canonical short name
  (RCC, HCC, NSCLC)? → use that bare name, don't decompose further,
  skip to STEP 5.
  Is this histotype in the entity-first exception list (Rule 3)?
    YES → CORE_ENTITY = histotype stem (e.g. MEL, ADCC).
    NO  → CORE_ENTITY = organ/site stem (default).

STEP 3 — Append BEHAVIOR suffix (Rule 5)
  Use the closed vocabulary. If nothing fits well, extend the table
  (add a row, with a one-line justification) rather than inventing a
  one-off abbreviation elsewhere in the file.

STEP 4 — Append SITE/SUBTYPE qualifier, if the entry has one (Rule 4)
  Qualifiers get more specific left → right, and the entry gets a
  parent: pointing at the code it sits under (Rule 9).

STEP 5 — Any remaining subtype discriminator?
  Arabic numerals (Rule 7).

STEP 6 — Validate
  Length and charset (Rule 8), direction consistency within the family
  (Rule 6), uniqueness against the rest of the file (Rule 13).

STEP 7 — Populate fields (Rules 10-12)
  name (verbatim WHO wording), who_volume (best-suited, not just
  first-sourced), site, lineage_broad, lineage_detail, families,
  parent.
```

---

## 3. Rule 1 — Preserve literature-established acronyms verbatim

If an entity already has an acronym pathologists say out loud as one
word — `IMT`, `GIST`, `DFSP`, `MPNST`, `SFT`, `EWS`, `RMS`, `ALCL`,
`DLBCL`, `HNSCC`, `NSCLC`, `PEC` (PEComa) — it is used as-is. **Never**
decompose or "systematize" a code that is already canonical, even if it
breaks the grammar or direction rules below. This rule outranks
everything else in this document — it's the one true hard override.

The test is spoken atomicity, not surface resemblance. A string that
merely *looks* like a fused acronym (an ad hoc `XYSCC` built by
concatenating a site abbreviation with `SCC`) is not exempt just because
it's short — if it isn't something already said as one word independent
of any grammar being constructed here, it follows the constructed-code
rules instead. This includes an external classifier's own compositional
subtype label (e.g. `GBM_RTK_I/II/III`) — that's built from this file's
own organ-behavior-subtype grammar with someone else's numeral style,
not a protected atomic acronym (see Rule 7 on numerals).

---

## 4. Rule 2 — Grammar for constructed codes

```
CORE_ENTITY [ _BEHAVIOR ] [ _SITE ] [ _SUBTYPE ]
```

Examples: `LU_ADCA`, `ESO_SCC`, `RCC_CC`, `CSA_IDH_MUT`, `RCC_TFE3`.
Qualifiers get more specific left → right.

---

## 5. Rule 3 — CORE_ENTITY choice

**Default: organ is the CORE_ENTITY.** For most entity families,
methylation clustering tracks cell-of-origin / tissue of origin more
strongly than any lineage program, so organ-first applies whenever the
behavior suffix describes a growth pattern many organs can
independently produce (`_ADCA`, `_SCC`, `_CA`). Examples: `LU_ADCA`,
`GAST_ADCA`, `ESO_SCC`, `LAR_SCC`, `CERV_SCC_HPV`.

**Some families cluster by lineage instead.** For a smaller set of
histotypes, the lineage-intrinsic methylation program dominates the
site signal, and members of that family cluster together across organs
rather than by where they arose. For those families, the CORE_ENTITY is
the histotype stem, not the organ — e.g. `MEL_SS` / `MEL_ACR` /
`MEL_DESMO`, not `SKIN_MEL` / `ACRAL_MEL` / `SKIN_DESMO_MEL`.

**How to tell which applies.** The question is empirical, not
stylistic: *does the data put this family's members in one cross-organ
class, or does it split them by site?* If a documented clustering
result (or a published reference) shows a single lineage-anchored class
across organs, use the histotype stem. If it splits by site — or the
evidence is unclear — stay organ-first. The bar for switching to
histotype-first is a real basis (a citation, a release note, a
documented clustering result), not "it feels like melanoma."

**Not a closed list.** The families currently known to be
lineage-anchored include melanocytic, salivary-gland-type, vascular,
peripheral nerve sheath, skeletal muscle, Ewing-family, chondrogenic,
osteogenic, adipocytic, and smooth-muscle tumours — but this is a
snapshot, not a whitelist. When a new family is shown to be
lineage-anchored, add it; when a family turns out to split by site,
move it back to organ-first. Because the axis choice lives in the
acronym and the hierarchy lives in `parent:`, a re-clustering that
flips a family's axis is a rename, not a redesign — the comment
convention (Rule 0) is what keeps that call reviewable.

**Always exempt.** Organ-baked-into-canonical-name entities (`RCC`,
`HCC`, `NSCLC` — not decomposed into `KIDNEY_CA`) and Rule 1 acronyms
(`GIST`, `IMT`, `DFSP`, `HNSCC`, …) are unaffected by this rule.

---

## 6. Rule 4 — Naming a subtype or site variant

Where the file distinguishes a variant of a broader entity, the variant
code is the base code plus a qualifier, per the Rule 2 grammar, with
`parent:` pointing back at the base (Rule 9) — e.g. `RMS_ALV` under
`RMS`, `CERV_SCC_HPV` under `CERV_SCC`.

Where one code covers several WHO diagnoses or several anatomic
contexts, the code stays as it is and `site:` names the lineage the code
is defined by rather than every location it can turn up in. A one-line
inline comment records what's folded in, if it's worth preserving.

---

## 7. Rule 5 — Suffix vocabulary

Prefer this vocabulary; extend it with a new row (plus a one-line
reason) when a genuinely recurring behavior isn't covered, rather than
inventing an inconsistent one-off elsewhere.

| Suffix        | Meaning                                         |
| ------------- | ----------------------------------------------- |
| `_AD`         | adenoma                                         |
| `_CA`         | carcinoma                                       |
| `_ADCA`       | adenocarcinoma                                  |
| `_SCC`        | squamous cell carcinoma                         |
| `_ASC`        | adenosquamous carcinoma                         |
| `_SARC`       | sarcoma                                         |
| `_BL`         | blastoma                                        |
| `_ADSARC`     | adenosarcoma                                    |
| `_NET`        | neuroendocrine tumor, well-differentiated       |
| `_NEC`        | neuroendocrine carcinoma, poorly differentiated |
| `_CYSTAD`     | cystadenoma                                     |
| `_CYSTADCA`   | cystadenocarcinoma                              |
| `_PAP`        | papilloma / papillary                           |
| `_HG` / `_LG` | high-grade / low-grade                          |

Notes on three of these:

- `_ADCA` only where distinguishing adenocarcinoma from plain carcinoma
  matters; otherwise it folds into `_CA`.
- `_SCC` is used organ-first, e.g. `LAR_SCC`.
- `_HG` / `_LG` only where grade is the actual discriminator.

A suffix carries enough letters to be parsed on sight.  It also stays
short enough to keep composite codes within the length target:
`OVA_CYSTADCA` (12 chars) rather than `OVA_CYSTADENOCA` (15) — both
read the same to a pathologist.

`_CA` is not added to a stem that already means carcinoma on its own (no
`RCC_CA`, `SCC_CA`).

---

## 8. Rule 6 — Direction consistency within a family

Every member of an entity family sits on the same CORE_ENTITY axis
(Rule 3). Mixing directions within one family defeats the point of
choosing an axis at all: alongside `ESO_ADCA` and `GAST_ADCA`, the ear
entry is `EAR_ADCA`, not `ADCA_EAR`.

---

## 9. Rule 7 — Numerals: Arabic

Prefer Arabic numerals for methylation subtype discriminators — `RTK1`,
`RTK2`, `RTK3`, giving `GBM_RTK1` / `GBM_RTK2` / `GBM_RTK3` — including
where the underlying subtype concept comes from a classifier that writes
Roman numerals (DKFZ's `GBM_RTK_I/II/III`). Arabic numerals are shorter,
sort and grep correctly, and avoid `I`/`l`/`1` confusion in small plot
labels. Rule 1 doesn't protect the Roman numerals here — see Rule 1's
note on compositional vs. atomic acronyms.

Not every trailing capital is a numeral, and the ones that aren't are
spelled out rather than numbered: `HCL_VAR` is "hairy cell leukemia,
**variant**," not "class 5."

---

## 10. Rule 8 — Length and character set

- Constructed codes: **3–14 characters**, target ≤ 12. The floor exists
  because very short codes (`MM`, `SS`, `MF`) are frequently ambiguous
  even to a specialist without context; the cap is for legibility in
  confusion-matrix plot labels at normal font size.
- Rule 1 acronyms are exempt from both bounds.
- Character set: `[A-Z0-9_]` only, first character must be `A-Z` (not a
  digit or underscore). Regex: `^[A-Z][A-Z0-9_]{2,13}$` for constructed
  codes.
- Quote any `name:` value containing `:` or other YAML-special
  characters (has caused real parse failures).

---

## 11. Rule 9 — `parent:` links a code to the one above it

`parent:` points at the base code, or the next level up: `RMS_ALV` →
`RMS`; `CSA_IDH_HR` → `CSA_IDH_MUT` → `CSA`; `CERV_SCC_HPV` →
`CERV_SCC` → `SCC`. This is what lets tooling reconstruct the hierarchy
even though the code stays short.

Because the hierarchy lives in `parent:` and not in the acronym, a code
whose clustering turns out to sit elsewhere gets a new `parent:` value;
the code itself stays as it is.

---

## 12. Rule 10 — Required fields

- `who_volume`, `site`, `lineage_broad`, `lineage_detail` (where
  determinable), `families` — populate, don't leave `null`, wherever the
  source is known.
- `parent`, wherever the entry sits under a broader code.

---

## 13. Rule 11 — `name:` mirrors the WHO source verbatim

`name:` is the exact WHO name for the entity — spelling included.
WHO/IARC volumes are written in British English, so most `name:` values
will legitimately read `haemangioma`, `tumour`, `naevus`, `oesophagus`,
etc.; these are not normalized to American spelling. The point of
`name:` is traceability back to the source classification, and silently
rewriting spelling breaks that. (Constructed acronyms and everything
else in this file can still be whatever's most useful — this rule is
specifically about the `name:` field's fidelity to its WHO source.)

---

## 14. Rule 12 — `who_volume:` is the best-suited source

`who_volume` points to whichever WHO volume is currently the most
specific and applicable source for this entity — not necessarily the
volume it happened to be originally sourced from. E.g., if an entity was
first captured from a general or pediatric-tumours volume but a newer,
more specific volume (say, a current Soft Tissue and Bone Tumours
edition) now covers it more precisely, `who_volume` points there
instead. When multiple volumes plausibly apply, pick the one a
pathologist would actually reach for to look this entity up.

---

## 15. Rule 13 — Validation before merging any change

These are mechanical, not judgment calls — run them, don't eyeball them:

1. **Duplicate-key check** — use a YAML loader that errors on repeated
   keys; the default permissive loader silently lets a later key win.
2. **Code pattern check** — every code matches
   `^[A-Z][A-Z0-9_]{2,13}$`, unless it's a Rule 1 exemption.
3. **Direction check** — no family has both an organ-first and
   entity-first member (Rule 6).
4. **Orphan-parent check** — every `parent:` value resolves to an
   existing code.

---

## Quick reference

1. Atomic literature acronym? → verbatim, stop. *(Rule 1)*
2. CORE_ENTITY: organ by default; histotype only per the exception
   table; bare canonical name if organ's already baked in. *(Rules 2-3)*
3. Closed-vocabulary behavior suffix, extend the table if genuinely
   needed. *(Rule 5)*
4. Site/subtype qualifier appended per the grammar, with `parent:`
   pointing one level up. *(Rules 4, 9)*
5. Arabic numerals for methylation subtypes — `GBM_RTK1`. *(Rule 7)*
6. Validate length/charset/direction/uniqueness. *(Rules 6, 8, 13)*
7. Fill `name` (verbatim WHO wording/spelling), best-suited
   `who_volume`, `site`, lineage fields, `families`, `parent`.
   *(Rules 10-12)*
