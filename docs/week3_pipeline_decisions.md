# Week 3 — V1 Data Pipeline Decisions

- **Project:** Mechanical Engineering Knowledge Assistant
- **Course:** SAIA 3113 AI Engineering
- **Selected data pathway:** Pathway A — PDF/TXT (PDF documents only)
**Notebook:** `notebooks/week3_pipeline.ipynb`

## 1. Project Requirements and Traceability

The pipeline prepares approved technical documents for a future retrieval-augmented chatbot. It does not implement retrieval, answer generation, or model evaluation in Week 3.

| Topic 2 ID | Requirement | Week 3 connection |
|---|---|---|
| FR1 | Answer conceptual maintenance questions using approved documents. | Extract and prepare mechanical-science reference content for later retrieval. |
| FR2 | Retrieve relevant supporting passages. | Store text in JSONL chunks with explicit source filenames. |
| FR3 | Cite document title and page/section. | Source filenames are retained; **PDF page numbers are not yet preserved** and must be addressed in a later iteration. |
| RAI1 | Provide accurate, source-supported citations. | Preserve source identifiers and SHA-256 fingerprints for provenance; citation quality is not yet tested. |
| RAI4 | Use authorised reference materials. | Use selected, publicly distributed DOE PDFs; record the distribution statement and review sharing permissions before publication. |
| NFR2 | Reach Recall@3 of at least 85% in later evaluation. | Prepare a consistent chunk dataset for subsequent retrieval evaluation; the target has **not** been measured in this lab. |

## 2. Selected Sources and Inspection

| ID | Document | Inspection evidence |
|---|---|---|
| S01 | `data/raw/mechanical_science_vol1.pdf` — DOE-HDBK-1018/1-93, *Mechanical Science*, Volume 1 (1993) | 122 pages; 169,246 extracted characters; readable technical text about diesel engines and related equipment. |
| S02 | `data/raw/mechanical_science_vol2.pdf` — DOE-HDBK-1018/2-93, *Mechanical Science*, Volume 2 (1993) | 130 pages; 192,232 extracted characters; readable technical text about valves and related mechanical systems. |

Both source documents contain **Distribution Statement A: Approved for public release; distribution is unlimited**. This provides evidence of public distribution, but does not by itself establish that all possible reuse rights or downstream redistribution conditions have been checked. The sources are older fundamentals handbooks, not current operating procedures.

## 3. Part B — Preparation Comparison and Decision

**Preparation steps:** Extract PDF text with `pypdf`, join extracted pages, normalize repeated spaces/tabs, and split the cleaned text into character-bounded chunks.

| Source | Fixed-size chunks (500 chars) | Paragraph-aware chunks (500 chars) |
|---|---:|---:|
| Volume 1 | 334 | 341 |
| Volume 2 | 380 | 385 |
| **Total** | **714** | **726** |

A comparison using technical content from PDF page 30 found **four chunks with each method for each PDF**. In both samples, the compared chunk boundaries were identical; examples split phrases such as "head casting / of the engine" and "not used to / regulate or throttle flow". The earlier keyword-based samples also included table-of-contents material.

**Chosen configuration:** `method="paragraph-aware"`, `chunk_size=500`, producing `paragraph-aware-char-500` records. This option was retained for consistency with the prepared output. The sampled comparison did **not** establish a clear quality advantage over fixed-size chunking. The implementation falls back to fixed-size slicing when a paragraph exceeds 500 characters.

**Part B output:** `data/processed/prepared_text.jsonl` — **726 records**, **537,464 bytes**. Each record stores `record_id`, `text`, `source`, `source_sha256`, `processing`, and `page`.

## 4. Executed V1 Pipeline and Stage Contracts

**Workflow:** Source → Ingest → Inspect → Prepare / Transform → Store → Validate Output → Record Lineage.

| Stage | Input / operation / evidence | Failure response or limitation |
|---|---|---|
| Ingest | Select the `data/raw/` folder; collect PDF/TXT files. Executed on two PDFs. | Missing folder triggers `FileNotFoundError`; no valid files triggers `ValueError`. The code does not independently enforce the exact two-file inventory. |
| Inspect | Read each PDF with `PdfReader`; record page counts and extracted character counts; reject documents without readable text. | Raise `ValueError` for an empty/non-extractable document; unsupported/corrupt PDF errors interrupt execution. |
| Prepare / Transform | Normalize spaces/tabs; apply the selected 500-character paragraph-aware chunking; retain source-specific IDs and hashes. | Raise an error for empty cleaned text or invalid method; some sentences may still be split across chunks. |
| Store | Write the combined dataset to `data/pipeline_v1/documents/prepared_text.jsonl`. | Write failures interrupt execution. |
| Validate | Require output files to exist and be non-empty; store output SHA-256, bytes, and output count. Compare Part C output SHA-256 against Part B. | Raise an error for missing/empty outputs or for a mismatch with Part B. A matching hash is not proof of semantic accuracy. |
| Record lineage | Save source file paths/hashes, output path/hash, processing configuration, inspections, mappings and execution timestamp. | Manifest-writing errors interrupt execution; mapping completeness is recorded but not explicitly asserted by the provided pipeline code. |

Two failure cases shown on the pipeline diagram are **missing source folder** (stop with `FileNotFoundError`) and **empty prepared output** (stop with `ValueError`).

## 5. Engineering Decisions

**ETL rather than ELT:** The workflow extracts PDF text, transforms it into cleaned chunks, and then loads the prepared records into a JSONL file. No data warehouse is involved.

**Batch rather than streaming:** Reference PDFs are finite documents updated infrequently. Running the pipeline on demand is simpler than maintaining a continuous ingestion stream. Updates can be handled by rerunning the notebook with reviewed source files.

**Single combined JSONL output:** Both PDFs feed one document dataset, while per-record source metadata and separate manifest source-to-output mappings preserve basic traceability. The output count of one is expected for the two inputs.

**No embeddings or vector database:** These belong to later project stages and are not required for the Topic 3 data-engineering workflow.

## 6. Validation, Repeatability and Accepted Limitations

- **Part B:** `data/week3_manifest.json` contains two lineage entries. Verification passed for the existence and matching SHA-256 checksums of the registered sources and prepared output.
- **Part C:** Pipeline output matches the Part B JSONL file by SHA-256. Console evidence: `SUCCESS: documents | Inputs: 2 | Outputs: 1` and `Total chunks: 726`.
- **Repeatability:** Cell 9 reran the document pipeline and reported matching source fingerprints, prepared-output fingerprints, file sizes, output counts, and source-to-output mappings. Execution timestamps are expected to differ.
- **Accepted limitation — page references:** Because pages are concatenated before splitting, output records contain `"page": null`. FR3 cannot be fully supported until chunk-level page/section provenance is implemented.
- **Accepted limitation — text boundaries:** The selected method can split sentences when extracted PDF content lacks paragraph separation; no chunk-quality or retrieval benchmark was completed.
- **Accepted limitation — access metadata:** The manifests currently retain placeholder source-version/access-rights fields. These should be replaced with verified document metadata before public sharing.
- **Accepted limitation — source age:** The 1993 handbooks support general mechanical concepts but must not be treated as authoritative current maintenance procedures or safety instructions.

The repeatability check is a **smoke test**, not full reproducibility across machines or a complete data-quality assessment. Retrieval evaluation and Responsible AI assessment remain future work.

## 7. Files and Evidence

| Deliverable | Location |
|---|---|
| Executable notebook | `notebooks/week3_pipeline.ipynb` |
| Data inventory | `docs/week3_data_inventory.md` |
| Pipeline diagram | `docs/week3_pipeline_diagram.png` |
| Pipeline decisions | `docs/week3_pipeline_decisions.md` |
| Part B prepared data | `data/processed/prepared_text.jsonl` |
| Part B lineage manifest | `data/week3_manifest.json` |
| Part C prepared data | `data/pipeline_v1/documents/prepared_text.jsonl` |
| Part C execution manifest | `data/pipeline_v1/documents/pipeline_manifest.json` |

**Next checkpoint:** Save and review the notebook, diagram, manifests, prepared data and README; commit only approved non-sensitive artefacts to the existing project repository at the final submission stage.
