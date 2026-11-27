"""Join HK261 R1/R2 by frozen key and audit candidate PDF locators locally."""

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
from functools import cache
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
RESTART = HERE.parents[2]
PROJECT = RESTART.parent
FINAL = RESTART / "synthesis/final_46"
PACKET = FINAL / "human_review_packet"
PAGE = re.compile(r"(?<!\w)(?:pp?\.|pages?|tr\.)\s*(\d{1,3})(?:\s*[-–—]\s*(\d{1,3}))?", re.I)
APPRAISAL = re.compile(r"^(YES|NO|PARTIAL|NOT_REPORTED|NOT_APPLICABLE|UNRESOLVED)\b")
COVERAGE = re.compile(r"^(VERIFIED_EXACT|PLOT_ONLY|PRINTED_UNRESOLVED)\b")
NUMBER = re.compile(r"(?<![\w./])\d+\.\d+(?![\w./])|(?<![\w./])\d+\s*%")
TEX_ESCAPES = str.maketrans({
    "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
})

CHECKS = {
    "D01": "mục tiêu nghiên cứu và mô hình hệ thống",
    "D02": "giả định, ràng buộc và cách chúng được áp dụng",
    "D03": "cấu hình đủ để tái tạo thí nghiệm",
    "D04": "điều kiện dùng chung để so sánh với đối chứng",
    "D05": "định nghĩa chỉ số và mức phù hợp với mục tiêu",
    "D06": "lặp thí nghiệm, biến thiên hoặc phân tích độ nhạy",
    "D07": "giả định mạng và di động tương ứng với kết luận",
    "D08": "giới hạn kết luận theo phạm vi đánh giá",
    "D09": "đường dẫn hoặc cách tiếp cận mã, dữ liệu, trace hay hiện vật",
    "D10": "giới hạn nghiên cứu và các tuyên bố liên quan",
    "t2_topology": "các nút, hướng luồng suy luận và vai trò từng nút",
    "t2_workload": "mô hình, tác vụ và tập dữ liệu thực sự được đánh giá",
    "t2_partition": "đơn vị phân chia và bước được thực thi ở mỗi nút",
    "t2_decisions_objective_solver": "biến quyết định, mục tiêu, ràng buộc và bộ giải",
    "t3_platform_modality": "cấu hình triển khai và mức đánh giá thực tế",
    "t3_network_event_response": "điều kiện mạng, di động, sự kiện và bằng chứng phản ứng",
}

# Specific recommendations are authored from the original-page audit and retained
# even when a provider row used the wrong metric or cited the wrong context.
PRIORITIES = {
    ("R0003", "D06"): ("5–6", "Hình 2 và §V.B", "Chốt PARTIAL cho D06. Thử độ nhạy theo số yêu cầu/UAV, chưa có biến thiên giữa các lần lặp độc lập."),
    ("R0036", "Q01"): ("12", "§VI, Hình 8(a)", "Dùng đúng điều kiện 20 Mbps và đối chứng RU cho 22% tác giả báo cáo. Giữ dấu vết đơn vị 20 MHz đang sai trong sổ."),
    ("R0080", "Q03"): ("6", "§IV.C, Hình 3 và Bảng I", "Giữ nguyên cách nguồn in “0.9% higher” và “1.5% higher”. Treo đơn vị chênh lệch tương đối hay điểm phần trăm. Điều kiện Hình 3 là 100 MHz, còn 100 Mbps thuộc Bảng I."),
    ("R0090", "Q05"): ("5", "Hình 5 và định nghĩa chỉ số", "Dùng 91% cho tỷ lệ hoàn thành ở 20 UAV nếu giữ chỉ số này. Treo tuyên bố throughput trên 90% do mẫu số và định nghĩa chưa khớp."),
    ("R0092", "Q02"): ("13", "§V.D, Bảng V", "Dùng 1.477 ± 0.054 Wh cho năng lượng toàn hệ thống, trung bình ± SD qua 30 lượt chung seed. Bỏ diễn giải Wh cho mỗi tác vụ."),
    ("R0118", "t2_workload"): ("9", "§VI.B", "Mã hóa thí nghiệm CIFAR-100 là workload thị giác. Giới hạn sửa ở thí nghiệm được đối chiếu."),
    ("R0121", "t3_network_event_response"): ("5, 7–8", "§4, Hình 3 và Bảng 4", "Giữ kết luận ở mức mô hình phân tích. Treo cách gán tham số xác suất và mọi kết luận xác nhận bằng thực nghiệm."),
    ("R0125", "D09"): ("3–5", "§§III–V và phần cuối bài", "Chốt NOT_REPORTED cho đường dẫn hiện vật do tác giả cung cấp trong phạm vi đã kiểm tra. Ghi riêng các framework được nêu."),
    ("R0125", "Q01"): ("3", "§IV.B, Hình 1", "Gắn 12.8 FPS với đúng cấu hình hai worker và kiểm tra riêng đối chứng một worker bốn luồng. Tách hai cấu hình cùng có con số 12.8 FPS."),
    ("R0145", "D06"): ("18", "§6.3, đoạn dưới Hình 11", "Chốt PARTIAL. 20 kịch bản edge cloud cho thấy biến thiên theo kịch bản. Giữ thiếu số lần lặp và độ phân tán trong cùng cấu hình."),
    ("R0145", "Q01"): ("8, 15", "§3.4, Hình 4", "Gắn TTFT ở Hình 4 với dữ liệu chuẩn mà bài dẫn ở [3]. Treo quy kết cho phần cứng/thí nghiệm tại chỗ."),
    ("R0145", "Q02"): ("8, 15", "§3.4, Hình 4", "Gắn TPOT ở Hình 4 với dữ liệu chuẩn mà bài dẫn ở [3]. Treo quy kết cho phần cứng/thí nghiệm tại chỗ."),
}

PAGE_RECHECKS = {
    ("R0080", "D09"): (
        {5: r"IV\.\s*EXPERIMENTS", 6: r"ACKNOWLEDG"},
        "Chốt NOT_REPORTED trong phạm vi PDF đã đọc nếu chưa có hiện vật kèm theo. "
        "Trang 5–6 định vị thiết lập, kết luận và lời cảm ơn. Không thấy đường dẫn hiện vật do tác giả cung cấp.",
    ),
    ("R0089", "Q01"): (
        {9: r"upload.{0,10}ratio.{0,24}0\s*%"},
        "Giữ 0% cho tỷ lệ tải lên của đối chứng All-Local (AL), đúng §5.1/Hình 4(a). "
        "Đây là hành vi của đối chứng, không dùng làm điểm của chính sách được đề xuất.",
    ),
    ("R0089", "t2_decisions_objective_solver"): (
        {7: r"propose.{0,12}two.{0,12}heuristic", 8: r"waiting.{0,16}com.{0,12}putation.{0,10}queue"},
        "Ghi hai heuristic xử lý theo ngưỡng/độ ưu tiên và cơ chế cân bằng theo hàng đợi ở §§4.1–4.2. "
        "Trích lại theo phân cách từ trên PDF.",
    ),
    ("R0089", "t3_network_event_response"): (
        {5: r"orthogonal.{0,25}frequency|OFDMA", 11: r"mobility.{0,14}redundancy.{0,15}future"},
        "Chốt PARTIAL. Ghi giả định OFDMA và phạm vi mô hình. Dự phòng khi UAV di chuyển là việc tương lai. "
        "Giữ cách nguồn mô tả độ trễ biên là bỏ qua trong mô hình.",
    ),
}


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def indexed(items, key):
    result = {key(row): row for row in items}
    if len(items) != len(result):
        raise ValueError("Duplicate evidence keys")
    return result


def normalize(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().replace("\u00ad", "").split())


@cache
def original(path, digest, restricted):
    file = PROJECT / path
    with file.open("rb") as stream:
        actual = hashlib.file_digest(stream, "sha256").hexdigest()
    if actual != digest:
        raise ValueError(f"PDF SHA-256 mismatch: {path}")
    with pymupdf.open(file) as doc:
        return ([None] * len(doc) if restricted else
                [normalize(page.get_text(sort=False)) for page in doc])


def check_pages(path, expectations):
    with pymupdf.open(PROJECT / path) as pdf:
        for page, pattern in expectations.items():
            text = normalize(pdf[page - 1].get_text(sort=True))
            if not re.search(pattern, text, re.I):
                raise ValueError(f"Could not reproduce page recheck: {path} p. {page}")
    return " | ".join(f"gốc p. {page}" for page in expectations)


def numbers_in_pages(value):
    pages = set()
    for match in PAGE.finditer(value):
        first = int(match[1])
        last = int(match[2]) if match[2] else first
        pages.update(range(first, last + 1) if first <= last <= first + 30 else [first])
    return pages


def anchors(row, channel):
    locators = row[f"{channel}_locator"].split(" | ")
    quotes = row[f"{channel}_excerpt"].split(" | ")
    pairs = list(zip(locators, quotes)) if len(locators) == len(quotes) else []
    if channel != "codex":
        for entry in row[f"{channel}_semantic_recheck"].split(" | "):
            if ": " in entry:
                pairs.append(tuple(entry.split(": ", 1)))
    return pairs


def judgment(kind, form, finding):
    value = form["verified_value_or_judgment"]
    status = value.split(" | ", 1)[0]
    pattern = APPRAISAL if kind == "appraisal" else COVERAGE if kind == "report_coverage" else None
    match = pattern.match(finding) if pattern else None
    return (status, match[1] if match else "")


def guidance(row, flags, status1, status2):
    kind, key = row["kind"], row["key"]
    if "NGUON_GIOI_HAN" in flags:
        return "Giữ kết luận trong phạm vi minh chứng đã được phép rà. Tạm treo phần không xác minh được."
    if (priority := PRIORITIES.get((row["record_id"], key))):
        return priority[2]
    if (recheck := PAGE_RECHECKS.get((row["record_id"], key))):
        return recheck[1]
    if kind == "outcome":
        return ("Chốt đúng tên chỉ số, giá trị in, đơn vị, hệ thống/mẫu số, cấu hình và đối chứng tại trang ghi ở dòng này. "
                "Treo phần thiếu căn cứ và giữ riêng giá trị xấp xỉ, giá trị suy ra hoặc điều kiện chưa rõ.")
    if kind == "report_coverage":
        return ("Đọc phần kết quả và phụ lục liên quan. Chốt VERIFIED_EXACT nếu có số kết quả in với điều kiện rõ, "
                "PLOT_ONLY nếu chỉ có hình, hoặc PRINTED_UNRESOLVED nếu số in còn vướng định nghĩa/điều kiện.")
    criterion = CHECKS[key]
    if "NOT_REPORTED" in (status1, status2):
        return f"Kiểm tra {criterion} trong mục đã ghi và tài liệu kèm theo. Giữ NOT_REPORTED nếu nguồn vẫn không nêu."
    if kind == "appraisal":
        return f"Đối chiếu tiêu chí {key} về {criterion}. Chốt YES, PARTIAL, NO hoặc NOT_REPORTED theo bằng chứng cụ thể."
    return f"Chỉ ghi phần nguồn chứng minh về {criterion}. Giữ mức một phần hoặc treo phần chưa định vị được."


def reconcile(row, left, right, study, visual):
    channel = "correction" if row["correction_status"] else "gemini"
    verdict = row[f"{channel}_semantic"]
    first = row["codex_finding"]
    second = row[f"{channel}_finding"]
    status1, label1 = judgment(row["kind"], left, first)
    status2, label2 = judgment(row["kind"], right, second)
    restricted = row["author_attention"] == "RESTRICTED_SOURCE"
    flags = []
    if restricted:
        flags.append("NGUON_GIOI_HAN")
    if status1 != status2:
        flags.append("KHAC_TRANG_THAI")
    if label1 and label2 and label1 != label2 and not restricted:
        flags.append("KHAC_NHAN_GOC")
    if "DISCREPANCY" in (status1, status2):
        flags.append("LECH_DU_LIEU_DA_LUU")
    if verdict == "FAIL":
        flags.append("R2_KHONG_QUA_DOI_CHIEU")
    if "UNRESOLVED" in (status1, status2):
        flags.append("CHUA_GIAI_QUYET")
    if set((status1, status2)) & {"PARTIAL", "NOT_REPORTED", "PLOT_ONLY", "PRINTED_UNRESOLVED",
                                  "VERIFIED_EXACT with PRINTED_UNRESOLVED entries"}:
        flags.append("GIOI_HAN_MINH_CHUNG")
    if row["kind"] == "outcome" and status1 == status2 == "VERIFIED":
        n1 = set(NUMBER.findall(first.split(". Comparison:", 1)[0]))
        n2 = set(NUMBER.findall(second))
        if not n1 or not n1 <= n2:
            flags.append("RA_LAI_GIA_TRI_HAI_BEN")
    if (row["record_id"], row["key"]) in PRIORITIES:
        flags.append("CHOT_TRUOC")

    matched, candidate, locations = set(), set(), []
    editions = [(row["pdf_path"], row["pdf_sha256"], "gốc")]
    if row["supplemental_pdf_path"]:
        editions.append((row["supplemental_pdf_path"], row["supplemental_pdf_sha256"], "IEEE"))
    for path, sha, edition in editions:
        pages = original(path, sha, restricted)
        if restricted:
            continue
        for direction, side in ((left, "codex"), (right, channel)):
            location = direction["original_page_and_locator"]
            for locator, quote in anchors(row, side):
                # The archived audit only used the publisher version when explicitly marked.
                if (edition == "IEEE") != ("ieee publisher pdf" in normalize(locator)):
                    continue
                for n in numbers_in_pages(locator):
                    if 1 <= n <= len(pages) and len(normalize(quote)) >= 12 and normalize(quote) in pages[n - 1]:
                        matched.add((edition, n))
            for part in location.split(" | "):
                if (edition == "IEEE") == ("ieee publisher pdf" in normalize(part)):
                    locations += [part] if part else []
                    candidate.update((edition, n) for n in numbers_in_pages(part) if 1 <= n <= len(pages))
        if edition == "gốc" and not candidate and not matched:
            candidate.update((edition, n) for n in numbers_in_pages(row["suggested_locator"]) if 1 <= n <= len(pages))
    visual_pages = {(v["physical_page"], v["locator"]) for v in visual} if not restricted else set()
    priority = PRIORITIES.get((row["record_id"], row["key"])) if not restricted else None
    page_recheck = PAGE_RECHECKS.get((row["record_id"], row["key"])) if not restricted else None
    rechecked = check_pages(row["pdf_path"], page_recheck[0]) if page_recheck else ""
    if page_recheck:
        candidate -= {("gốc", n) for n in page_recheck[0]}
    if priority:
        candidate.update(("gốc", n) for n in numbers_in_pages("p. " + priority[0].replace(", ", ", p. ")))
    suggested = display_pages(candidate - matched)
    matches = display_pages(matched)
    if flags and not (matches or suggested or visual_pages or rechecked or restricted):
        flags.append("CHUA_CO_TRANG")
    if not flags:
        tier = ""
    elif "NGUON_GIOI_HAN" in flags:
        tier = "4 — giới hạn nguồn"
    elif priority:
        tier = "1 — chốt trước"
    elif set(flags) & {"KHAC_TRANG_THAI", "KHAC_NHAN_GOC", "RA_LAI_GIA_TRI_HAI_BEN"}:
        tier = "2 — đối chiếu"
    else:
        tier = "3 — minh chứng thiếu"
    section = priority[1] if priority else ""
    if not section and not restricted and not matches and not suggested:
        section = row["suggested_locator"]
    return {
        "uu_tien": tier, "co": " | ".join(flags), "ma_bai": row["record_id"], "ma_hkf": row["packet_id"],
        "loai": row["kind"], "khoa": row["key"], "bai": study["title"], "doi": study["doi"],
        "pdf_goc": row["pdf_path"], "pdf_goc_sha256": row["pdf_sha256"],
        "pdf_ieee_bo_sung": row["supplemental_pdf_path"],
        "pdf_ieee_sha256": row["supplemental_pdf_sha256"],
        "trang_khop_cum_trich": matches, "trang_ung_vien": suggested,
        "trang_chot_truoc": priority[0] if priority else "",
        "trang_doc_lai_theo_ngu_canh": rechecked,
        "trang_doi_chieu_bang_hinh": " | ".join(f"gốc p. {n}, {loc}" for n, loc in sorted(visual_pages)),
        "muc_can_doc": section or " | ".join(dict.fromkeys(locations)),
        "tinh_trang_trang": ("Giới hạn nguồn" if restricted else "Có neo văn bản hoặc bằng chứng hình"
                             if matches or visual_pages or rechecked else "Trang ứng viên" if suggested else "Chưa định vị trang"),
        "r1_trang_thai": status1, "r2_trang_thai": status2,
        "r1_nhan_dinh": left["verified_value_or_judgment"], "r2_nhan_dinh": right["verified_value_or_judgment"],
        "r1_don_vi": left["unit"], "r2_don_vi": right["unit"],
        "r1_dieu_kien": left["workload_conditions_and_denominator"],
        "r2_dieu_kien": right["workload_conditions_and_denominator"],
        "r1_ly_do": left["reason_or_verbatim_anchor"],
        "r2_ly_do": right["reason_or_verbatim_anchor"],
        "r2_luot": "rà lại" if channel == "correction" else "ban đầu",
        "r2_kiem_tra_noi_dung": verdict,
        "de_xuat": guidance(row, flags, status1, status2) if flags else "",
        "tac_gia_chot": "",
    }


def display_pages(items):
    return " | ".join(f"{edition} p. {n}" for edition, n in sorted(items))


def write_csv(path, entries):
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=entries[0], lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)


def write_report_data(path, queue, summary):
    cases = [row for row in queue if row["trang_chot_truoc"]]
    lines = [
        rf"\newcommand{{\KeyCount}}{{{summary['keys']}}}",
        rf"\newcommand{{\QueueCount}}{{{summary['queue']}}}",
        rf"\newcommand{{\QueueReports}}{{{summary['queue_reports']}}}",
        rf"\newcommand{{\SemanticDiff}}{{{summary['flags_overlap']['KHAC_NHAN_GOC']}}}",
        rf"\newcommand{{\StateDiff}}{{{summary['flags_overlap']['KHAC_TRANG_THAI']}}}",
        rf"\newcommand{{\AnchoredCount}}{{{summary['locators']['Có neo văn bản hoặc bằng chứng hình']}}}",
        rf"\newcommand{{\CandidateCount}}{{{summary['locators'].get('Trang ứng viên', 0)}}}",
        rf"\newcommand{{\RestrictedCount}}{{{summary['locators']['Giới hạn nguồn']}}}",
        rf"\newcommand{{\SourcePDFCount}}{{{summary['source_pdfs_hash_checked']}}}",
    ]
    for command, block in (("PriorityFirst", cases[:5]), ("PriorityRest", cases[5:])):
        lines.append(f"\\newcommand{{\\{command}}}{{%")
        for row in block:
            identity = f"{row['ma_bai']} · {row['khoa'].replace('t2_workload', 'workload').replace('t3_network_event_response', 'mạng và đánh giá')}"
            where = f"PDF gốc tr. {row['trang_chot_truoc']} · {row['muc_can_doc']}"
            first, second = row["r1_trang_thai"], row["r2_trang_thai"]
            values = (identity, where, f"R1 {first} · R2 {second}", row["de_xuat"])
            lines.append(r"\caseitem" + "".join("{" + value.translate(TEX_ESCAPES) + "}" for value in values))
        lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    form_key = lambda r: (r["packet_id"], r["check_type"], r["check_key"])
    source_key = lambda r: (r["packet_id"], r["kind"], r["key"])
    left, right = [indexed(rows(PACKET / r / "source_verification.csv"), form_key) for r in ("R1", "R2")]
    source = indexed(rows(HERE.parent / "source_review_887.csv"), source_key)
    studies = indexed(rows(FINAL / "study_characteristics.csv"), lambda r: r["report_id"])
    visuals = {}
    for row in rows(HERE.parent / "primary_visual_checks.csv"):
        visuals.setdefault(source_key(row), []).append(row)
    if len(left) != 887 or left.keys() != right.keys() or left.keys() != source.keys() or len(studies) != 46:
        raise ValueError("Source or form inventory differs from the frozen packet")
    entries = [reconcile(row, left[k], right[k], studies[row["record_id"]], visuals.get(k, []))
               for k, row in source.items()]
    queue = sorted((row for row in entries if row["co"]), key=lambda row:
                   (row["uu_tien"], row["ma_bai"], row["loai"], row["khoa"]))
    if len([r for r in queue if r["uu_tien"].startswith("1")]) != len(PRIORITIES):
        raise ValueError("Priority-key mapping changed")
    write_csv(args.output / "muc_can_chot.csv", queue)
    write_csv(args.output / "doi_chieu_887.csv", entries)
    summary = {
        "keys": len(entries), "reports": len(studies), "source_pdfs_hash_checked": original.cache_info().currsize,
        "queue": len(queue), "queue_reports": len({r["ma_bai"] for r in queue}),
        "priority": dict(Counter(r["uu_tien"] for r in queue)),
        "flags_overlap": dict(Counter(flag for r in queue for flag in r["co"].split(" | "))),
        "locators": dict(Counter(r["tinh_trang_trang"] for r in queue)),
        "kinds": dict(Counter(r["loai"] for r in queue)),
        "author_decisions": 0, "pymupdf": pymupdf.VersionBind,
    }
    (args.output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    write_report_data(args.output / "report_data.tex", queue, summary)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
