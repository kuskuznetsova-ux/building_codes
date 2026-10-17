# -*- coding: utf-8 -*-
"""ОАЭ (Дубай) по стадиям: что подтверждено (DDA Master Planning Guidelines, Dubai Building Code) и какие документы найти."""
import os,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','fire_gen'))
from qlib import Q
MPG='https://dda.gov.ae/-/media/0CDFF6B21C134DD793DA846C3525C17A.pdf'
DBC='https://dda.gov.ae/-/media/DC97EA219133466D908BDEC8A462A2A8.pdf'
sM=f'[DDA MPG]({MPG})'; sD=f'[DBC 2021]({DBC})'
NEED_PERMIT=['Правила и процедура выдачи разрешения на строительство в Дубае (Dubai Municipality / DDA / Trakhees / DSOA — по зоне участка)','Development Control Regulations (DCR) и «план привязки» (affection plan) участка — на них DBC B.4.2 ссылается как на приоритетные']
Q1=Q('mpg','The master planning process consists of three stages','Final Master Plan (FMP).')
Q2=Q('mpg','The Preliminary Master Plan (PMP) is the first stage','goals and objectives.')
Q3=Q('mpg','Stage 2: Sign-Off Sheet (SOS) Following the approval of the PMP','maximum building height.')
Q4=Q('mpg','Stage 3: Final Master Plan (FMP) The Final Master Plan (FMP) forms the final stage','authority approvals.')
Q5=Q('dbc','Projects in design or construction that have a final approved design from the Authority','shall conform to the DBC.')
def pair(lab,q,ru): return ('q',lab,q,ru)
AE={
'01-strategiya':('◐ PMP — Preliminary Master Plan (общее видение и стратегия освоения территории; уровень мастер-плана, не здания)',[sM],
  [pair('DDA MPG, гл. ii.1',Q2+' '+Q1,'Мастер-планирование состоит из трёх стадий: 1) Preliminary Master Plan (PMP); 2) Sign-off Sheet (SOS); 3) Final Master Plan (FMP). PMP — первая стадия согласования: описывает общее видение проекта, цели и задачи; это комплексный отчёт об общей стратегии освоения территории (землепользование, подход к застройке).')],
  ['Dubai Municipality / DDA: порядок оценки целесообразности и «Initial NOC» для отдельного здания (вне мастер-плана) ⏳']),
'02-zadanie':('⏳ не сверено (план привязки участка / DCR; задание на проектирование — частная практика)',[],[],NEED_PERMIT),
'03-koncepciya':('⏳ не сверено (концепция здания — вне прочитанных документов)',[],[],['Требования к концептуальным (эскизным) материалам для согласования в Dubai Municipality / DDA ⏳']),
'04-eskiz':('⏳ не сверено',[],[],['Правила подачи эскизного проекта (если такая стадия есть) ⏳']),
'05-ago-agr':('◐ SOS и FMP — «Sign-off Sheet» и «Final Master Plan» (DDA): согласование мастер-плана и участков, не архитектурного облика здания',[sM],
  [pair('DDA MPG, гл. ii.1, стадии 2–3',Q3+' … '+Q4,'Стадия 2 — Sign-Off Sheet (SOS): после утверждения PMP составляется лист с окончательным делением проекта: план и таблица по участкам (номер, назначение, площадь, GFA, число зданий, число квартир, максимальная высота здания). Стадия 3 — Final Master Plan (FMP): итоговая стадия; добавляет к предыдущим руководства по застройке участков и согласования органов.')],
  ['Правила согласования «архитектурного облика» здания в Дубае (Architectural Review / Design Guidelines застройщика) ⏳']),
'06-proekt-razresheniya':('⏳ не сверено: DBC задаёт требования к проекту, но не состав документации для подачи',[sD],
  [pair('DBC 2021, A.7',Q5,'Проекты в стадии проектирования или строительства, имеющие окончательно утверждённый проект от уполномоченного органа, не обязаны соответствовать DBC. Проекты в стадии проектирования без окончательно утверждённого проекта обязаны соответствовать DBC.')],
  NEED_PERMIT+['Перечень чертежей и разделов, подаваемых на разрешение (по каждому органу) ⏳']),
'07-ekspertiza':('⏳ не сверено: в MPG — согласования «Service Authorities» (NOC); сроки, состав и порядок — ⏳',[sM],[],['Порядок согласования с Civil Defence (UAE Fire and Life Safety Code), DEWA и другими «Service Authorities» ⏳','Dubai Municipality / DDA: процедура технической экспертизы проекта ⏳']),
'08-razreshenie':('⏳ не сверено',[],[],NEED_PERMIT),
'09-rabochaya':('⏳ не сверено',[],[],['Требования к рабочим (shop) чертежам по DBC/DCR ⏳']),
'10-stroitelstvo':('⏳ не сверено',[],[],['Правила надзора и приёмки этапов строительства (Dubai Municipality / DDA / Civil Defence) ⏳']),
'11-ispolnitelnaya':('⏳ не сверено',[],[],['Требования к исполнительной (as-built) документации ⏳']),
'12-priemka-vvod':('⏳ не сверено',[],[],['Процедура выдачи сертификата завершения (Completion Certificate) и подключения коммунальных служб ⏳']),
'13-peredacha':('⏳ не сверено',[],[],['Правила передачи здания и гарантийных обязательств ⏳']),
'14-ekspluatatsiya':('⏳ не сверено',[],[],['Требования к эксплуатации и техническому обслуживанию зданий (в DBC — A.9? «maintenance of DBC» — это про сам код) ⏳']),
}
