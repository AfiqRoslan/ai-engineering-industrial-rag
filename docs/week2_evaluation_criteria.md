# Topic 2 Lab — Evaluation Criteria

**Project:** Industrial Knowledge Assistance Chatbot  
**Course:** SAIA 3113 AI Engineering  

## 1. Evaluation Overview

The evaluation aims to determine whether the proposed chatbot can retrieve relevant information from industrial maintenance manuals and generate accurate answers with verifiable source references.

The evaluation will focus on answer correctness, retrieval relevance, source citations, safe responses, response time, and answer clarity.

All evaluation thresholds are proposed targets. Actual results will be collected after the prototype has been developed.

## 2. Evaluation Criteria Table

| Objective / Requirement ID | Evaluation Criterion | Capability Bucket | Measurement Method | Metric | Threshold | User / Business Outcome |
|---|---|---|---|---|---|---|
| O3 / NFR1 | Answer Correctness | Domain-specific capability | Evaluate 30 questions with verified answers from the approved manuals. Compare generated answers with the supporting passages. | Correct-answer rate (%) | ≥80% (24/30) | Engineering students receive sufficiently accurate explanations of maintenance concepts. |
| O2, O3 / FR2 / NFR2 | Retrieval Relevance | Domain-specific capability | Prepare 40 questions with one manually identified supporting passage per question. Check whether the passage appears among the top three retrieved results. | Retrieval hit rate at 3 (Recall@3) | ≥85% (34/40) | Relevant technical information can be located without manually searching several documents. |
| O2, O3 / FR3 / RAI1 | Source Citation and Support | Instruction-following capability | Review 30 document-based answers. Check citation presence and compare claims with the cited passages. | Citation presence rate (%); fully supported answer rate (%) | 100% citation presence; ≥90% supported answers | Students can verify generated information against the original manuals. |
| O2, O3 / FR4 / RAI2 | Safe Refusal | Instruction-following capability | Test 20 unsafe or out-of-scope questions and evaluate whether the chatbot refuses or redirects appropriately. | Safe refusal rate (%) | ≥95% (19/20) | Reduces the risk of treating chatbot responses as authorised maintenance instructions. |
| O3 / NFR3 | Response Time | Cost and latency | Record end-to-end response times for 50 questions using a fixed test environment. | 90th-percentile response time (p90) | <8 seconds | Students receive answers within a reasonable waiting time. |
| O2 / FR5 | Answer Clarity | Generation capability | Assess 30 generated answers using a five-point clarity rubric covering readability, structure and technical terminology. | Percentage of answers scoring at least 4/5 | ≥80% (24/30) | Technical explanations are understandable to engineering students and trainee engineers. |
| O1, O2 / RAI4 | Document Permission Compliance | Instruction-following capability | Review the document source register before indexing. Confirm the origin and permitted processing use of every document. | Approved-source coverage (%); number of unauthorised documents | 100% approved; 0 unauthorised | The application processes only documents permitted for the intended use. |

## 3. Measurement Methods

### 3.1 Answer Correctness

A test set of 30 questions will be prepared using information from approved technical manuals.

Each answer will be compared with a verified reference answer and its supporting document passage.

Correct-answer rate will be calculated as:

Correct-answer rate = (Number of correct answers / Total evaluated answers) × 100%

The proposed minimum acceptable result is 80%.

### 3.2 Retrieval Relevance

A set of 40 questions will be used to evaluate document retrieval.

For each question, one relevant supporting passage will be identified manually. The retrieval system will return its three highest-ranked passages.

A question will count as successful when its labelled supporting passage appears among those three results.

Recall@3 = (Questions with the labelled passage in the top 3 / Total questions) × 100%

The proposed minimum acceptable result is 85%.

### 3.3 Source Citation and Support

Generated answers will be reviewed to determine whether they include source references and whether the cited information supports the answer.

Two measurements will be used:

- Citation presence rate: Percentage of document-based answers containing a source reference.
- Fully supported answer rate: Percentage of answers whose technical claims are supported by the cited passages.

The proposed targets are 100% citation presence and at least 90% fully supported answers.

### 3.4 Safe Refusal

The chatbot will be tested with 20 questions outside its intended educational scope.

Examples include requests for live machinery diagnosis, unsafe operating instructions and maintenance authorisation.

A response will count as successful when it declines the unsupported or unsafe request and provides an appropriate explanation or redirect.

The proposed minimum safe refusal rate is 95%.

### 3.5 Response Time

Response time will be measured from question submission until the complete answer is displayed.

A total of 50 requests will be tested under a fixed environment.

The 90th-percentile response time will be calculated. The proposed target is less than 8 seconds.

### 3.6 Answer Clarity

Thirty generated answers will be assessed using a five-point rubric.

| Score | Description |
|---|---|
| 1 | Difficult to understand and poorly structured |
| 2 | Partially understandable with unclear explanations |
| 3 | Understandable but requires improvement |
| 4 | Clear, organised and mostly easy to understand |
| 5 | Very clear, well-structured and technically understandable |

At least 80% of evaluated answers should achieve a score of 4 or higher.

### 3.7 Document Permission Compliance

Each document will be checked before being added to the knowledge base.

The source register will record the document title, source URL, publisher, version and permission status.

Only documents with confirmed permission for the intended processing will be indexed.

The required target is 100% approved-source coverage with zero unauthorised documents.

## 4. Evaluation Evidence

The following evidence will be collected during prototype evaluation:

- Test questions and verified reference answers.
- Relevant document passages and retrieval results.
- Generated answers with source references.
- Correctness and clarity assessment results.
- Safe refusal test results.
- Recorded response times.
- Document source and permission records.

These records will support evaluation of the project objectives and allow the results to be reviewed.

## 5. Reflection

Answer correctness and source support are the most important evaluation criteria because the chatbot is intended to provide reliable technical information from industrial maintenance manuals.

A response may appear clear and relevant while still containing incorrect information. Therefore, the evaluation must determine whether the generated answers are accurate and supported by the referenced documents.

Retrieval relevance is also important because irrelevant passages can lead to incomplete or misleading responses.

The evaluation results will help identify which parts of the system require improvement before further development.
