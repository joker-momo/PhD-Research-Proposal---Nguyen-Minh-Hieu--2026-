"""Verify lawful retrieval leads against the newly deduplicated HK261 records."""
import argparse
import csv
import hashlib
import ipaddress
import json
import re
import shutil
import socket
import subprocess
import tempfile
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import Request, HTTPRedirectHandler, build_opener
from zoneinfo import ZoneInfo


DOI = re.compile(r"10\.\d{4,9}/[^\s<>\"?#]+", re.I)
POPPLER = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin"
LIMIT = 25 * 1024 * 1024


def norm(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text.casefold()) if c.isalnum())


def doi_key(text):
    return text.strip().removeprefix("https://doi.org/").rstrip(".,;").casefold()


def doi_url(doi):
    return "https://doi.org/" + quote(doi, safe="/:;()+._-")


def now():
    return datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).isoformat(timespec="seconds")


def public_url(url):
    parsed = urlsplit(url)
    host = parsed.hostname
    if parsed.scheme != "https" or not host or "." not in host or parsed.username or parsed.password:
        raise ValueError("HTTPS public host required")
    if parsed.port not in (None, 443):
        raise ValueError("Nonstandard destination port")
    if not all(ipaddress.ip_address(addr[4][0]).is_global for addr in socket.getaddrinfo(host, 443)):
        raise ValueError("Nonpublic network destination")
    return parsed


class PublicRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url, kind):
    event = {"timestamp": now(), "route": kind, "url": url}
    try:
        public_url(url)
        request = Request(url, headers={"User-Agent": "HK261-Scholarly-Fulltext/1.0", "Accept": "*/*"})
        with build_opener(PublicRedirect()).open(request, timeout=5) as response:
            event.update(http=response.status, final_url=response.url, media_type=response.headers.get_content_type())
            cap = 3 * 1024 * 1024 if kind in {"crossref", "openalex", "publisher_landing"} else LIMIT
            data = response.read(cap + 1)
            if len(data) > cap:
                return event | {"outcome": "size_limit"}, b""
            return event | {"outcome": "response"}, data
    except HTTPError as e:
        outcome = "anti_bot_challenge" if e.headers.get("cf-mitigated") == "challenge" else "http_error"
        return event | {"outcome": outcome, "http": e.code, "final_url": e.url}, b""
    except (URLError, OSError, ValueError) as e:
        return event | {"outcome": "unavailable", "detail": str(e)[:220]}, b""


def pdf_text(path, first=1, last=2):
    return subprocess.check_output(
        [str(POPPLER / "pdftotext"), "-f", str(first), "-l", str(last), str(path), "-"],
        stderr=subprocess.DEVNULL, timeout=8,
    ).decode("utf-8", errors="replace")


def pdf_identity(path, row, *, linked=False):
    with path.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            return None
    try:
        info = subprocess.check_output([str(POPPLER / "pdfinfo"), str(path)], stderr=subprocess.DEVNULL, timeout=8).decode()
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
        first = pdf_text(path, 1, min(pages, 2))
        end = pdf_text(path, pages, pages) if pages > 2 else ""
    except (subprocess.SubprocessError, OSError, AttributeError, ValueError):
        return None
    first_norm = norm(first)
    title = norm(row["title"])
    names = re.findall(r"[^\W\d_]{3,}", row["authors"].split(";")[0])
    author = names[-1] if names and row["authors"] != "AUTHOR_NOT_FOUND" else ""
    exact_title = title and title in first_norm[:2850]
    doi = doi_key(row.get("verified_doi") or row["doi"])
    exact_doi = DOI.fullmatch(doi) and doi in re.sub(r"\s+", "", first.casefold())
    if not exact_title or not (exact_doi or linked or (author and norm(author) in first_norm)):
        return None
    # A single page can be a cover or abstract. Require substantive body and final-page text.
    if pages < 2 or len(first_norm) < 1900 or (pages > 2 and len(norm(end)) < 130):
        return None
    top = first.casefold()
    if "accepted manuscript" in top or "author accepted version" in top:
        version = "ACCEPTED_MANUSCRIPT"
    elif re.search(r"arxiv:\s*\d{4}\.\d{4,5}", top) or "this preprint" in top:
        version = "PREPRINT"
    elif exact_doi and re.search(r"©|copyright|journal|proceedings|digital object identifier", top):
        version = "PUBLISHER_VERSION"
    else:
        version = "VERSION_UNCONFIRMED"
    return {"page_count": pages, "identity_check": "EXACT_TITLE_AND_DOI" if exact_doi else
            ("EXACT_TITLE_AND_LINKED_PROVIDER_METADATA" if linked else "EXACT_TITLE_AND_FIRST_AUTHOR"),
            "version": version}


def local_candidates(project, rows):
    folders = [project / "screening_46/pdf", project / "corpus_expansion/preserved_candidate_fulltext",
               Path("/Users/joker/Downloads/bai_tap_lon_ref")]
    matches = {row["screening_id"]: [] for row in rows}
    files = sorted({p for folder in folders if folder.is_dir() for p in folder.glob("*.pdf")})
    titles = {row["screening_id"]: norm(row["title"]) for row in rows}
    for file in files:
        try:
            body = norm(pdf_text(file))
        except (subprocess.SubprocessError, OSError):
            continue
        for sid, title in titles.items():
            if title and title in body:
                matches[sid].append(str(file))
    return matches



class ArticleHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.text = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.skip += 1
        if tag == "meta":
            meta = dict(attrs)
            if meta.get("name") in {"citation_title", "citation_doi", "citation_pdf_url"}:
                self.meta[meta["name"]] = meta.get("content") or ""

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.text.append(data.strip())


def article_html(data, title, doi):
    parser = ArticleHTML()
    parser.feed(data.decode("utf-8", "replace"))
    if norm(parser.meta.get("citation_title", "")) != norm(title):
        return None, ""
    if not doi or doi_key(parser.meta.get("citation_doi", "")) != doi:
        return None, ""
    text = "\n".join(parser.text)
    lines = [line.strip().casefold() for line in parser.text]
    sections = [r"(?:(?:\d+)|(?:[ivxlc]+))?\.?\s*(?:method[s]?|materials and methods|system model|proposed method|methodology)",
                r"(?:(?:\d+)|(?:[ivxlc]+))?\.?\s*(?:results|evaluation|performance evaluation|experiments|experimental results)",
                r"(?:(?:\d+)|(?:[ivxlc]+))?\.?\s*(?:bibliography|references)"]
    full = len(norm(text)) > 8500 and all(any(re.fullmatch(pattern, line) for line in lines) for pattern in sections)
    return (text if full else None), parser.meta.get("citation_pdf_url", "")


def get_articles(data, key):
    try:
        result = json.loads(data)
        return result.get(key, {}) if key else result
    except (ValueError, AttributeError):
        return {}


def source_class(url, publisher):
    if not url:
        return ""
    a, b = urlsplit(url).hostname, urlsplit(publisher or "https://doi.org").hostname
    return "PUBLISHER" if a == b else "PUBLIC_REPOSITORY_OR_AUTHOR"


def verify_one(record, lead, local, out):
    rec = record.copy()
    sid = rec["screening_id"]
    attempts = []
    rec.update(status="NOT_RETRIEVED", verified_doi="", landing_url="", identity_url="", source_url="",
               source_class="", version="", local_path="", sha256="", page_count="", identity_check="",
               reason_if_no_pdf="", next_route="", checked_at=now(), provider_notes=json.dumps(lead, ensure_ascii=False))
    doi = doi_key(rec["doi"])
    def attempt(url, route):
        event, data = fetch(url, route)
        attempts.append(event)
        return event, data
    def finish():
        rec["attempts"] = json.dumps(attempts,ensure_ascii=False)
        return rec
    candidate_doi = doi_key(lead.get("doi", ""))
    if not DOI.fullmatch(doi) and DOI.fullmatch(candidate_doi):
        doi = candidate_doi
    publisher = ""
    candidates = {}
    checked_html = None
    if DOI.fullmatch(doi):
        metadata_url = "https://api.crossref.org/works/" + quote(doi, safe="/")
        cross_event, cross_body = attempt(metadata_url, "crossref")
        cross = get_articles(cross_body, "message")
        if cross.get("DOI") and doi_key(cross["DOI"]) == doi:
            if not any(norm(rec["title"]) == norm(t) for t in cross.get("title", [])):
                cross_event["outcome"] = "exact_doi_title_mismatch"
            else:
                cross_event["outcome"] = "exact_doi_title_match"
                rec.update(verified_doi=cross["DOI"], identity_url=metadata_url)
        if rec["doi"] == "DOI_NOT_FOUND" and not rec["verified_doi"]:
            doi = ""
        if doi:
            rec["landing_url"] = doi_url(doi)
    for path in local:
        result = pdf_identity(Path(path), rec)
        attempts.append({"timestamp":now(),"route":"local_exact_title","locator":path,
                         "outcome":"matched_readable_pdf" if result else "version_identity_or_pdf_check_failed"})
        if result and result["version"] in {"PUBLISHER_VERSION", "ACCEPTED_MANUSCRIPT"}:
            dst = out / f"{sid}.pdf"
            shutil.copyfile(path, dst)
            rec.update(result,status="RETRIEVED_PDF",source_class="USER_OR_PROJECT_LOCAL",
                       source_url=rec["landing_url"],identity_url=rec["identity_url"] or rec["landing_url"],local_path=f"pdf/{dst.name}",
                       sha256=hashlib.sha256(dst.read_bytes()).hexdigest())
            return finish()
    if doi:
        landing_event, landing_body = attempt(rec["landing_url"],"publisher_landing")
        publisher = landing_event.get("final_url", "")
        if landing_body and landing_event.get("media_type") in {"text/html","application/xhtml+xml"}:
            text, pdf_link = article_html(landing_body, rec["title"], doi)
            if text:
                checked_html = (publisher, text)
                rec.update(verified_doi=doi, identity_url=publisher)
            if pdf_link.startswith("https://"):
                candidates[pdf_link]=("publishedversion",publisher,True)
        lookup_url = "https://api.openalex.org/works/https://doi.org/" + quote(doi,safe="/")
        oa_event, oa_body = attempt(lookup_url,"openalex")
        oa = get_articles(oa_body, "")
        oa_id = oa.get("doi") or ""
        if doi_key(oa_id) == doi and norm(oa.get("title") or "") == norm(rec["title"]):
            oa_event["outcome"] = "exact_doi_title_match"
            if not rec["verified_doi"]:
                rec.update(verified_doi=doi, identity_url=lookup_url)
            for loc in [oa.get("best_oa_location")] + (oa.get("locations") or []):
                if loc and loc.get("is_oa") and loc.get("pdf_url"):
                    candidates[loc["pdf_url"]] = (loc.get("version") or "", lookup_url, True)
        elif oa_id:
            oa_event["outcome"] = "exact_doi_title_mismatch"
        if doi.startswith("10.1145/") and rec["verified_doi"]:
            notional_acm_pdf = "https://dl.acm.org/doi/pdf/" + quote(doi,safe="/")
            candidates.setdefault(notional_acm_pdf,("publishedversion",rec["identity_url"],True))
        if rec["verified_doi"]:
            for link in cross.get("link", []):
                if link.get("content-type") == "application/pdf" and link.get("URL", "").startswith("https://"):
                    candidates.setdefault(link["URL"],("publishedversion",metadata_url,True))
    for lead_candidate in lead.get("candidates", []):
        url = lead_candidate.get("url", "")
        if lead_candidate.get("format") == "PDF" and url.startswith("https://"):
            candidates.setdefault(url,(lead_candidate.get("version",""),lead_candidate.get("evidence_url",""),False))
    if not doi and lead.get("publisher_url","").startswith("https://"):
        landing_event,_=attempt(lead["publisher_url"],"title_lead_landing")
        rec["landing_url"] = landing_event.get("final_url",lead["publisher_url"])
    for url,(version,evidence,linked) in list(candidates.items())[:6]:
        event, body = attempt(url,"public_pdf_candidate")
        event.update(version_metadata=version,evidence_url=evidence)
        if not body.startswith(b"%PDF-"):
            if body:
                event["outcome"]="non_pdf_response"
            continue
        with tempfile.TemporaryDirectory() as tmp:
            trial=Path(tmp)/"candidate.pdf"
            trial.write_bytes(body)
            result=pdf_identity(trial,rec,linked=linked)
        if not result:
            event["outcome"]="download_failed_identity_or_readability"
            continue
        if (result["version"] == "PREPRINT" or "submittedversion" in version.casefold()
            or "preprint" in version.casefold()) and result["identity_check"] != "EXACT_TITLE_AND_DOI":
            event["outcome"]="preprint_exact_version_link_unconfirmed"
            continue
        if result["version"] == "VERSION_UNCONFIRMED" and linked:
            result["version"]={"publishedversion":"PUBLISHER_VERSION","acceptedversion":"ACCEPTED_MANUSCRIPT",
                               "submittedversion":"PREPRINT"}.get(version.casefold(),result["version"])
        if result["version"] not in {"PUBLISHER_VERSION", "ACCEPTED_MANUSCRIPT"}:
            event["outcome"]="pdf_report_version_unverified"
            continue
        dst=out/f"{sid}.pdf"
        dst.write_bytes(body)
        event["outcome"]="verified_pdf"
        final=event["final_url"]
        rec.update(result,status="RETRIEVED_PDF",source_url=final,source_class=source_class(final,publisher),
                   local_path=f"pdf/{dst.name}",sha256=hashlib.sha256(body).hexdigest())
        return finish()
    if any(x["outcome"]=="exact_doi_title_mismatch" for x in attempts) and not rec["verified_doi"]:
        rec["reason_if_no_pdf"]="DOI_TITLE_CONFLICT"
    elif any(x["outcome"]=="preprint_exact_version_link_unconfirmed" or x["outcome"]=="preprint_not_verified_target_report_version" for x in attempts):
        rec["reason_if_no_pdf"]="PREPRINT_ONLY_TARGET_VERSION_UNVERIFIED"
    elif any(x["outcome"]=="pdf_report_version_unverified" for x in attempts):
        rec["reason_if_no_pdf"]="PDF_REPORT_VERSION_UNVERIFIED"
    elif any(x["outcome"]=="download_failed_identity_or_readability" for x in attempts):
        rec["reason_if_no_pdf"]="PDF_FAILED_IDENTITY_OR_READABILITY"
    elif any(a["outcome"]=="anti_bot_challenge" for a in attempts):
        rec["reason_if_no_pdf"]="PUBLISHER_ANTI_BOT_CHALLENGE"
    elif any(a.get("http") in (401,402,403) for a in attempts if a["route"] in {"publisher_landing","public_pdf_candidate"}):
        rec["reason_if_no_pdf"]="PUBLISHER_OR_PDF_ACCESS_RESTRICTED"
    elif any(a.get("http") in (202,429,503) for a in attempts if a["route"] in {"publisher_landing","public_pdf_candidate"}):
        rec["reason_if_no_pdf"]="PUBLISHER_OR_PDF_AUTOMATED_ACCESS_UNAVAILABLE"
    elif not doi:
        rec["reason_if_no_pdf"]="DOI_OR_TITLE_IDENTITY_UNRESOLVED"
    else:
        rec["reason_if_no_pdf"]="NO_VERIFIED_PDF_FROM_CHECKED_ROUTES"
    if checked_html:
        url,text=checked_html
        html=out.parent/"html"
        html.mkdir(exist_ok=True)
        path=html/f"{sid}.txt"
        path.write_text(text)
        rec.update(status="RETRIEVED_HTML",version="PUBLISHER_VERSION",source_url=url,source_class="PUBLISHER",
                   local_path=f"html/{path.name}",sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                   identity_check="PUBLISHER_CITATION_TITLE_AND_DOI_WITH_FULL_SECTIONS")
    rec["next_route"]="Open the DOI/publisher link in a standard browser or via HCMUT library access. Request an author manuscript if needed."
    if not rec["landing_url"]:
        rec["next_route"]="Use the exact title in HCMUT library search and provide the publisher link or PDF."
    return finish()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical", type=Path, required=True)
    parser.add_argument("--batch", type=Path, required=True)
    parser.add_argument("--leads", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args=parser.parse_args()
    rows=[json.loads(line) for line in args.batch.read_text().splitlines()]
    raw_leads=list(map(json.loads,args.leads.read_text().splitlines()))
    leads={item["id"]:item for item in raw_leads}
    if len(raw_leads) != len(leads) or set(leads)!={row["screening_id"] for row in rows}:
        parser.error("Lead IDs must match the exact batch")
    pdf=args.canonical/"restart_2026_11_26/fulltext_retrieval/pdf"
    pdf.mkdir(parents=True,exist_ok=True)
    local=local_candidates(args.canonical, rows)
    with ThreadPoolExecutor(max_workers=10) as pool:
        results=list(pool.map(lambda row:verify_one(row,leads[row["screening_id"]],local[row["screening_id"]],pdf),rows))
    with args.output.open("w",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=list(results[0]),lineterminator="\n")
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()
