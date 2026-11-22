# Document Source Register and Provenance

**Project:** Mechanical Engineering Knowledge Assistant (formerly scoped as
Industrial Knowledge Assistance Chatbot)
**Course:** SAIA 3113 — AI Engineering
**Status:** Source metadata for the completed Week 3 PDF pipeline; not a record
of new pipeline execution.

## 1. Actual Week 3 Sources (selected and processed)

| ID | Official source | Edition / publisher | Local raw filename | Pages processed | Access |
|---|---|---|---|---:|---|
| S01 | [DOE Mechanical Science, Volume 1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL1.pdf) | DOE-HDBK-1018/1-93, January 1993; U.S. Department of Energy | `data/raw/mechanical_science_vol1.pdf` | 122 | Distribution Statement A |
| S02 | [DOE Mechanical Science, Volume 2](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL2.pdf) | DOE-HDBK-1018/2-93, January 1993; U.S. Department of Energy | `data/raw/mechanical_science_vol2.pdf` | 130 | Distribution Statement A |

**Distribution Statement A:** Approved for public release; distribution is
unlimited. The official DOE PDF links were checked as document sources. This
register does **not** establish that the exact bytes formerly processed in
Week 3 are identical to any later downloads.

### Original Week 3 source fingerprints

| ID | Local filename | SHA-256 saved in the historical execution manifest |
|---|---|---|
| S01 | `mechanical_science_vol1.pdf` | `c1e37601164acf95cbaecad93b1db9841ad8d7670bf30a4fdd6ff0a87c6a0070` |
| S02 | `mechanical_science_vol2.pdf` | `f569f8de24e0c9b23fa8f5c965c3d0740daa5e41db0f029ad8e3893d3fd9e2fd` |

These values come from the executed Week 3 manifests, not from newly downloaded
files. To verify a local source, run `Get-FileHash` in PowerShell, or run
`python apply_traceability.py --verify-raw` from the repository root.

## 2. Source-to-output traceability

| Input | Preparation | Derived output / evidence | Status |
|---|---|---|---|
| S01 + S02 | PDF extraction (`pypdf`), whitespace normalization, paragraph-aware 500-character chunks | [`data/processed/prepared_text.jsonl`](../data/processed/prepared_text.jsonl) — [Part B lineage manifest](../data/week3_manifest.json) | Executed in Week 3 |
| S01 + S02 | Batch V1 document ETL | [`data/pipeline_v1/documents/prepared_text.jsonl`](../data/pipeline_v1/documents/prepared_text.jsonl) — [Part C pipeline manifest](../data/pipeline_v1/documents/pipeline_manifest.json) | Executed and repeatability smoke-tested in Week 3 |

The recorded totals are **2 PDFs, 252 pages, and 726 output chunks**. These are
prior Week 3 observations; adding links does not constitute a new run or
revalidation. The exported chunks still have `page: null`, so full
page-level citation traceability is **not yet achieved**.

The historical manifests have some `source_version` / `access_rights`
placeholders. This document supplies supplemental source information but
**does not retroactively alter the historical execution records**. A future
pipeline version should populate URLs, document IDs, and verified rights fields
within generated manifests, and preserve chunk-level page references.

## 3. Proposed sources in Topics 1–2 (not used in Week 3)

| Original proposal | Official PDF |
|---|---|
| FIST 2-12 — Mechanical Maintenance of Hydroelectric and Large Pump Units (2024) | [U.S. Bureau of Reclamation PDF](https://www.usbr.gov/power/data/fist/FIST_2-12_%285-2024%29.pdf) |
| FIST 2-1 — Alignment of Rotating Machinery (2024) | [U.S. Bureau of Reclamation PDF](https://www.usbr.gov/power/data/fist/FIST_2-1_%285-2024%29.pdf) |
| FIST 2-4 — Lubrication of Equipment (2024) | [U.S. Bureau of Reclamation PDF](https://www.usbr.gov/power/data/fist/FIST_2-4_%285-2024%29.pdf) |

These documents informed the original project scope but were **not** inputs to
the executed Week 3 pipeline. Keep this distinction when discussing source
selection and evaluation. The implemented data collection concerns DOE
mechanical-science fundamentals; original planned alignment/lubrication coverage
must not be assumed without checking the corpus.

## 4. Linked engineering evidence

- [Week 1 project scope](week1_project_scope.md): original problem and proposed FIST documents.
- [Week 2 requirements](week2_requirements.md): intended functions, quality and RAI constraints.
- [Week 2 evaluation criteria](week2_evaluation_criteria.md): proposed tests; **not results**.
- [Week 3 data inventory](week3_data_inventory.md): actual sources and inspection evidence.
- [Week 3 pipeline decisions](week3_pipeline_decisions.md): preparation method, trade-offs, counts and limitations.
- [Week 3 pipeline notebook](../notebooks/week3_pipeline.ipynb): executed lab notebook.
- [Raw data directory documentation](../data/raw/README.md): instructions for restoring PDFs locally.

**Important:** Links to the source PDF establish document identity and public
location, not the correctness of every extracted chunk or future generated
answer. Full source-page provenance and retrieval evaluations remain future work.
