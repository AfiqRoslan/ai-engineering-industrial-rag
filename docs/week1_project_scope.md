# Week 1 Project Scope — Industrial Knowledge Assistance Chatbot

**Course:** SAIA 3113 AI Engineering  
**Activity:** Topic 1 Lab, Part C (Individual)

## Project Name
Industrial Knowledge Assistance Chatbot

## Domain
Industrial equipment maintenance and technical information retrieval.

## Problem Statement
Industrial maintenance manuals contain useful technical information, but related topics are often covered in separate documents. For example, understanding rotating machinery maintenance may involve reading different manuals on mechanical maintenance, shaft alignment and lubrication.

This project proposes a chatbot that helps engineering students find and understand information from selected technical manuals. The chatbot will retrieve relevant document sections and provide source references rather than relying only on a language model's general knowledge.

## Evidence of the Problem

**Evidence 1:** The U.S. Bureau of Reclamation publishes separate manuals for mechanical maintenance, rotating machinery alignment and lubrication. Closely related information is therefore distributed across multiple documents. However, the existence of separate manuals does not establish how much difficulty readers experience when searching them.

- **Source:** U.S. Bureau of Reclamation, *Facilities Instructions, Standards, and Techniques (FIST) Manuals*. https://www.usbr.gov/power/data/fist_pub.html

**Evidence 2:** Naqvi et al. (2024) discuss challenges in searching industrial maintenance records containing specialised terms, abbreviations and unstructured text. The study explores transformer-based semantic search for retrieving relevant maintenance information. Although the study examines records rather than technical manuals, it shows the potential value of better retrieval methods for industrial text.

- **Source:** Naqvi, S. M. R., et al. (2024). *Unlocking maintenance insights in industrial text through semantic search*. *Computers in Industry, 157–158*, 104083. https://doi.org/10.1016/j.compind.2024.104083

## Initial Related Work / Existing Approaches

**1. Reading and searching PDF manuals**

- **Source:** U.S. Bureau of Reclamation, FIST Manuals. https://www.usbr.gov/power/data/fist_pub.html
- **Existing approach:** Readers use tables of contents and keyword searches to locate information within manuals.
- **Limitation:** Questions involving several manuals may still require manual searching and comparison of different sections.

**2. Semantic search for industrial maintenance text**

- **Source:** Naqvi et al. (2024). https://doi.org/10.1016/j.compind.2024.104083
- **Existing approach:** Transformer-based semantic search is used to retrieve relevant industrial maintenance records.
- **Limitation:** The study focuses on retrieving records rather than generating referenced answers to questions from a selected collection of maintenance manuals.

**3. Retrieval-Augmented Generation (RAG)**

- **Source:** Lewis et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. https://arxiv.org/abs/2005.11401
- **Existing approach:** RAG combines information retrieval with a language model to generate responses using external knowledge.
- **Limitation:** The approach still requires adaptation and evaluation for industrial manuals, particularly to assess retrieval relevance and whether generated answers are supported by the sources.

## Engineering Gap / Limitation
Existing manuals provide technical information, while semantic search and RAG offer ways to retrieve and present it. The remaining engineering task is to build and evaluate a small question-answering application for the selected industrial manuals, with clear source references and appropriate handling of unsupported questions. The project focuses on applying established methods rather than developing a new AI model.

## Initial Project Objectives

- **O1:** To design a chatbot that uses selected industrial maintenance manuals as its information source.
- **O2:** To develop a RAG-based prototype that retrieves relevant sections and answers questions with document references.
- **O3:** To evaluate answer accuracy, retrieval relevance, response time and the handling of questions not supported by the documents.

## Target Users
Engineering students and trainee engineers learning about rotating machinery and basic equipment maintenance.

## Data Sources

The following publicly accessible U.S. Bureau of Reclamation manuals are proposed as initial sources:

1. **FIST 2-12 — Mechanical Maintenance of Hydroelectric and Large Pump Units (2024)**  
   https://www.usbr.gov/power/data/fist/FIST_2-12_%285-2024%29.pdf
2. **FIST 2-1 — Alignment of Rotating Machinery (2024)**  
   https://www.usbr.gov/power/data/fist/FIST_2-1_%285-2024%29.pdf
3. **FIST 2-4 — Lubrication of Equipment (2024)**  
   https://www.usbr.gov/power/data/fist/FIST_2-4_%285-2024%29.pdf

These are candidate documents, not an approved dataset. The manuals are publicly accessible but include an internal-use disclaimer. Processing and reuse conditions must be checked before their contents are indexed. The PDF files will not be uploaded to a public GitHub repository without the necessary permission.

## Similar to EduAdvisor
Both systems aim to answer questions using a limited collection of documents and provide references that allow information to be checked against the original sources.

## Different from EduAdvisor
EduAdvisor focuses on university academic information. The Industrial Knowledge Assistance Chatbot focuses on industrial equipment and maintenance concepts. Its purpose is educational information support, not diagnosis of operating equipment or authorisation of maintenance work.

## Responsible AI Risks

**Risk 1 — Incorrect or unsupported answers:** The chatbot may misunderstand a manual or generate information not supported by the documents. Incorrect explanations could mislead learners. The proposed controls are source references and clear responses when sufficient evidence is unavailable.

**Risk 2 — Unsafe maintenance advice:** Generated information could be mistaken for instructions to operate or repair actual machinery. The application will be limited to educational explanations and will not provide site-specific maintenance approval or safety-critical operational decisions.

**Risk 3 — Document permissions and privacy:** Some manuals may have usage restrictions, and submitted questions could contain confidential industrial information or personal data. Only documents permitted for the intended processing will be used, and the prototype will avoid collecting confidential or personal information.
