"""Rebuild masked HK261 physical-page text and the isolated Gemini inputs."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESTART = HERE.parents[1]
SYNTHESIS = RESTART / "synthesis/final_46"
MASKED = RESTART / "fulltext_retrieval/pdf/human_review_full_136"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract(manifest, pages):
    program = pages / "pdfkit_pages"
    subprocess.run(["swiftc", "-O", str(SYNTHESIS / "pdfkit_pages.swift"), "-o", str(program)], check=True)
    for row in manifest["records"]:
        original = MASKED / row["basename"]
        if digest(original) != row["sha256"]:
            raise ValueError(f"Source PDF hash mismatch: {row['id']}")
        target = pages / f"{row['id']}.json"
        target.write_bytes(subprocess.check_output([str(program), str(original)]))


def isolated(manifest, pages, context):
    (context / "criteria.txt").write_text(manifest["protocol_excerpt"] + "\n")
    shutil.copyfile(MASKED / "HKF-093.pdf", context / "HKF-093.pdf")
    for batch in range(8):
        chunks = []
        for row in manifest["records"][batch * 17:(batch + 1) * 17]:
            chunks.append(r"\n===== REPORT " + row["id"] + " =====")
            for page_no, page in enumerate(json.loads((pages / f"{row['id']}.json").read_text()), 1):
                page = re.sub(r"[ \t]+", " ", page)
                page = re.sub(r"\n{2,}", "\n", page)
                references = re.search(r"(?im)^\s*(?:[XVI1-9]+[.]?\s+)?(?:REFERENCES|Bibliography)\s*$", page)
                contents = page[:references.start()] if references and page_no > 1 else page
                chunks.append(f"----- PHYSICAL PAGE {page_no} -----\n{contents}")
                if references and page_no > 1:
                    break
        (context / f"reports-{batch + 1}.txt").write_text("\n".join(chunks))
    expected = json.loads((HERE / "isolated_context_manifest.json").read_text())["files"]
    if {p.name for p in context.iterdir()} != expected.keys() or any(
        digest(context / name) != row["sha256"] for name, row in expected.items()
    ):
        raise ValueError("Rebuilt Gemini input hashes differ from the dispatched copy.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("page_directory", type=Path)
    parser.add_argument("--gemini-context", type=Path)
    parser.add_argument("--reuse-pages", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((HERE / "phase_manifest.json").read_text())
    args.page_directory.mkdir(parents=True, exist_ok=True)
    if not args.reuse_pages:
        extract(manifest, args.page_directory)
    if args.gemini_context:
        args.gemini_context.mkdir(parents=True, exist_ok=True)
        isolated(manifest, args.page_directory, args.gemini_context)
    print(f"{len(manifest['records'])} masked record IDs.")


if __name__ == "__main__":
    main()
