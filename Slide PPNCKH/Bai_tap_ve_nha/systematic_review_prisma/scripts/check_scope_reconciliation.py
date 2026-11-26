"""Check scope-reconciliation structure and source locators; never infer semantics.

Inputs: provider JSON, accepted consolidated ledger, canonical project root, IDs.
Output: JSON check report to stdout/optional file; exit 1 for failed checks,
2 for invalid/unreadable input. Source files and provider input are never edited.
"""
import argparse
import json
import re
from pathlib import Path

from check_46screening import normalized

SCOPE = {"multi_uav_evaluated", "collaborative_inference"}
ARCHITECTURE = {"uav_roles", "inference_execution_nodes", "inference_workload",
                "coordinated_decisions", "evaluated_conditions", "evidence_ids"}
OTHER = {"primary_full_report", "evaluative_evidence", "date_window", "english"}
FIELDS = {"id", "title", "authors", "year", "venue", "doi", "prior_decision",
          "proposed_decision", "scope_gates", "other_gates_preserved", "architecture",
          "supporting_interpretation", "contrary_interpretation", "evidence",
          "unresolved", "human_question"}


def line_bounds(value):
    if isinstance(value, list) and len(value) == 2:
        lo, hi = value
    elif isinstance(value, int) and not isinstance(value, bool):
        lo = hi = value
    elif isinstance(value, str):
        match = re.fullmatch(r"(?:text )?lines?\s+(\d+)(?:\s*[-–]\s*(\d+))?|(?:(\d+)(?:\s*[-–]\s*(\d+))?)", value.strip(), re.I)
        if not match:
            raise ValueError("invalid line range")
        lo = int(match[1] or match[3]); hi = int(match[2] or match[4] or lo)
    else:
        raise ValueError("line range must be an integer, pair or range string")
    if type(lo) is not int or type(hi) is not int or not 1 <= lo <= hi:
        raise ValueError("invalid line bounds")
    return lo, hi


def evidence_references(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "evidence_ids":
                yield child
            else:
                yield from evidence_references(child)
    elif isinstance(value, list):
        for child in value:
            yield from evidence_references(child)


def check(data, ledger, project_root, expected_ids):
    errors, quote_checks = [], []
    baseline = {r["report_id"]: r["accepted_record"] for r in ledger["records"]}
    records = data.get("records", [])
    if not isinstance(records, list) or any(not isinstance(r, dict) for r in records):
        return {"errors": ["A1 records must be object array"], "semantic_review": "PENDING"}
    ids = [r.get("id") for r in records]
    if ids != list(expected_ids) or len(set(ids)) != len(ids):
        errors.append("A1 record IDs/order differ from brief")
    for field in ("title", "doi"):
        values = [normalized(str(r.get(field, ""))) for r in records
                  if r.get(field) not in (None, "", "DOI_NOT_FOUND")]
        if len(values) != len(set(values)):
            errors.append(f"A1 duplicate normalized {field}")
    all_evidence = [e for r in records for e in r.get("evidence", []) if isinstance(e, dict)]
    eids = [e.get("evidence_id") for e in all_evidence]
    if None in eids or len(set(eids)) != len(eids):
        errors.append("A2 missing/duplicate evidence IDs")
    for r in records:
        rid = r.get("id")
        if rid not in baseline:
            errors.append(f"A1 unknown report {rid}"); continue
        if missing := FIELDS - r.keys():
            errors.append(f"A1 {rid} missing fields {sorted(missing)}")
        prior = baseline[rid]
        for field in ("title", "authors", "year", "venue", "doi"):
            if r.get(field) != prior.get(field):
                errors.append(f"A1 {rid} changed identity {field}")
        if r.get("prior_decision") != prior["decision"]:
            errors.append(f"A1 {rid} incorrect prior decision")
        gates = r.get("scope_gates", {})
        other = r.get("other_gates_preserved", {})
        if set(gates) != SCOPE or set(other) != OTHER:
            errors.append(f"A3 {rid} wrong gate keys")
        states = []
        for key in SCOPE:
            gate = gates.get(key, {})
            states.append(gate.get("status"))
            if not gate.get("rationale") or not gate.get("evidence_ids"):
                errors.append(f"A3 {rid} gate {key} lacks rationale/evidence")
        for key in OTHER:
            value = other.get(key); states.append(value)
            if value != prior["gates"][key]["status"]:
                errors.append(f"A3 {rid} changed preserved gate {key}")
        if any(s not in {"YES", "NO", "UNCERTAIN"} for s in states):
            errors.append(f"A3 {rid} invalid gate value")
        decision = "EXCLUDE" if "NO" in states else "INCLUDE" if all(s == "YES" for s in states) else "UNCERTAIN"
        if r.get("proposed_decision") != decision:
            errors.append(f"A3 {rid} decision truth-table mismatch")
        if not isinstance(r.get("unresolved"), list) or (decision == "UNCERTAIN" and not r.get("human_question")):
            errors.append(f"A5 {rid} missing uncertainty information")
        architecture = r.get("architecture", {})
        if not isinstance(architecture, dict) or any(not architecture.get(k) for k in ARCHITECTURE):
            errors.append(f"A4 {rid} incomplete architecture")
        for refs in evidence_references(r):
            local_ids = [e.get("evidence_id") for e in r.get("evidence", [])]
            if isinstance(refs, list) and any(ref not in local_ids for ref in refs):
                errors.append(f"A2 {rid} evidence reference belongs to another report")
        for key in ("supporting_interpretation", "contrary_interpretation"):
            if not r.get(key, {}).get("note") or not r.get(key, {}).get("evidence_ids"):
                errors.append(f"A4 {rid} missing {key}")
        evidence = r.get("evidence", [])
        if len(evidence) != 4:
            errors.append(f"A2 {rid} expected four quotes")
        text_path = project_root / "screening_46" / "text" / f"{rid}.txt"
        lines = text_path.read_bytes().replace(b"\x00", b"").decode("utf-8").splitlines()
        allowed = {text_path.resolve(), (project_root / "screening_46" / "pdf" / f"{rid}.pdf").resolve()}
        for e in evidence:
            result = {"id": rid, "evidence_id": e.get("evidence_id"), "match": False}
            try:
                lo, hi = line_bounds(e.get("line_range"))
                quoted = e.get("quote", ""); page = e.get("page")
                file = Path(e.get("file", ""))
                if not file.is_absolute(): file = project_root / file
                if file.resolve() not in allowed or not file.is_file():
                    raise ValueError("file is not the supplied source")
                if hi > len(lines): raise ValueError("line range exceeds source")
                marker = [re.search(r"=== PDF PAGE (\d+) ===", x) for x in lines[:lo]]
                pages = [int(m[1]) for m in marker if m]
                if not pages or pages[-1] != page: raise ValueError("page/line mismatch")
                span = "\n".join(lines[lo-1:hi])
                if any(re.search(r"=== PDF PAGE (\d+) ===", x) and int(re.search(r"PAGE (\d+)", x)[1]) != page for x in lines[lo-1:hi]):
                    raise ValueError("line range crosses pages")
                if not 1 <= len(quoted.split()) <= 40: raise ValueError("quote length outside 1..40")
                if not normalized(quoted) or normalized(quoted) not in normalized(span): raise ValueError("quote not present in line range")
                result.update(match=True, page=page, line_range=[lo, hi], words=len(quoted.split()))
            except (ValueError, TypeError, KeyError) as exc:
                errors.append(f"A2 {rid} {e.get('evidence_id')}: {exc}")
            quote_checks.append(result)
    for refs in evidence_references(data):
        if not isinstance(refs, list) or not refs or any(ref not in eids for ref in refs):
            errors.append("A2 unresolved/empty evidence references")
    checks = data.get("consistency_checks", [])
    if len(checks) != 3 or any(not all(c.get(k) for k in ("principle", "applies_to_ids", "evidence_ids", "assessment")) for c in checks):
        errors.append("A4 expected three complete consistency checks")
    for item in checks:
        if not isinstance(item.get("applies_to_ids"), list) or any(rid not in expected_ids for rid in item["applies_to_ids"]):
            errors.append("A4 consistency check references an unknown report")
    if data.get("shortfall") != [] or data.get("project_files_changed") != 0 or data.get("final_prose_written") is not False:
        errors.append("A6 shortfall/ownership declaration failed")
    return {"records": len(records), "evidence_count": len(quote_checks),
            "quote_matches": sum(q["match"] for q in quote_checks), "errors": errors,
            "quote_checks": quote_checks, "semantic_review": "PENDING_CODEX_SOURCE_REVIEW"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path); parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--ids", nargs="+", required=True); parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.output:
            output = args.output.resolve()
            evidence_root = (args.project_root / "screening_46").resolve()
            if output in {args.result.resolve(), args.ledger.resolve()} or any(
                output.is_relative_to(evidence_root / folder) for folder in ("text", "pdf")
            ):
                raise ValueError("output must not overwrite input or evidence files")
        result = check(json.loads(args.result.read_text()), json.loads(args.ledger.read_text()), args.project_root, args.ids)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({"input_error": str(exc)})); return 2
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        try:
            args.output.write_text(rendered)
        except OSError as exc:
            print(json.dumps({"output_error": str(exc)}))
            return 2
    print(rendered); return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
