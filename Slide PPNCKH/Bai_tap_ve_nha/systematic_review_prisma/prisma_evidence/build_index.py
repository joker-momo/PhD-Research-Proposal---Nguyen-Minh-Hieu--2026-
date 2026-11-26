#!/usr/bin/env python3
"""Build the human-readable index of the HK261 evidence recorded in Git."""
import argparse
from collections import Counter
import json
from pathlib import Path
from urllib.parse import quote


FOLDER = Path(__file__).resolve().parent
PROJECT = FOLDER.parent
RESTART = PROJECT / "restart_2026_11_26"
STATUSES = {
    "completed": "Đã chốt theo sổ tiến độ",
    "active": "Đang làm",
    "pending": "Chưa bắt đầu",
    "blocked": "Đang bị chặn",
    "rejected": "Chưa đạt",
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_link(project, name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Đường dẫn phải nằm trong dự án: {name}")
    target = project / path
    if not target.resolve().is_relative_to(project.resolve()):
        raise ValueError(f"Liên kết trỏ ra ngoài dự án: {name}")
    if not target.is_file():
        return f"`{name}` — **Thiếu tệp tại đường dẫn đã đăng ký.**"
    return f"[{path.name}](../{quote(path.as_posix())})"


def render_index(project, progress, extra_paths):
    steps = progress["steps"]
    expected = [f"restart-{number:02}" for number in range(1, 17)]
    if [step["task_id"] for step in steps] != expected:
        raise ValueError("Sổ tiến độ phải có đủ 16 bước theo đúng thứ tự.")
    lines = [
        "# Minh chứng PRISMA HK261",
        "",
        "Mở mục của từng bước để xem bằng chứng gốc, biên bản nghiệm thu và tệp đầu ra đã đăng ký.",
        "Các liên kết trỏ tới bản gốc trong dự án. PDF có giới hạn truy cập được truy vết từ sổ thu thập và chỉ mục nhận dạng ở bước 08.",
        "Kết quả thô hoặc biên bản FAIL được lưu để truy vết. Chỉ biên bản nghiệm thu mới xác nhận bằng chứng được sử dụng.",
        "",
        f"Sổ tiến độ cập nhật lúc `{progress['updated_at']}`.",
        "",
        "- [Kế hoạch 16 bước đã duyệt](../restart_2026_11_26/approved_plan.md)",
        "- [Sổ tiến độ và các tiêu chí nghiệm thu](../restart_2026_11_26/progress.json)",
        "- [Trạng thái dự án](../MUST_READ_AI_AGENT/current_state.json)",
        "- [Nhật ký sự kiện theo thời gian](../MUST_READ_AI_AGENT/events.jsonl)",
        "- [Cách kiểm tra và cập nhật thư mục](MAINTENANCE.md)",
        "",
    ]
    lines.extend(f"- [Bước {number:02}](#buoc-{number:02}) · {step['title']}"
                 for number, step in enumerate(steps, 1))
    for number, step in enumerate(steps, 1):
        verdicts = Counter(item["verdict"] for item in step["acceptance"])
        lines.extend([
            "", f'<a id="buoc-{number:02}"></a>',
            f"## Bước {number:02} · {step['title']}", "",
            f"**{STATUSES[step['status']]}** · `{step['updated_at']}`",
        ])
        if verdicts:
            counts = ", ".join(f"{key}={count}" for key, count in sorted(verdicts.items()))
            lines.extend(["", f"Nghiệm thu cấp bước đã ghi trong sổ: {counts}."])
        paths = dict.fromkeys([*step["artifacts"], *extra_paths.get(step["task_id"], [])])
        lines.append("")
        if not paths:
            lines.append("Chưa có tệp minh chứng được đăng ký cho bước này.")
        lines.extend(f"- {evidence_link(project, name)}" for name in paths)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify the saved index.")
    args = parser.parse_args()
    inventory = read_json(RESTART / "step01_inventory.json")
    locked = read_json(RESTART / "search_dataset_manifest.json")
    extra_paths = {
        "restart-01": [item["path"] for item in inventory["files"] + inventory["checksum_checks"]],
        "restart-04": [item["path"] for item in locked["canonical_raw_inputs"]],
    }
    content = render_index(PROJECT, read_json(RESTART / "progress.json"), extra_paths)
    output = FOLDER / "README.md"
    if args.check:
        if "**Thiếu tệp tại đường dẫn đã đăng ký.**" in content:
            parser.exit(1, "Có tệp minh chứng được đăng ký nhưng chưa tìm thấy.\n")
        if not output.is_file() or output.read_text(encoding="utf-8") != content:
            parser.exit(1, "Mục lục chưa cập nhật. Hãy chạy build_index.py.\n")
    else:
        output.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
