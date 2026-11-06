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

- DOE Mechanical Science Volume 1 (1993) - 122 pages
- DOE Mechanical Science Volume 2 (1993) - 130 pages

These documents carry Distribution Statement A, approving public release with unlimited distribution. The previously proposed FIST manuals were not used for this pipeline.

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
## Weekly Progress

| Week | Focus | Deliverable | Status |
|---|---|---|---|
| 1 | AI system analysis and project scoping | Observation sheet, system map, project scope and README | Completed |
| 2 | Requirements, evaluation criteria and V1 architecture | Requirements specification, evaluation criteria, architecture diagram and design decisions | Completed |
| 3 | PDF data engineering | Prepared dataset, lineage manifests, executable pipeline and repeatability verification | Completed |

## Current Status

Topics 1-3 are complete. The project has defined its requirements and architecture, prepared 726 text records from two DOE mechanical science PDFs, and verified pipeline repeatability.

The RAG chatbot, retrieval evaluation and page-level citation support have not yet been implemented.
