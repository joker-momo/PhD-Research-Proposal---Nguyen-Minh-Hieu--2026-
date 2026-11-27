"""Validate, reconcile, and render two masked HK261 AI screening passes."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

from audit_review_inputs import HERE, SYNTHESIS, anchor_on_page, csv_rows, normalize, write_csv

DECISIONS = {"INCLUDE", "EXCLUDE", "AWAITING_CLASSIFICATION"}
PRIORITY = (5, 6, 1, 7, 2, 3, 4)
LABELS = {"INCLUDE": "Đưa vào", "EXCLUDE": "Loại", "AWAITING_CLASSIFICATION": "Chờ"}


def objects(items):
    return [part for artifact in items for part in artifact.get("parts", [])
            if isinstance(part.get("text"), str)]


def unpack(path, kind):
    if kind == "codex":
        return path.read_text()
    result = json.loads(path.read_text())
    return "\n".join(item["text"] for item in objects(result.get("artifacts", [])))


def parse(text, source, pages):
    rows = {}
    rejected = {}
    malformed = 0
    seen = set()
    identities = {}
    for line in text.splitlines():
        key = None
        if not line.lstrip().startswith("{"):
            continue
        try:
            item = json.loads(line)
            key = item.get("record_id") if source == "codex" else item.get("id")
            if key not in pages:
                raise ValueError("Unexpected ID")
            if key in seen:
                rows.pop(key, None)
                rejected[key] = "Trùng mã"
                continue
            seen.add(key)
            decision = item.get("decision")
            criteria = item.get("criteria", {})
            if source == "codex":
                codes = {"PASS": "P", "FAIL": "F", "UNRESOLVED": "U"}
                gates = "".join(codes.get(criteria.get(f"E{i}"), "?") for i in range(1, 8))
                reason = item.get("reason")
                primary = item.get("primary_criterion")
                anchors = [{"page": item.get("physical_pdf_page"), "section": item.get("locator"),
                            "quote": item.get("excerpt")}]
                anchors.extend({"page": anchor.get("physical_pdf_page"), "section": anchor.get("locator"),
                                "quote": anchor.get("excerpt")}
                               for anchor in item.get("additional_evidence", []))
            else:
                gates = item.get("gates", "")
                reason = item.get("why")
                primary = item.get("primary")
                anchors = item.get("evidence", [])
            if not isinstance(gates, str) or not re.fullmatch("[PFU]{7}", gates):
                raise ValueError("Mã E1–E7 sai")
            if not isinstance(reason, str) or not reason.strip() or decision not in DECISIONS:
                raise ValueError("Thiếu đề xuất hoặc giải thích")
            failure = next((f"E{i}" for i in PRIORITY if gates[i - 1] == "F"), "")
            unknown = {f"E{i + 1}" for i, code in enumerate(gates) if code == "U"}
            criteria_ok = ((decision == "INCLUDE" and gates == "PPPPPPP" and not primary)
                or (decision == "EXCLUDE" and bool(failure) and primary == failure)
                or (decision == "AWAITING_CLASSIFICATION" and not failure and primary in unknown))
            if not criteria_ok:
                raise ValueError("Đề xuất không khớp mã và thứ tự tiêu chí")
            if not isinstance(anchors, list) or not anchors:
                raise ValueError("Thiếu neo nguồn")
            for anchor in anchors:
                loc, quote = anchor.get("section"), anchor.get("quote")
                if (not isinstance(loc, str) or not loc.strip() or not isinstance(quote, str)
                        or not anchor_on_page(pages[key], anchor.get("page"), quote)):
                    raise ValueError("Neo không khớp trang nguồn")
            if decision == "INCLUDE" and len({(a["page"], normalize(a["quote"])) for a in anchors}) < 2:
                raise ValueError("Thiếu hai neo về phương pháp và đánh giá")
            if source == "gemini":
                if (not isinstance(item.get("authors"), list) or not item["authors"]
                        or any(not isinstance(a, str) or not a.strip() for a in item["authors"])):
                    raise ValueError("Thiếu tác giả")
                if any(not isinstance(item.get(k), str) or not item[k].strip() for k in ("title", "venue", "doi")):
                    raise ValueError("Thiếu trường thư mục")
                if not re.fullmatch(r"(?:19|20)\d{2}|UNKNOWN", str(item.get("year", ""))):
                    raise ValueError("Năm sai hoặc thiếu mã UNKNOWN")
                doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", item["doi"], flags=re.I).lower().strip()
                if doi != "doi_not_found" and not re.fullmatch(r"10\.\d{4,9}/\S+", doi):
                    raise ValueError("DOI sai hoặc thiếu mã DOI_NOT_FOUND")
                title = re.sub(r"[^\w]+", "", normalize(item["title"]))
                for ident in (("doi", doi), ("title", title)):
                    if ident[1] in {"doi_not_found", "unknown", ""}:
                        continue
                    previous = identities.setdefault(ident, key)
                    if previous != key:
                        flags = ("duplicate", "cross-reference", "version")
                        flagged = any(
                            previous.lower() in line and key.lower() in line and any(word in line for word in flags)
                            for line in map(normalize, text.splitlines())
                        )
                        if not flagged:
                            raise ValueError(f"Thiếu truy vết bản trùng {previous}")
            rows[key] = dict(decision=decision, criterion=primary or "", gates=gates,
                             locator=" | ".join(f"tr. {a['page']}, {a['section']}" for a in anchors),
                             evidence=" | ".join(a["quote"] for a in anchors),
                             reason=reason)
        except (ValueError, TypeError, AttributeError) as error:
            if key in pages:
                rejected[key] = str(error)
            else:
                malformed += 1
    return rows, rejected, malformed


def tex(text):
    replace = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$", "&": r"\&",
               "#": r"\#", "%": r"\%", "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(replace.get(ch, ch) for ch in str(text))


def compare(key, codex, gemini, gemini_pass):
    pairs = Counter()
    report = []
    for meta in key:
        alias = meta["packet_id"]
        row = {field: meta[field] for field in ("packet_id", "record_id", "frozen_disposition",
                                               "primary_exclusion_code", "source_pdf")}
        for name, parsed in (("codex", codex), ("gemini", gemini)):
            valid, invalid, _ = parsed
            data = valid.get(alias, {})
            for field in ("decision", "criterion", "gates", "locator", "evidence", "reason"):
                row[f"{name}_{field}"] = data.get(field, "")
            row[f"{name}_status"] = ("ANCHORS_VALIDATED" if data else
                                    invalid.get(alias, "Không có hồ sơ đối chiếu"))
        c, g = row["codex_decision"], row["gemini_decision"]
        if c and g and gemini_pass:
            pairs[c, g] += 1
        row["comparison"] = ("Đủ hai neo đã soát" if c and g and gemini_pass else "Chưa có cặp được chấp nhận")
        report.append(row)
    return report, pairs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pages", type=Path)
    parser.add_argument("codex", type=Path)
    parser.add_argument("gemini", type=Path)
    parser.add_argument("--gemini-gate", type=Path)
    args = parser.parse_args()
    key = csv_rows(SYNTHESIS / "human_review_packet/coordinator/key.csv")
    pages = {row["packet_id"]: json.loads((args.pages / (row["packet_id"] + ".json")).read_text()) for row in key}
    source_text = {name: unpack(getattr(args, name), name) for name in ("codex", "gemini")}
    c, g = [parse(source_text[name], name, pages) for name in ("codex", "gemini")]
    raw = json.loads(args.gemini.read_text())
    review = json.loads(args.gemini_gate.read_text()) if args.gemini_gate else {}
    expected = json.loads((HERE / "isolated_context_manifest.json").read_text())["files"]
    metadata = raw.get("metadata", {})
    context_ok = (
        metadata.get("context_audit", {}).get("unchanged") is True
        and metadata.get("geminiApp", {}).get("files") == expected
    )
    required = {"original_pdf", "provenance", "method_and_evaluation", "quantitative_claims",
                "unresolved_ids", "worker_statement"}
    gate = (context_ok and len(g[0]) == len(key) and not g[1] and not g[2]
            and raw["status"]["state"] == "TASK_STATE_COMPLETED"
            and "END_HK261_136" in source_text["gemini"]
            and review.get("task_id") == raw.get("id")
            and set(review.get("criteria", {})) == required
            and all(value == "PASS" for value in review["criteria"].values()))
    visible_gemini = g if gate else ({}, g[1], g[2])
    report, pairs = compare(key, c, visible_gemini, gate)
    write_csv(HERE / "review_136.csv", report)
    extraction = Counter(row["automated_check"] for row in csv_rows(HERE / "extraction_locator_audit.csv"))
    summary = dict(
        records=len(key), codex_valid=len(c[0]), codex_rejected=c[1], codex_malformed=c[2],
        gemini_valid=len(g[0]), gemini_rejected=g[1], gemini_malformed=g[2],
        gemini_transport=raw["status"]["state"], gemini_context_verified=context_ok,
        gemini_cleanup=metadata.get("chat_cleanup", {}).get("state", "not_reported"),
        gemini_gate="PASS" if gate else "FAIL",
        codex_decisions=dict(Counter(row["decision"] for row in c[0].values())),
        gemini_decisions=dict(Counter(row["decision"] for row in g[0].values())),
        paired=sum(pairs.values()), agreement=sum(n for (a, b), n in pairs.items() if a == b),
        cross_tab=[dict(codex=a, gemini=b, count=n) for (a, b), n in sorted(pairs.items())],
        automated_extraction_checks=dict(extraction),
    )
    summary["codex_matches_frozen"] = sum(
        row["codex_decision"] == row["frozen_disposition"] for row in report
    )
    summary["codex_differs_from_frozen"] = sum(
        bool(row["codex_decision"]) and row["codex_decision"] != row["frozen_disposition"] for row in report
    )
    summary["codex_cross_tab_frozen"] = [
        dict(frozen=a, codex=b, count=n) for (a, b), n in sorted(Counter(
            (row["frozen_disposition"], row["codex_decision"]) for row in report
        ).items())
    ]
    summary["codex_uncertainty_counts"] = dict(Counter(
        row["codex_criterion"] for row in report if row["codex_decision"] == "AWAITING_CLASSIFICATION"
    ))
    total = summary["paired"]
    if total:
        expected = sum(sum(n for (a, _), n in pairs.items() if a == label)
                       * sum(n for (_, b), n in pairs.items() if b == label) for label in DECISIONS)
        summary["kappa_ai"] = ((total * summary["agreement"] - expected) / (total ** 2 - expected)
                               if total ** 2 != expected else None)
    (HERE / "review_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    codex_overview = ", ".join(f"{summary['codex_decisions'].get(decision, 0)} {label.lower()}"
                               for decision, label in LABELS.items())
    status = [
        r"\section*{Tiến độ và giới hạn}",
        tex(f"Codex: {summary['codex_valid']}/136 đề xuất qua kiểm tra mã tiêu chí và neo nguyên văn, "
            f"gồm {codex_overview}. Có {summary['codex_differs_from_frozen']} đề xuất khác quyết định trong sổ."),
    ]
    shifted = Counter((row["frozen_disposition"], row["codex_decision"]) for row in report)
    if not c[1] and not c[2] and len(c[0]) == len(key):
        status.append(tex(
            f"Trong 46 hồ sơ đã đưa vào, Codex giữ {shifted['INCLUDE', 'INCLUDE']}, "
            f"đề xuất loại {shifted['INCLUDE', 'EXCLUDE']} và chờ {shifted['INCLUDE', 'AWAITING_CLASSIFICATION']}. "
            f"Trong 90 hồ sơ đã loại, Codex giữ {shifted['EXCLUDE', 'EXCLUDE']}, "
            f"đề xuất đưa vào {shifted['EXCLUDE', 'INCLUDE']} và chờ {shifted['EXCLUDE', 'AWAITING_CLASSIFICATION']}."
        ))
    if gate:
        status.append(tex(f"Gemini: {summary['gemini_valid']}/136 hồ sơ qua cửa kiểm tra. Hai AI trùng quyết định "
                          f"{summary['agreement']}/{total} cặp. Cohen’s kappa giữa hai AI: {summary['kappa_ai']}."))
    else:
        status.append(tex(f"Gemini.app: {raw['status']['state']}. Có {summary['gemini_valid']}/136 dòng qua kiểm tra "
                          "cấu trúc và neo. Lượt này chưa đạt cửa kiểm tra toàn bộ; chưa có số đồng thuận giữa hai AI."))
    (HERE / "report_status.tex").write_text("\n\n".join(status) + "\n")
    tex_rows = []
    priority_rows = sorted(report, key=lambda row: (
        row["codex_decision"] == row["frozen_disposition"]
        and (not gate or row["gemini_decision"] == row["frozen_disposition"]),
        row["record_id"],
    ))
    for row in priority_rows:
        frozen = LABELS[row["frozen_disposition"]]
        ctext = LABELS.get(row["codex_decision"], "Chưa có") + " " + row["codex_criterion"]
        gtext = LABELS.get(row["gemini_decision"], "Chưa có") + " " + row["gemini_criterion"]
        context = "Codex: " + (row["codex_locator"] + ". " + row["codex_reason"] if row["codex_decision"]
                              else row["codex_status"])
        if row["gemini_decision"]:
            context += " Gemini: " + row["gemini_locator"] + ". " + row["gemini_reason"]
        elif row["gemini_status"] != "Không có hồ sơ đối chiếu":
            context += " Gemini: " + row["gemini_status"] + "."
        tex_rows.append(" & ".join(map(tex, (row["record_id"] + " / " + row["packet_id"],
                                             frozen, ctext, gtext, context))) + r" \\ \hline")
    (HERE / "review_rows.tex").write_text("\n".join(tex_rows) + "\n")
    print(json.dumps({k:v for k,v in summary.items() if not k.endswith("_rejected")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
