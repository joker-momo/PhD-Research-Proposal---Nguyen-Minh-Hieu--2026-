"""Escape reviewed embedded quote marks in the seven malformed batch-09 rows."""

import argparse
import json
from pathlib import Path

from prepare import dump
from review_sources import extract, key_of, load


QUOTES = {
    ("HKF-011", "t2_decisions_objective_solver"): ["The second action"],
    ("HKF-035", "Q01"): ["2", "With 2 threads, inference requires approximately 275 milliseconds per frame, yielding a maximum throughput of 3.6 FPS."],
    ("HKF-044", "t2_decisions_objective_solver"): ["TABLE II SIMULATION PARAMETERS"],
    ("HKF-049", "t3_platform_modality"): ["family of Raspberry pi B+", "Raspberry pi B+"],
    ("HKF-100", "D08"): ["different UAV speeds, varying mission areas, and fluctuating task arrival rates,"],
    ("HKF-110", "Q05"): ["maintained task throughput above 90% even with 20 drones,", "Task completion rate of different systems"],
    ("HKF-121", "D07"): ["ETH"],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    parser.add_argument("targets", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    data = load(args.receipt)
    expected = {(i, row["kind"], row["key"]) for i, src in load(args.targets).items() for row in src["targets"]}
    part, = data["artifacts"][0]["parts"]
    recovered, errors, _ = extract(part["text"], expected)
    amended = []
    changes = []
    for line in part["text"].splitlines():
        if line.startswith("{"):
            try:
                json.loads(line)
            except json.JSONDecodeError:
                record, = [key for key in QUOTES if f'"id":"{key[0]}"' in line and f'"key":"{key[1]}"' in line]
                for value in QUOTES[record]:
                    raw = '"' + value + '"'
                    if raw not in line:
                        raise ValueError(f"Missing reviewed quotation for {record}")
                    line = line.replace(raw, r'\"' + value + r'\"')
                parsed_key = key_of(json.loads(line))
                if parsed_key in recovered or parsed_key not in expected:
                    raise ValueError(f"Invalid revised key {parsed_key}")
                changes.append(parsed_key)
        amended.append(line)
    part["text"] = "\n".join(amended)
    revised, remaining, _ = extract(part["text"], expected)
    if len(changes) != len(QUOTES) or remaining or set(revised) != expected:
        raise ValueError("Revised receipt does not recover exactly the committed key set")
    data["metadata"]["quote_normalization"] = {
        "method": "Escape reviewed embedded ASCII quotation marks only",
        "original_errors": errors,
        "recovered_keys": sorted(changes),
    }
    dump(args.destination, data)


if __name__ == "__main__":
    main()
