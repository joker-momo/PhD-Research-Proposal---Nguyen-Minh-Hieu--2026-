"""Mechanical screening checks; semantic source review remains a separate gate."""
import argparse
import collections
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'screening_46'
GATES = ['primary_full_report', 'multi_uav_evaluated', 'collaborative_inference',
         'evaluative_evidence', 'date_window', 'english']

def normalized(text):
    return ''.join(c for c in unicodedata.normalize('NFKC', text).lower() if c.isalnum())

def check(path):
    manifest = {r['id']: r for r in json.loads((ROOT / 'manifest.json').read_text())['records']}
    data = json.loads(path.read_text())
    errors = []
    evidence = []
    ids = [r.get('id') for r in data.get('records', [])]
    ranges = [(0,6),(6,12),(12,18),(18,24),(24,30),(30,36),(36,41),(41,46)]
    batch = data.get('batch')
    if not isinstance(batch,int) or not 1 <= batch <= 8:
        errors.append('A1 invalid batch number')
    else:
        start,end = ranges[batch-1]
        expected_ids = list(manifest)[start:end]
        if set(ids) != set(expected_ids):
            errors.append(f'A1 expected IDs {expected_ids}; observed {ids}')
    if len(ids) != len(set(ids)):
        errors.append('A1 duplicate IDs')
    seen_dois = []
    seen_titles = []
    for r in data.get('records', []):
        rid = r.get('id')
        if rid not in manifest:
            errors.append(f'A1 unknown ID {rid}')
            continue
        source = manifest[rid]
        blocks = re.split(r'=== PDF PAGE (\d+) ===\n', Path(source['text']).read_text())
        pages = {int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}
        for field in ['title','authors','year','venue','doi','source_version','identity_evidence','gates','decision','primary_reason','evaluation_modes','alignment','unresolved']:
            if field not in r or (not r[field] and field != 'unresolved'):
                errors.append(f'A2 {rid} missing {field}')
        authors = [normalized(x) for x in r.get('authors', [])]
        if len(authors) != len(set(authors)):
            errors.append(f'A2 {rid} duplicate authors')
        doi = r.get('doi','').strip().lower().removeprefix('https://doi.org/')
        if doi != source['doi'] and doi != 'doi_not_found':
            errors.append(f'A2 {rid} DOI differs from intake: {doi}')
        seen_dois.append(doi)
        seen_titles.append(normalized(r.get('title','')))
        if set(r.get('gates',{})) != set(GATES):
            errors.append(f'A3 {rid} incorrect gate keys')
        entries = [('identity',r.get('identity_evidence',{})), ('alignment',r.get('alignment',{}))]
        entries += list(r.get('gates',{}).items())
        for label, e in entries:
            page = e.get('page')
            quote = e.get('quote','')
            matched = bool(quote) and page in pages and normalized(quote) in normalized(pages[page])
            if not matched:
                errors.append(f'A3 {rid} {label} quote/page mismatch p{page}')
            evidence.append({'id':rid,'field':label,'page':page,'quote':quote,
                             'literal_normalized_match':matched,'rationale':e.get('rationale','')})
        states = [e.get('status') for e in r.get('gates',{}).values()]
        if any(s not in {'YES','NO','UNCERTAIN'} for s in states):
            errors.append(f'A3 {rid} invalid gate status')
        expected = 'EXCLUDE' if 'NO' in states else ('INCLUDE' if states and all(s=='YES' for s in states) else 'UNCERTAIN')
        if r.get('decision') != expected:
            errors.append(f'A4 {rid} decision {r.get("decision")} expected {expected}')
        if r.get('decision')=='INCLUDE' and not 2021 <= int(r.get('year',0)) <= 2026:
            errors.append(f'A6 {rid} included outside year range')
    if len(seen_titles) != len(set(seen_titles)) or len([x for x in seen_dois if x!='doi_not_found']) != len(set(x for x in seen_dois if x!='doi_not_found')):
        errors.append('A2 duplicate normalized DOI/title')
    if data.get('project_files_changed') != 0:
        errors.append('A6 mutation count missing/nonzero')
    result = {'file':str(path),'records':len(ids),'ids':ids,'decisions':dict(collections.Counter(r.get('decision') for r in data.get('records',[]))),
              'mechanical_errors':errors,'quote_checks':len(evidence),'quote_matches':sum(e['literal_normalized_match'] for e in evidence),
              'semantic_review':'PENDING_CODEX_SOURCE_REVIEW','evidence':evidence}
    out = ROOT / 'reviews' / (path.stem + '_mechanical.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='evidence'},ensure_ascii=False))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('result',type=Path)
    check(parser.parse_args().result)
