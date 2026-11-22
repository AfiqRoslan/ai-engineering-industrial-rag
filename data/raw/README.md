# Raw PDF data — how to reproduce the Week 3 inputs

The original PDF files used in the Week 3 pipeline were stored locally in
`data/raw/`. They **are not committed to GitHub**. This tracked README keeps
`data/raw/` visible and provides official links for downloading the inputs.

| ID | Original PDF / official download | Save locally as | Week 3 pages |
|---|---|---|---:|
| S01 | [DOE Mechanical Science, Volume 1 (1993)](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL1.pdf) | `mechanical_science_vol1.pdf` | 122 |
| S02 | [DOE Mechanical Science, Volume 2 (1993)](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL2.pdf) | `mechanical_science_vol2.pdf` | 130 |

**How to restore the local raw files:** Download the two PDFs from the links
above into this directory and rename them to the filenames in the table. From
PowerShell, while in the repository root, you can use:

```powershell
Invoke-WebRequest -Uri "https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL1.pdf" -OutFile "data/raw/mechanical_science_vol1.pdf"
Invoke-WebRequest -Uri "https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1018-93_VOL2.pdf" -OutFile "data/raw/mechanical_science_vol2.pdf"
Get-FileHash "data/raw/mechanical_science_vol1.pdf" -Algorithm SHA256
Get-FileHash "data/raw/mechanical_science_vol2.pdf" -Algorithm SHA256
```

The Week 3 pipeline recorded the following fingerprints **for its original local input files**:

| ID | SHA-256 from the Week 3 execution manifest |
|---|---|
| S01 | `c1e37601164acf95cbaecad93b1db9841ad8d7670bf30a4fdd6ff0a87c6a0070` |
| S02 | `f569f8de24e0c9b23fa8f5c965c3d0740daa5e41db0f029ad8e3893d3fd9e2fd` |

If a newly downloaded copy does not have the same hash, **do not claim it is
byte-identical** to the Week 3 input. Record the new hash and rerun the
preparation pipeline if exact reproduction is required. Source URLs, editions,
and publisher can be checked in the [source register](../../docs/source_register.md)
and [structured source manifest](source_manifest.json).

**Output lineage:** These two sources feed
`data/processed/prepared_text.jsonl` (Part B) and
`data/pipeline_v1/documents/prepared_text.jsonl` (Part C). The historical
execution manifests are `data/week3_manifest.json` and
`data/pipeline_v1/documents/pipeline_manifest.json`. No embedding or retrieval
index was created in Week 3.

**Scope and rights:** Both January 1993 handbooks carry Distribution Statement A
(approved for public release; unlimited distribution). Any additional
processing or reuse requirements should still be reviewed, especially before
sharing the derived content or using an external model provider. These are
educational fundamentals, not current maintenance instructions.
