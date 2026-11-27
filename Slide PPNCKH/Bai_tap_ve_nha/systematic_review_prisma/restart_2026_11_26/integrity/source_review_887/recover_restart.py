"""Preserve a finished Gemini restart response while retaining its failed transport receipt."""

import argparse
import hashlib
import json
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def sha(data):
    return hashlib.sha256(data).hexdigest()


def force_save(path, data):
    with path.open("xb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bridge_repo", type=Path)
    parser.add_argument("transport", type=Path)
    parser.add_argument("targets", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--clean-owned-chat", action="store_true")
    args = parser.parse_args()
    bridge = args.bridge_repo / ".runtime/snapshot"
    original = json.loads(args.transport.read_text(encoding="utf-8"))
    task = original["id"]
    meta = original["metadata"]
    app = meta["geminiApp"]
    folder = Path(app["folder"])
    affected = json.loads(args.targets.read_text(encoding="utf-8"))
    expected = {(key, item[0], item[1]) for key, items in affected.items() for item in items}
    dest = args.destination
    evidence = dest.with_suffix(".recovery.json")
    attempt = dest.with_suffix(".cleanup-attempt.json")

    def run(*args):
        return json.loads(subprocess.check_output([str(bridge), *args], timeout=20))

    def read_owned(state, attachment):
        if state["generating"] or state["draft"] or state["mode"] != "task":
            raise ValueError("App is generating, contains a draft, or is out of Task mode")
        users = [r["text"] for r in state["rows"] if r["user"] and r["text"]]
        answers = [r["text"] for r in state["rows"] if not r["user"] and r["text"]]
        if (len(users) != 1 or users[0].splitlines()[0] != "BRIDGE_TASK_" + task or len(answers) != 1):
            raise ValueError("Snapshot does not identify exactly the original prompt and answer")
        if attachment and (state["selectionCount"] != 1 or state["buttonLabels"].count(folder.name) != 1):
            raise ValueError("Expected isolated attachment is missing")
        if not attachment and state["hasSelection"]:
            raise ValueError("An attachment is still selected")
        return answers[0]

    first = read_owned(run(), True)
    time.sleep(2)
    if read_owned(run(), True) != first:
        raise ValueError("Response changed between independent snapshots")
    if not all(sha((folder / name).read_bytes()) == item["sha256"] for name, item in app["files"].items()):
        raise ValueError("An isolated input changed")
    lines = first.splitlines()
    begin, end = "BEGIN_BRIDGE_RESULT_" + task, "END_BRIDGE_RESULT_" + task
    indices = [i for i, line in enumerate(lines) if line == begin]
    if len(indices) != 2 or lines.count(end) != 1 or lines[-1] != end or indices[0] != 0:
        raise ValueError("Unexpected restart envelope")
    selected = "\n".join(lines[indices[-1] + 1:-1])
    observed = []
    for line in selected.splitlines():
        if line.startswith("{"):
            row = json.loads(line)
            if "key" in row:
                observed.append((row["id"], row["kind"], row["key"]))
    if set(observed) != expected or len(observed) != len(expected) or "END_HK261_SOURCE_BATCH" not in selected:
        raise ValueError("Restart segment does not cover exactly the batch keys")
    now = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).isoformat(timespec="seconds")
    evidence_data = {
        "task_id": task, "transport": original["status"], "observed_at": now, "snapshot_count": 2,
        "exact_raw_answer_sha256": sha(first.encode()), "selected_answer_sha256": sha(selected.encode()),
        "restart_lines_0_based": indices, "observed_keys": len(observed), "raw_answer": first,
        "attachment": folder.name,
    }
    force_save(evidence, (json.dumps(evidence_data, ensure_ascii=False, indent=2) + "\n").encode())
    original["artifacts"] = [{"name": "read-only-late-response", "parts": [{"text": selected}]}]
    meta["context_audit"] = {"unchanged": True, "method": "independent attached-copy SHA-256 verification"}
    meta["read_only_recovery"] = {k: v for k, v in evidence_data.items() if k != "raw_answer"}
    meta["chat_cleanup"] = {"state": "preserved"}
    # The source and both complete segments are persisted before detaching or deleting anything.
    force_save(dest, (json.dumps(original, ensure_ascii=False, indent=2) + "\n").encode())
    if args.clean_owned_chat:
        if attempt.exists() or read_owned(run(), True) != first:
            raise ValueError("Cleanup precondition failed; chat preserved")
        run("detach-folder", task, folder.name)
        if read_owned(run(), False) != first:
            raise ValueError("Exact response changed after detachment; chat preserved")
        run("prepare-delete", task)
        force_save(attempt, json.dumps({"task_id": task, "phase": "confirm_once", "at": now}).encode())
        run("confirm-delete", task)
        for _ in range(25):
            state = run()
            if state["title"] == "Gemini — New chat" and not state["rows"] and not state["generating"] and not state["draft"]:
                meta["chat_cleanup"] = {"state": "deleted", "verified_new_chat": True, "method": "owned native helper"}
                dest.write_text(json.dumps(original, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                break
            time.sleep(0.2)
        else:
            raise ValueError("Deletion postcondition unverified; do not repeat confirmation")
    print(json.dumps({"task": task, "keys": len(observed), "cleanup": meta["chat_cleanup"]["state"]}))


if __name__ == "__main__":
    main()
