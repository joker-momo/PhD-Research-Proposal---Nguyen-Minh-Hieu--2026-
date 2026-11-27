"""Build a bounded correction packet retaining the original physical PDF page map."""

import argparse
import re
import shutil
import uuid
from collections import defaultdict
from pathlib import Path

import pymupdf

from prepare import HERE, LIMITED, PROJECT, digest, dump, rows
from review_sources import load


PAGE = re.compile(r"\b(?:pp?|pages?)\.?\s*(\d+)(?:\s*[–−-]\s*(\d+))?", re.IGNORECASE)


def page_numbers(text):
    pages = set()
    for start, end in PAGE.findall(text):
        start = int(start)
        end = int(end) if end else start
        pages.update(range(start, min(start + 4, end) + 1))
    return pages


def compact_images(path):
    compact = path.with_suffix(".compact.pdf")
    with pymupdf.open(path) as readable, pymupdf.open() as image_pdf:
        for page in readable:
            pixmap = page.get_pixmap(dpi=120, colorspace=pymupdf.csGRAY, alpha=False)
            output = image_pdf.new_page(width=page.rect.width, height=page.rect.height)
            output.insert_image(output.rect, stream=pixmap.tobytes("jpg", jpg_quality=48))
        image_pdf.save(compact, garbage=4, deflate=True, use_objstms=1, no_new_id=True)
    if compact.stat().st_size < path.stat().st_size:
        compact.replace(path)
        return True
    compact.unlink()
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=False)
    phase = load(HERE / "phase_manifest.json")
    selected = defaultdict(list)
    for row in rows(args.review):
        ident = row["packet_id"]
        if ident in LIMITED:
            continue
        if (row["gemini_semantic"] != "FAIL"
                and row["gemini_locator_check"] != "SCHEMA_INVALID"
                and row["gemini_status"] != "MISSING_PASS"):
            continue
        description = row["gemini_semantic_reason"] or row["gemini_locator_check"] or "Provider row missing."
        locators = (row["gemini_semantic_recheck"], row["codex_locator"], row["gemini_locator"],
                    row["suggested_locator"], description)
        pages = sorted(set().union(*(page_numbers(text) for text in locators)))
        selected[ident].append({
            "kind": row["kind"], "key": row["key"], "prior_issue": description,
            "original_pdf_pages": pages,
        })
    source_map = {}
    for ident, items in sorted(selected.items()):
        source = phase["pdfs"][ident]
        original = PROJECT / source["source_pdf"]
        if digest(original) != source["sha256"]:
            raise ValueError(f"Source PDF hash changed for {ident}")
        subset_name = f"{ident}-selected-pages.pdf"
        with pymupdf.open(original) as original_pdf, pymupdf.open() as subset:
            relevant = {page for item in items for page in item["original_pdf_pages"]}
            if not relevant:
                raise ValueError(f"No correction page for {ident}")
            pages = sorted(relevant & set(range(1, len(original_pdf) + 1)) | {1})
            for page in pages:
                subset.insert_pdf(original_pdf, from_page=page - 1, to_page=page - 1)
            subset.save(args.destination / subset_name, garbage=4, deflate=True, use_objstms=1, no_new_id=True)
        source_map[ident] = {
            "attachment": subset_name, "original_sha256": source["sha256"],
            "attachment_physical_to_original_physical": pages, "targets": items,
        }
    shutil.copyfile(PROJECT / phase["pdfs"]["HKF-118"]["source_pdf"], args.destination / "HKF-118.pdf")
    max_bytes = 8 * 1024 * 1024
    candidates = sorted(source_map.values(), key=lambda row: -(args.destination / row["attachment"]).stat().st_size)
    for row in candidates:
        if sum(p.stat().st_size for p in args.destination.iterdir()) < max_bytes - 100000:
            break
        if compact_images(args.destination / row["attachment"]):
            row["render"] = "Original PDF pages rendered in grayscale at 120 dpi for attachment-size limit"
    text_first = sorted(source_map, key=lambda ident: (
        any(re.search(r"table|fig(?:ure)?\.|printed cell|equation", row["prior_issue"], re.IGNORECASE)
            for row in source_map[ident]["targets"]),
        -(args.destination / source_map[ident]["attachment"]).stat().st_size,
    ))
    for ident in text_first:
        if sum(p.stat().st_size for p in args.destination.iterdir()) < max_bytes - 100000:
            break
        row = source_map[ident]
        replaced = args.destination / row["attachment"]
        attachment = replaced.with_suffix(".txt")
        with pymupdf.open(PROJECT / phase["pdfs"][ident]["source_pdf"]) as original:
            attachment.write_text("\n".join(
                f"===== {ident} original physical page {page} =====\n{original[page - 1].get_text()}"
                for page in row["attachment_physical_to_original_physical"]
            ), encoding="utf-8")
        replaced.unlink()
        row.update(attachment=attachment.name, render="Text extracted by original physical page with PyMuPDF 1.26.7")
    dump(args.destination / "targets.json", source_map)
    files = list(args.destination.iterdir())
    if len(files) > 50 or sum(path.stat().st_size for path in files) > max_bytes:
        raise ValueError("Correction context exceeds bridge limits")
    total = sum(len(items) for items in selected.values())
    linked = [b["message_id"] for b in phase["batches"] if selected.keys() & set(b["reports"])]
    message = uuid.uuid5(uuid.NAMESPACE_URL, f"hk261:source-review-887:correction:{digest(args.destination / 'targets.json')}")
    manifest = {"number": 9, "reports": sorted(selected), "keys": total, "message_id": str(message),
                "linked_message_ids": linked, "assets": {p.name: digest(p) for p in sorted(files)}}
    dump(args.destination.parent / "correction_manifest.json", manifest)
    print(total)


if __name__ == "__main__":
    main()
