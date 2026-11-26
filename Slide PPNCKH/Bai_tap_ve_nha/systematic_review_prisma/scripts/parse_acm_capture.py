#!/usr/bin/env python3
"""Normalize auditable page-level ACM Digital Library captures."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin


DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(20(?:21|22|23|24|25|26))\b")
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def clean_text(value: str) -> str:
    return " ".join(value.split())


def normalize_doi(value: str) -> str:
    match = DOI_RE.search(value or "")
    return match.group(0).lower().rstrip(".,;)>") if match else "DOI_NOT_FOUND"


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


@dataclass
class Node:
    tag: str
    attrs: dict[str, str]
    children: list["Node"] = field(default_factory=list)
    parts: list["Node | str"] = field(default_factory=list)

    def text(self) -> str:
        values = [part.text() if isinstance(part, Node) else part for part in self.parts]
        return clean_text(" ".join(values))

    def walk(self) -> Iterable["Node"]:
        yield self
        for child in self.children:
            yield from child.walk()

    def has_class(self, name: str) -> bool:
        return name in self.attrs.get("class", "").split()


class FragmentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {})
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag, {key: value or "" for key, value in attrs})
        self.stack[-1].children.append(node)
        self.stack[-1].parts.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        self.stack[-1].parts.append(data)


def first(nodes: Iterable[Node], predicate) -> Node | None:
    return next((node for node in nodes if predicate(node)), None)


def parse_item(html: str, *, variant: str, page: int, rank: int, source_url: str, captured_at: str) -> dict:
    parser = FragmentParser()
    parser.feed(html)
    nodes = list(parser.root.walk())

    heading = first(nodes, lambda node: node.has_class("issue-heading"))
    date_node = first(nodes, lambda node: node.has_class("bookPubDate"))
    title_node = first(nodes, lambda node: node.has_class("issue-item__title"))
    detail_node = first(nodes, lambda node: node.has_class("issue-item__detail"))
    abstract_node = first(nodes, lambda node: node.has_class("issue-item__abstract"))
    author_list = first(nodes, lambda node: node.attrs.get("aria-label") == "authors")

    title = title_node.text() if title_node else ""
    display_date = date_node.text() if date_node else ""
    full_date = date_node.attrs.get("data-title", "") if date_node else ""
    year_match = YEAR_RE.search(f"{display_date} {full_date}")
    year = int(year_match.group(1)) if year_match else None

    authors: list[str] = []
    if author_list:
        for node in author_list.walk():
            if node.tag == "a" and "/profile/" in node.attrs.get("href", ""):
                name = clean_text(node.attrs.get("title", "") or node.text())
                if name and name not in authors:
                    authors.append(name)

    venue = "VENUE_NOT_FOUND"
    if detail_node:
        venue_link = first(
            detail_node.walk(),
            lambda node: node.tag == "a" and node.attrs.get("href", "").startswith("/toc/"),
        )
        if venue_link:
            venue = clean_text(venue_link.attrs.get("title", "") or venue_link.text())

    doi = "DOI_NOT_FOUND"
    for node in nodes:
        if node.has_class("issue-item__doi"):
            doi = normalize_doi(node.attrs.get("href", "") or node.text())
            break
    if doi == "DOI_NOT_FOUND":
        checkbox = first(nodes, lambda node: node.tag == "input" and node.has_class("issue-Item__checkbox"))
        if checkbox:
            doi = normalize_doi(checkbox.attrs.get("name", ""))

    title_link = first(
        title_node.walk() if title_node else [],
        lambda node: node.tag == "a" and bool(node.attrs.get("href")),
    )
    if doi != "DOI_NOT_FOUND":
        url = f"https://doi.org/{doi}"
    elif title_link:
        url = urljoin("https://dl.acm.org", title_link.attrs["href"])
    else:
        url = "URL_NOT_FOUND"

    return {
        "source": "ACM Digital Library",
        "collection": "The ACM Full-Text Collection",
        "query_variant": variant,
        "page": page,
        "rank": rank,
        "record_type": heading.text().upper() if heading else "TYPE_NOT_FOUND",
        "display_date": display_date or "DATE_NOT_FOUND",
        "year": year,
        "title": title,
        "authors": authors,
        "venue": venue,
        "doi": doi,
        "url": url,
        "abstract_snippet": abstract_node.text() if abstract_node else "",
        "source_page_url": source_url,
        "captured_at": captured_at,
    }


def load_browser_page(path: Path, variant: str) -> list[dict]:
    payload = json.loads(path.read_text())
    match = re.search(r"startPage_(\d+)\.json$", path.name)
    if not match:
        raise ValueError(f"cannot derive startPage from {path}")
    start_page = int(match.group(1))
    items = payload.get("items")
    if not isinstance(items, list) or not 1 <= len(items) <= 20:
        raise ValueError(f"invalid item count in {path}: {len(items) if isinstance(items, list) else 'not-list'}")
    return [
        parse_item(
            html,
            variant=variant,
            page=start_page + 1,
            rank=start_page * 20 + offset,
            source_url=payload["url"],
            captured_at=payload["captured_at"],
        )
        for offset, html in enumerate(items, start=1)
    ]


def load_manual_pages(input_dir: Path) -> list[dict]:
    records: list[dict] = []
    for path in sorted(input_dir.glob("complementary_page_*.json")):
        payload = json.loads(path.read_text())
        for record in payload["records"]:
            normalized = dict(record)
            match = YEAR_RE.search(record.get("display_date", ""))
            normalized["year"] = int(match.group(1)) if match else None
            normalized["abstract_snippet"] = ""
            normalized["source_page_url"] = f"raw:{path.name}"
            normalized["captured_at"] = payload["captured_at"]
            normalized["doi"] = normalize_doi(record.get("doi", ""))
            if normalized["doi"] != "DOI_NOT_FOUND":
                normalized["url"] = f"https://doi.org/{normalized['doi']}"
            elif not normalized.get("url"):
                normalized["url"] = "URL_NOT_FOUND"
            records.append(normalized)
    return records


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def duplicate_count(records: list[dict]) -> int:
    identifiers: set[str] = set()
    duplicates = 0
    for record in records:
        if record["doi"] != "DOI_NOT_FOUND":
            identifier = f"doi:{record['doi']}"
        else:
            identifier = f"title:{normalize_title(record['title'])}"
        if identifier in identifiers:
            duplicates += 1
        identifiers.add(identifier)
    return duplicates


def qa_variant(records: list[dict], expected: int) -> dict:
    ranks = [record["rank"] for record in records]
    return {
        "expected_records": expected,
        "observed_records": len(records),
        "contiguous_ranks": ranks == list(range(1, expected + 1)),
        "duplicate_ranks": len(ranks) - len(set(ranks)),
        "missing_titles": sum(not bool(record["title"].strip()) for record in records),
        "invalid_or_missing_years": sum(record["year"] not in range(2021, 2027) for record in records),
        "missing_doi_marker": sum(not bool(record["doi"]) for record in records),
        "missing_url_marker": sum(not bool(record["url"]) for record in records),
        "doi_not_found": sum(record["doi"] == "DOI_NOT_FOUND" for record in records),
        "url_not_found": sum(record["url"] == "URL_NOT_FOUND" for record in records),
        "missing_source_page": sum(not bool(record["source_page_url"]) for record in records),
        "normalized_duplicates": duplicate_count(records),
    }


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    complementary = load_manual_pages(args.input_dir)
    for path in sorted(args.input_dir.glob("browser_comp_startPage_*.json")):
        complementary.extend(load_browser_page(path, "complementary"))
    high_recall: list[dict] = []
    for path in sorted(args.input_dir.glob("browser_high_startPage_*.json")):
        high_recall.extend(load_browser_page(path, "high_recall"))
    complementary.sort(key=lambda record: record["rank"])
    high_recall.sort(key=lambda record: record["rank"])

    outputs = {
        "acm_complementary_records.json": complementary,
        "acm_high_recall_records.json": high_recall,
    }
    for name, records in outputs.items():
        write_json(args.output_dir / name, records)

    csv_path = args.output_dir / "acm_all_records.csv"
    columns = [
        "source", "collection", "query_variant", "page", "rank", "record_type", "display_date", "year",
        "title", "authors", "venue", "doi", "url", "abstract_snippet", "source_page_url", "captured_at",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for record in high_recall + complementary:
            row = dict(record)
            row["authors"] = "; ".join(record["authors"])
            writer.writerow(row)

    qa = {
        "schema_version": 1,
        "high_recall": qa_variant(high_recall, 79),
        "complementary": qa_variant(complementary, 325),
    }
    mandatory_zero_fields = [
        "duplicate_ranks", "missing_titles", "invalid_or_missing_years", "missing_doi_marker",
        "missing_url_marker", "missing_source_page",
    ]
    qa["acceptance_pass"] = all(
        result["observed_records"] == result["expected_records"]
        and result["contiguous_ranks"]
        and all(result[field] == 0 for field in mandatory_zero_fields)
        for result in (qa["high_recall"], qa["complementary"])
    )
    qa["duplicate_interpretation"] = (
        "normalized_duplicates are repeated source-result rows preserved at distinct ranks; "
        "they are reported for the next deduplication task and do not invalidate capture completeness"
    )
    write_json(args.output_dir / "acm_capture_qa.json", qa)

    input_files = sorted(args.input_dir.glob("*.json"))
    output_files = [
        args.output_dir / "acm_complementary_records.json",
        args.output_dir / "acm_high_recall_records.json",
        args.output_dir / "acm_capture_qa.json",
        csv_path,
    ]
    manifest = {
        "schema_version": 1,
        "database": "ACM Digital Library",
        "collection": "The ACM Full-Text Collection",
        "capture_method": "authenticated browser page capture; Basic Edition",
        "query_results": {"high_recall": len(high_recall), "complementary": len(complementary)},
        "raw_files": [{"path": str(path), "sha256": sha256(path)} for path in input_files],
        "normalized_files": [{"path": str(path), "sha256": sha256(path)} for path in output_files],
        "qa": qa,
    }
    write_json(args.output_dir / "acm_capture_manifest.json", manifest)
    ledger_files = input_files + output_files + [args.output_dir / "acm_capture_manifest.json"]
    (args.output_dir / "acm_capture_checksums.sha256").write_text(
        "".join(f"{sha256(path)}  {path}\n" for path in ledger_files)
    )
    if not qa["acceptance_pass"]:
        raise SystemExit("ACM capture QA failed; inspect acm_capture_qa.json")


if __name__ == "__main__":
    main()
