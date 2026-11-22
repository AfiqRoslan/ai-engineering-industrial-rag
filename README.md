# Mechanical Engineering Knowledge Assistant

A semester project for SAIA 3113 AI Engineering. This project prepares mechanical engineering reference documents for a future Retrieval-Augmented Generation (RAG) knowledge assistant for engineering students and trainee engineers.

## Problem Statement

Industrial maintenance information is often spread across several manuals. Finding a complete explanation may require searching different PDFs and comparing related sections. This project explores whether a Retrieval-Augmented Generation (RAG) chatbot can make the information easier to access while providing references to the original documents.

## Evidence of the Problem

- The [U.S. Bureau of Reclamation's FIST manuals](https://www.usbr.gov/power/data/fist_pub.html) include separate publications on mechanical maintenance, rotating machinery alignment and lubrication.
- [Naqvi et al. (2024)](https://doi.org/10.1016/j.compind.2024.104083) study information retrieval challenges involving technical industrial maintenance text.

These sources support the project direction, but any time-saving benefit over manual PDF search still needs to be tested.

## Initial Related Work / Existing Approaches

1. **PDF manuals and keyword search:** Official [FIST manuals](https://www.usbr.gov/power/data/fist_pub.html) can be searched individually, but some questions require information from more than one document.
2. **Industrial semantic search:** [Naqvi et al. (2024)](https://doi.org/10.1016/j.compind.2024.104083) explore transformer-based retrieval for maintenance records, rather than a chatbot that generates referenced answers from technical manuals.
3. **Retrieval-Augmented Generation:** [Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) introduce an approach that combines retrieval and text generation. This project will apply and evaluate that approach on a small industrial-manual collection.

## Engineering Gap / Limitation

A small document-grounded question-answering application is needed to combine information from the selected industrial manuals and provide verifiable references. The main engineering challenge is ensuring that retrieved passages are relevant and generated answers remain supported by the documents.

## Project Objectives

- **O1:** Design a chatbot that uses selected industrial maintenance manuals as its information source.
- **O2:** Develop a RAG prototype that retrieves relevant sections and answers questions with document references.
- **O3:** Evaluate answer accuracy, retrieval relevance, response time and handling of unsupported questions.

## Target Users

Engineering students and trainee engineers learning about rotating machinery and basic equipment maintenance.

## Proposed Data Sources (Topics 1-2)

- [FIST 2-12 — Mechanical Maintenance of Hydroelectric and Large Pump Units (2024)](https://www.usbr.gov/power/data/fist/FIST_2-12_%285-2024%29.pdf)
- [FIST 2-1 — Alignment of Rotating Machinery (2024)](https://www.usbr.gov/power/data/fist/FIST_2-1_%285-2024%29.pdf)
- [FIST 2-4 — Lubrication of Equipment (2024)](https://www.usbr.gov/power/data/fist/FIST_2-4_%285-2024%29.pdf)

*These manuals are proposed sources. Their internal-use disclaimer and reuse conditions must be reviewed before any document content is processed or published. PDF copies will not be committed to the public repository without permission.*

## Project Scope

The chatbot will support educational questions about the selected manuals. It will not diagnose operating machinery, make maintenance decisions or replace qualified engineers and official safety procedures.

## Week 1 Lab Work

- [Group observation sheet — Claude.ai](docs/week1_observation_sheet.md)
- [Group conceptual system map — Claude.ai](docs/week1_system_map.png)
- [Individual project scope](docs/week1_project_scope.md)

## Week 2 Documentation

- [Requirements Specification](docs/week2_requirements.md)
- [Evaluation Criteria](docs/week2_evaluation_criteria.md)
- [V1 Architecture Diagram](docs/week2_architecture_v1.png)
- [Architecture Decisions and Traceability](docs/week2_architecture_decisions.md)
- [Editable Architecture Diagram](docs/week2_architecture_v1.drawio)

## Week 3 - PDF Data Engineering Pipeline

### Objective

Develop an executable and repeatable pipeline to prepare mechanical engineering documents for future retrieval-based question answering.

### Actual Data Sources

- [DOE Mechanical Science Volume 1 (1993) — 122 pages](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL1.pdf) — DOE-HDBK-1018/1-93 (`mechanical_science_vol1.pdf`)
- [DOE Mechanical Science Volume 2 (1993) — 130 pages](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL2.pdf) — DOE-HDBK-1018/2-93 (`mechanical_science_vol2.pdf`)

These documents carry Distribution Statement A, approving public release with unlimited distribution. The previously proposed FIST manuals were not used for this pipeline.

### Data Storage and Source Traceability

- **Raw inputs (local only):** `data/raw/` — [download instructions and original checksums](data/raw/README.md). The raw PDFs are not tracked in Git.
- **Canonical source register:** [source identity, official PDF URLs, access statements, checksums and lineage](docs/source_register.md).
- **Structured source manifest:** [`data/raw/source_manifest.json`](data/raw/source_manifest.json).
- **Part B prepared data:** [`data/processed/prepared_text.jsonl`](data/processed/prepared_text.jsonl).
- **Part C prepared data:** [`data/pipeline_v1/documents/prepared_text.jsonl`](data/pipeline_v1/documents/prepared_text.jsonl).
- **Historical execution evidence:** [Part B manifest](data/week3_manifest.json) and [Part C manifest](data/pipeline_v1/documents/pipeline_manifest.json).

The executed manifests still contain placeholder version/access fields; the supplemental source register does not modify past run metadata. Source-page citations are not yet supported because output records contain `page: null`.

### Implementation

The pipeline follows:

**Ingest -> Inspect -> Prepare -> Store -> Validate -> Record Lineage**

- Language: Python
- PDF parser: pypdf
- Processing: Whitespace cleaning and paragraph-aware chunking
- Chunk size: 500 characters
- Output format: JSONL
- Integrity verification: SHA-256
- Processing architecture: Batch ETL

### Results

| Metric | Result |
|---|---|
| Input documents | 2 PDFs |
| Total PDF pages | 252 |
| Fixed-size chunks | 714 |
| Paragraph-aware chunks | 726 |
| Selected output records | 726 |
| Part B lineage records | 2 |
| Part B validation | PASS |
| Part C repeatability | PASS |

Both methods can split sentences. The selected paragraph-aware configuration does not preserve PDF page references, so page-level citation support remains future work.

### Week 3 Deliverables

- [Executable notebook](notebooks/week3_pipeline.ipynb)
- [Data inventory](docs/week3_data_inventory.md)
- [Pipeline diagram](docs/week3_pipeline_diagram.png)
- [Editable diagram](docs/week3_pipeline_diagram.drawio)
- [Engineering decisions](docs/week3_pipeline_decisions.md)
- [Part B prepared data](data/processed/prepared_text.jsonl)
- [Part B lineage manifest](data/week3_manifest.json)
- [Part C prepared data](data/pipeline_v1/documents/prepared_text.jsonl)
- [Part C pipeline manifest](data/pipeline_v1/documents/pipeline_manifest.json)

### Limitations

- PDF page numbers are not preserved.
- Chunk boundaries can split technical explanations.
- The 1993 documents are suitable for foundational concepts, not current equipment-specific procedures.
- Retrieval relevance and answer accuracy have not been evaluated.
- Source access metadata requires final review.

### Reproduce / Validate the Topic 3 Outputs

- [Runbook and preserved historical evidence](docs/week3_reproducibility.md): execute the notebook in Google Colab or from the local repository with verified DOE PDFs.
- [Published-data verification script](scripts/verify_week3_artifacts.py): run `py scripts/verify_week3_artifacts.py` (Windows) to verify both JSONL datasets against their recorded 6 November 2026 SHA-256 fingerprints.
- The two raw PDFs are restored from [official-source download instructions](data/raw/README.md) and remain untracked. Notebook installation of `pypdf` is handled in its Pathway A cell.

## Week 4 - Data Quality and Responsible Data Practices

### Objective

Assess the quality, coverage, and responsible use of the prepared Topic 3 dataset before proceeding with retrieval and RAG development.

The assessment focuses on five quality dimensions: completeness, consistency, accuracy, timeliness, and uniqueness. It also examines validation results, potential bias, source provenance, and data governance.

### Audited Dataset

The audit uses the existing Topic 3 Part C output and its corresponding pipeline manifest:

- **Prepared dataset:** [`data/pipeline_v1/documents/prepared_text.jsonl`](data/pipeline_v1/documents/prepared_text.jsonl)
- **Matching manifest:** [`data/pipeline_v1/documents/pipeline_manifest.json`](data/pipeline_v1/documents/pipeline_manifest.json)
- **Data pathway:** A — PDF/TXT
- **Total records:** 726 text chunks
- **Source documents:** 2 DOE Mechanical Science handbooks
- **Inspection sample:** 16 representative chunks, eight from each document

The audit focuses on two Topic 2 functional requirements:

- **FR2:** Retrieve relevant passages from approved documents before generating technical answers.
- **FR3:** Include the source document title and page or section in document-based answers.

### Data Quality Findings

| Quality Dimension | Finding | Assessment |
|---|---|---|
| Completeness | All 726 records contain nonempty text, but structured page/section metadata is missing. | Warning |
| Consistency | Records use the same processing configuration, but some contain broken text boundaries and formatting artifacts. | Warning |
| Accuracy | Source hashes match the historical manifest, but full source-to-chunk fidelity is not verified. | N.V. |
| Timeliness | Both source documents were published in 1993; suitability for current maintenance procedures is unverified. | Warning |
| Uniqueness | All 726 record IDs and exact text values are unique. | Pass |

N.V. means **Not Verified**, indicating that available evidence is insufficient to confirm the result.

### Validation Results

Two validation rules were applied to all 726 prepared records.

| Rule | Requirement | Passed | Failed | Result |
|---|---|---:|---:|---|
| V1 — Text and source validation | FR2 | 726 | 0 | PASS |
| V2 — Structured citation metadata validation | FR3 | 0 | 726 | FAIL |

V1 confirms that all records contain nonempty text and reference one of the two expected source documents.

V2 identifies missing page or section metadata in every record. This prevents the current dataset from reliably supporting the citation requirement defined in FR3.

### Duplicate, Anomaly and Coverage Findings

- **Record uniqueness:** 726 unique record IDs.
- **Exact text duplicates:** 0 duplicate groups.
- **Chunk boundary screening:** 442 of 724 boundaries (61.05%) were flagged as possible word splits. This is a screening result, not a confirmed defect rate.
- **PDF extraction:** 239 of 252 pages returned extracted text. Of the remaining 13 pages, five were visually confirmed blank and eight remain unverified.
- **Pumps:** 148 keyword-matching chunks (129 from Volume 1, 19 from Volume 2).
- **Valves:** 277 keyword-matching chunks (61 from Volume 1, 216 from Volume 2).

Keyword counts indicate topic mentions, not confirmed depth or completeness of technical coverage.

### Bias and Governance Assessment

The audit identified potential representation bias because the dataset consists of only two mechanical-science handbooks published in 1993. Some topics may be more strongly represented than others, while the originally proposed alignment and lubrication coverage remains unverified.

The current chunking process also introduces possible pipeline-induced risks by splitting technical explanations and losing reliable page-level provenance.

Both source documents include Distribution Statement A, allowing public release and unlimited distribution. However, additional intended-use permissions for indexing, redistribution, or external-service processing remain Not Verified.

No complete sensitive-information screening was performed. Source verification, responsible storage, and permission reviews remain necessary before further use.

### Quality-Gate Decision

**HOLD — For downstream citation-based RAG integration.**

The dataset passed structural validation but failed structured citation-metadata validation for all 726 records. Chunk-boundary issues and unresolved governance checks also require attention.

The HOLD decision does not invalidate the completed Topic 3 pipeline. The existing dataset remains the verified baseline for controlled improvements and future comparison.

### Outstanding Actions

1. **Improve chunking and citation traceability.** Create a separately versioned pipeline output that preserves page or section references and improves word/sentence boundaries. Repeat V1 and V2 and perform representative source-to-chunk checks before citation-based indexing.
2. **Review data coverage and governance.** Verify intended processing permissions, inspect remaining unverified source pages, and assess topic coverage before downstream indexing, evaluation, or public sharing.

### Week 4 Deliverable

- [Data Quality & Bias Report](docs/week4_data_quality_report.md)

The full report documents the inspection sample, five-dimension scorecard, validation evidence, duplicate and coverage findings, potential bias, governance safeguards, mitigation actions, and the HOLD decision.

No new data pipeline or RAG model was implemented during Topic 4. All additional checks were read-only, and the original Topic 3 dataset was preserved.

## Weekly Progress

| Week | Focus | Deliverable | Status |
|---|---|---|---|
| 1 | AI system analysis and project scoping | Observation sheet, system map, project scope and README | Completed |
| 2 | Requirements, evaluation criteria and V1 architecture | Requirements specification, evaluation criteria, architecture diagram and design decisions | Completed |
| 3 | PDF data engineering | Prepared dataset, lineage manifests, executable pipeline and repeatability verification | Completed |
| 4 | Data quality and responsible data practices | Data Quality & Bias Report, validation findings, coverage assessment and quality-gate decision | Completed |

## Current Status

Topics 1–4 laboratory activities are complete.

The project has defined its requirements and architecture, prepared 726 text chunks from two DOE Mechanical Science PDFs, verified the Topic 3 pipeline outputs, and completed a data-quality and responsible-data audit.

The Topic 4 quality gate is **HOLD for downstream citation-based RAG use** because all 726 records lack structured page or section references. The existing dataset is retained as the historical baseline while source traceability, chunk boundaries, permissions, and coverage require further review.

The RAG chatbot, retrieval evaluation, generated-answer accuracy assessment, and page-level citation support have not yet been implemented.