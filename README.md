# Industrial Knowledge Assistance Chatbot

A semester project for SAIA 3113 AI Engineering. The proposed chatbot will answer basic questions about industrial equipment maintenance using information from selected technical manuals.

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

## Data Sources

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

## Weekly Progress

| Week | Focus | Deliverable | Status |
|---|---|---|---|
| 1 | AI system analysis and project scoping | Observation sheet, system map, project scope and README | Individual project scope revised |

## Current Status

The project is at the planning stage. The chatbot has not yet been developed or evaluated.
