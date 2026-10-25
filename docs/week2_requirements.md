# Topic 2 Lab — Requirements Specification

**Project:** Industrial Knowledge Assistance Chatbot  
**Course:** SAIA 3113 AI Engineering  
**Status:** Proposed requirements; system not yet developed

## Section 0 — Project Framing and Application Scope

| Element | Description |
|---|---|
| **Problem and evidence** | Maintenance information can be spread across separate manuals. The U.S. Bureau of Reclamation publishes different documents for mechanical maintenance, machinery alignment and lubrication [1]. Naqvi et al. (2024) also examine information retrieval from specialised industrial maintenance text [2]. These sources justify exploring better document search; the effect on reading time has not yet been tested. |
| **Existing approaches** | **(1)** Manual reading and PDF keyword search: useful for locating exact terms, but related details may require searching several manuals [1]. **(2)** Semantic search for maintenance records: retrieves text by meaning, but does not directly produce referenced answers from the selected manuals [2]. **(3)** Retrieval-Augmented Generation (RAG): combines retrieval and answer generation, but still needs evaluation for relevance and faithfulness in this domain [3]. |
| **Engineering gap** | A small document-based assistant is needed to retrieve relevant maintenance information and present answers with checkable source references. Its answer quality and handling of insufficient information must be evaluated. This is an application engineering gap, not a claim of new research. |
| **O1 — Design** | To design a chatbot that uses selected industrial maintenance manuals as its information source. |
| **O2 — Develop** | To develop a RAG-based prototype that retrieves relevant sections and answers questions with document references. |
| **O3 — Evaluate** | To evaluate answer accuracy, retrieval relevance, response time and handling of questions not supported by the documents. |
| **Intended users** | Engineering students and trainee engineers learning basic equipment maintenance concepts. |
| **Supported tasks** | Ask questions about mechanical maintenance, machinery alignment and lubrication; obtain short explanations; view manual references; recognise when an answer is unavailable. |
| **Knowledge domain** | Selected manuals concerning hydroelectric/large-pump units and rotating machinery. Only documents cleared for the intended use will enter the knowledge base. |
| **Operating context** | English-language questions through a simple educational chatbot. No connection to plant equipment or operational systems. |
| **Important constraints** | One-semester schedule, small budget, limited document collection, technical PDF layouts, and unresolved reuse permissions for candidate manuals. |
| **Out of scope** | Real-time equipment diagnosis, maintenance approval, hazardous step-by-step operating instructions, control-system access, and advice based on private company records. |
| **Evaluation focus** | Can the chatbot locate relevant manual passages, give accurate and verifiable explanations, and respond safely when the evidence or request is outside scope? |

**Candidate documents** (subject to a documented permission review):

- **D1:** FIST 2-12, *Mechanical Maintenance of Hydroelectric and Large Pump Units* (2024) — https://www.usbr.gov/power/data/fist/FIST_2-12_%285-2024%29.pdf
- **D2:** FIST 2-1, *Alignment of Rotating Machinery* (2024) — https://www.usbr.gov/power/data/fist/FIST_2-1_%285-2024%29.pdf
- **D3:** FIST 2-4, *Lubrication of Equipment* (2024) — https://www.usbr.gov/power/data/fist/FIST_2-4_%285-2024%29.pdf

The candidate manuals are publicly accessible but have an internal-use notice. Public access does not by itself confirm permission to index, redistribute or send their content to an external AI service. Alternative permitted manuals may be needed.

## Section 1 — Functional Requirements

| ID | The system SHALL | Scope boundary — SHALL NOT |
|---|---|---|
| **FR1** | Answer conceptual questions about maintenance topics covered by the approved documents. | Provide equipment-specific settings or limits not found in those documents. |
| **FR2** | Retrieve relevant passages from the approved document collection before generating a technical answer. | Use unsupported model knowledge as a substitute for retrieved evidence. |
| **FR3** | Include the source document title and page or section in each document-based answer. | Attach citations that do not support the stated information. |
| **FR4** | State when the documents do not contain enough information, and refuse or redirect unsafe operational requests. | Diagnose running equipment, authorise maintenance, or give hazardous operational instructions. |
| **FR5** | Present answers in clear language suitable for engineering students, including any important uncertainty. | Present guessed information as confirmed technical guidance. |

## Section 2 — Non-Functional Requirements

These are proposed V1 targets rather than measured results.

| ID | Quality attribute | Requirement | Measurement method | Metric | Threshold |
|---|---|---|---|---|---|
| **NFR1** | Correctness | Technical answers shall agree with the supporting source passages. | Score 30 answerable questions against manually checked source passages. | Correct-answer rate | **≥80%** (24 of 30) |
| **NFR2** | Retrieval quality | Relevant supporting information shall appear among the first three retrieved passages. | Label one supporting passage for each of 40 questions; examine the top three results. | Retrieval hit rate at 3 (Recall@3) | **≥85%** (34 of 40) |
| **NFR3** | Latency | The application shall respond within a reasonable waiting time for educational use. | Time 50 full requests, from submission to displayed response, using a fixed test setup. | 90th-percentile response time (p90) | **<8 seconds** |
| **NFR4** | Maintainability | A revised, approved source document shall be incorporated without changing unrelated application code. | Replace one document in a controlled update and time its index refresh. | Document update time | **≤15 minutes** |

**Measurement notes:** The retrieval metric is the proportion of questions whose single labelled supporting passage appears among the top three. Correctness is counted only for questions with a documented answer. Test questions, passage labels and hardware/model settings will be recorded for repeatability.

## Section 3 — Responsible AI Requirements

| ID | Risk | Requirement | Measurement method | Metric | Threshold |
|---|---|---|---|---|---|
| **RAI1** | Hallucinated answers or citations | The system shall give verifiable document references and avoid unsupported technical claims. | Review 30 answered queries and compare each citation with the actual supporting passage. | Citation presence; answer support rate | **100%** of answered questions cited; **≥90%** fully supported |
| **RAI2** | Unsafe maintenance advice | The system shall decline requests requiring live diagnosis, risky operating instructions or professional approval. | Run 20 predefined unsafe/out-of-scope questions and check the refusal or redirection. | Safe refusal rate | **≥95%** (19 of 20) |
| **RAI3** | Confidential information exposure | The system shall not send personal identifiers or confidential plant information to an external model service. | Use 15 synthetic sensitive-data prompts and inspect outgoing payloads and logs. | Detected disclosures | **0** |
| **RAI4** | Unauthorised document use | The system shall index only documents whose provenance and permission for the intended use are recorded. | Inspect the source register for all indexed documents before testing. | Approved-source coverage; unauthorised files | **100%** approved; **0** unauthorised |

### Part A Reflection

**RAI1 is the most difficult to measure.** A citation can point to the correct topic without supporting the actual answer. Each important claim must therefore be compared with its cited passage. RAI4 also needs to be checked before document processing begins.

## References

[1] U.S. Bureau of Reclamation. *Facilities Instructions, Standards, and Techniques (FIST) manuals.* https://www.usbr.gov/power/data/fist_pub.html

[2] Naqvi, S. M. R., et al. (2024). *Unlocking maintenance insights in industrial text through semantic search.* *Computers in Industry.* https://doi.org/10.1016/j.compind.2024.104083

[3] Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* https://arxiv.org/abs/2005.11401
