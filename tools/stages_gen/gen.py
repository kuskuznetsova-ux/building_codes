# -*- coding: utf-8 -*-
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import STAGES
from pages import P
from orig_pages import TERMS, ORIG, LANG
from anchors import REFS
from origx import resolve
from rs_pages import RS
for _k,_v in RS.items(): P[_k]['rs']=_v
from ext_pages import EXT
for (_slug,_c),(_secs,_srcs) in EXT.items():
    _lst=P[_slug][_c]
    # вставляем перед разделом «Источники»
    _idx=[i for i,(h,_) in enumerate(_lst) if h=='Источники']
    _pos=_idx[0] if _idx else len(_lst)
    for _j,_sec in enumerate(_secs): _lst.insert(_pos+_j,_sec)
    _idx=[i for i,(h,_) in enumerate(_lst) if h=='Источники']
    if _idx:
        _h,_it=_lst[_idx[0]]; _lst[_idx[0]]=(_h,_it+[x for x in _srcs if x not in _it])
    else:
        _lst.append(('Источники',list(_srcs)))
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','docs')
os.makedirs(OUT+'/stadii',exist_ok=True)
FLAG={'ru':'🇷🇺 Россия','rs':'🇷🇸 Сербия','eu':'🇪🇺 ЕС (EN 16310)','uk':'🇬🇧 Англия (RIBA 2020)'}

# --- страницы стадий
for n,(slug,name,cells) in enumerate(STAGES,1):
    d=P[slug]
    md=[f'# {n}. {name}','',f'[← К матрице стадий](../sravnenie/stadii.md) · {d["intro"]}','',
        '!!! warning "Статус: черновик"','    Источник каждого раздела указан в конце вкладки. Пометка **⏳** — не сверено. Сербия: по Правилнику 96/2023 (заменил 73/2019) и Закону о планировании и строительстве (ред. до 80/2026).','']
    for k in ['ru','rs','eu','uk']:
        md.append(f'=== "{FLAG[k]}"'); md.append('')
        if (slug,k) in TERMS:
            md.append('    **Термины**'); md.append('')
            md.append(f'    | Язык страны ({LANG[k]}) | Русский |'); md.append('    |---|---|')
            import re as _re
            for it in TERMS[(slug,k)]:
                a_,_,b_=it.partition(' — ')
                if _re.search('[А-Яа-яЁё]',_re.sub(r'\(.*?\)|\*','',a_)) and not _re.search('[А-Яа-яЁё]',_re.sub(r'\*','',b_)):
                    a_,b_=b_,a_
                md.append(f'    | {a_} | {b_} |')
            md.append('')
        for head,items in d[k]:
            md.append(f'    **{head}**'); md.append('')
            for ii,it in enumerate(items):
                refs=[]
                if k!='ru':
                    for hp,ix,rf in REFS.get((slug,k),[]):
                        if ix==ii and head.startswith(hp): refs=rf; break
                if k=='ru':
                    md.append(f'    - {it}'); continue
                md.append('    <div class="pair" markdown>'); md.append('    <div class="orig" markdown>'); md.append('')
                if refs:
                    for ref in refs:
                        res=resolve(ref)
                        if not res: raise SystemExit(f'не найдено: {slug} {k} {head} {ii} {ref}')
                        lab,txt=res
                        md.append(f'    *{LANG[k]} · {lab}:* {txt}'); md.append('')
                md.append('    </div>'); md.append('    <div class="ru" markdown>'); md.append('')
                md.append(f'    {it}'); md.append('')
                md.append('    </div>'); md.append('    </div>'); md.append('')
            md.append('')
    prev_=STAGES[n-2][0] if n>1 else None; next_=STAGES[n][0] if n<len(STAGES) else None
    nav=[]
    if prev_: nav.append(f'[← {STAGES[n-2][1]}]({prev_}.md)')
    if next_: nav.append(f'[{STAGES[n][1]} →]({next_}.md)')
    md.append(' · '.join(nav)); md.append('')
    open(f'{OUT}/stadii/{slug}.md','w').write('\n'.join(md))

# --- матрица
rows=[]
for n,(slug,name,cells) in enumerate(STAGES,1):
    cs=[]
    for k in ['ru','rs','eu','uk']:
        t,src=cells[k]
        s=f'[{t}](../stadii/{slug}.md#{k})'+(('<br><small>'+'; '.join(src)+'</small>') if src else '')
        cs.append(s)
    rows.append(f'| {n} | [{name}](../stadii/{slug}.md) | '+' | '.join(cs)+' |')
matrix='\n'.join(['| № | Сквозная стадия | 🇷🇺 Россия | 🇷🇸 Сербия | 🇪🇺 ЕС (EN 16310) | 🇬🇧 Англия (RIBA 2020) |','|--:|---|---|---|---|---|']+rows)
p=OUT+'/sravnenie/stadii.md'; s=open(p).read()
i=s.index('<div class="matrix" markdown>'); j=s.index('</div>',i)
s=s[:i]+'<div class="matrix" markdown>\n\n'+matrix+'\n\n'+s[j:]
open(p,'w').write(s)
print('ok',len(STAGES))
