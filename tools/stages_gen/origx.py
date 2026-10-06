# -*- coding: utf-8 -*-
import re, json
import os
S=os.environ.get('NORM_SRC',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','src'))+'/'
HEAD=re.compile(r'^(\d+(\.\d+)*\.|[IVX]+) [A-ZČĆŠŽĐ]')
def _arts_from_text(t):
    arts={}; cur=None; closed=False
    for line in t.split('\n'):
        l=line.strip()
        m=re.match(r'^Član (\d+[a-zđž]*)\*{0,3}$',l)
        if m: cur=m.group(1); arts.setdefault(cur,[]); closed=False; continue
        if cur is None or not l: continue
        if HEAD.match(l) and len(l)<110: closed=True
        if not closed: arts[cur].append(l)
    return arts
_p=open(S+'rs/prav_par.txt').read()
P=_arts_from_text(_p)
Zraw=json.load(open(S+'rs/zakon_arts.json'))
Z={}
for k,v in Zraw.items():
    lines=[x.strip() for x in v.split('\n') if x.strip()]
    out=[]
    for l in lines:
        if HEAD.match(l) and len(l)<110: break
        out.append(l)
    merged=[]
    for l in out:
        if merged and not merged[-1].rstrip().endswith(('.',':',';','?','!','”','"',')')) :
            merged[-1]=merged[-1].rstrip()+' '+l
        else: merged.append(l)
    Z[k]=merged
def _norm(t): return re.sub(r'\s+',' ',t.replace('­','').replace('­',''))
def _clean(t):
    t=re.sub(r'Page \d+ sur \d+\s+Practice of the Profession\s+GA2/13/SoS-Report\s+Work Group Scope of Services\s+Agenda item? ?6\.2\s+The Design and Construction Phases of a Construction Project\s+For Information\s+Draft\s+Date: 16 September 2013\s+Ref: 235/13/PR/PO',' ',t)
    t=re.sub(r'Practice of the Profession\s+GA2/13/SoS-Report\s+Work Group Scope of Services\s+Agenda [Ii]tem 6\.2\s+The Design and Construction Phases of a Construction Project\s+For Information\s+Draft\s+Date: 16 September 2013\s+Ref: 235/13/PR/PO',' ',t)
    t=re.sub(r'Page \d+ sur \d+',' ',t)
    t=re.sub(r'\b(F|S|CZ)\d{1,2}\s+(?=[A-Z])','',t)
    t=re.sub(r'©\s*RIBA 2020',' ',t)
    t=re.sub(r'www\.ribaplanofwork\.com\s*\d*',' ',t)
    t=re.sub(r'RIBA Plan of Work 2020 Overview \| Part \d: [A-Za-z0-9 ]+?(?= [A-Z])',' ',t)
    t=re.sub(r'\d{2,3}\s+RIBA Plan of Work 2020 Overview \| Part \d: RIBA Plan of Work 2020',' ',t)
    return re.sub(r'\s+',' ',t)
def _corp(path): return _clean(_norm(open(S+path).read()))
CORP={'R':_corp('st/riba.txt'),'A':_corp('st/ace.txt'),'C':_corp('eu/cka.txt'),'G':_corp('uk/gw.txt')}
LABEL={'R':'RIBA Plan of Work 2020','A':'ACE, 2013','C':'CKA, 2017','G':'BSR, The three gateways'}
def _sentence(text,phrase,maxlen=300):
    a=text.lower().find(phrase.lower().replace('’',"'") ) if False else text.lower().find(phrase.lower())
    if a<0: return None
    # начало предложения
    st=max(text.rfind('. ',0,a),text.rfind('? ',0,a),text.rfind('! ',0,a))
    st=0 if st<0 else st+2
    if phrase[0].isupper(): st=a
    en=len(text)
    for m in re.finditer(r'[.!?](?=\s+[A-Z“"«(•●0-9])|[.!?]$',text[a:]):
        en=a+m.end(); break
    sent=re.sub(r'^\d+\.\d+\s+','',text[st:en].strip())
    if len(sent)>maxlen:
        cut=sent[:maxlen]; k=max(cut.rfind(', '),cut.rfind('; '))
        sent=(cut[:k] if k>maxlen*0.5 else cut.rsplit(' ',1)[0])+' …'
    return sent
def _para(lines,sel):
    if sel is None: return lines
    if sel.startswith('#'):
        a,_,b=sel[1:].partition('-'); a=int(a); b=int(b) if b else a
        return lines[a:b+1]
    if sel.startswith('~'):
        ph=sel[1:].lower()
        for l in lines:
            if ph in l.lower(): return [l]
        return []
def resolve(ref,maxlen=560):
    """-> (label, text) или None"""
    if ref[0] in 'PZ' and ref[1].isdigit():
        m=re.match(r'^([PZ])(\d+[a-zđž]*)(#[\d-]+|~.+)?$',ref)
        src=P if m.group(1)=='P' else Z
        art=m.group(2); lines=src.get(art)
        if not lines: return None
        sel=_para(lines,m.group(3))
        if not sel: return None
        txt=' '.join(sel)
        if len(txt)>maxlen:
            cut=txt[:maxlen]; k=max(cut.rfind('. '),cut.rfind('; '))
            txt=(cut[:k+1] if k>maxlen*0.5 else cut.rsplit(' ',1)[0])+' …'
        label=('Правилник 96/2023, чл. ' if m.group(1)=='P' else 'Закон, чл. ')+art
        return label,txt
    if ref.startswith('T~'):
        body=ref[2:]; lab,_,txt=body.partition('|'); return lab,txt
    if ref[0] in 'RACG' and ref[1]=='~':
        txt=_sentence(CORP[ref[0]],ref[2:])
        if not txt: return None
        return LABEL[ref[0]],txt
    return None
