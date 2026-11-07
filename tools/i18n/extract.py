# -*- coding: utf-8 -*-
"""Извлечение русских фрагментов из страниц-матриц для перевода (EN). Результат: JSON {русская строка: ''} (заполняется переводом)."""
import re,json,sys,os
DOCS=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','docs'))
PAGES=['pozharnaya/index.md','pozharnaya/vysotnye/index.md','gradostroitelstvo/index.md','sravnenie/arhitektura.md','dostupnaya/index.md','obshchestvennye/index.md','parkovki/index.md','vysotnye-zhilye/index.md','vysotnye-obshchestvennye/index.md','zhile-do-75/index.md']
KEEP=re.compile(r'^(<small>.*</small>|\[Далее\]\([^)]*\)\{ \.more \})$')
def segs(path):
    """Возвращает список (kind, text) для всех русских фрагментов страницы."""
    out=[]
    lines=open(os.path.join(DOCS,path),encoding='utf-8').read().split('\n')
    for l in lines:
        if not l.strip(): continue
        if l.startswith('|'):
            cells=l.split('|')[1:-1]
            for ci,c in enumerate(cells):
                c=c.strip()
                if re.fullmatch(r'-+|:?-+:?',c): continue
                for part in c.split('<br>'):
                    part=part.strip()
                    if not part or KEEP.match(part): continue
                    out.append(part)
        elif l.startswith(('---','hide:','  - toc','<div','</div>')): continue
        else: out.append(l.strip())
    return out
if __name__=='__main__':
    allu={}
    for p in PAGES:
        for s in segs(p):
            if re.search('[А-Яа-я]',s): allu.setdefault(s,'')
    json.dump(allu,open(sys.argv[1],'w'),ensure_ascii=False,indent=0)
    print(len(allu),'строк',sum(len(k) for k in allu),'символов')
