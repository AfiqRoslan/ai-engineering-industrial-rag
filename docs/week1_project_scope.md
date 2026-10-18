# Week 1 Project Scope: InternGuide AI

**Course:** SAIA 3113 AI Engineering  
**Project type:** Individual semester project

## Project Name

InternGuide AI: UTM Industrial Training Information Assistant

## Domain

Higher Education and Student Support

## Problem Statement

UTM students need to refer to several documents when preparing for industrial training. Information about eligibility, placement procedures, training duration and assessment may be found in different university guidelines and faculty handbooks. This makes it harder to find the right information quickly.

InternGuide AI aims to help students ask questions about industrial training and receive clear answers based on official UTM documents. The system will show its sources and tell users when it cannot confirm an answer.

## Evidence of the Problem

**Evidence 1:** UTM's *Industrial Training Guidelines (2024)* cover several steps, including registration, placement, supervision and report submission. Students need to refer to different sections depending on their questions.

**Source:** Universiti Teknologi Malaysia. (2024). *Garis Panduan Latihan Industri: Program Sarjana Muda*, Sections 2.6 to 2.9.  
https://ugs.utm.my/wp-content/uploads/sites/19/2024/11/Final-Garis-Panduan-LI-UTM-2024-Senat.pdf

**Evidence 2:** The *FAI Bachelor in Artificial Intelligence Academic Handbook (2025/2026)* states that SAIA 3146 Industrial Training carries 6 credits and requires at least 20 weeks of placement. Students may need both the faculty handbook and general UTM guidelines to understand the requirements.

**Source:** Faculty of Artificial Intelligence. (2025). *Academic Handbook: Bachelor in Artificial Intelligence with Honours 2025/2026*.  
https://drive.google.com/file/d/1coXIUom2QVI_YlUtQ0CjFeNkZU2xOPy3/view

These documents show that the information is spread across several sources. However, further student feedback would be needed to confirm how difficult the current process is for students.

## Initial Related Work

**1. UTM Industrial Training Guidelines and FAI Academic Handbook**

- **Source:** UTM Industrial Training Guidelines (2024) and FAI Academic Handbook (2025/2026).
- **Approach:** Students read official documents to find information about industrial training.
- **Limitation:** Students must search through different documents and identify which rules apply to their programme.

**2. UTM Industrial Training System (ITS)**

- **Source:** UTM Industrial Training Guidelines (2024), Section 2.9; [UTM Faculty of Electrical Engineering Industrial Training website](https://fke.utm.my/li/).
- **Approach:** ITS is used for industrial training administration and related submissions.
- **Limitation:** The available information mainly describes administrative functions. It does not establish whether ITS provides a document-based question-answering feature.

**3. Retrieval-Augmented Generation (RAG) Chatbots for Education**

- **Source:** Swacha, J., and Gracel, M. (2025). *Retrieval-Augmented Generation (RAG) Chatbots for Education: A Survey of Applications*. *Applied Sciences, 15*(8), 4234. https://doi.org/10.3390/app15084234
- **Approach:** RAG combines information retrieval with AI-generated answers.
- **Limitation:** RAG systems can still retrieve irrelevant information or generate answers that are not fully supported by their sources. The survey does not provide a system specifically for FAI industrial training.

## Engineering Gap / Limitation

UTM provides official industrial training documents and an administrative system, but the sources reviewed do not identify a dedicated assistant that answers FAI students' industrial training questions with references to the relevant documents. InternGuide AI will focus on making this information easier to access while reducing unsupported or misleading answers.

## Initial Project Objectives

**O1:** To design an AI question-answering system that uses selected official UTM industrial training documents as its knowledge source.

**O2:** To develop a RAG-based prototype that retrieves relevant information, answers student questions and provides source references.

**O3:** To evaluate the prototype based on answer accuracy, source relevance, response time and handling of questions that cannot be answered from the documents.

## Target Users

The main users are UTM Bachelor in Artificial Intelligence students preparing for compulsory industrial training, especially those looking for information about requirements, placements and reports.

## Data Sources

**Source 1:** UTM Industrial Training Guidelines (2024)  
URL: https://ugs.utm.my/wp-content/uploads/sites/19/2024/11/Final-Garis-Panduan-LI-UTM-2024-Senat.pdf

**Source 2:** FAI Bachelor in Artificial Intelligence Academic Handbook (2025/2026)  
URL: https://drive.google.com/file/d/1coXIUom2QVI_YlUtQ0CjFeNkZU2xOPy3/view

**Source 3:** UTM Undergraduate Academic Rules, 16th Edition (2022)  
URL: https://drive.google.com/file/d/1MKWo-wUZzrHM9PZBNO2S8qZiVVhB-oTh/view

**Note:** The documents are useful for planning the project, but access does not automatically mean they can be copied into an AI database. The FAI handbook includes copyright restrictions. Permission or suitable alternative documents will be needed before using full document content in the prototype. Current faculty requirements should also be checked before development.

## Similar to EduAdvisor

Both systems use official university documents to answer student questions. They aim to provide relevant answers with sources rather than relying only on a language model's general knowledge.

## Different from EduAdvisor

EduAdvisor covers general academic matters such as courses and graduation requirements. InternGuide AI focuses on industrial training for FAI students, including placement requirements, procedures and reporting. It will not apply for placements or make academic decisions for students.

## Responsible AI Risks

**Risk 1: Incorrect or invented information**  
The AI might give the wrong requirement, procedure or deadline. Students could make mistakes in their industrial training preparation. To reduce this risk, the system should provide references and avoid answering when the documents do not support a claim.

**Risk 2: Outdated information**  
University or faculty requirements may change between academic sessions. Students could follow rules that are no longer valid. The system should display document dates and remind users to confirm important details with the faculty.

**Risk 3: Privacy and document permissions**  
Students might enter personal information, and some university documents may not be permitted for reuse in an AI system. The prototype should avoid collecting sensitive personal details and only process documents that are authorised for this use.

## Initial Evaluation Plan

A small set of questions will be prepared from the approved source documents. The prototype will be tested for answer accuracy, correct references, response time and whether it can recognise questions that are not covered by its sources. Where possible, its results will be compared with basic keyword search.

## Project Scope

The first version will focus on searching approved documents and answering common questions about UTM industrial training. It will not search for job vacancies, submit applications, access private student records or decide whether a student is eligible for training.
