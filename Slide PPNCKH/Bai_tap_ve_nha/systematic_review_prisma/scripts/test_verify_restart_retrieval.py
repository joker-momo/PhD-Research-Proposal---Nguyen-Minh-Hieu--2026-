import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import verify_restart_retrieval as retrieval


class RetrievalTests(unittest.TestCase):
    def test_rejects_non_pdf_and_nonpublic_urls(self):
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/"login.pdf"
            file.write_text("<html>Sign in</html>")
            self.assertIsNone(retrieval.pdf_identity(file, {}))
        for url in ("http://example.org", "https://localhost", "https://a:b@example.org", "https://example.org:999"):
            with self.assertRaises(ValueError):
                retrieval.public_url(url)
        with patch.object(retrieval.socket,"getaddrinfo",return_value=[(None,None,None,None,("127.0.0.1",443))]):
            with self.assertRaises(ValueError):
                retrieval.public_url("https://127.0.0.1/")

    def test_literal_spaces_in_public_pdf_url_are_encoded(self):
        from urllib.parse import urlsplit
        url = "https://example.org/files/example paper.pdf"
        with patch.object(retrieval, "public_url", side_effect=urlsplit), patch.object(retrieval, "build_opener") as opener:
            opener.return_value.open.side_effect = retrieval.HTTPException("transport")
            event, _ = retrieval.fetch(url, "public_pdf_candidate")
            self.assertEqual(event["outcome"], "unavailable")
            request = opener.return_value.open.call_args.args[0]
            self.assertTrue(request.full_url.endswith("example%20paper.pdf"))

    def test_slow_pdf_body_stops_at_deadline(self):
        from urllib.parse import urlsplit

        url = "https://example.org/files/example.pdf"
        with patch.object(retrieval, "public_url", side_effect=urlsplit), \
             patch.object(retrieval, "build_opener") as opener, \
             patch.object(retrieval, "monotonic", side_effect=[0, 1, 16]):
            response = opener.return_value.open.return_value.__enter__.return_value
            response.read1.return_value = b"%PDF-"
            event, data = retrieval.fetch(url, "public_pdf_candidate")

        self.assertEqual(event["outcome"], "unavailable")
        self.assertIn("body budget", event["detail"])
        self.assertEqual(data, b"")
        self.assertEqual(response.read1.call_count, 1)

    def test_publication_reuses_identical_pdf_and_preserves_conflicting_pdf(self):
        with tempfile.TemporaryDirectory() as d:
            pdf = Path(d) / "R0001.pdf"
            self.assertEqual(retrieval.publish_pdf(pdf, b"%PDF-original"),
                             retrieval.publish_pdf(pdf, b"%PDF-original"))
            with self.assertRaisesRegex(FileExistsError, "R0001.pdf"):
                retrieval.publish_pdf(pdf, b"%PDF-different")
            self.assertEqual(pdf.read_bytes(), b"%PDF-original")
            self.assertEqual(list(Path(d).iterdir()), [pdf])

    def test_retry_reuses_existing_verified_pdf(self):
        record = {"screening_id": "R0001", "doi": "10.1234/test",
                  "title": "Example paper", "authors": "J. Doe"}
        with tempfile.TemporaryDirectory() as d, \
             patch.object(retrieval, "fetch", return_value=({"route": "crossref", "outcome": "response"}, b"")), \
             patch.object(retrieval, "pdf_identity", return_value={"version": "PUBLISHER_VERSION"}):
            pdf = Path(d) / "R0001.pdf"
            pdf.write_bytes(b"%PDF-original")
            result = retrieval.verify_one(record, {"candidates": []}, [], Path(d))
            self.assertEqual(result["status"], "RETRIEVED_PDF")
            self.assertEqual(pdf.read_bytes(), b"%PDF-original")

    def test_retry_never_reports_existing_unverifiable_pdf_as_missing(self):
        record = {"screening_id": "R0001", "doi": "", "title": "Example paper", "authors": "J. Doe"}
        with tempfile.TemporaryDirectory() as d:
            pdf = Path(d) / "R0001.pdf"
            pdf.write_bytes(b"previous evidence")
            with self.assertRaisesRegex(FileExistsError, "could not be reverified"):
                retrieval.verify_one(record, {"candidates": []}, [], Path(d))
            self.assertEqual(pdf.read_bytes(), b"previous evidence")

    def test_cli_rejects_duplicate_batch_ids_before_writing(self):
        with tempfile.TemporaryDirectory() as d:
            directory = Path(d)
            batch = directory / "batch.jsonl"
            leads = directory / "leads.jsonl"
            row = json.dumps({"screening_id": "R0001"}) + "\n"
            batch.write_text(row * 2)
            leads.write_text(json.dumps({"id": "R0001"}) + "\n")
            output = directory / "out.csv"
            args = ["verify_restart_retrieval.py", "--canonical", str(directory),
                    "--batch", str(batch), "--leads", str(leads), "--output", str(output)]
            with patch("sys.argv", args), self.assertRaises(SystemExit) as caught:
                retrieval.main()
            self.assertEqual(caught.exception.code, 2)
            self.assertFalse(output.exists())
            self.assertFalse((directory / "restart_2026_11_26").exists())

    def test_unavailable_remains_unretrieved(self):
        record={"screening_id":"R0001","doi":"10.1234/test","title":"Example paper","authors":"J. Doe"}
        with tempfile.TemporaryDirectory() as d, patch.object(retrieval,"fetch",side_effect=lambda url, route: ({"route":route,"url":url,"outcome":"http_error","http":403},b"")):
            result=retrieval.verify_one(record,{"candidates":[]},[],Path(d))
            self.assertEqual(result["status"],"NOT_RETRIEVED")
            self.assertEqual(result["reason_if_no_pdf"],"PUBLISHER_OR_PDF_ACCESS_RESTRICTED")
            self.assertFalse(result["local_path"])


if __name__=="__main__":
    unittest.main()
