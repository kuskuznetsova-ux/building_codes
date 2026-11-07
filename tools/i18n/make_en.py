# -*- coding: utf-8 -*-
"""Создаёт английские версии страниц-матриц (*.en.md) из русских по словарю tools/i18n/ru_en.json.
Переводятся только тексты в колонках и подписи; ссылки «Далее» и источники (<small>) не меняются.
Словарь пополняется командой: python tools/i18n/extract.py <файл> (новые русские строки) и переводом вручную."""
import re,json,os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from extract import PAGES,DOCS,KEEP
TR=json.load(open(os.path.join(HERE,'ru_en.json'),encoding='utf-8'))
LINK=re.compile(r'^\[\*\*(.*)\*\*\]\((.*)\)$')
def tr(s):
    s0=s.strip()
    if s0 in TR: 
        t=TR[s0]
        m=LINK.match(s0)
        return f'[**{t}**]({m.group(2)})' if m else t
    return s
def cell(c):
    parts=[]
    for p in c.strip().split('<br>'):
        p=p.strip()
        m=re.match(r'^\[Далее\]\(([^)]*)\)\{ \.more \}$',p)
        if m: parts.append(f'[More]({m.group(1)}){{ .more }}')
        elif KEEP.match(p): parts.append(p)
        else: parts.append(tr(p))
    return ' '+'<br>'.join(parts)+' '
miss=set()
for page in PAGES:
    src=os.path.join(DOCS,page); out=src[:-3]+'.en.md'
    lines=open(src,encoding='utf-8').read().split('\n'); res=[]
    for l in lines:
        if l.startswith('|'):
            cs=l.split('|')[1:-1]
            res.append('|'+'|'.join(c if re.fullmatch(r'\s*:?-+:?\s*',c) else cell(c) for c in cs)+'|')
        elif not l.strip() or l.startswith(('---','hide:','  - toc','<div','</div>')): res.append(l)
        else: res.append(tr(l))
    txt='\n'.join(res)
    for m in re.finditer(r'[А-Яа-я]{3,}',txt): miss.add(m.group(0))
    open(out,'w',encoding='utf-8').write(txt)
print('готово;',len(miss),'русских слов осталось (источники/названия документов)')
