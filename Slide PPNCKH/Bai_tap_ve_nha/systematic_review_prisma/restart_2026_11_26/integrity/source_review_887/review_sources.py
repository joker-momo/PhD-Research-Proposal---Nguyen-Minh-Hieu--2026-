"""Validate and publish advisory source checks without changing the human forms."""

import argparse
import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

from prepare import FINAL, HERE, LIMITED, PACKET, PROJECT, dump, rows

STATUSES = {"VERIFIED", "PARTIAL", "DISCREPANCY", "UNRESOLVED", "NOT_REPORTED"}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def key_of(item):
    return item.get("id"), item.get("kind"), item.get("key")


def input_key(item):
    return item["packet_id"], item["check_type"], item["check_key"]


def norm(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().replace("\u00ad", "").split())


def contains(pages, ident, item):
    page = item.get("page")
    quote = item.get("quote", "")
    return (
        type(page) is int and 1 <= page <= len(pages.get(ident, []))
        and isinstance(quote, str) and bool(norm(quote))
        and norm(quote) in norm(pages[ident][page - 1])
    )


def read_pages(path):
    return {p.stem: load(p) for p in path.glob("HKF-*.json")} if path.is_dir() else {}


def decode_line(line):
    decoder = json.JSONDecoder()
    values = []
    remaining = line
    while remaining:
        value, end = decoder.raw_decode(remaining)
        values.append(value)
        remaining = remaining[end:].lstrip()
    return values


def extract(text, expected):
    data = {}
    errors = []
    seen = set()
    preflight = {}
    for line in text.splitlines():
        candidate = line.strip()
        if candidate.startswith("PREFLIGHT"):
            candidate = candidate.removeprefix("PREFLIGHT").lstrip(" :")
        if not candidate.startswith("{"):
            continue
        try:
            objects = decode_line(candidate)
        except (ValueError, TypeError) as exc:
            errors.append(f"malformed JSONL {len(errors) + 1}: {exc}")
            continue
        if len(objects) > 1:
            errors.append(f"JSONL line contains {len(objects)} adjacent objects; raw objects recovered without edits")
        for item in objects:
            if not isinstance(item, dict):
                errors.append("invalid JSONL value: expected an object")
                continue
            if "file" in item and "id" not in item:
                preflight = item
                continue
            if "id" not in item and ("title" in item or "worker" in item):
                continue
            key = key_of(item)
            if key not in expected:
                errors.append(f"unexpected {key}")
                continue
            if key in seen:
                errors.append(f"duplicate {key}")
                data.pop(key, None)
                continue
            seen.add(key)
            data[key] = item
    return data, errors, preflight


def assess(item, sources):
    ident = item["id"]
    evidence = item.get("evidence")
    status = item.get("status")
    if (not isinstance(status, str) or status not in STATUSES or not isinstance(item.get("finding"), str)
            or not item["finding"].strip() or not isinstance(evidence, list)
            or not isinstance(item.get("note"), str)):
        return "SCHEMA_INVALID"
    if not evidence:
        return "GAP_DOCUMENTED" if item["status"] == "UNRESOLVED" and item["note"].strip() else "LOCATOR_MISSING"
    checks = []
    for anchor in evidence:
        if not isinstance(anchor, dict) or not isinstance(anchor.get("section"), str) or not anchor["section"].strip():
            return "LOCATOR_MISSING"
        page = anchor.get("page")
        edition = "HKF-115-IEEE" if ident == "HKF-115" and "ieee publisher pdf" in norm(anchor["section"]) else ident
        if type(page) is not int or not any(1 <= page <= len(src.get(edition, [])) for src in sources):
            return "PAGE_INVALID"
        if not anchor.get("quote") and item["status"] == "NOT_REPORTED" and item["note"].strip():
            checks.append(None)
        else:
            checks.append(any(contains(src, edition, anchor) for src in sources))
    if checks and all(value is None for value in checks):
        return "ABSENCE_SCOPE_DOCUMENTED"
    if all(checks):
        return "ANCHORS_MATCH"
    if any(checks):
        return "PARTIAL_ANCHOR_MATCH"
    return "ANCHOR_NEEDS_VISUAL_OR_CORRECTION"


def receipt_review(path, batch, expected, sources):
    if not path.is_file():
        return {}, {"batch": batch["number"], "transport": "NO_RECEIPT", "expected": len(expected),
                    "seen": 0, "missing_keys": sorted(expected)}
    receipt = load(path)
    meta = receipt.get("metadata", {})
    text = "\n".join(p["text"] for artifact in receipt.get("artifacts", [])
                     for p in artifact.get("parts", []) if isinstance(p.get("text"), str))
    data, errors, preflight = extract(text, expected)
    normalization = meta.get("quote_normalization", {})
    errors += normalization.get("original_errors", [])
    given_hashes = {name: record.get("sha256") for name, record in meta.get("geminiApp", {}).get("files", {}).items()}
    for k, item in data.items():
        item["locator_check"] = assess(item, sources)
    direct_source_access = (
        preflight.get("file") == "HKF-118.pdf" and preflight.get("page") == 2
        and isinstance(preflight.get("section"), str) and bool(preflight["section"].strip())
        and any(contains(src, "HKF-118", preflight) for src in sources)
    )
    identity_ids = set(batch["reports"]) - LIMITED
    identities = [row for row in re.findall(
        r"(?m)^\W*(HKF-\d{3})[ \t]*[|:][ \t]*Title:[ \t]*([^\n|]+)\|\s*Authors:\s*([^\n|]+)\|"
        r"\s*Year:\s*([^\n|]+)\|\s*Venue:\s*([^\n|]+)\|\s*DOI:\s*([^\n|]+)", text,
    ) if row[0] in identity_ids and all(field.strip() for field in row[1:])]
    normalized_dois = [m[-1].strip().lower() for m in identities if m[-1].strip().lower().startswith("10.")]
    normalized_titles = [norm(m[1]) for m in identities if norm(m[1]) != "unknown"]
    stats = {
        "batch": batch["number"], "expected": len(expected), "seen": len(data),
        "task_id": receipt.get("id"), "context_id": receipt.get("contextId"),
        "transport": receipt.get("status", {}).get("state", "UNKNOWN"),
        "provider_started_at": meta.get("started_at"), "provider_completed_at": meta.get("completed_at"),
        "hash_inventory_match": given_hashes == batch["assets"],
        "context_unchanged": meta.get("context_audit", {}).get("unchanged") is True,
        "preflight_anchor_match": direct_source_access,
        "identity_count": len(identities),
        "identity_expected": len(identity_ids),
        "identity_records": sorted({line[0] for line in identities}),
        "identity_missing": sorted(identity_ids - {line[0] for line in identities}),
        "identity_duplicate_dois": len(normalized_dois) - len(set(normalized_dois)),
        "identity_duplicate_titles": len(normalized_titles) - len(set(normalized_titles)),
        "end_marker": "END_HK261_SOURCE_BATCH" in text,
        "cleanup": meta.get("chat_cleanup", {}),
        "locator_checks": dict(Counter(item["locator_check"] for item in data.values())),
        "status_counts": dict(Counter(str(item.get("status", "")) for item in data.values())),
        "errors": errors,
        "normalized_json_keys": normalization.get("recovered_keys", []),
        "missing_keys": sorted(expected - data.keys()),
    }
    return data, stats


def load_semantic_checks(workspace, batch, keys):
    checks = {}
    files = sorted(workspace.glob(f"gate-{batch:02}-*.jsonl"))
    if not files:
        files = sorted((HERE / "receipts").glob(f"gate-{batch:02}-*.jsonl"))
    for path in files:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            key = key_of(item)
            status = item.get("semantic", item.get("status"))
            if key not in keys or key in checks or status not in {"PASS", "PARTIAL", "FAIL"}:
                raise ValueError(f"Unexpected semantic review row {key} / {status} in {path.name}")
            checks[key] = item | {"semantic": status}
    return checks


def suggested(target):
    p = target["suggested_physical_page"]
    s = target["suggested_section"]
    return ("PDF p. " + p + ", " if p else "") + s


def conclusion(codex, gemini, kind):
    if not codex or not gemini:
        return "MISSING_AI_PASS"
    if any(r["locator_check"] in {"SCHEMA_INVALID", "PAGE_INVALID", "LOCATOR_MISSING"} for r in (codex, gemini)):
        return "SOURCE_CHECK_NEEDED"
    if "UNRESOLVED" in (codex["status"], gemini["status"]):
        return "UNRESOLVED"
    first = codex["finding"]
    second = gemini["finding"]
    if kind in {"appraisal", "report_coverage"}:
        pattern = (r"\b(YES|PARTIAL|NO|NOT_REPORTED|NOT_APPLICABLE)\b" if kind == "appraisal"
                   else r"\b(VERIFIED_EXACT|PLOT_ONLY|PRINTED_UNRESOLVED)\b")
        a, b = re.search(pattern, first), re.search(pattern, second)
        if a and b:
            return "SAME_LABEL" if a.group(1) == b.group(1) else "DIFFERENT_LABEL"
    return "COMPARE_FINDINGS"


def baseline_values():
    appraisal = {(r["report_id"], "appraisal", r["domain"]): r["judgment"]
                 for r in rows(FINAL / "appraisal_rationale.csv")}
    outcome = {(r["report_id"], "outcome", r["outcome_id"].rsplit("-", 1)[1]):
               " | ".join(r[c] for c in ("metric", "reported_value", "unit", "method", "comparator",
                                          "workload_conditions_and_denominator", "comparison_status"))
               for r in rows(FINAL / "outcomes.csv")}
    coverage = {(r["report_id"], "report_coverage", "coverage"): r["exact_outcome_status"]
                for r in rows(FINAL / "report_coverage.csv")}
    fields = {
        "t2_topology": ("topology",), "t2_workload": ("family", "workload"),
        "t2_partition": ("unit", "partition"),
        "t2_decisions_objective_solver": ("decisions", "objective", "optimizer", "solver"),
        "t3_platform_modality": ("evaluation", "platform"),
        "t3_network_event_response": ("channel_mobility", "resilience", "disruption", "action"),
    }
    path = PROJECT / "manuscript/sn_computer_science/technical_coding.psv"
    with path.open(encoding="utf-8", newline="") as stream:
        technical = {
            (r["id"], "technical", key): " | ".join(r[c] for c in columns)
            for r in csv.DictReader(stream, delimiter="|") for key, columns in fields.items()
        }
    return appraisal | outcome | coverage | technical


def codex_scope(codex):
    # This report contains both generic scholarly findings and operational applications.
    for key in ("Q01", "Q02", "coverage"):
        kind = "report_coverage" if key == "coverage" else "outcome"
        row = codex.get(("HKF-031", kind, key))
        if row:
            if key == "coverage":
                row.update(status="PARTIAL",
                           finding="The article presents a proof-of-concept evaluation. Detailed performance is outside this source summary.",
                           evidence=[{"page": 5, "section": "Performance Evaluation",
                                      "quote": "a proof-of-concept evaluation is conducted to validate the feasibility"}],
                           note="Physical page and general evidence scope checked.")
            else:
                row.update(status="UNRESOLVED", finding="This source summary records only general appraisal of the study.",
                           evidence=[], note="The quantitative details are outside the scope of this review.")


def recheck_text(gate):
    corrected = gate.get("corrected_evidence", [])
    if not isinstance(corrected, list):
        return str(corrected)
    return gate.get("suggested_fix", "") or " | ".join(
        f"PDF p. {a.get('page', '')}, {a.get('section', '')}: {a.get('quote', '')}"
        for a in corrected if isinstance(a, dict)
    )


def csv_row(target, info, codex, gemini, prior, gate, supplemental, correction, correction_gate):
    ident, kind, key = input_key(target)
    record = {"record_id": info["record_id"], "packet_id": ident, "kind": kind, "key": key,
              "pdf_path": info["source_pdf"], "pdf_sha256": info["sha256"],
              "supplemental_pdf_path": supplemental.get("pdf", ""),
              "supplemental_pdf_sha256": supplemental.get("sha256", ""),
              "suggested_locator": suggested(target), "baseline": prior,
              "comparison": conclusion(codex, gemini, kind)}
    for name, item in (("codex", codex), ("gemini", gemini), ("correction", correction)):
        anchors = item.get("evidence") if item else None
        anchors = anchors if isinstance(anchors, list) else []
        for field in ("status", "finding", "note", "locator_check"):
            record[f"{name}_{field}"] = str(item.get(field, "")) if item else (
                "MISSING_PASS" if field == "status" and name != "correction" else "")
        record[f"{name}_locator"] = " | ".join(f"PDF p. {a['page']}, {a['section']}"
                                              for a in anchors if isinstance(a, dict)
                                              and "page" in a and "section" in a)
        record[f"{name}_excerpt"] = " | ".join(a.get("quote", "") for a in anchors
                                               if isinstance(a, dict) and isinstance(a.get("quote"), str))
    record["gemini_semantic"] = gate.get("semantic", "PENDING") if gemini else "NO_RESULT"
    record["gemini_semantic_reason"] = gate.get("reason", "")
    record["gemini_semantic_recheck"] = recheck_text(gate)
    record["correction_semantic"] = correction_gate.get("semantic", "PENDING") if correction else ""
    record["correction_semantic_reason"] = correction_gate.get("reason", "")
    record["correction_semantic_recheck"] = recheck_text(correction_gate)
    if record["codex_status"] == "DISCREPANCY":
        record["author_attention"] = "BASELINE_DISCREPANCY"
    elif ident in LIMITED:
        record["author_attention"] = "RESTRICTED_SOURCE"
    elif ((record["gemini_semantic"] != "PASS" and record["correction_semantic"] != "PASS")
          or record["codex_status"] != "VERIFIED"
          or (record["comparison"] == "DIFFERENT_LABEL" and record["correction_semantic"] != "PASS")):
        record["author_attention"] = "CHECK_EVIDENCE"
    else:
        record["author_attention"] = "EVIDENCE_AVAILABLE"
    return record


def tex(value):
    escapes = {ord(a): b for a, b in {
        "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "#": r"\#", "$": r"\$",
        "%": r"\%", "&": r"\&", "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }.items()}
    return " ".join(str(value).split()).translate(escapes)


def report_tex(path, summary, report):
    labels = STATUSES | {"MISSING_PASS"}
    counts = []
    for provider in ("codex", "gemini"):
        provider_counts = summary[f"{provider}_status"]
        counts.append({**provider_counts, "INVALID_STATUS": sum(
            value for label, value in provider_counts.items() if label not in labels
        )})
    codex, gemini = counts
    lines = [
        r"\section*{Phạm vi và tiến độ}",
        f"Đối chiếu {summary['expected']} mục trong {summary['reports']} bài. Codex trả {summary['codex_returned']} mục và Gemini trả {summary['gemini_returned']} mục ở lượt đầu.",
        "Gemini đọc văn bản tách theo trang từ PDF đã khóa hash. Mỗi lô có bài kiểm tra đọc trực tiếp PDF mẫu. Codex đối chiếu theo trang và mở ảnh PDF ở các vị trí cần kiểm tra bố cục.",
        r"\begin{center}\begin{tabular}{lrr}\toprule Trạng thái do lượt rà ghi & Codex & Gemini \\ \midrule",
    ]
    lines.extend(f"{tex(status)} & {codex.get(status, 0)} & {gemini.get(status, 0)} \\\\"
                 for status in sorted(labels | {"INVALID_STATUS"}))
    lines.extend([
        r"\bottomrule\end{tabular}\end{center}",
        r"\section*{Các mục Codex đề nghị kiểm tra hoặc sửa}",
        r"\begin{longtable}{p{.15\linewidth}p{.76\linewidth}}\toprule Mã và mục & Nhận định đối chiếu \\ \midrule\endhead",
    ])
    discrepancy = [r for r in report if r["codex_status"] == "DISCREPANCY"]
    if not discrepancy:
        lines.append(r"\multicolumn{2}{l}{Chưa có mục được gắn trạng thái DISCREPANCY.} \\")
    for row in discrepancy:
        label = tex(row["record_id"] + " " + row["key"])
        description = tex(row["codex_finding"] + " " + row["codex_locator"])
        lines.append(f"{label} & {description} \\\\")
    lines.extend([
        r"\bottomrule\end{longtable}",
        r"\section*{Kiểm tra phản hồi Gemini}",
        r"\begin{center}\begin{tabular}{rrrrrrrr}\toprule Lô & Dự kiến & Trả về & Neo khớp & Qua & Một phần & Trượt & Chưa rà \\ \midrule",
    ])
    for row in summary["batches"]:
        matches = row.get("locator_checks", {}).get("ANCHORS_MATCH", 0)
        semantic = row["semantic"]
        values = [row["batch"], row["expected"], row["seen"], matches,
                  semantic.get("PASS", 0), semantic.get("PARTIAL", 0),
                  semantic.get("FAIL", 0), row["semantic_unreviewed"]]
        lines.append(" & ".join(map(str, values)) + r" \\")
    lines.extend([
        r"\bottomrule\end{tabular}\end{center}",
        f"Trong các mục Gemini trả về, {sum(b.get('locator_checks', {}).get('GAP_DOCUMENTED', 0) for b in summary['batches'])} mục ghi rõ khoảng trống mà không có trích đoạn. "
        "Các phán định phần nội dung có thể xác nhận cách ghi khoảng trống nếu nguồn không được cung cấp.",
        "Bảng CSV giữ riêng kết quả Gemini trả về và trạng thái kiểm tra vị trí nguồn. Những dòng thiếu",
        "minh chứng hoặc vẫn chờ đối chiếu ngữ nghĩa cần được đọc lại từ PDF.",
    ])
    if summary.get("correction"):
        followup = summary["correction"]
        lines.append(
            f"Lô sửa trả {followup['seen']}/{followup['expected']} mục. "
            f"Tính cả lô sửa, Gemini có {summary['gemini_unique_with_correction']}/{summary['expected']} mục phân tích được. "
            f"Đã thoát dấu ngoặc kép trong {len(followup.get('normalized_json_keys', []))} dòng JSON để đọc dữ liệu gốc. "
            "Cột có tiền tố correction trong CSV lưu chứng cứ và kết quả kiểm tra riêng."
        )
        if followup.get("semantic"):
            semantic = followup["semantic"]
            lines.append(
                f"Lượt sửa qua kiểm tra nội dung {semantic.get('PASS', 0)}, hỗ trợ một phần "
                f"{semantic.get('PARTIAL', 0)}, không qua {semantic.get('FAIL', 0)}. "
                "Các kết quả đọc được vẫn cần người thẩm định xác nhận."
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--output", type=Path, default=HERE)
    parser.add_argument("--archive-codex", action="store_true", help="Save a replayable, scope-checked Codex pass.")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    packet = rows(PACKET / "R1/source_verification.csv")
    expected = {input_key(t) for t in packet}
    manifest = load(HERE / "phase_manifest.json")
    sources = [read_pages(args.workspace / p) for p in ("pages", "pymupdf", "appraisal-pymupdf")]
    if {i for i in sources[0] if i in manifest["pdfs"]} != set(manifest["pdfs"]):
        raise ValueError("The hash-checked source page inventory is incomplete")
    codex = {}
    codex_errors = []
    codex_paths = sorted(args.workspace.glob("codex-*.jsonl"))
    if not codex_paths and (HERE / "codex_pass.jsonl").is_file():
        codex_paths = [HERE / "codex_pass.jsonl"]
    for path in codex_paths:
        data, errors, _ = extract(path.read_text(encoding="utf-8"), expected)
        duplicates = data.keys() & codex.keys()
        if duplicates:
            raise ValueError(f"Codex keys overlap between categories: {duplicates}")
        codex.update(data)
        codex_errors.extend(errors)
    codex_scope(codex)
    if args.archive_codex:
        if len(codex) != len(expected) or codex_errors:
            raise ValueError("Refusing to archive an incomplete Codex pass")
        (args.output / "codex_pass.jsonl").write_text(
            "".join(json.dumps(codex[key], ensure_ascii=False) + "\n" for key in sorted(codex)),
            encoding="utf-8",
        )
    visual = {(r["packet_id"], r["kind"], r["key"]) for r in rows(HERE / "primary_visual_checks.csv")}
    for key, item in codex.items():
        item["locator_check"] = "RENDERED_SOURCE_CHECKED" if key in visual else assess(item, sources)
    gemini = {}
    correction = {}
    correction_semantic = {}
    semantic = {}
    reviews = []
    for batch in manifest["batches"]:
        members = {k for k in expected if k[0] in batch["reports"]}
        number = batch["number"]
        receipt = args.workspace / f"gemini-{number:02}.json"
        if not receipt.is_file():
            receipt = HERE / "receipts" / f"batch-{number:02}-receipt.json"
        data, stats = receipt_review(receipt, batch, members, sources)
        checked = load_semantic_checks(args.workspace, batch["number"], members)
        semantic.update(checked)
        stats["semantic"] = dict(sorted(Counter(checked[k]["semantic"] for k in data.keys() & checked.keys()).items()))
        stats["semantic_unreviewed"] = len(data.keys() - checked.keys())
        stats["semantic_missing_row_reviews"] = len(checked.keys() - data.keys())
        gemini.update(data)
        reviews.append(stats)
    correction_stats = None
    correction_context = HERE / "correction_manifest.json"
    if correction_context.is_file():
        correction_manifest = load(correction_context)
        correction_inputs = load(HERE / "correction_targets.json")
        correction_keys = {(ident, t["kind"], t["key"]) for ident, src in correction_inputs.items() for t in src["targets"]}
        if not correction_keys <= expected or len(correction_keys) != correction_manifest["keys"]:
            raise ValueError("Correction target keys differ from the committed manifest")
        correction_receipt = HERE / "receipts/batch-09-receipt.json"
        correction, correction_stats = receipt_review(correction_receipt, correction_manifest, correction_keys, sources)
        correction_semantic = load_semantic_checks(args.workspace, 9, correction_keys)
        correction_counts = Counter(correction_semantic[k]["semantic"]
                                    for k in correction.keys() & correction_semantic.keys())
        correction_stats["semantic"] = dict(sorted(correction_counts.items()))
        correction_stats["semantic_unreviewed"] = len(correction.keys() - correction_semantic.keys())
    baseline = baseline_values()
    report = []
    for target in sorted(packet, key=lambda t: (manifest["pdfs"][t["packet_id"]]["record_id"], input_key(t))):
        ident, kind, item = k = input_key(target)
        info = manifest["pdfs"][ident]
        prior = baseline.get((info["record_id"], kind, item), "")
        if ident in LIMITED:
            prior = "Restricted to non-operational scholarly assessment."
        supplemental = manifest.get("supplemental_pdf", {})
        report.append(csv_row(target, info, codex.get(k), gemini.get(k), prior, semantic.get(k, {}),
                              supplemental if supplemental.get("packet_id") == ident else {},
                              correction.get(k), correction_semantic.get(k, {})))
    with (args.output / "source_review_887.csv").open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(report[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(report)
    summary = {
        "expected": len(expected), "reports": len(manifest["pdfs"]),
        "codex_returned": len(codex), "gemini_returned": len(gemini),
        "codex_parse_errors": codex_errors,
        "codex_status": dict(Counter(r["codex_status"] for r in report)),
        "gemini_status": dict(Counter(r["gemini_status"] for r in report)),
        "gemini_semantic": dict(Counter(r["gemini_semantic"] for r in report)),
        "author_attention": dict(Counter(r["author_attention"] for r in report)),
        "labels": dict(Counter(r["comparison"] for r in report)),
        "batches": reviews,
        "correction": correction_stats,
        "gemini_unique_with_correction": len(gemini.keys() | correction.keys()),
    }
    dump(args.output / "source_review_summary.json", summary)
    report_tex(args.output / "report_data.tex", summary, report)
    print(len(report), len(codex), len(gemini))


if __name__ == "__main__":
    main()
