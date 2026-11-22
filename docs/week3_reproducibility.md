# Topic 3 — Reproduction and artifact verification

This note supplements the [Topic 3 decisions](week3_pipeline_decisions.md) and the [source register](source_register.md). It does **not** replace the historical 6 November 2026 lab evidence or claim a new notebook execution.

## Scope required by the Topic 3 lab

The selected pathway is **A — PDF/TXT**. The existing notebook demonstrates ingestion, inspection, comparison of fixed-size and paragraph-aware 500-character chunks, preparation, validation, JSONL storage, source-to-output metadata/lineage, and a repeatability smoke test. The source handbooks are the two DOE *Mechanical Science* volumes. Topic 2 requirements FR1/FR2, FR3, NFR2 and RAI4 drive this selection. No other data modalities are claimed.

## Run in Google Colab (the lab's stated platform)

1. Open `notebooks/week3_pipeline.ipynb` in Colab. The initial setup cell creates `/content/week3_project/data/raw` and `/content/week3_project/data/processed`.
2. Run the source-restoration cell immediately after setup. It **attempts** official DOE PDF downloads and verifies the source checksums recorded in Topic 3. If download is unavailable, manually upload the two approved PDFs to `/content/week3_project/data/raw/` and rerun that cell.
3. Run the remaining cells in notebook order. The existing Pathway A cell installs `pypdf` within Colab. Do not run pathways B–F.
4. Check the printed ingestion/inspection evidence, 726 prepared records, manifest paths and `PASS` repeatability messages. Export the created files if you need to retain the runtime results; Colab `/content` storage is temporary.

## Run from a local clone (optional)

1. Restore the two PDFs into `data/raw/` following [the raw input instructions](../data/raw/README.md). Both file hashes must match the source register.
2. Start Jupyter/VS Code with the repository root (or `notebooks/`) as the working directory.
3. Install `pypdf` if not already installed (`py -m pip install pypdf` on Windows); the notebook also contains an installation cell designed for Colab.
4. Execute notebook cells from the beginning. The `BASE_DIR` setup now resolves the repository path rather than the original student's `.../Assignment` folder.

## Published versus historical JSONL bytes

The original Week 3 manifests record **537,464 bytes** and SHA-256 `7790007170745e2008690b80411c0cf943aad3f9b71efe5c3cf606371c15694f` for both Part B and Part C outputs. An initial Git commit converted the 726 Windows CRLF record separators to Unix LF, leaving 536,738-byte published copies. This was a Git line-ending normalization artifact, not a reported change to the parsed record content.

The Topic 3 cleanup restores the original CRLF separators and adds `*.jsonl -text` to `.gitattributes`, so Git preserves the recorded byte sequence rather than normalizing it. The notebook's future export cells explicitly write CRLF-separated JSONL on either platform. The [verification script](../scripts/verify_week3_artifacts.py) compares both published outputs with the historical manifest hashes and checks record structure.

**Expected historical evidence:** 2 sources, 252 PDF pages, 726 paragraph-aware records (341 from Volume 1; 385 from Volume 2), 714 fixed-size comparison chunks, two Part B lineage entries, and Part C repeatability PASS.

## Limitations and integrity boundaries

- Notebook output cells show historical results and machine-specific paths. Editing setup code does **not** constitute a new successful Colab run.
- The precise `pypdf` version used in the original run was not recorded. Re-extraction under another version may differ; do not assume byte-level reproduction until checksums match.
- Prepared chunks have `page: null`: document-level provenance exists, but page-level citation cannot yet meet FR3 in a full RAG application.
- Source manifests still contain historical access/version placeholders. The supplemental source register identifies the documents and distribution statement without rewriting past records.
- The checks here are structural and deterministic-output checks, **not** an AI accuracy, retrieval, or safe-answer evaluation. These belong to later development.
