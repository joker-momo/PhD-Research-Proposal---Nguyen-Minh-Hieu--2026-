"""Dispatch already-written briefs serially; persist unreviewed transport evidence."""
import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'screening_46'
AGENT = Path('/Users/joker/.config/a2a-cli/agents/gemini-research')

def run(args):
    return subprocess.run(args, cwd=AGENT, capture_output=True, text=True)

def collect(batch, routing):
    task_id = routing.get('fallback_task_id') or routing['primary_task_id']
    url = 'http://127.0.0.1:51699' if routing.get('fallback_task_id') else 'http://127.0.0.1:51698'
    response = run(['a2a','task','get','-a',url,task_id,'-o','json'])
    response.check_returncode()
    raw = json.loads(response.stdout)
    task = raw.get('task', raw)
    (ROOT / 'results' / f'batch_{batch:02}_raw.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
    texts = [p['text'] for a in task.get('artifacts',[]) for p in a.get('parts',[]) if isinstance(p.get('text'),str)]
    if not texts:
        texts = [p['text'] for p in task.get('status',{}).get('message',{}).get('parts',[]) if isinstance(p.get('text'),str)]
    for text in reversed(texts):
        stripped = text.strip()
        if stripped.startswith('```'):
            stripped = '\n'.join(stripped.splitlines()[1:-1])
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            continue
        if isinstance(data,dict) and 'records' in data:
            (ROOT / 'results' / f'batch_{batch:02}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
            routing.update(task_id=task_id,context_id=task.get('contextId'),state=task.get('status',{}).get('state'),review='UNREVIEWED')
            (ROOT / 'results' / f'batch_{batch:02}_routing.json').write_text(json.dumps(routing,indent=2)+'\n')
            print(json.dumps({'batch':batch,'task_id':task_id,'records':len(data['records']),'review':'UNREVIEWED'}),flush=True)
            return
    raise RuntimeError(f'No JSON records artifact in batch {batch}; raw task preserved')

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--start',type=int,default=2)
    parser.add_argument('--end',type=int)
    args=parser.parse_args()
    args.end = args.start if args.end is None else args.end
    if args.end != args.start:
        raise RuntimeError('Dispatch one batch only; review and commit it before the next task.')
    status = subprocess.run(['git','status','--porcelain'],cwd=ROOT,capture_output=True,text=True,check=True)
    if status.stdout.strip():
        raise RuntimeError('Project working tree must be clean before dispatch.')
    primary=run(['a2a-serve','status','--dir',str(AGENT),'--url'])
    primary.check_returncode()
    for batch in range(args.start,args.end+1):
        if (ROOT/'results'/f'batch_{batch:02}_routing.json').exists():
            raise RuntimeError(f'Existing batch {batch} must be reconciled, not redispatched')
        print(f'Dispatching batch {batch} at {datetime.now(timezone.utc).isoformat()}',flush=True)
        result=run([str(AGENT/'scripts/a2a-route'),'--brief',str(ROOT/'briefs'/f'batch_{batch:02}.md'),
                    '--project','a2a-continuity','--primary-agent-url',primary.stdout.strip(),'--wait-timeout','10m'])
        (ROOT/'results'/f'batch_{batch:02}_transport.txt').write_text(result.stdout+'\n'+result.stderr)
        if result.returncode:
            print(f'Batch {batch} transport failed; reconcile its exact task ID before proceeding.',flush=True)
            raise SystemExit(result.returncode)
        collect(batch,json.loads(result.stdout))
