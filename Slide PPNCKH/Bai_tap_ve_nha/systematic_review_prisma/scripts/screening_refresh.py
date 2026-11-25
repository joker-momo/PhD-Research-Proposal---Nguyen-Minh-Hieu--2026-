"""Atomic validation helpers for the frozen 46-report screening pack."""

import copy
import hashlib
import json
import logging
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    from .screening_paths import resolve_screening_path, to_screening_locator
except ImportError:  # Direct execution through prepare_46screening.py
    from screening_paths import resolve_screening_path, to_screening_locator


logging.disable(logging.CRITICAL)
ROOT = Path(__file__).resolve().parents[1]
SCREENING_ROOT = ROOT / "screening_46"
INPUT_MARKER = "Input records (title_hint is NOT verified metadata):\n"
GROUP_RANGES = ((0, 6), (6, 12), (12, 18), (18, 24),
                (24, 30), (30, 36), (36, 41), (41, 46))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_checksum_ledger(path: Path) -> dict[str, str]:
    ledger = {}
    for line in path.read_text().splitlines():
        digest, locator = line.split("  ", 1)
        if locator in ledger:
            raise ValueError(f"duplicate checksum locator: {locator}")
        ledger[locator] = digest
    return ledger


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as handle:
            handle.write(content)
            temporary = Path(handle.name)
        os.replace(temporary, path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def validate_and_publish_staged_texts(
    staged_root: Path, live_root: Path, ledger: dict[str, str]
) -> None:
    """Validate every staged text before filling any missing live text file."""
    expected = {path: digest for path, digest in ledger.items()
                if path.startswith("text/")}
    if not expected:
        raise ValueError("checksum ledger has no text entries")

    missing_live = []
    for locator, expected_digest in expected.items():
        staged = staged_root / locator
        if not staged.is_file():
            raise ValueError(f"missing staged text: {locator}")
        observed = sha256(staged)
        if observed != expected_digest:
            raise ValueError(
                f"checksum mismatch for staged {locator}: "
                f"{observed} != {expected_digest}"
            )
        live = live_root / locator
        if live.exists():
            observed_live = sha256(live)
            if observed_live != expected_digest:
                raise ValueError(
                    f"checksum mismatch for live {locator}: "
                    f"{observed_live} != {expected_digest}"
                )
        else:
            missing_live.append((staged, live, expected_digest))

    for staged, live, expected_digest in missing_live:
        live.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=live.parent, delete=False) as handle:
                temporary = Path(handle.name)
            shutil.copy2(staged, temporary)
            if sha256(temporary) != expected_digest:
                raise RuntimeError(f"temporary checksum mismatch: {live}")
            os.replace(temporary, live)
        finally:
            if temporary and temporary.exists():
                temporary.unlink()


def _absolute_evidence_record(record: dict, evidence_root: Path) -> dict:
    result = copy.deepcopy(record)
    for field in ("source", "pdf", "text"):
        path = resolve_screening_path(evidence_root, result[field])
        if not path.is_file():
            raise FileNotFoundError(f"missing {field} evidence: {path}")
        result[field] = str(path)
    return result


def _has_dispatch_artifact(screening_root: Path, number: int) -> bool:
    stem = f"batch_{number:02}"
    return any(
        any((screening_root / directory).glob(stem + "*"))
        for directory in ("results", "reviews")
    )


def _render_undispatched_briefs(
    project_root: Path,
    screening_root: Path,
    items: list[dict],
    evidence_root: Optional[Path] = None,
) -> tuple[dict[int, str], list[tuple[Path, str]]]:
    del project_root  # The committed prefix already contains canonical protocols.
    if len(items) != 46:
        raise ValueError(f"expected 46 manifest records, observed {len(items)}")
    evidence_root = (evidence_root or screening_root).resolve()
    preserved_numbers = {1, 2, 3} | {
        number for number in range(4, 9)
        if _has_dispatch_artifact(screening_root, number)
    }
    preserved = {
        number: sha256(screening_root / "briefs" / f"batch_{number:02}.md")
        for number in preserved_numbers
    }

    rendered = []
    for number, (start, end) in enumerate(GROUP_RANGES, 1):
        if number in preserved_numbers:
            continue
        path = screening_root / "briefs" / f"batch_{number:02}.md"
        current = path.read_text()
        if INPUT_MARKER not in current:
            raise ValueError(f"brief {number} lacks the input-record marker")
        prefix, _ = current.split(INPUT_MARKER, 1)
        records = [_absolute_evidence_record(item, evidence_root)
                   for item in items[start:end]]
        rendered.append(
            (path, prefix + INPUT_MARKER
             + json.dumps(records, ensure_ascii=False, indent=2) + "\n")
        )
    return preserved, rendered


def _publish_brief_updates(
    preserved: dict[int, str], rendered: list[tuple[Path, str]], screening_root: Path
) -> None:
    for path, content in rendered:
        atomic_write_text(path, content)

    for number, expected_digest in preserved.items():
        path = screening_root / "briefs" / f"batch_{number:02}.md"
        if sha256(path) != expected_digest:
            raise RuntimeError(f"dispatched brief {number} was modified")


def write_pending_briefs(
    project_root: Path,
    screening_root: Path,
    items: list[dict],
    evidence_root: Optional[Path] = None,
) -> None:
    """Refresh only briefs with no transport, result, or review artifact."""
    preserved, rendered = _render_undispatched_briefs(
        project_root, screening_root, items, evidence_root
    )
    _publish_brief_updates(preserved, rendered, screening_root)


def publish_refresh_metadata(
    manifest_path: Path,
    manifest_content: str,
    project_root: Path,
    screening_root: Path,
    items: list[dict],
    evidence_root: Optional[Path] = None,
) -> None:
    """Validate every brief input before publishing manifest or brief metadata."""
    preserved, rendered = _render_undispatched_briefs(
        project_root, screening_root, items, evidence_root
    )
    atomic_write_text(manifest_path, manifest_content)
    _publish_brief_updates(preserved, rendered, screening_root)


def portable_provenance(locator: str) -> str:
    if locator.startswith("legacy-root:"):
        return locator
    marker = "/systematic_review_prisma/"
    normalized = locator.replace("\\", "/")
    if marker in normalized:
        return "legacy-root:" + normalized.split(marker, 1)[1]
    if Path(normalized).is_absolute():
        raise ValueError(f"absolute provenance cannot be made portable: {locator}")
    return locator


def refresh_frozen_pack() -> dict:
    """Re-extract into staging, verify the ledger, then refresh metadata."""
    if ".codex" in ROOT.parts and "worktrees" in ROOT.parts:
        raise RuntimeError("run refresh only from the canonical root checkout")
    try:
        from pypdf import PdfReader
    except ImportError as error:
        raise RuntimeError("pypdf is required for extraction validation") from error

    manifest_path = SCREENING_ROOT / "manifest.json"
    ledger_path = SCREENING_ROOT / "evidence_checksums.sha256"
    if not manifest_path.is_file() or not ledger_path.is_file():
        raise FileNotFoundError("manifest and evidence checksum ledger are required")
    items = json.loads(manifest_path.read_text())["records"]
    if not (len(items) == len({item["id"] for item in items})
            == len({item["doi"] for item in items}) == 46):
        raise ValueError("manifest must contain 46 unique IDs and DOIs")
    ledger = parse_checksum_ledger(ledger_path)
    pdf_entries = {path: digest for path, digest in ledger.items()
                   if path.startswith("pdf/")}
    text_entries = {path: digest for path, digest in ledger.items()
                    if path.startswith("text/")}
    if len(pdf_entries) != 46 or len(text_entries) != 46 or len(ledger) != 92:
        raise ValueError("evidence ledger must contain 46 PDFs and 46 texts")

    with tempfile.TemporaryDirectory(dir=SCREENING_ROOT) as directory:
        staged_root = Path(directory)
        (staged_root / "text").mkdir()
        for item in items:
            pdf_path = resolve_screening_path(SCREENING_ROOT, item["pdf"])
            pdf_locator = to_screening_locator(SCREENING_ROOT, pdf_path)
            digest = sha256(pdf_path)
            if pdf_entries.get(pdf_locator) != digest or item.get("sha256") != digest:
                raise ValueError(f"PDF checksum mismatch: {item['id']}")
            reader = PdfReader(pdf_path)
            raw_pages = [page.extract_text() or "" for page in reader.pages]
            replacement_count = sum(
                sum(0xD800 <= ord(character) <= 0xDFFF for character in page)
                for page in raw_pages
            )
            pages = [page.encode("utf-8", errors="replace").decode("utf-8")
                     for page in raw_pages]
            if not pages or not all(page.strip() for page in pages):
                raise ValueError(f"empty extracted page: {item['id']}")
            text_locator = f"text/{item['id']}.txt"
            text = "\n\n".join(
                f"=== PDF PAGE {index} ===\n{page}"
                for index, page in enumerate(pages, 1)
            )
            (staged_root / text_locator).write_text(text)
            item.update(
                source=pdf_locator,
                source_provenance=portable_provenance(
                    item.get("source_provenance", item.get("source", ""))
                ),
                pdf=pdf_locator,
                text=text_locator,
                sha256=digest,
                pages=len(pages),
                extraction_surrogates_replaced=replacement_count,
                intake_status="FILE_READABLE_IDENTITY_AND_ELIGIBILITY_REVIEW_PENDING",
            )

        validate_and_publish_staged_texts(staged_root, SCREENING_ROOT, ledger)

    for locator, expected_digest in ledger.items():
        if sha256(SCREENING_ROOT / locator) != expected_digest:
            raise ValueError(f"live evidence checksum mismatch: {locator}")

    manifest = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "cutoff": "2026-11-25",
        "records": items,
        "record_count": 46,
        "duplicate_dois": 0,
        "boundary": (
            "Supplied PDF inventory; not 46 eligible studies or proof of "
            "provenance/version correspondence."
        ),
    }
    publish_refresh_metadata(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        ROOT,
        SCREENING_ROOT,
        items,
    )
    return {
        "records": len(items),
        "batches": len(GROUP_RANGES),
        "group_sizes": [end - start for start, end in GROUP_RANGES],
        "manifest": str(manifest_path),
        "accepted_briefs_preserved": [1, 2, 3],
        "pending_briefs_refreshed": [4, 5, 6, 7, 8],
    }


def main() -> None:
    print(json.dumps(refresh_frozen_pack()))
