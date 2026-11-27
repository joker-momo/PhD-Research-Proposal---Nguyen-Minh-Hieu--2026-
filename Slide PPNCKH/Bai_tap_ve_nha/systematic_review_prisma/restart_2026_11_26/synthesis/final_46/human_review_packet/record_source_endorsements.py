"""Transcribe the recorded HK261 endorsements without upgrading source claims."""

import argparse
import csv
import io
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

PACKET = Path(__file__).resolve().parent
EVIDENCE = PACKET.parents[2] / "integrity/source_review_887/source_review_887.csv"
KEY = ("packet_id", "check_type", "check_key")
ANSWERS = (
    "verified_value_or_judgment", "unit", "workload_conditions_and_denominator",
    "original_page_and_locator", "reason_or_verbatim_anchor", "reviewer_id", "date",
)
COVERAGE = re.compile(r"^(VERIFIED_EXACT(?: with PRINTED_UNRESOLVED entries)?|PLOT_ONLY|PRINTED_UNRESOLVED)\b")
UNIT = r"%|ms/image|ms|s|seconds|mJ|J/token|J|Wh|W|fps|FPS|Mbps|TOPS|MB|MiB|GB|GFLOPs|tokens/s|frames/s"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return tuple(reader.fieldnames), list(reader)


def outcome_fields(finding):
    before, marker, conditions = finding.partition("Conditions: ")
    explicit = re.search(rf"\(unit:\s*({UNIT})(?=,|\))", before)
    metric, method, _ = before.partition(". Method:")
    leading = re.search(rf"\d\s*({UNIT})$", metric) if method else None
    unit = explicit or leading
    return unit.group(1) if unit else "", conditions if marker else ""


def adjudicated(row, reviewer):
    if row["author_attention"] == "RESTRICTED_SOURCE":
        if reviewer == "R1":
            return row["codex_status"], "", "", (
                "Codex: source scope limited. This form records the disposition only. "
                "See the restricted-source flag in the source review."
            ), False
        return "UNRESOLVED", "", "", "Gemini: original-source access limited.", False

    if reviewer == "R1":
        status, finding = row["codex_status"], row["codex_finding"]
        anchor = " | ".join(filter(None, (row["codex_excerpt"], row["codex_note"])))
        return status, finding, row["codex_locator"], f"Codex: {anchor}", bool(finding)

    channel = "correction" if row["correction_status"] else "gemini"
    label = "Gemini correction" if channel == "correction" else "Gemini"
    status = row[f"{channel}_status"]
    verdict = row[f"{channel}_semantic"]
    explanation = row[f"{channel}_semantic_reason"]
    recheck = row[f"{channel}_semantic_recheck"]
    audit = f"{label} ({status}; source check {verdict}): {explanation}"
    if verdict in {"FAIL", "NO_RESULT"}:
        return "UNRESOLVED", "", "", audit, False
    if verdict == "PARTIAL":
        locators = " | ".join(
            dict.fromkeys(anchor.split(": ", 1)[0] for anchor in recheck.split(" | ")
                          if anchor.startswith("PDF p."))
        )
        return "PARTIAL", explanation, locators, f"{audit} | Recheck: {recheck}".rstrip(), False
    if verdict != "PASS":
        raise ValueError(f"Unexpected source verdict: {verdict}")
    finding = row[f"{channel}_finding"]
    anchor = row[f"{channel}_excerpt"]
    return status, finding, row[f"{channel}_locator"], f"{audit} | {anchor}", True


def fill_row(row, reviewer, recorded_date):
    status, finding, locator, reason, extract = adjudicated(row, reviewer)
    unit, conditions = outcome_fields(finding) if extract and row["kind"] == "outcome" else ("", "")
    coverage = COVERAGE.match(finding) if row["kind"] == "report_coverage" else None
    judgment = " | ".join(filter(None, (status, finding)))
    if coverage:
        judgment = coverage.group(1)
        reason = f"{finding} | Source disposition: {status} | {reason}"
    return status, dict(zip(ANSWERS, (judgment, unit, conditions, locator, reason, reviewer, recorded_date)))


def render(reviewer, packet, source, recorded_date):
    path = packet / reviewer / "source_verification.csv"
    fields, rows = read_csv(path)
    keys = [tuple(row[field] for field in KEY) for row in rows]
    if len(keys) != 887 or len(set(keys)) != 887 or set(keys) != source.keys():
        raise ValueError(f"{reviewer} does not match the 887 frozen source keys")
    if fields[-len(ANSWERS):] != ANSWERS:
        raise ValueError(f"{reviewer} has unexpected answer columns")

    output, stats = io.StringIO(newline=""), Counter()
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for original, key in zip(rows, keys):
        status, answers = fill_row(source[key], reviewer, recorded_date)
        stats[status] += 1
        if any(original[field] for field in ANSWERS) and any(
            original[field] != answers[field] for field in ANSWERS
        ):
            raise ValueError(f"{reviewer} has a different existing response for {key}")
        writer.writerow(original | answers)
    return path, output.getvalue().encode(), dict(sorted(stats.items()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("recorded_date", type=date.fromisoformat)
    parser.add_argument("--packet", type=Path, default=PACKET)
    parser.add_argument("--check", action="store_true", help="Verify exact output and perform no writes.")
    args = parser.parse_args()
    _, rows = read_csv(EVIDENCE)
    source = {(row["packet_id"], row["kind"], row["key"]): row for row in rows}
    if len(source) != 887 or len(rows) != 887:
        raise ValueError("Expected 887 distinct source rows")
    results = {reviewer: render(reviewer, args.packet, source, args.recorded_date.isoformat())
               for reviewer in ("R1", "R2")}
    for path, payload, _ in results.values():
        if args.check and path.read_bytes() != payload:
            raise ValueError(f"Saved file differs from the reproducible output: {path}")
        if not args.check and path.read_bytes() != payload:
            temporary = path.with_suffix(".csv.tmp")
            temporary.write_bytes(payload)
            temporary.replace(path)
    print(json.dumps({reviewer: result[2] for reviewer, result in results.items()}, sort_keys=True))


if __name__ == "__main__":
    main()
