# Topic 3 Lab — Data Inventory

**Project:** Mechanical Engineering Knowledge Assistant
- **Course:** SAIA 3113 AI Engineering

## Part A — Data Source Inventory

| Source ID | Filename | Type and Purpose | Version / Date / Owner | Access / Rights | Inspection Evidence |
|---|---|---|---|---|---|
| S01 | mechanical_science_vol1.pdf | PDF; mechanical science fundamentals, including diesel engines and pumps | DOE-HDBK-1018/1-93; January 1993; U.S. Department of Energy | Approved for public release; distribution unlimited | 122 pages; page 30 contains readable diesel engine explanations (1,610 characters) |
| S02 | mechanical_science_vol2.pdf | PDF; mechanical science fundamentals, including valves | DOE-HDBK-1018/2-93; January 1993; U.S. Department of Energy | Approved for public release; distribution unlimited | 130 pages; page 30 contains readable gate valve explanations (1,828 characters) |

## Requirements and Data Needs

- **FR1 / FR2:** Technical documents provide the information needed for conceptual questions and passage retrieval.
- **FR3 / RAI1:** Document identity and page information are needed to support verifiable citations.
- **NFR2:** Readable, relevant passages are needed for future retrieval evaluation.
- **RAI4:** Source identity and permissions must be recorded before documents are indexed.

## Inspection Findings

1. Both PDF files were successfully detected in `data/raw/`.
2. Both documents contain readable text extracted using `pypdf`.
3. Technical explanations were verified on page 30 of each PDF.
4. Extracted content contains irregular spacing and figure captions that may affect text quality.
5. Text cleaning and chunking will be performed in Part B.

## Data Storage

- **Raw data:** `data/raw/`
- **Prepared data:** `data/processed/`
- **Data type:** Unstructured text (PDF)
- **Selected pathway:** Pathway A — PDF/TXT

## Limitations

- The documents were published in 1993 and may not reflect current maintenance practices.
- PDF extraction may not preserve the original formatting and layout.
- The selected documents cover mechanical fundamentals and do not fully cover every maintenance topic in the original project proposal.
- Public distribution permission is recorded, but any additional reuse conditions should be checked before publishing processed content.
