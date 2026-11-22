#!/usr/bin/env python3
"""Read-only verification of published Topic 3 JSONL artifacts against Week 3 evidence."""
from __future__ import annotations
import collections
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PART_B = ROOT / "data/processed/prepared_text.jsonl"
PART_C = ROOT / "data/pipeline_v1/documents/prepared_text.jsonl"
MANIFEST = ROOT / "data/week3_manifest.json"
RUN = ROOT / "data/pipeline_v1/documents/pipeline_manifest.json"
EXPECTED_COUNT = 726


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    run = json.loads(RUN.read_text(encoding="utf-8"))
    expected = {x["prepared_sha256"] for x in manifest["records"]}
    expected.update(run["validation"]["output_sha256"])
    if len(expected) != 1:
        raise AssertionError("Historical manifests disagree on output fingerprint")
    expected_hash = expected.pop()
    parts = [PART_B, PART_C]
    contents = [p.read_bytes() for p in parts]
    if contents[0] != contents[1]:
        raise AssertionError("Part B and Part C JSONL bytes differ")
    for path, blob in zip(parts, contents):
        actual = sha256(blob)
        print(f"{path.relative_to(ROOT)}: {len(blob):,} bytes; SHA-256 {actual}")
        if actual != expected_hash:
            crlf = blob.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
            if sha256(crlf) == expected_hash:
                raise AssertionError(
                    "Git line-ending conversion detected. Run the Topic 3 update "
                    "to restore historical CRLF bytes, then verify again."
                )
            raise AssertionError("Artifact does not match the historical manifest")
    assert len(contents[0]) == run["validation"]["output_bytes"][0], "Output size mismatch"
    rows = []
    for lineno, line in enumerate(contents[0].splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL record on line {lineno}") from exc
    assert len(rows) == EXPECTED_COUNT, f"Expected {EXPECTED_COUNT}, got {len(rows)}"
    assert len({r["record_id"] for r in rows}) == len(rows), "Duplicate record IDs"
    assert all(r.get("text", "").strip() for r in rows), "Empty text chunk"
    assert all(len(r["text"]) <= 500 for r in rows), "Chunk size exceeded"
    fingerprints = {r["source_filename"]: r["source_sha256"] for r in manifest["records"]}
    assert all(r["source"] in fingerprints and r["source_sha256"] == fingerprints[r["source"]] for r in rows), "Source lineage mismatch"
    counts = collections.Counter(r["source"] for r in rows)
    assert counts == {"mechanical_science_vol1.pdf": 341, "mechanical_science_vol2.pdf": 385}, f"Unexpected per-source counts: {counts}"
    assert all(r.get("page") is None for r in rows), "Historical page provenance unexpectedly changed"
    print(f"PASS: {len(rows)} valid, nonempty records; no duplicate IDs; both sources verified by recorded hashes")
    print("PASS: Part B, Part C, output size and SHA-256 match historical manifests")
    print("NOTE: This validates committed artifacts; it does not rerun PDF extraction or assert page-level citations.")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, FileNotFoundError, KeyError) as e:
        print("FAIL:", e, file=sys.stderr)
        sys.exit(1)
