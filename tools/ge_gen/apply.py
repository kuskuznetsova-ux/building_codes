# -*- coding: utf-8 -*-
"""Добавляет колонку «Грузия» в матрицы и вкладку «Грузия» на страницы тем.
Запускать ПОСЛЕ генераторов (build.py, build_uk.py, stages_gen/gen.py): работает поверх готовых docs/.
Повторный запуск безопасен (уже обработанные файлы пропускаются).
  NORM_SRC=<папка с корпусами, внутри ge/> python tools/ge_gen/apply.py"""
import os,re,sys,glob
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import gedata
from gedata import GE,NA,NORMY
from qlib import pair
DOCS=os.path.normpath(os.path.join(HERE,'..','..','docs'))
HDR='Грузия'
DEFAULT_NEED={
 'pozharnaya':'Пост. № 41 (IBC-регламент) по этой теме не прочитан; нужно найти и сверить разделы регламента и технический регламент «Условия пожарной безопасности» (Закон об общественной безопасности, ст. 25)',
 'pozharnaya/vysotnye':'Пост. № 41, п. 403 (высотные здания) по этой теме не вынесен',
 'gradostroitelstvo':'акты о зонировании и детальных планах застройки (К1, К2, К3, линии регулирования), нормы инсоляции и расстояний между зданиями — документы не найдены',
 'dostupnaya':'национальный технический регламент «Национальные стандарты доступности» (по сторонним данным — постановление № 732 от 04.12.2020; на основе ICC A117.1) и IBC-регламент, гл. 11 (Пост. № 41)',
 'obshchestvennye':'Пост. № 41 (гл. 4–10: группы по назначению, лестницы, лифты, выходы) — разделы по общественным зданиям не вынесены',
 'parkovki':'Пост. № 41, п. 406 и гл. 10 (стоянки) — не вынесены; нормы размеров мест и рамп не найдены',
 'vysotnye-zhilye':'Пост. № 41, п. 403 (высотные здания) и нормы по высотному жилью — не вынесены',
 'vysotnye-obshchestvennye':'Пост. № 41, п. 403 (высотные здания) и нормы по общественным высотным зданиям — не вынесены',
 'zhile-do-75':'нормы по жилым зданиям (площади квартир, высота помещений, лестницы) — IBC-регламент покрывает только безопасность; архитектурные нормы жилья не найдены',
 'stadii':'документ Грузии по этой стадии не найден',
}
def esc(s): return s.replace('|','/')
SHORTL={'3176389':'Пост. № 41','4578072':'Пост. № 255','4276845':'Кодекс № 3213','4243170':'Закон № 2608'}
def shortsrc(x):
    m=re.search(r'\]\(([^)]*)\)',x); u=m.group(1) if m else ''
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
        s=NA+': '+esc(DEFAULT_NEED.get(d,'документы Грузии не найдены'))
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
        if 'ОАЭ' not in h or 'Грузия' in h: continue
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
        for it in items:
            if it[0]=='n': o+=['    '+it[1],'']
            elif it[0] in ('q','t'):
                lang=it[4] if len(it)>4 else 'ka'
                ru=it[3]
                o+=pair(it[1],it[2],ru,lang)
        if src:
            o+=['    **Источники**','']+['    - '+s for s in src]+['']
    else:
        o+=['    '+NA+': документы Грузии для этой темы пока не найдены.','','    **Какие документы нужно найти**','','    - '+DEFAULT_NEED.get(d,'документы Грузии')+' ⏳','']
    return o
def do_tab(path,txt):
    if '=== "ОАЭ' not in txt or '=== "'+HDR in txt: return txt,False
    lines=txt.split('\n')
    s=next(i for i,l in enumerate(lines) if l.startswith('=== "ОАЭ'))
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
        if 'Грузия' in lines[a] and lines[a].rstrip().endswith(HDR+' |'):
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
