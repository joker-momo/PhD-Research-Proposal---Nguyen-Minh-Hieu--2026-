"""Record a completed Gemini source batch and authorize only its next dispatch."""

import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from prepare import HERE, PROJECT, dump
from review_sources import load

TASK = "hk261-dual-ai-source-review-887"


def gate_row(label, passed, evidence):
    return f"| {label} | {'PASS' if passed else 'FAIL'} | {evidence} |"


def write_review(stats, path):
    locators = stats.get("locator_checks", {})
    missing = stats["expected"] - stats["seen"]
    bad_anchors = stats["seen"] - locators.get("ANCHORS_MATCH", 0) - locators.get("GAP_DOCUMENTED", 0)
    lines = [
        f"# Gemini · Kiểm tra lô {stats['batch']:02}",
        "",
        f"Task `{stats.get('task_id', '')}`, context `{stats.get('context_id', '')}`.",
        f"Trạng thái bridge `{stats['transport']}`. Bắt đầu {stats.get('provider_started_at')},"
        f" kết thúc {stats.get('provider_completed_at')}.",
        "",
        "| Tiêu chí | Kết quả | Minh chứng |",
        "| --- | --- | --- |",
        gate_row("Hash đầu vào và đầu ra bridge", stats.get("hash_inventory_match", False)
                 and stats.get("context_unchanged", False), "Đối chiếu manifest và biên nhận."),
        gate_row("Neo kiểm tra đọc PDF", stats.get("preflight_anchor_match", False), "HKF-118, PDF tr. 2."),
        gate_row("Khóa chính xác và dấu kết thúc", not missing and not stats.get("errors") and stats.get("end_marker", False),
                 f"{stats['seen']}/{stats['expected']} dòng. {len(stats.get('errors', []))} lỗi cấu trúc hoặc khóa."),
        gate_row("Neo nguồn hoặc khoảng trống rõ", not bad_anchors and not missing,
                 f"{locators.get('ANCHORS_MATCH', 0)} neo khớp đủ; {locators.get('GAP_DOCUMENTED', 0)} ghi khoảng trống; {bad_anchors} cần chỉnh."),
        gate_row("Đủ căn cứ cho toàn bộ kết luận", False, "Cần rà nội dung, đơn vị và điều kiện từng nhận định."),
        "",
        "Kết quả lô giữ ở trạng thái tham khảo. Việc khớp neo chưa xác nhận nội dung của phán định.",
    ]
    if stats.get("missing_keys"):
        lines.extend(("", "Mục chưa thấy trong phản hồi", ""))
        lines.extend("- " + " / ".join(key) for key in stats["missing_keys"])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=int)
    parser.add_argument("summary", type=Path)
    args = parser.parse_args()
    batches = load(HERE / "phase_manifest.json")["batches"]
    summary = load(args.summary)
    stats = summary["batches"][args.batch - 1]
    task_state = PROJECT / "MUST_READ_AI_AGENT/current_state.json"
    events = PROJECT / "MUST_READ_AI_AGENT/events.jsonl"
    state = load(task_state)
    if (state["task"]["task_id"] != TASK
            or state["next_task"].get("message_id") != batches[args.batch - 1]["message_id"]
            or stats.get("transport") not in {"TASK_STATE_COMPLETED", "TASK_STATE_FAILED", "TASK_STATE_CANCELED"}):
        parser.error("A terminal provider result for the currently authorized batch is required")
    relative = HERE.relative_to(PROJECT)
    receipts = HERE / "receipts"
    receipts.mkdir(exist_ok=True)
    review = receipts / f"batch-{args.batch:02}-review.md"
    write_review(stats, review)
    dump(receipts / f"batch-{args.batch:02}-gate.json", stats)
    now = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).isoformat(timespec="seconds")
    checkpoint = str(review.relative_to(PROJECT))
    state["updated_at"] = now
    state["task"].update(updated_at=now, checkpoint_path=checkpoint)
    if args.batch < len(batches):
        n = batches[args.batch]
        state["next_task"] = {
            "task_id": f"{TASK}-batch-{n['number']:02}", "owner": "GEMINI_RESEARCH", "status": "ready",
            "action": f"Assess batch {n['number']:02} using only the attached source materials.",
            "acceptance": f"Direct source access check and {n['keys']} distinct keys or transparent gaps.",
            "dispatch_brief": str(relative / "gemini_brief.md"),
            "message_id": n["message_id"],
        }
    else:
        state["next_task"] = {"task_id": TASK + "-reconcile", "owner": "CODEX_WRITING", "status": "ready",
                              "action": "Reconcile returned evidence and record item-level gaps.",
                              "acceptance": "Publish all 887 keys with explicit source evidence or gaps."}
    dump(task_state, state)
    event = {
        "timestamp": now, "event": "gemini-source-review-batch-inspected", "task_id": TASK,
        "decision_id": state["task"]["decision_id"], "artifact": checkpoint, "batch": args.batch,
        "task_provider_id": stats.get("task_id"), "context_provider_id": stats.get("context_id"),
        "provider_started_at": stats.get("provider_started_at"),
        "provider_completed_at": stats.get("provider_completed_at"),
        "readout_returned": stats["seen"], "expected": stats["expected"],
    }
    with events.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(event, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
