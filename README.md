# InternGuide AI

> A document-grounded AI assistant that helps UTM Bachelor in Artificial Intelligence students find information about compulsory industrial training.

## Problem Statement

Students may need to check several university and faculty documents to understand industrial training requirements, placement procedures and reporting. InternGuide AI aims to answer common questions using official UTM information and provide references so users can check the original sources.

## Evidence of the Problem

- The [UTM Industrial Training Guidelines (2024)](https://ugs.utm.my/wp-content/uploads/sites/19/2024/11/Final-Garis-Panduan-LI-UTM-2024-Senat.pdf) cover registration, placement, supervision and reporting across different sections.
- The [FAI Academic Handbook (2025/2026)](https://drive.google.com/file/d/1coXIUom2QVI_YlUtQ0CjFeNkZU2xOPy3/view) lists SAIA 3146 Industrial Training as a 6-credit course with a minimum placement period of 20 weeks.

These sources show that information comes from more than one document. Student feedback would be needed to establish how difficult it is to find in practice.

## Initial Related Work / Existing Approaches

1. **Official UTM guidelines and faculty handbook:** Reliable sources, but users need to locate and interpret relevant sections across documents.
2. **UTM Industrial Training System (ITS):** Supports industrial training administration. The reviewed information does not establish a document-grounded question-answering feature. See the [UTM Industrial Training Guidelines](https://ugs.utm.my/wp-content/uploads/sites/19/2024/11/Final-Garis-Panduan-LI-UTM-2024-Senat.pdf).
3. **Educational RAG chatbots:** Combine retrieval and language generation, but can still return irrelevant or unsupported answers. See [Swacha and Gracel (2025)](https://doi.org/10.3390/app15084234).

## Engineering Gap / Limitation

The reviewed UTM sources do not identify a dedicated assistant for FAI industrial training questions that provides answers grounded in the relevant official documents. InternGuide AI will focus on source-backed answers and clear handling of missing information.

## Project Objectives

- **O1:** Design a question-answering system using selected official UTM industrial training documents.
- **O2:** Develop a retrieval-augmented generation (RAG) prototype that answers questions and provides source references.
- **O3:** Evaluate answer accuracy, source relevance, response time and handling of unsupported questions.

## Target Users

UTM Bachelor in Artificial Intelligence students preparing for compulsory industrial training.

## Data Sources

- [UTM Industrial Training Guidelines (2024)](https://ugs.utm.my/wp-content/uploads/sites/19/2024/11/Final-Garis-Panduan-LI-UTM-2024-Senat.pdf)
- [FAI Bachelor in Artificial Intelligence Academic Handbook (2025/2026)](https://drive.google.com/file/d/1coXIUom2QVI_YlUtQ0CjFeNkZU2xOPy3/view)
- [UTM Undergraduate Academic Rules, 16th Edition (2022)](https://drive.google.com/file/d/1MKWo-wUZzrHM9PZBNO2S8qZiVVhB-oTh/view)

**Document use:** The source links are included for reference. Some documents have copyright or reuse restrictions, so full-text ingestion into the prototype requires permission or a suitable authorised alternative. Current faculty requirements must also be verified.

## Week 1 Engineering Evidence

- [Claude AI observation sheet](docs/week1_observation_sheet.md) (Group 6 activity)
- [Claude conceptual system map](docs/week1_system_map.png) (Group 6 activity)
- [InternGuide AI project scope](docs/week1_project_scope.md) (Individual activity)

## Weekly Progress

| Week | Focus | Deliverable | Status |
|---|---|---|---|
| 1 | Analyse an AI system and define the project scope | Observation sheet, system map, project scope, README | In progress |

## Current Status

This project is at the planning stage. No RAG prototype has been implemented yet.
