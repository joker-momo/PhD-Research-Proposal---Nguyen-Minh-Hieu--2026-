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

    def test_unavailable_remains_unretrieved(self):
        record={"screening_id":"R0001","doi":"10.1234/test","title":"Example paper","authors":"J. Doe"}
        with tempfile.TemporaryDirectory() as d, patch.object(retrieval,"fetch",side_effect=lambda url, route: ({"route":route,"url":url,"outcome":"http_error","http":403},b"")):
            result=retrieval.verify_one(record,{"candidates":[]},[],Path(d))
            self.assertEqual(result["status"],"NOT_RETRIEVED")
            self.assertEqual(result["reason_if_no_pdf"],"PUBLISHER_OR_PDF_ACCESS_RESTRICTED")
            self.assertFalse(result["local_path"])


if __name__=="__main__":
    unittest.main()
