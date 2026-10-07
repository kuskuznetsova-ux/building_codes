# -*- coding: utf-8 -*-
import re
import os
S=os.environ.get('NORM_SRC',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','src'))+'/'
FILES={'sp1':'fire/sp1.txt','sp4':'fire/sp4.txt','sp477':'hr/sp477.txt','sp267':'hr/sp267.txt',
 'rs22':'fire/rs22b.txt','rs80':'fire/rs22.txt','adb1':'fire/adb1_26.txt','cpr':'fire/cpr_uk.txt',
 'bsa':'hr/bsa65_c.txt','hrb2':'hr/hrb2_c.txt','hrb6':'hr/hrb6_c.txt','mbo':'hr/mbo.txt','fz':'fire/fz123.txt','mhhr':'hr/mhhr2.txt','sp486':'sp/sp486.txt','garv':'sp/garstvo.txt','adb2':'fire/adb2_26.txt','msb':'hr/msb2.txt','ba1':'uk2/ba_s1.txt','ba6':'uk2/ba_s6.txt','ba7':'uk2/ba_s7.txt','br7':'uk2/br_r7.txt','brs1':'uk2/br_s1.txt','hp3':'uk2/hp_r3.txt','hp4':'uk2/hp_r4.txt','hp5':'uk2/hp_r5.txt','hp9':'uk2/hp_r9.txt','hp41':'uk2/hp_r41.txt','hp44':'uk2/hp_r44.txt','bb100':'uk2/bb100f2.txt','br12':'uk2/br_r12.txt','br16':'uk2/br_r16.txt','br17':'uk2/br_r17.txt','dmpo4':'uk2/dmpo_s4.txt','br11a':'uk2/br_11a.txt','br11e':'uk2/br_11e.txt','br11f':'uk2/br_11f.txt','adb2_06':'uk2/adb2_2006b.txt','es':'eu5/es_n.txt','at':'eu5/at_n.txt','atb':'eu5/atb_n.txt','at23':'eu5/at23o_n.txt','sp59':'acc/sp59.txt','adm2':'acc/adm2.txt','sua':'acc/sua.txt','rsa':'acc/rs.txt','uae':'ae/ud.txt','at22':'eu5/at22_n.txt','at4':'eu5/at4_n.txt','fr':'eu5/fr_n.txt','sp2':'up/sp2r.txt','sp42':'ins/sp42.txt','san':'ins/san_all.txt','rspar':'ins/rs_par.txt','lich':'ins/lich.txt'}
NOISE=re.compile(r'Thorium|Mobile:|Kontakt:|^\s*Email:|Izvrsni in|info@thorium|direndulic|^\s*\d+/27\s*$|ONLINE VERSION|Approved Document B Volume \d, 2019 edition|Building Regulations 2010\s*$|Информация об изменениях|Preuzeto iz elektronske|BUDITE NA PRAVNOJ|online@paragraf|www\.paragraf|poslednju verziju|Ukoliko ovaj propis')
_C={}
def corp(k):
    if k not in _C:
        t=open(S+FILES[k],errors='ignore').read().replace('­','')
        if t.count('\n')>5: t='\n'.join(l for l in t.split('\n') if not NOISE.search(l))
        t=re.sub(r'\s+',' ',t)
        t=t.replace('“ ','“').replace(' ”','”')
        if k in ('ba1','ba6','ba7','br7','brs1','hp3','hp4','hp5','hp9','hp41','hp44','br12','br16','br17','dmpo4','br11a','br11e','br11f','bsa','hrb2','hrb6'):
            t=re.sub(r'\[ F\d+ ','',t); t=re.sub(r'\[ ?','',t); t=re.sub(r' ?\]','',t); t=re.sub(r' M\d+ ',' ',t); t=re.sub(r' {2,}',' ',t)
        if k in ('sp477','sp1','sp4'): t=re.sub(r'\bм 2\b','м²',t)
        if k=='msb': t=re.sub(r'(?<=\s)[1-9](?=[A-ZÄÖÜ])','',t)
        if k=='mhhr': t=re.sub(r'(?<=[a-zäöüß])(?<!Satz)(?<!Nummer)(?<!Absatz) \d (?=[a-zäöüß])',' ',t)
        if k=='mhhr': t=re.sub(r'(?<= )\d(?= [A-ZÄÖÜ])','',t)
        if k=='mbo': t=re.sub(r'(?<=[ .)])\d(?=[A-ZÄÖÜ])','',t)
        _C[k]=t
    return _C[k]
def Q(k,start,end,after=None):
    t=corp(k); a=0
    if after:
        a=t.find(after); assert a>=0,('after?',k,after)
    i=t.find(start,a); assert i>=0,('start?',k,start)
    j=t.find(end,i+len(start)-1 if end.startswith(start[-3:]) else i); assert j>=0,('end?',k,end)
    return t[i:j+len(end)].strip()
LANG={'ru':'ru','rs':'sr','eu':'en','uk':'en','de':'de'}
import datetime
PUB=os.environ.get('PUBDATE') or datetime.date.today().strftime('%d.%m.%y')
ACT=f'<small class="actual">актуально на момент публикации {PUB}</small>'
def pair(lab,quote,ru,lang):
    """возвращает markdown-блок пары (с отступом 4)"""
    o=[]
    o.append('    <div class="pair" markdown>'); o.append('    <div class="orig" markdown>'); o.append('')
    if quote.startswith('|'):   # таблица
        o.append(f'    *{lang} · {lab}:* {ACT}'); o.append('')
        for l in quote.strip('\n').split('\n'): o.append('    '+l)
    else:
        o.append(f'    *{lang} · {lab}:* {ACT} {quote}')
    o.append(''); o.append('    </div>'); o.append('    <div class="ru" markdown>'); o.append('')
    for l in ru.strip('\n').split('\n'): o.append('    '+l)
    o.append(''); o.append('    </div>'); o.append('    </div>'); o.append('')
    return o
