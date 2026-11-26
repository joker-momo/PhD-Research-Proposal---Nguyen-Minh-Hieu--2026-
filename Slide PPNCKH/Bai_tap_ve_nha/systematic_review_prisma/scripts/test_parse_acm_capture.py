#!/usr/bin/env python3

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("parse_acm_capture.py")
SPEC = importlib.util.spec_from_file_location("parse_acm_capture", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ParseAcmCaptureTests(unittest.TestCase):
    def test_normalize_doi(self) -> None:
        self.assertEqual(MODULE.normalize_doi("https://doi.org/10.1145/3786145"), "10.1145/3786145")
        self.assertEqual(MODULE.normalize_doi(""), "DOI_NOT_FOUND")

    def test_parse_item(self) -> None:
        fragment = """
        <li><input class='issue-Item__checkbox' name='10.1145/1234567'>
        <div class='issue-heading'>research-article</div>
        <div class='bookPubDate' data-title='Published: 04 May 2024'>May 2024</div>
        <h4 class='issue-item__title'><a href='/doi/10.1145/1234567'>A <span>Test</span> Paper</a></h4>
        <ul aria-label='authors'><li><a href='/profile/1' title='A. Author'>A. Author</a></li></ul>
        <div class='issue-item__detail'><a href='/toc/test/2024/1' title='Test Venue'>Volume 1</a></div>
        <div class='issue-item__abstract'><p>Short abstract.</p></div></li>
        """
        record = MODULE.parse_item(
            fragment,
            variant="high_recall",
            page=1,
            rank=1,
            source_url="https://dl.acm.org/action/doSearch?startPage=0",
            captured_at="2026-11-26T10:00:00Z",
        )
        self.assertEqual(record["title"], "A Test Paper")
        self.assertEqual(record["authors"], ["A. Author"])
        self.assertEqual(record["year"], 2024)
        self.assertEqual(record["doi"], "10.1145/1234567")
        self.assertEqual(record["venue"], "Test Venue")


if __name__ == "__main__":
    unittest.main()
