#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, shutil, struct, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
MANIFEST_PATH=HERE/'slides-manifest.json'

def now_iso(): return datetime.now(timezone.utc).isoformat(timespec='seconds')
def die(msg,code=1): print(f'CHYBA: {msg}',file=sys.stderr); raise SystemExit(code)
def load_manifest():
    if not MANIFEST_PATH.exists(): die(f'Manifest neexistuje: {MANIFEST_PATH}')
    try: return json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e: die(f'Manifest není platný JSON: {e}')
def save_manifest(data):
    text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    fd,tmp=tempfile.mkstemp(prefix='.slides-manifest.',suffix='.tmp',dir=str(MANIFEST_PATH.parent),text=True)
    try:
        with os.fdopen(fd,'w',encoding='utf-8',newline='\n') as f:
            f.write(text); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,MANIFEST_PATH)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
def get_slide(data,sid):
    for s in data['slides']:
        if s['id']==sid: return s
    die(f'Neznámé ID snímku: {sid}')
def abs_project_path(data,rel):
    root=(HERE/data.get('project_root','.')).resolve(); p=(root/rel).resolve()
    try: p.relative_to(root)
    except ValueError: die(f'Cesta opouští kořen projektu: {rel}')
    return p
def png_dimensions(path):
    with path.open('rb') as f:
        if f.read(8)!=b'\x89PNG\r\n\x1a\n': die(f'Soubor není platný PNG: {path}')
        lb=f.read(4); ct=f.read(4)
        if len(lb)!=4 or ct!=b'IHDR': die(f'PNG nemá očekávanou IHDR hlavičku: {path}')
        if struct.unpack('>I',lb)[0]<8: die(f'Poškozená IHDR hlavička: {path}')
        return struct.unpack('>II',f.read(8))
def validate_png(data,source):
    if not source.exists() or not source.is_file(): die(f'Zdrojový PNG neexistuje: {source}')
    w,h=png_dimensions(source); warning=None; pol=data.get('policy',{}); ew=pol.get('expected_width'); eh=pol.get('expected_height')
    if ew and eh and (w!=ew or h!=eh):
        ratio=w/h if h else 0
        if abs(ratio-16/9)>0.02: die(f'Neočekávaný poměr stran {w}×{h}; požadováno přibližně 16:9.')
        warning=f'PNG má {w}×{h}, očekáváno ideálně {ew}×{eh}; poměr stran je přijatelný.'
    return w,h,warning
def move_into_place(data,slide,source_arg):
    source=Path(source_arg); source=(Path.cwd()/source).resolve() if not source.is_absolute() else source.resolve()
    w,h,warning=validate_png(data,source); target=abs_project_path(data,slide['output']); target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists() and source!=target: die(f'Cílový soubor už existuje: {target}. Nepřepisuji hotovou práci automaticky.')
    if source!=target: shutil.move(str(source),str(target))
    return target,w,h,warning

def prepare(a):
    d=load_manifest(); abs_project_path(d,d.get('staging_dir','_generated')).mkdir(parents=True,exist_ok=True)
    for l in d.get('lessons',[]): abs_project_path(d,l['output_dir']).mkdir(parents=True,exist_ok=True)
    print(f'Připraveno. Počet snímků: {len(d["slides"])}')
def summary(a):
    d=load_manifest(); counts={s:0 for s in d.get('status_values',[])}
    for s in d['slides']: counts[s['status']]=counts.get(s['status'],0)+1
    print(f'Projekt: {d.get("project","")}'); print(f'Celkem: {len(d["slides"])}')
    for k in ['pending','generating','done','needs_review','failed']: print(f'{k:13s}: {counts.get(k,0)}')
    for label,status,key in [('NEEDS_REVIEW','needs_review','qa_note'),('FAILED','failed','last_error')]:
        rows=[s for s in d['slides'] if s['status']==status]
        if rows:
            print('\n'+label+':')
            for s in rows: print(f'  {s["id"]} — {s["title"]} :: {s.get(key) or ""}')
    print('\nBATCH_COMPLETE' if counts.get('pending',0)==0 and counts.get('generating',0)==0 else '\nBATCH_INCOMPLETE')
def next_slide(a):
    d=load_manifest(); mx=int(d.get('policy',{}).get('max_generation_attempts',3))
    for s in d['slides']:
        if s['status']=='pending' and int(s.get('attempts',0))<mx:
            print(json.dumps({'id':s['id'],'lesson':s['lesson'],'title':s['title'],'scenario_file':s['scenario_file'],'output':s['output'],'attempts':s.get('attempts',0),'max_attempts':mx},ensure_ascii=False,indent=2)); return
    print('NONE')
def start(a):
    d=load_manifest(); s=get_slide(d,a.slide_id); mx=int(d.get('policy',{}).get('max_generation_attempts',3))
    if s['status']=='done': die(f'{s["id"]} je již done; nepřegenerovávám.')
    if s['status']=='generating': die(f'{s["id"]} už je generating.')
    if int(s.get('attempts',0))>=mx: die(f'{s["id"]} vyčerpal limit {mx} pokusů.')
    s['status']='generating'; s['attempts']=int(s.get('attempts',0))+1; s['last_error']=None; s['updated_at']=now_iso(); save_manifest(d)
    print(f'STARTED {s["id"]} attempt={s["attempts"]}/{mx}'); print(f'SCENARIO {s["scenario_file"]}'); print(f'TARGET   {s["output"]}')
def retry(a):
    d=load_manifest(); s=get_slide(d,a.slide_id); mx=int(d.get('policy',{}).get('max_generation_attempts',3))
    if s['status']!='generating': die(f'{s["id"]} není generating.')
    s['last_error']=a.reason; s['qa_note']=None; s['updated_at']=now_iso()
    if int(s.get('attempts',0))>=mx:
        s['status']='failed'; save_manifest(d); print(f'FAILED {s["id"]}: dosažen limit {mx} pokusů.'); return
    s['status']='pending'; save_manifest(d); print(f'REQUEUED {s["id"]} :: {a.reason}')
def complete(a):
    d=load_manifest(); s=get_slide(d,a.slide_id)
    if s['status']!='generating': die(f'{s["id"]} musí být generating; aktuálně {s["status"]}.')
    target,w,h,warning=move_into_place(d,s,a.source); s.update(status='done',last_error=None,qa_note=warning,width=w,height=h,updated_at=now_iso()); save_manifest(d)
    print(f'DONE {s["id"]} -> {target}'); print(f'WARNING: {warning}' if warning else '')
def review(a):
    d=load_manifest(); s=get_slide(d,a.slide_id)
    if s['status']=='done': die(f'{s["id"]} je již done.')
    target,w,h,warning=move_into_place(d,s,a.source); note=a.reason+(f' | {warning}' if warning else '')
    s.update(status='needs_review',last_error=None,qa_note=note,width=w,height=h,updated_at=now_iso()); save_manifest(d); print(f'NEEDS_REVIEW {s["id"]} -> {target}'); print(f'NOTE: {note}')
def fail(a):
    d=load_manifest(); s=get_slide(d,a.slide_id)
    if s['status']=='done': die(f'{s["id"]} je již done.')
    s.update(status='failed',last_error=a.reason,qa_note=None,updated_at=now_iso()); save_manifest(d); print(f'FAILED {s["id"]} :: {a.reason}')
def reset_stale(a):
    d=load_manifest(); n=0
    for s in d['slides']:
        if s['status']=='generating': s.update(status='pending',last_error='Předchozí běh byl přerušen během generování.',updated_at=now_iso()); n+=1
    if n: save_manifest(d)
    print(f'RESET_STALE {n}')
def reconcile(a):
    d=load_manifest(); n=0; bad=0
    for s in d['slides']:
        if s['status']=='done': continue
        target=abs_project_path(d,s['output'])
        if not target.exists(): continue
        try: w,h,warning=validate_png(d,target)
        except SystemExit: bad+=1; continue
        note='Stav obnoven podle existujícího validního PNG.'+(f' {warning}' if warning else '')
        s.update(status='done',last_error=None,qa_note=note,width=w,height=h,updated_at=now_iso()); n+=1
    if n: save_manifest(d)
    print(f'RECONCILED {n}'); print(f'SKIPPED_INVALID {bad}' if bad else '')

def parser():
    p=argparse.ArgumentParser(description='Správa dávkového generování snímků.'); sub=p.add_subparsers(dest='command',required=True)
    for name,func in [('prepare',prepare),('summary',summary),('next',next_slide),('reset-stale',reset_stale),('reconcile',reconcile)]: sub.add_parser(name).set_defaults(func=func)
    q=sub.add_parser('start'); q.add_argument('slide_id'); q.set_defaults(func=start)
    q=sub.add_parser('retry'); q.add_argument('slide_id'); q.add_argument('reason'); q.set_defaults(func=retry)
    q=sub.add_parser('complete'); q.add_argument('slide_id'); q.add_argument('source'); q.set_defaults(func=complete)
    q=sub.add_parser('review'); q.add_argument('slide_id'); q.add_argument('source'); q.add_argument('reason'); q.set_defaults(func=review)
    q=sub.add_parser('fail'); q.add_argument('slide_id'); q.add_argument('reason'); q.set_defaults(func=fail)
    return p
if __name__=='__main__':
    a=parser().parse_args(); a.func(a)
