import csv
import tempfile
import unittest
from pathlib import Path

from prisma_openalex_search import (
    collect_variant,
    duplicate_report,
    normalize_work,
    validate_config,
    validate_observed_at,
    write_bundle,
)


def valid_config():
    return {
        "schema_version": 1,
        "source": "OpenAlex",
        "source_role": "supplementary_compensatory_search",
        "base_url": "https://api.openalex.org/works",
        "query_set_version": "test-1",
        "from_date": "2021-01-01",
        "to_date": "2026-11-26",
        "language": "en",
        "per_page": 2,
        "select": ["id", "doi", "title", "authorships"],
        "variants": [
            {
                "id": "high_recall",
                "search_parameter": "search.title_and_abstract",
                "query": '"UAV swarm" AND "edge intelligence"',
            },
            {
                "id": "complementary",
                "search_parameter": "search.title_and_abstract.exact",
                "query": '"UAV swarm" AND partition*',
            },
        ],
    }


def work(identifier, title, doi=None):
    return {
        "id": f"https://openalex.org/{identifier}",
        "doi": doi,
        "title": title,
        "display_name": title,
        "publication_year": 2025,
        "publication_date": "2025-01-02",
        "type": "article",
        "language": "en",
        "authorships": [
            {"author_position": "first", "author": {"display_name": "A. Author"}},
            {"author_position": "last", "author": {"display_name": "B. Author"}},
        ],
        "primary_location": {
            "landing_page_url": f"https://doi.org/{doi}" if doi else None,
            "source": {"display_name": "Test Venue"},
        },
        "locations_count": 1,
        "is_retracted": False,
    }


class ConfigTests(unittest.TestCase):
    def test_valid_config_accepts_exact_search_for_wildcards(self):
        validate_config(valid_config())

    def test_stemmed_search_rejects_wildcards(self):
        config = valid_config()
        config["variants"][1]["search_parameter"] = "search.title_and_abstract"
        with self.assertRaisesRegex(ValueError, "wildcard"):
            validate_config(config)

    def test_duplicate_variant_ids_are_rejected(self):
        config = valid_config()
        config["variants"][1]["id"] = "high_recall"
        with self.assertRaisesRegex(ValueError, "duplicate variant"):
            validate_config(config)

    def test_observed_at_requires_timezone(self):
        self.assertEqual(
            validate_observed_at("2026-11-26T14:00:00+07:00"),
            "2026-11-26T14:00:00+07:00",
        )
        with self.assertRaisesRegex(ValueError, "timezone"):
            validate_observed_at("2026-11-26T15:00:00")


class CollectionTests(unittest.TestCase):
    def test_cursor_pagination_reconciles_api_total(self):
        pages = iter(
            [
                {
                    "meta": {"count": 3, "next_cursor": "next", "x_query": {"oql": "first"}},
                    "results": [work("W1", "One"), work("W2", "Two")],
                },
                {
                    "meta": {"count": 3, "next_cursor": None, "x_query": {"oql": "first"}},
                    "results": [work("W3", "Three")],
                },
            ]
        )
        requests = []

        def fetch(url, params):
            requests.append((url, dict(params)))
            return next(pages)

        result = collect_variant(valid_config(), valid_config()["variants"][0], fetch)
        self.assertEqual(result["api_reported_total"], 3)
        self.assertEqual(len(result["records"]), 3)
        self.assertEqual(result["page_count"], 2)
        self.assertEqual(requests[0][1]["cursor"], "*")
        self.assertEqual(requests[1][1]["cursor"], "next")
        self.assertEqual(result["interpreted_query"], "first")

    def test_total_mismatch_is_rejected(self):
        def fetch(_url, _params):
            return {
                "meta": {"count": 2, "next_cursor": None, "x_query": {"oql": "query"}},
                "results": [work("W1", "One")],
            }

        with self.assertRaisesRegex(RuntimeError, "count mismatch"):
            collect_variant(valid_config(), valid_config()["variants"][0], fetch)


class OutputTests(unittest.TestCase):
    def test_normalize_work_preserves_identity_and_provenance(self):
        normalized = normalize_work(work("W1", "  Test   Title  ", "10.1000/ABC"), "high_recall")
        self.assertEqual(normalized["openalex_id"], "W1")
        self.assertEqual(normalized["doi"], "10.1000/abc")
        self.assertEqual(normalized["title"], "Test Title")
        self.assertEqual(normalized["authors"], "A. Author; B. Author")
        self.assertEqual(normalized["query_variant"], "high_recall")

    def test_duplicate_report_counts_doi_title_and_openalex_id(self):
        rows = [
            normalize_work(work("W1", "Same Title", "10.1000/a"), "x"),
            normalize_work(work("W2", "Same title", "10.1000/a"), "x"),
        ]
        self.assertEqual(
            duplicate_report(rows),
            {"openalex_id_duplicates": 0, "doi_duplicates": 1, "title_duplicates": 1},
        )

    def test_write_bundle_creates_raw_csv_manifest_and_checksums(self):
        result = {
            "variant": "high_recall",
            "query": "test query",
            "search_parameter": "search.title_and_abstract",
            "filters": "from_publication_date:2021-01-01,to_publication_date:2026-11-26,language:en",
            "api_reported_total": 1,
            "page_count": 1,
            "interpreted_query": "interpreted",
            "records": [work("W1", "One", "10.1000/one")],
            "request_urls": ["https://api.openalex.org/works?example=1"],
        }
        with tempfile.TemporaryDirectory() as temp:
            manifest = write_bundle(
                valid_config(), result, Path(temp), "2026-11-26T15:00:00+07:00"
            )
            raw_path = Path(temp) / manifest["raw_file"]
            csv_path = Path(temp) / manifest["normalized_file"]
            manifest_path = Path(temp) / manifest["manifest_file"]
            checksum_path = Path(temp) / manifest["checksum_file"]
            self.assertTrue(raw_path.is_file())
            self.assertTrue(csv_path.is_file())
            self.assertTrue(manifest_path.is_file())
            self.assertTrue(checksum_path.is_file())
            with csv_path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            self.assertEqual(manifest["api_reported_total"], 1)
            self.assertEqual(manifest["exported_total"], 1)
            self.assertEqual(manifest["duplicate_counts"]["doi_duplicates"], 0)
            self.assertEqual(manifest["source"], "OpenAlex")
            self.assertNotEqual(manifest["source"], "Web of Science Core Collection")
            self.assertTrue(any("not Web of Science" in item for item in manifest["limitations"]))
            self.assertNotIn(b"\r\n", csv_path.read_bytes())
            checksum_text = checksum_path.read_text(encoding="utf-8")
            self.assertIn(raw_path.name, checksum_text)
            self.assertIn(csv_path.name, checksum_text)

    def test_write_bundle_rejects_existing_evidence(self):
        result = {
            "variant": "high_recall",
            "query": "test query",
            "search_parameter": "search.title_and_abstract",
            "filters": "from_publication_date:2021-01-01,to_publication_date:2026-11-26,language:en",
            "api_reported_total": 1,
            "page_count": 1,
            "interpreted_query": "interpreted",
            "records": [work("W1", "One", "10.1000/one")],
            "request_urls": ["https://api.openalex.org/works?example=1"],
        }
        with tempfile.TemporaryDirectory() as temp:
            write_bundle(valid_config(), result, Path(temp), "2026-11-26T15:00:00+07:00")
            with self.assertRaisesRegex(FileExistsError, "refusing to overwrite"):
                write_bundle(valid_config(), result, Path(temp), "2026-11-26T15:00:00+07:00")


if __name__ == "__main__":
    unittest.main()
