# -*- coding: utf-8 -*-
"""Добавляет колонку «Индия» (после «Грузия») в матрицы и вкладку «Индия» на страницы тем.
Запускать ПОСЛЕ генераторов и после ge_gen/apply.py: работает поверх готовых docs/.
Повторный запуск безопасен (уже обработанные файлы пропускаются).
  NORM_SRC=<папка с корпусами, внутри in/> python tools/in_gen/apply.py"""
import os,re,sys,glob
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import indata
from indata import IN as GE,NA,NORMY
from qlib import pair
DOCS=os.path.normpath(os.path.join(HERE,'..','..','docs'))
HDR='Индия'; PREV='Грузия'
DEFAULT_NEED={
 'pozharnaya':'NBC 2016 Part 4 и DCPR 2034 по этой теме не вынесены; нужно найти и сверить соответствующие разделы',
 'pozharnaya/vysotnye':'NBC 2016 Part 4 (Annex E) и DCPR 2034 (Прил. I) по этой теме не вынесены',
 'gradostroitelstvo':'DCPR 2034 (Part V — FSI, Part VII — зонирование, отступы), нормы инсоляции — не вынесены',
 'dostupnaya':'NBC 2016 Part 3 (Development Control, accessibility), Harmonised Guidelines (2021), DCPR 2034 — не прочитаны',
 'obshchestvennye':'NBC 2016 Part 3/Part 4 (разделы по общественным зданиям) и DCPR 2034 — по этой теме не вынесены',
 'parkovki':'DCPR 2034, п. 44 (таблица числа мест), NBC Part 4, Annex H — не вынесены',
 'vysotnye-zhilye':'NBC 2016 Part 4 (Annex E) и DCPR 2034 (Прил. I) — архитектурная часть для высотного жилья не вынесена',
 'vysotnye-obshchestvennye':'NBC 2016 Part 4 (Annex E) и DCPR 2034 — архитектурная часть для высотных общественных зданий не вынесена',
 'zhile-do-75':'DCPR 2034, п. 37 (требования к частям зданий) и NBC Part 3 — по этой теме не вынесены',
 'stadii':'документ Индии по этой стадии не найден',
}
def esc(s): return s.replace('|','/')
SHORTL={'DCPR':'DCPR 2034','nmcnagpur':'NBC 2016 Part 4','studiomatrx':'Studio Matrx'}
def shortsrc(x):
    m=re.search(r'\]\(([^)]*)\)',x); u=m.group(1) if m else ''
    if 'DCPR%202034' in u: u=u
    for k,v in SHORTL.items():
        if k in u: return f'[{v}]({u})'
    return x
def cell(d,slug,rel):
    k=(d,slug)
    if k in GE:
        short,src,_=GE[k]
        s=esc(short)
        if src: s+='<br><small>'+'; '.join(esc(shortsrc(x)) for x in src)+'</small>'
    else:
        s=NA+': '+esc(DEFAULT_NEED.get(d,'документы Индии не найдены'))
    return s+f'<br>[Далее]({rel}#ge){{ .more }}'
def table_blocks(lines):
    i=0
    while i<len(lines):
        if lines[i].startswith('|'):
            j=i
            while j<len(lines) and lines[j].startswith('|'): j+=1
            yield i,j; i=j
        else: i+=1
def do_matrix(path,txt):
    lines=txt.split('\n'); changed=False
    rel=os.path.relpath(os.path.dirname(path),DOCS).replace('\\','/')
    for i,j in reversed(list(table_blocks(lines))):
        h=lines[i]
        if PREV not in h or HDR in h: continue
        lines[i]=h.rstrip()+' '+HDR+' |'
        lines[i+1]=lines[i+1].rstrip()+'---|'
        for r in range(i+2,j):
            row=lines[r]; m=re.search(r'\]\(([^)#\s:]+\.md)\)','|'.join(row.split('|')[1:3]))
            if m:
                target=os.path.normpath(os.path.join(os.path.dirname(path),m.group(1)))
                d=os.path.relpath(os.path.dirname(target),DOCS).replace('\\','/')
                slug=os.path.splitext(os.path.basename(target))[0]
                c=cell(d,slug,m.group(1))
            else:
                key=re.sub(r'[*]','',row.split('|')[1]).strip()
                c=NORMY.get(key,NA)
            lines[r]=row.rstrip()+' '+c+' |'
        changed=True
    return '\n'.join(lines),changed
def tab_block(d,slug):
    k=(d,slug); o=['=== "'+HDR+'"','']
    if k in GE:
        short,src,items=GE[k]
        nb=[i for i in items if i[0] in ('q','t') and i[1].startswith('NBC')]
        dc=[i for i in items if i[0] in ('q','t') and i[1].startswith('DCPR')]
        nt=[i for i in items if i[0]=='n']
        def emit(group):
            for it in group:
                o.extend(pair(it[1],it[2],it[3],it[4] if len(it)>4 else 'en'))
        if nb:
            o+=['    **Национальный уровень — NBC 2016 (Национальный строительный кодекс Индии)**','']; emit(nb)
        if dc:
            o+=['    **Мумбаи — DCPR 2034 (местные нормы Большого Мумбаи; не действуют в других городах)**','']; emit(dc)
        for it in nt: o+=['    '+it[1],'']
        if src:
            o+=['    **Источники**','']+['    - '+x for x in src]+['']
    else:
        o+=['    '+NA+': документы Индии для этой темы пока не найдены.','','    **Какие документы нужно найти**','','    - '+DEFAULT_NEED.get(d,'документы Индии')+' ⏳','']
    return o
def do_tab(path,txt):
    if '=== "'+PREV not in txt or '=== "'+HDR in txt: return txt,False
    lines=txt.split('\n')
    s=next(i for i,l in enumerate(lines) if l.startswith('=== "'+PREV))
    e=len(lines)
    for i in range(s+1,len(lines)):
        if lines[i].strip() and not lines[i].startswith('    '): e=i; break
    # откатываем пустые строки в конце вкладки
    while e>s and lines[e-1].strip()=='' : e-=1
    d=os.path.relpath(os.path.dirname(path),DOCS).replace('\\','/'); slug=os.path.splitext(os.path.basename(path))[0]
    blk=['']+tab_block(d,slug)
    while blk and blk[-1]=='': blk.pop()
    lines[e:e]=blk+['']
    return '\n'.join(lines),True
def strip(txt):
    """Убирает ранее добавленные колонку и вкладку Грузии (для обновления)."""
    lines=txt.split('\n'); out=[]; i=0
    while i<len(lines):
        l=lines[i]
        if l.startswith('=== "'+HDR):
            i+=1
            while i<len(lines) and (not lines[i].strip() or lines[i].startswith('    ')): i+=1
            while out and out[-1]=='': out.pop()
            out.append(''); continue
        out.append(l); i+=1
    lines=out
    for a,b in reversed(list(table_blocks(lines))):
        if HDR in lines[a] and lines[a].rstrip().endswith(HDR+' |'):
            for r in range(a,b):
                parts=lines[r].rstrip().split('|')
                # '| a | b | c |' -> убираем последнюю ячейку (с учётом возможных '|' нет: ячейки без '|')
                lines[r]='|'.join(parts[:-2])+'|'
    return '\n'.join(lines)
def main():
    n=[0,0]
    for p in sorted(glob.glob(DOCS+'/**/*.md',recursive=True)):
        t=open(p,encoding='utf-8').read(); o=t
        if HDR in t: t=strip(t)
        t,c1=do_matrix(p,t); t,c2=do_tab(p,t)
        if t!=o: open(p,'w',encoding='utf-8').write(t); n[0]+=c1; n[1]+=c2
    print('матриц:',n[0],'вкладок:',n[1])
if __name__=='__main__': main()
