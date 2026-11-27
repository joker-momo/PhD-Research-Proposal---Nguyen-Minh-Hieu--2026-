"""Resegment the incomplete Gemini screening inputs below its read ceiling."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

MAX_BYTES = 200_000


def group_sections(source, keys):
    records = {}
    for path in sorted(source.glob("reports-*.txt")):
        for block in path.read_text().split(r"\n===== REPORT ")[1:]:
            header, body = block.split("\n", 1)
            key = header.split()[0]
            text = f"\n===== REPORT {key} =====\n{body.rstrip()}\n"
            records[key] = [text] if len(text.encode()) <= MAX_BYTES else re.split(
                r"(?=----- PHYSICAL PAGE \d+ -----)", text
            )
    if not set(keys).issubset(records):
        raise ValueError("The original supplied context lacks correction targets.")
    group = []
    size = 0
    for key in keys:
        for section in records[key]:
            payload = section
            if not payload.lstrip().startswith("===== REPORT "):
                payload = f"\n===== REPORT {key} (continued) =====\n{payload}"
            length = len(payload.encode())
            if length > MAX_BYTES:
                raise ValueError(f"One physical page exceeds the file cap: {key}")
            if size + length > MAX_BYTES:
                yield group
                group = []
                size = 0
            group.append((key, payload))
            size += length
    if group:
        yield group


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("summary", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--keys", nargs="+")
    args = parser.parse_args()
    rejected = json.loads(args.summary.read_text())["gemini_rejected"]
    followup = {"HKF-058", "HKF-073", "HKF-086"} if args.keys is None else set(args.keys)
    keys = sorted(set(rejected) | followup)
    if args.keys is None and len(keys) != 101:
        raise ValueError("Initial correction expects 101 named targets.")
    args.target.mkdir(exist_ok=True)
    index = {}
    for seq, group in enumerate(group_sections(args.source, keys), 1):
        name = f"correction-{seq:02d}.txt"
        (args.target / name).write_text("".join(text for _, text in group))
        for key, _ in group:
            locations = index.setdefault(key, [])
            if name not in locations:
                locations.append(name)
    for name in ("criteria.txt", "HKF-093.pdf"):
        shutil.copyfile(args.source / name, args.target / name)
    (args.target / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    files = {path.name: {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                         "bytes": path.stat().st_size} for path in sorted(args.target.iterdir())}
    if len(files) > 50 or sum(row["bytes"] for row in files.values()) > 8 * 1024 * 1024:
        raise ValueError("Correction exceeds the bridge attachment limits.")
    args.manifest.write_text(json.dumps({"record_ids": keys, "file_index": index, "files": files}, indent=2) + "\n")
    print(len(keys), len(files), sum(row["bytes"] for row in files.values()),
          max(row["bytes"] for row in files.values()))


if __name__ == "__main__":
    main()
