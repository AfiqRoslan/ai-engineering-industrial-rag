# Topic 4 Lab: Data Quality and Bias Report

Mechanical Engineering Knowledge Assistant (Industrial Knowledge Assistance Chatbot)

| Field | Details |
|---|---|
| Student name | Mohamad Afiq Ikmal bin Mohd Roslan |
| Matric number | A24AI0046 |
| Course | SAIA 3113 AI Engineering |
| Audit scope | Topic 3 Part C document dataset |
| Audit date | 22 November 2026 |
| Quality-gate decision | HOLD for downstream citation-based RAG use |


## 1. Project and Data Overview

The proposed educational chatbot helps engineering students and trainee engineers find document-grounded explanations of mechanical concepts. This audit focuses on two Topic 2 requirements: **FR2** (retrieve relevant passages from approved documents) and **FR3** (cite source title and page or section). FR2 needs readable, source-attributed chunks. FR3 also needs reliable chunk-level location metadata.

- **Pathway and unit:** Topic 3 Pathway A (PDF/TXT). The inspection unit is one prepared text chunk.
- **Audited output:** data/pipeline_v1/documents/prepared_text.jsonl (Part C).
- **Matching manifest:** data/pipeline_v1/documents/pipeline_manifest.json.
- **Population:** 726 chunks from **S01** (mechanical_science_vol1.pdf, 341 chunks) and **S02** (mechanical_science_vol2.pdf, 385 chunks). The DOE *Mechanical Science* handbooks are dated January 1993.
- **Inspection sample:** 16 chunks (8 per document), taken from seven distributed positions per document plus one suspected boundary case. The samples include front matter, technical content and end matter. This targeted sample is **not** a statistical estimate of overall semantic accuracy.
- **Labels used:** N.V. means Not Verified.

## 2. Five-Dimension Quality Scorecard

| Dimension | Observed finding / evidence | Task impact | Decision |
| --- | --- | --- | --- |
| Completeness | 726/726 chunks have nonempty text. However, 726/726 have page: null and no structured section reference. | FR3 page/section citation cannot be supported reliably from the current metadata. | Warning |
| Consistency | All 726 records use paragraph-aware-char-500 and one of the two expected source filenames. Some text includes page headers and broken sentence/word boundaries (e.g., Serv / ices). | Chunk formatting may reduce retrieval usefulness under FR2. | Warning |
| Accuracy | Both raw-file SHA-256 hashes match the recorded manifest. Source-to-chunk fidelity was not manually compared page by page. Current pypdf extraction counts differ from the historical manifest by 386 and 470 characters. | Exact content fidelity and technical correctness remain N.V. | N.V. |
| Timeliness | Both handbooks are 1993 editions. Whether newer editions apply was not verified. | Appropriate for foundational concepts, but not an authoritative source for current maintenance procedures. | Warning |
| Uniqueness | All 726 record IDs are unique. There are 726 distinct exact text values and 0 identical-text duplicate groups. | No exact duplicates were found that would unnecessarily inflate retrieval results. | Pass (exact only) |

## 3. Validation Findings

Two dataset-wide rules were executed against the 726-record Part C JSONL without modifying it.

| Rule / link | Checkable condition | Observed result | Action |
| --- | --- | --- | --- |
| V1 → FR2 | Each record has nonempty text, and source equals one of the two expected PDF filenames. | 726 passed; 0 failed (726 tested). | Retain records for inspection and future processing. |
| V2 → FR3 | Each record has a known source plus a nonempty structured page or section value. | 0 passed; 726 failed (726 tested). Examples: mechanical_science_vol1-0001 through -0005. | Block citation-based RAG use until location metadata is fixed and revalidated. |

A filename alone does not meet the FR3 page/section requirement. Neither rule establishes retrieval relevance or generated-answer correctness. Those assessments belong to later topics.

## 4. Duplicate, Anomaly and Coverage Findings

- **Exact duplicates:** 0 duplicate ID values and 0 identical-text duplicate groups across 726 chunks. Near-duplicates and overlapping content were **not verified**.
- **Boundary anomaly:** A screening check flagged **442/724 inter-chunk boundaries (61.05%)** where the left chunk ended with a letter and the next chunk began with a letter. This is **not** a confirmed word-split percentage, but manual examples such as Serv / ices show genuine splitting. Sample mechanical_science_vol1-0171 also contains table-of-contents material.
- **PDF inspection:** The two PDFs have 252 pages in total, and 13 returned no extracted text. Five selected pages were visually checked and confirmed blank. The other eight remain **N.V.** for visual content. Historical and current extraction character counts differ slightly.
- **Coverage by keyword (whole population):** the counts below are numbers of chunks that mention each keyword. Categories can overlap. Keywords also appear in headers and contents, so these counts show *mentions*, not confirmed depth or quality of coverage.

| Keyword | Chunks (of 726) | From S01 | From S02 |
| --- | --- | --- | --- |
| Pumps | 148 | 129 | 19 |
| Valves | 277 | 61 | 216 |

## 5. Bias Assessment

**Inferred representation bias.** Selecting only two 1993 mechanical-science manuals emphasizes the subjects and language present in those volumes. Valves are mentioned more often than pumps (277 versus 148 chunks), and the originally proposed alignment and lubrication topics are not confirmed as adequately covered. The future retriever might therefore perform unevenly across questions, particularly for less-represented concepts. **Proposed control:** restrict the advertised scope to verified topics, create topic-stratified retrieval tests, and add approved documents only when needed.

**Inferred pipeline-induced risk.** Whole-document, 500-character chunking can split technical terms and removes reliable page provenance. **Proposed control:** compare a separate page-aware, boundary-preserving pipeline against the verified Week 3 baseline. Neither risk demonstrates measured chatbot unfairness or retrieval failure.

## 6. Privacy, Rights and Governance

**Provenance.** S01 is DOE-HDBK-1018/1-93 and S02 is DOE-HDBK-1018/2-93. Both were published by the U.S. Department of Energy in January 1993. The source manifest records SHA-256 values, which matched the original local PDFs:

- **S01:** c1e37601164acf95cbaecad93b1db9841ad8d7670bf30a4fdd6ff0a87c6a0070
- **S02:** f569f8de24e0c9b23fa8f5c965c3d0740daa5e41db0f029ad8e3893d3fd9e2fd

**Rights.** Both handbooks carry the statement *Distribution Statement A: Approved for public release; distribution is unlimited*. Whether all intended indexing, redistribution and external-service processing uses are permitted is **N.V.**, and the historical pipeline manifest still contains access/version placeholders.

**Privacy and collection basis.** The reviewed content is technical and publication material. A systematic sensitive-information scan is **N.V.** No student or plant-operational records were intentionally collected, so individual consent is not applicable to this source selection.

**Safeguards.** Keep the raw PDFs local, document sources and rights in docs/source_register.md, exclude personal or confidential uploads, and recheck permissions before indexing or public sharing. The project owner should revalidate the data whenever source editions or processing methods change.

## 7. Mitigation and Impact on Requirements

| Priority, owner and timing | Action and requirement affected | Residual risk |
| --- | --- | --- |
| P1. Project owner, before building a citation-based index | Create a new version of the pipeline with page/section provenance, word/sentence-aware boundaries and source-to-chunk spot checks, then rerun V1 and V2 (FR2, FR3, later RAI1). Preserve the historical Week 3 output. | Extraction/layout or citation errors may persist and need human review. |
| P2. Project owner, before indexing or sharing, and before later evaluation | Resolve intended-use and redistribution permissions, update source metadata, inspect the remaining ambiguous pages, and test category-specific coverage for the supported educational scope (RAI4, FR2, NFR2). | Historical age and limited topic coverage remain even after administrative verification. |

## 8. Quality-Gate Decision

**HOLD** for advancing this particular 726-chunk dataset into a citation-based RAG application. The evidence is: (1) V1 structural readiness passes 726/726, but (2) V2 citation readiness fails 726/726, and boundary defects and open permissions questions add further risk. The existing Week 3 data may be retained as an **audited baseline** and used for controlled comparison. It should not be represented as citation-ready or approved for operational maintenance advice.

**Re-review trigger.** A separate versioned output with verifiable page/section references passes V1 and V2, representative source-to-chunk checks are documented, intended processing rights are confirmed, and the relevant topic-coverage risks are reviewed. Retrieval accuracy and answer safety still require later evaluation.

## Appendix: Evidence References

### A. Topic 2 and Topic 3 references

- **Topic 2:** docs/week2_requirements.md (FR2, FR3, RAI1, RAI4); docs/week2_evaluation_criteria.md.
- **Topic 3:** docs/week3_data_inventory.md; docs/week3_pipeline_decisions.md; docs/source_register.md; data/pipeline_v1/documents/pipeline_manifest.json; data/pipeline_v1/documents/prepared_text.jsonl.

### B. Sixteen inspected chunk IDs

Each ID uses the prefix mechanical_science_vol1- (S01) or mechanical_science_vol2- (S02).

- **S01:** 0001, 0003, 0057, 0114, 0171, 0228, 0285, 0341
- **S02:** 0001, 0003, 0065, 0129, 0193, 0257, 0321, 0385

### C. Additional read-only audit checks (22 November 2026)

Two rule counts (V1 726/726; V2 0/726), the exact-duplicate count (0), keyword coverage, boundary-screening counts and SHA-256 verification were recorded in local PowerShell console output. The original prepared files were not modified.
