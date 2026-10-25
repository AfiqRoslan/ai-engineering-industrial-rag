# Topic 2 Lab — Architecture Decisions and Traceability

**Project:** Industrial Knowledge Assistance Chatbot  
**Course:** SAIA 3113 AI Engineering  

## 1. Architecture Overview

The proposed architecture uses Retrieval-Augmented Generation (RAG) to answer questions based on selected industrial maintenance manuals.

The system consists of two main workflows:

1. **Document preparation:** Approved technical manuals are processed into searchable passages with source information.
2. **Question answering:** User questions are checked, relevant passages are retrieved, and a language model generates answers supported by the documents.

The architecture also includes safety controls and evaluation to assess system performance.

The design remains conceptual. Specific models, frameworks and databases will be selected during development.

## 2. Architecture Needs from Requirements

The initial architecture follows a simple process:

User Question → AI Application → Language Model → Response

However, this approach does not guarantee that answers are supported by the selected maintenance manuals.

Additional components are required to meet the functional, non-functional and Responsible AI requirements.

| Requirement ID | Requirement Need | Architecture Response |
|---|---|---|
| FR1, FR2, NFR1, NFR2 | Answers must use relevant technical information from approved manuals. | Knowledge index and passage retrieval component. |
| FR3, RAI1 | Generated answers must include verifiable source references. | Source metadata and citation verification. |
| FR4, RAI2 | Unsafe and out-of-scope requests must be handled appropriately. | Scope and safety controls. |
| RAI3 | Sensitive information must not be transmitted to external model services. | Privacy screening before model processing. |
| RAI4, NFR4 | Only authorised documents may be processed, and document updates must be manageable. | Source approval and document preparation components. |
| NFR3 | The chatbot must respond within the proposed latency threshold. | Query coordination and response-time evaluation. |

## 3. Architecture Decision Record (ADR)

The following decisions are based on the project requirements and constraints.

| Decision | Requirement / Constraint | Alternatives Considered | Selected Option | Trade-off Accepted |
|---|---|---|---|---|
| ADR1 — Include document retrieval | FR2, NFR1, NFR2: Answers must use relevant information from technical manuals. | Language model without retrieval; keyword search; retrieval-based question answering. | Document retrieval with a searchable knowledge index. | Improves access to relevant information but increases system complexity and processing time. |
| ADR2 — Include safety and privacy controls | FR4, RAI2, RAI3: Unsafe requests and sensitive information must be controlled. | Language model instructions only; separate input screening and output checks. | Input screening and response safety checks. | Reduces unsafe responses and information exposure, but may reject some valid questions. |
| ADR3 — Include source approval | RAI4: Only documents permitted for the intended use may be processed. | Directly process publicly accessible documents; review documents before indexing. | Source approval before document preparation. | Requires additional document checks and may limit available data, but reduces unauthorised document processing. |
| ADR4 — Include source references | FR3, RAI1: Answers must be supported by the original documents. | Answers without citations; document-level references; document and page references. | Document and page or section references with a citation support check. | Improves transparency and verification, but requires accurate source metadata and additional checking. |

### ADR Summary

Document retrieval is selected because the chatbot must provide information grounded in the chosen technical manuals.

Safety and privacy controls are included to limit inappropriate requests and reduce information exposure.

Source approval is required to ensure that the knowledge base contains only documents permitted for the intended use.

Source references are included so that generated answers can be checked against the original manuals.

These decisions prioritise answer reliability, traceability and responsible information use over minimum system complexity.

## 4. Initial Requirements Traceability Matrix

The traceability matrix connects project objectives, requirements, evaluation criteria, architecture components and the evidence expected during implementation.

| Objective | Requirement | Evaluation Criterion | Architecture Element | Later Evidence |
|---|---|---|---|---|
| O1 | RAI4 | 100% approved-source coverage | Source approval gate | Document source register and permission records |
| O2 | FR2, NFR2 | Retrieval hit rate at 3 ≥85% | Knowledge index and passage retriever | Retrieval results from 40 labelled questions |
| O2 | FR3, RAI1 | 100% citation presence and ≥90% fully supported answers | Source metadata and citation verification | Citation assessment of 30 generated answers |
| O2 | FR4, RAI2 | Safe refusal rate ≥95% | Scope and safety controls | Results from 20 unsafe or out-of-scope test questions |
| O3 | NFR1 | Answer correctness ≥80% | Passage retriever and language model | Results from 30 verified questions |
| O3 | NFR3 | p90 response time <8 seconds | Query coordinator and response pipeline | Response times from 50 test requests |
| O3 | FR5 | At least 80% of answers achieve a clarity score of 4/5 or higher | Language model and response presentation | Clarity assessment of 30 generated answers |

The evaluation thresholds are proposed targets. Actual results will be recorded after the prototype has been developed.

## 5. Final Architecture Review

The proposed V1 architecture supports the main requirements identified during project planning.

The document preparation workflow separates source approval from document processing. This reduces the risk of adding unauthorised documents to the knowledge base.

The passage retriever provides relevant technical information to the language model. Source metadata and citation checks support the verification of generated answers.

Scope and privacy controls are included to manage unsafe requests and sensitive information. The evaluation component supports future assessment of correctness, retrieval relevance, citations, response time and safety.

The architecture does not include unnecessary functions such as real-time equipment monitoring, autonomous maintenance decisions or direct access to industrial control systems.

The proposed components are considered appropriate for an initial prototype and may be refined during development.

## 6. Reflection

**Which architecture decision involved the most important trade-off? Which requirement drove the decision, and what trade-off was accepted?**

The most important trade-off is the decision to include document retrieval in the chatbot architecture.

A language model without retrieval would be simpler to develop and maintain. However, its responses may not be supported by the selected industrial maintenance manuals.

Document retrieval allows the system to locate relevant information before generating an answer. This supports FR2 and NFR2 by improving access to relevant source information.

The accepted trade-off is greater system complexity and potentially longer response times. This is considered reasonable because the main purpose of the chatbot is to provide reliable technical explanations based on verifiable documents.
