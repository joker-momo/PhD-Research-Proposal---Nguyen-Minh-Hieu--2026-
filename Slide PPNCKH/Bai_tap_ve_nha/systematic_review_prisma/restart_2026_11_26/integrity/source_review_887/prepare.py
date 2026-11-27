"""Produce disjoint Gemini review batches from the original HK261 PDFs."""

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import uuid
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESTART = HERE.parents[1]
PROJECT = RESTART.parent
FINAL = RESTART / "synthesis/final_46"
PACKET = FINAL / "human_review_packet"
MASKED = RESTART / "fulltext_retrieval/pdf/human_review_full_136"
PREFLIGHT = "HKF-118.pdf"
LIMITED = {"HKF-031", "HKF-130"}
IEEE_R0082 = RESTART / "fulltext_retrieval/pdf/R0082_ieee_wcnc_2023.pdf"


def rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def physical_text(files, workspace):
    parser = workspace / "pdfkit_pages"
    subprocess.run(["swiftc", "-O", str(FINAL / "pdfkit_pages.swift"), "-o", str(parser)], check=True)
    original_pages = workspace / "pages"
    original_pages.mkdir(exist_ok=True)
    for packet_id, pdf in files.items():
        (original_pages / f"{packet_id}.json").write_bytes(subprocess.check_output([str(parser), str(pdf)]))
    return original_pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    workspace = args.workspace
    workspace.mkdir(parents=True, exist_ok=True)
    targets = rows(PACKET / "R1/source_verification.csv")
    peer = rows(PACKET / "R2/source_verification.csv")
    fields = ("packet_id", "check_type", "check_key")
    expected = {tuple(r[field] for field in fields) for r in targets}
    if len(targets) != 887 or len(peer) != 887 or len(expected) != 887 or expected != {
        tuple(r[field] for field in fields) for r in peer
    }:
        raise ValueError("R1/R2 inventory does not match 887 distinct shared keys")
    outcomes = {r["outcome_id"]: r for r in rows(FINAL / "outcomes.csv")}
    key = {r["packet_id"]: r for r in rows(PACKET / "coordinator/key.csv") if r["frozen_disposition"] == "INCLUDE"}
    by_report = defaultdict(list)
    for r in targets:
        prompt = [r[field] for field in ("check_type", "check_key", "suggested_physical_page", "suggested_section")]
        if r["check_type"] == "outcome" and r["packet_id"] not in LIMITED:
            o = outcomes[f"{key[r['packet_id']]['record_id']}-{r['check_key']}"]
            prompt.extend(o[field] for field in ("domain", "metric", "method"))
        by_report[r["packet_id"]].append(prompt)
    if len(key) != 46 or key.keys() != by_report.keys():
        raise ValueError("The source verification packet must match the 46 frozen reports")
    files = {}
    for packet_id, r in key.items():
        original = PROJECT / r["source_pdf"]
        masked = MASKED / f"{packet_id}.pdf"
        if digest(original) != r["sha256"] or digest(masked) != r["sha256"]:
            raise ValueError(f"PDF version mismatch for {packet_id}")
        files[packet_id] = original
    ieee_hash = json.loads((FINAL / "r0082_publisher_crosscheck.json").read_text())["ieee_pdf_sha256"]
    if digest(IEEE_R0082) != ieee_hash:
        raise ValueError("The publisher PDF for R0082 changed")
    pages = physical_text(files | {"HKF-115-IEEE": IEEE_R0082}, workspace)
    sorted_ids = sorted(key, key=lambda packet_id: key[packet_id]["record_id"])
    counts = Counter(r["check_type"] for r in targets)
    manifest = {"version": 1, "keys": 887, "reports": 46, "counts": dict(counts), "batches": [],
                "supplemental_pdf": {"packet_id": "HKF-115", "pdf": str(IEEE_R0082.relative_to(PROJECT)), "sha256": ieee_hash}}
    for offset in range(0, len(sorted_ids), 6):
        number = 1 + offset // 6
        group = sorted_ids[offset:offset + 6]
        batch = workspace / f"batch-{number:02}"
        batch.mkdir(exist_ok=True)
        target_map = {}
        for packet_id in group:
            target_map[packet_id] = by_report[packet_id]
            if packet_id in LIMITED:
                # No original or operational material for the combat study is sent.
                continue
            source = json.loads((pages / f"{packet_id}.json").read_text(encoding="utf-8"))
            parts = [f"===== {packet_id} PDF page {i}/{len(source)} =====\n{page}"
                     for i, page in enumerate(source, 1)]
            # The desktop reader has previously skipped the tail of large text attachments.
            chunk = ""
            part = 1
            for page in parts:
                if chunk and len((chunk + page).encode("utf-8")) > 80000:
                    (batch / f"{packet_id}-{part:02}.txt").write_text(chunk, encoding="utf-8")
                    chunk = ""
                    part += 1
                chunk += page + "\n"
            (batch / f"{packet_id}-{part:02}.txt").write_text(chunk, encoding="utf-8")
        if "HKF-115" in group:
            ieee_pages = json.loads((pages / "HKF-115-IEEE.json").read_text())
            text = "\n".join(f"===== HKF-115 publisher PDF physical page {i}/{len(ieee_pages)} =====\n{p}"
                             for i, p in enumerate(ieee_pages, 1))
            (batch / "HKF-115-IEEE.txt").write_text(text, encoding="utf-8")
        shutil.copyfile(MASKED / PREFLIGHT, batch / PREFLIGHT)
        dump(batch / "targets.json", target_map)
        assets = {p.name: digest(p) for p in sorted(batch.iterdir()) if p.is_file()}
        if len(assets) > 50 or sum(p.stat().st_size for p in batch.iterdir()) > 8 * 1024 * 1024:
            raise ValueError(f"Batch {number} exceeds bridge limits")
        record = {"number": number, "reports": group, "keys": sum(len(target_map[i]) for i in group),
                  "message_id": str(uuid.uuid5(uuid.NAMESPACE_URL, f"hk261:source-review-887:v1:{number}")),
                  "assets": assets}
        manifest["batches"].append(record)
    manifest["restrictions"] = {packet_id: "Original omitted from Gemini context. Report inaccessible to Gemini."
                                for packet_id in sorted(LIMITED)}
    manifest["pdfs"] = {i: {field: r[field] for field in ("record_id", "source_pdf", "sha256")}
                        for i, r in sorted(key.items())}
    if args.write_manifest:
        dump(HERE / "phase_manifest.json", manifest)
    else:
        frozen = json.loads((HERE / "phase_manifest.json").read_text(encoding="utf-8"))
        if frozen != manifest:
            raise ValueError("Rebuilt source hashes or batch inventory diverged from the frozen manifest")
    print(json.dumps({str(r["number"]): r["keys"] for r in manifest["batches"]}))


if __name__ == "__main__":
    main()
