import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.prepare_46screening import (
    publish_refresh_metadata,
    validate_and_publish_staged_texts,
    write_pending_briefs,
)


class PrepareScreeningTests(unittest.TestCase):
    def test_invalid_staged_text_does_not_replace_live_pack(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            live = root / "live"
            staged = root / "staged"
            (live / "text").mkdir(parents=True)
            (staged / "text").mkdir(parents=True)
            original = b"verified original"
            (live / "text/S01.txt").write_bytes(original)
            (staged / "text/S01.txt").write_bytes(b"changed extraction")
            ledger = {
                "text/S01.txt": hashlib.sha256(original).hexdigest(),
            }

            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                validate_and_publish_staged_texts(staged, live, ledger)

            self.assertEqual((live / "text/S01.txt").read_bytes(), original)

    def test_valid_staged_text_can_fill_missing_live_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            live = root / "live"
            staged = root / "staged"
            (live / "text").mkdir(parents=True)
            (staged / "text").mkdir(parents=True)
            content = b"verified extraction"
            (staged / "text/S01.txt").write_bytes(content)
            ledger = {
                "text/S01.txt": hashlib.sha256(content).hexdigest(),
            }

            validate_and_publish_staged_texts(staged, live, ledger)

            self.assertEqual((live / "text/S01.txt").read_bytes(), content)

    def test_pending_briefs_use_existing_absolute_evidence_and_preserve_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "project"
            screening = project / "screening_46"
            (screening / "pdf").mkdir(parents=True)
            (screening / "text").mkdir(parents=True)
            (screening / "briefs").mkdir(parents=True)
            items = []
            for number in range(46):
                identifier = f"R{number + 1:02}"
                pdf = screening / "pdf" / f"{identifier}.pdf"
                text = screening / "text" / f"{identifier}.txt"
                pdf.write_bytes(b"pdf")
                text.write_text("text")
                items.append({
                    "id": identifier,
                    "doi": f"10.1/{identifier}",
                    "source": f"pdf/{identifier}.pdf",
                    "pdf": f"pdf/{identifier}.pdf",
                    "text": f"text/{identifier}.txt",
                })
            accepted = {}
            for number in range(1, 4):
                path = screening / "briefs" / f"batch_{number:02}.md"
                path.write_bytes(f"accepted-{number}".encode())
                accepted[number] = hashlib.sha256(path.read_bytes()).hexdigest()
            marker = "Input records (title_hint is NOT verified metadata):\n"
            for number in range(4, 9):
                path = screening / "briefs" / f"batch_{number:02}.md"
                path.write_text(f"pending-template-{number}\n{marker}[]\n")

            write_pending_briefs(project, screening, items)

            for number, digest in accepted.items():
                path = screening / "briefs" / f"batch_{number:02}.md"
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)
            batch_four = (screening / "briefs/batch_04.md").read_text()
            payload = json.loads(batch_four.split(
                "Input records (title_hint is NOT verified metadata):\n", 1
            )[1])
            self.assertEqual(len(payload), 6)
            for record in payload:
                for field in ("source", "pdf", "text"):
                    locator = Path(record[field])
                    self.assertTrue(locator.is_absolute())
                    self.assertTrue(locator.is_file())
            accepted_four = hashlib.sha256(
                (screening / "briefs/batch_04.md").read_bytes()
            ).hexdigest()
            (screening / "results").mkdir()
            (screening / "results/batch_04_accepted.json").write_text("{}")
            items[18]["title_hint"] = "must not replace dispatched brief"

            write_pending_briefs(project, screening, items)

            self.assertEqual(
                hashlib.sha256(
                    (screening / "briefs/batch_04.md").read_bytes()
                ).hexdigest(),
                accepted_four,
            )

    def test_interrupted_atomic_publish_leaves_no_partial_file_and_retry_succeeds(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            live = root / "live"
            staged = root / "staged"
            (live / "text").mkdir(parents=True)
            (staged / "text").mkdir(parents=True)
            content = b"verified extraction"
            (staged / "text/S01.txt").write_bytes(content)
            ledger = {
                "text/S01.txt": hashlib.sha256(content).hexdigest(),
            }

            def interrupted_copy(source, destination):
                Path(destination).write_bytes(Path(source).read_bytes()[:4])
                raise RuntimeError("simulated interruption")

            with mock.patch(
                "scripts.screening_refresh.shutil.copy2",
                side_effect=interrupted_copy,
            ):
                with self.assertRaisesRegex(RuntimeError, "simulated interruption"):
                    validate_and_publish_staged_texts(staged, live, ledger)

            self.assertFalse((live / "text/S01.txt").exists())
            validate_and_publish_staged_texts(staged, live, ledger)
            self.assertEqual((live / "text/S01.txt").read_bytes(), content)

    def test_late_validation_failure_does_not_partially_update_pending_briefs(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "project"
            screening = project / "screening_46"
            (screening / "pdf").mkdir(parents=True)
            (screening / "text").mkdir(parents=True)
            (screening / "briefs").mkdir(parents=True)
            items = []
            for number in range(46):
                identifier = f"R{number + 1:02}"
                pdf = screening / "pdf" / f"{identifier}.pdf"
                text = screening / "text" / f"{identifier}.txt"
                pdf.write_bytes(b"pdf")
                text.write_text("text")
                items.append({
                    "id": identifier,
                    "doi": f"10.1/{identifier}",
                    "source": f"pdf/{identifier}.pdf",
                    "pdf": f"pdf/{identifier}.pdf",
                    "text": f"text/{identifier}.txt",
                })
            marker = "Input records (title_hint is NOT verified metadata):\n"
            for number in range(1, 9):
                (screening / "briefs" / f"batch_{number:02}.md").write_text(
                    f"template-{number}\n{marker}[]\n"
                )
            before = {
                number: (screening / "briefs" / f"batch_{number:02}.md").read_bytes()
                for number in range(4, 9)
            }
            items[18]["title_hint"] = "must not be published"
            (screening / "text/R46.txt").unlink()
            manifest = screening / "manifest.json"
            manifest.write_bytes(b"original manifest")

            with self.assertRaises(FileNotFoundError):
                publish_refresh_metadata(
                    manifest,
                    "replacement manifest",
                    project,
                    screening,
                    items,
                )

            self.assertEqual(manifest.read_bytes(), b"original manifest")
            for number, content in before.items():
                self.assertEqual(
                    (screening / "briefs" / f"batch_{number:02}.md").read_bytes(),
                    content,
                )


if __name__ == "__main__":
    unittest.main()
