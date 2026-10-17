# -*- coding: utf-8 -*-
"""ОАЭ (Дубай): Dubai Building Code 2021 (DDA) и Master Planning Guidelines (DDA). Пожарные нормы — UAE FLSC (не прочитан), DBC только отсылает к нему."""
from qlib import Q
DBC='https://dda.gov.ae/-/media/DC97EA219133466D908BDEC8A462A2A8.pdf'
MPG='https://dda.gov.ae/-/media/0CDFF6B21C134DD793DA846C3525C17A.pdf'
def l(t,u): return f'[{t}]({u})'
def dq(lab,q,ru): return ('q','DBC 2021, '+lab,q,ru)
def mq(lab,q,ru): return ('q','DDA MPG, '+lab,q,ru)
AE={}   # (группа, slug) -> (кратко, [источники], [цитаты])
def e(g,s,short,src,items): AE[(g,s)]=(short,src,items)
NA='⏳ не сверено: пожарные требования — в UAE FLSC (Civil Defence), документ недоступен'
RISE=dq('B.2, D.2, E.2 (определения)',Q('dbc','Low-rise building: Building height less than or up to 15 m','given in UAE FLSC.'),
 'Low-rise (малоэтажное): высота не более 15 м, измеряется по UAE FLSC; более подробное определение — в UAE FLSC.')
RISE2=dq('D.2, B.2 (определения)',Q('dbc','High-rise building: Building height greater than or equal to 23 m and up to 90 m','given in UAE FLSC.'),
 'High-rise (высотное): высота от 23 м до 90 м (по UAE FLSC).')
RISE3=dq('B.2 (определения)',Q('dbc','Super high-rise building: Building height greater than 90 m','UAE FLSC'),'Super high-rise (супервысотное): высота более 90 м, измеряется по UAE FLSC.')
# ---------- пожарные темы ----------
e('F','klassy','Классов по пожароопасности в DBC нет — они в UAE FLSC; DBC: low-rise ≤15 м, high-rise 23–90 м, super high-rise >90 м',[l('DBC 2021, разд. B.2, D.2, E.2',DBC)],[RISE,RISE2,RISE3])
e('F','metodiki','Высота здания — по UAE FLSC; для планировки — от «уровня ворот» участка (gate level) до верха оболочки здания (MPG)',[l('DBC 2021',DBC),l('DDA MPG, гл. 6',MPG)],
 [mq('гл. 6, высота здания',Q('mpg','building heights must be measured as the maximum height from gate level (GL) to the top of the building envelope','machine rooms.'),
  'Высота здания в метрах измеряется как максимальная высота от уровня ворот (GL) до верха оболочки здания; включает архитектурные элементы и специальные элементы (купола, технические этажи, машинные помещения).')])
e('F','pravovaya-sila','DBC и UAE FLSC вместе — основные правила проектирования зданий в Дубае; допускаются альтернативные решения при доказанной равноценности (решает орган)',[l('DBC 2021, A.4.3, A.8',DBC)],
 [dq('A.4.3',Q('dbc','The DBC and UAE Fire and Life Safety Code of Practice (UAE FLSC)','referenced throughout the DBC.'),
   'DBC и UAE Fire and Life Safety Code of Practice (UAE FLSC) вместе образуют основные правила проектирования зданий в Дубае. UAE FLSC упоминается по всему DBC.'),
  dq('A.8',Q('dbc','An alternative solution shall meet the intent of the performance statements','prescriptive design requirements.'),
   'Альтернативное решение должно соответствовать цели «перформанс-положений» и обеспечивать не меньший уровень, чем все предписывающие требования. Допустимость решает уполномоченный орган; ответственность за доказательство — на консультанте.')])
e('F','vyhody','Число эвакуационных лестниц, ширину и отделение определяет UAE FLSC, гл. 3 (DBC, B.6.4.1.1)',[l('DBC 2021, B.6.4.1',DBC)],
 [dq('B.6.4.1.1',Q('dbc','The minimum number of exit stairways, stairway width','in accordance with Ch. 3 of UAE FLSC'),
   'Минимальное число эвакуационных лестниц, ширина лестницы, разнесение лестниц, организация выхода наружу и огнестойкость лестничной клетки определяются по гл. 3 UAE FLSC.')])
e('F','rasstoyanie',NA,[],[])
e('F','shirina','Лестница — не менее 1200 мм в свету; ширина эвакуационной лестницы — по UAE FLSC в зависимости от числа людей (DBC, B.6.4.1.3)',[l('DBC 2021, B.6.4.1.3',DBC)],
 [dq('B.6.4.1.3',Q('dbc','All stairways shall have a clear width of not less than 1,200 mm.','depending upon the number of occupants it serves.'),
   'Все лестницы — шириной в свету не менее 1 200 мм. Минимальная ширина эвакуационной лестницы определяется по разд. 4 гл. 3 UAE FLSC в зависимости от числа людей, которых она обслуживает.')])
e('F','ognestojkost','Огнестойкость и пожарные преграды — по табл. 1.9 гл. 1 UAE FLSC (DBC, B.9.2); эвакуационные лестницы — в огнестойких железобетонных стенах (B.6.4.1.2)',[l('DBC 2021, B.9.2, B.6.4.1.2',DBC)],
 [dq('B.9.2',Q('dbc','Fire separating construction shall be provided in accordance with','of UAE FLSC'),
   'Противопожарные разделяющие конструкции предусматриваются по табл. 1.9 гл. 1 UAE FLSC.'),
  dq('B.6.4.1.2',Q('dbc','Exit stairways shall be enclosed in fire resistance rated reinforced concrete','blockwork construction is permitted.'),
   'Эвакуационные лестницы заключаются в огнестойкую железобетонную (RCC) конструкцию, когда этого требует табл. 3.4 гл. 3 UAE FLSC; для малоэтажных зданий и малозаглублённых подземных зданий допускается блочная кладка с огнестойкостью 2 ч.')])
e('F','otseki','Секции и отсеки — по UAE FLSC (табл. 1.9, гл. 1), DBC только отсылает ⏳',[l('DBC 2021, B.9.2',DBC)],[])
e('F','razryvy','Отступы от соседей по таблице DBC (3 м до G+3, затем +0,75 м на этаж до 7,5 м); отступы должны учитывать и противопожарное разделение зданий и проезды (DBC, B.4.2.3; MPG, табл. 6.3)',[l('DBC 2021, B.4.2.3, E.10.1',DBC),l('DDA MPG, табл. 6.3',MPG)],
 [dq('E.10.1',Q('dbc','To prevent external fire spread, the building shall be physically separated','Sections 2.7 and 2.8, Ch. 1 of UAE FLSC'),
   'Чтобы предотвратить внешнее распространение огня, здание должно быть физически отделено от соседних участков/зданий либо оболочка здания должна иметь нормируемую огнестойкость (разд. 2.7 и 2.8 гл. 1 UAE FLSC).')])
e('F','fasady','Фасады: огнестойкость и пожарная безопасность — по гл. 1 UAE FLSC и дополнительным правилам DBC (E.10): допускаются бетон, терракота, стекло, керамика, минвата и сплошные металлические панели; спринклеры на балконах Civil Defence Дубая не требует',[l('DBC 2021, E.10',DBC)],
 [dq('E.10.1',Q('dbc','The fire safety of the façade and roof elements of the building envelope shall conform to Ch. 1 of UAE FLSC','and the specific requirements of this section.'),
   'Пожарная безопасность элементов фасада и кровли оболочки здания должна соответствовать гл. 1 UAE FLSC и специальным требованиям настоящего раздела.'),
  dq('E.10.4',Q('dbc','The exceptions listed in Section 4.2.1, Ch. 1 of UAE FLSC','solid metal panels conforming to E.10.5 may be used.'),
   'Исключения, перечисленные в разд. 4.2.1 гл. 1 UAE FLSC, расширяются: сюда включены бетон, терракота, стекло, керамика и минеральная вата. Дополнительно к материалам из UAE FLSC могут применяться сплошные металлические панели по E.10.5.')])
e('F','otdelka',NA,[],[])
e('F','sprinklery',NA+' (DBC: спринклеры на балконах и за навесными фасадами Civil Defence Дубая не требует — см. фасады)',[],[])
e('F','doo',NA,[],[])
e('F','avtostoyanki','Стоянки: закрытые — с механической вентиляцией (H.4.12.11); полы негорючие по табл. 3.37 гл. 3 UAE FLSC; стоянка не должна перекрывать пожарные выходы (DBC, B.7.2)',[l('DBC 2021, B.7.2',DBC)],
 [dq('B.7.2.3.3',Q('dbc','Parking shall not impede fire exit doors, their access and exit discharge path.','exit discharge path.'),
   'Стоянка не должна перекрывать пожарные выходные двери, подходы к ним и путь выхода наружу.')])
e('F','dymoudalenie',NA,[],[])
# ---------- высотные ----------
e('H','porog','High-rise: 23–90 м; super high-rise: >90 м (DBC по UAE FLSC); low-rise — до 15 м',[l('DBC 2021, B.2, D.2, E.2',DBC)],[RISE2,RISE3])
e('H','lestnitsy','Лестницы высотных зданий — по гл. 3 UAE FLSC; не менее одной защищённой лестницы выводится на все кровли; конструкция — огнестойкий RCC (DBC, B.6.4.1.2)',[l('DBC 2021, B.6.4.1.2',DBC)],
 [dq('B.6.4.1.2',Q('dbc','At least one protected exit stairway shall extend to all roofs.','All stairways shall have a clear width') if False else Q('dbc','At least one protected exit stairway shall extend to all roofs.','extend to all roofs.'),
   'Не менее одной защищённой эвакуационной лестницы должно выходить на все кровли.')])
e('H','puti',NA,[],[])
e('H','lifty','Пожарный лифт: не менее одного в любом высотном, супервысотном здании, торговом центре и здании «большой глубины» заглубления; обслуживает все этажи (DBC, D.8.3.1; UAE FLSC, гл. 2)',[l('DBC 2021, D.8.3',DBC)],
 [dq('D.8.3.1',Q('dbc','Section 2.9, Ch. 2 of UAE FLSC requires at least one firefighting elevator in a mall','high depth.'),
   'Разд. 2.9 гл. 2 UAE FLSC требует не менее одного пожарного лифта в торговом центре, многоэтажном парке аттракционов и в любом высотном (high-rise), супервысотном (super high-rise) здании или здании большой глубины заглубления (high depth).')])
e('H','ognestojkost','Огнестойкость — по UAE FLSC (табл. 1.9, гл. 1); DBC отсылает (B.9.2) ⏳',[l('DBC 2021, B.9.2',DBC)],[])
e('H','fasady','См. 2.10: DBC E.10 — гл. 1 UAE FLSC и допускаемые материалы фасада',[l('DBC 2021, E.10',DBC)],[])
e('H','sprinklery',NA,[],[])
# ---------- градостроительство ----------
e('G','insolyatsiya','Инсоляции по часам нет; нормируется дневной свет: остекление ≥10 % площади комнаты (жилые комнаты, спальни), ≥150 лк, глубина комнаты ≤3 ширины окна (DBC, B.6.5.2)',[l('DBC 2021, B.6.5.2',DBC)],
 [dq('B.6.5.2.1',Q('dbc','Daylighting provisions for habitable and occupiable spaces shall conform to Table B.8','Living, bedroom spaces (excluding kitchen area) 10%') if False else Q('dbc','Residential and hotel Living, bedroom spaces (excluding kitchen area) 10%','Table B.8 Minimum percentage of window to floor area'),
   'Residential and hotel: жилые комнаты и спальни (кроме кухни) — минимальная площадь остекления 10 % (отношение чистой площади остекления окна к площади комнаты). Табл. B.8.'),
  dq('B.6.5.2.1',Q('dbc','Lux levels from daylight shall achieve a minimum of 150 lux in bedrooms and living rooms.','living rooms.'),
   'Освещённость от дневного света — не менее 150 лк в спальнях и жилых комнатах (при обосновании моделированием допускается уменьшать минимальный процент проёмов).'),
  dq('B.6.5.2.2',Q('dbc','For habitable spaces to receive adequate natural light through windows','the window is located'),
   'Чтобы жилые помещения получали достаточно естественного света через окна, глубина комнаты не должна превышать трёх ширин стены, в которой расположено окно.')])
e('G','razryvy-genplan','Отступы от соседей: 3 м (до G+3), далее +0,75 м на каждый этаж до 7,5 м (G+9 и выше); от дороги 0 (DBC, табл. B.1; MPG, табл. 6.3); правила аффект-плана (DCR) имеют приоритет',[l('DBC 2021, B.4.2.3',DBC),l('DDA MPG, гл. 6, табл. 6.3',MPG)],
 [dq('B.4.2.3, табл. B.1',Q('dbc','When setback limitations for the plot or development are not defined','Table B.1 Setback calculation table'),
   'Если ограничения по отступам для участка не определены, отступы считаются от границы участка до грани здания по табл. B.1: подвал 0; ground и G+1…G+3 — 3 м от соседа; G+4 — 3,75 м; G+5 — 4,50 м; G+6 — 5,25 м; G+7 — 6 м; G+8 — 6,75 м; G+9 и выше — 7,50 м; от дороги — 0 м. Отступы считаются с первого этажа и выше.'),
  dq('B.4.2.3',Q('dbc','The building setback requirements in the affection plan or DCR shall take precedence','requirements in this section.'),
   'Требования к отступам в «плане привязки» (affection plan) или в Правилах контроля застройки (DCR) имеют приоритет над требованиями настоящего раздела.'),
  mq('гл. 6, табл. 6.3',Q('mpg','Conversion rate from height in meter to number of floors is three meters per floor.','requires a 5.25m setback.'),
   'Пересчёт высоты в метрах в число этажей — три метра на этаж. Например, здание высотой 20 м — это 7 этажей и требует отступа 5,25 м.')])
# ---------- доступная среда ----------
e('A','oblast','DBC 2021 применяется к новым зданиям и изменениям существующих; доступность — Part C; вместе с Dubai Universal Design Code; допускаются альтернативные решения',[l('DBC 2021, A.5, Part C',DBC)],
 [dq('A.5.1',Q('dbc','The DBC applies to new buildings and changes to existing buildings as described in Table A.1','described in Table A.2.'),
   'DBC применяется к новым зданиям и изменениям существующих зданий, как описано в табл. A.1, кроме случаев, когда допускается альтернативное решение (см. A.8). DBC применяется к видам использования и назначениям, перечисленным в табл. A.2.')])
e('A','pandusy','Пандус обязателен при уклоне пути >5 %; уклон ≤8,33 % (рекомендуется 5–8 %); длина марша ≤10 м; ширина между поручнями ≥1000 мм; площадки ≥1500×1500 мм; поперечный уклон ≤2 % (DBC, C.5.9.1)',[l('DBC 2021, C.5.9.1',DBC)],
 [dq('C.5.9.1.1',Q('dbc','b) Ramps shall be provided when a change in level has a gradient greater than 5%.','should be provided.'),
   'b) Пандусы предусматриваются, когда перепад уровней имеет уклон более 5 %. c) Рекомендуется также предусматривать ступенчатый доступ для людей с «амбулаторной» инвалидностью. d) Уклон пандуса — по табл. C.13. e) Максимальный поперечный уклон — 2 %. f) Площадки предусматриваются, если марш превышает 10 м. g) Если серия маршей поднимается более чем на 2,4 м, следует предусмотреть альтернативный безступенчатый доступ — закрытый лифт или подъёмную платформу.'),
  dq('C.5.9.1.2–C.5.9.1.3',Q('dbc','a) The usable clear width shall be a minimum of 1,000 mm when measured between handrails.','between handrails.'),
   'Ширина прохода пандуса в свету — не менее 1 000 мм между поручнями.')])
e('A','dveri','Одностворчатая дверь — свободная ширина ≥915 мм; порог ≤13 мм; усилие открывания ≤25 Н; свободное пространство для манёвра (DBC, C.5.8.1)',[l('DBC 2021, C.5.8.1',DBC)],
 [dq('C.5.8.1',Q('dbc','c) Single doors, except toilet doors, shall have a minimum clear width of 915 mm','door open 90° (see Figure C.24).'),
   'c) Одностворчатые двери, кроме дверей туалетов, имеют минимальную свободную ширину 915 мм, измеряемую между плоскостью двери и упором при открытии на 90°.'),
  dq('C.5.8.1',Q('dbc','e) Floor surfaces at doors should be levelled to the floor.','shall not exceed 25 N, unless the door is automatic/power-assisted.'),
   'Полы у дверей должны быть выровнены; если это невозможно, порог — не выше 13 мм со скосом до 6 мм (уклон ≤50 %). Усилие открывания двери — не более 25 Н, если она не автоматическая/с приводом.')])
e('A','lifty','Хотя бы один доступный лифт в здании выше одного этажа (исключения — малые двухэтажные и др.); кабина ≥1200×1500 мм (рекомендуется 1500×1500 мм); двери ≥900×2100 мм (DBC, C.5.9.3)',[l('DBC 2021, C.5.9.3, Table C.15',DBC)],
 [dq('C.5.9.3.1',Q('dbc','at least one accessible elevator (or lift platform as described in C.5.9.4) shall be provided in every building with more than one floor','with the following exemptions:'),
   'Не менее одного доступного лифта (или подъёмной платформы по C.5.9.4) предусматривается в каждом здании более чем с одним этажом, со следующими исключениями (двухэтажные рестораны при равных условиях, служебные помещения без пребывания людей, здания G+1 с неудобным этажом менее 250 м², участки менее 250 м² и др.).'),
  dq('C.5.9.3.2, табл. C.15',Q('dbc','Cabin type Minimum (width × depth) (mm) Recommended (width × depth) (mm)','Table C.15 Dimensions of accessible elevator cabins'),
   'Табл. C.15. Размеры кабин доступных лифтов (минимум / рекомендуется, ширина × глубина, мм): с одним входом — 1 200 × 1 500 / 1 500 × 1 500; с двумя противоположными входами — 1 200 × 1 500 / 1 500 × 1 500; для носилок — 1 100 × 2 100 / 1 200 × 2 300.')])
e('A','parkovka','2 % мест (не менее одного) при 25–500 местах, далее 1 % сверх 500; больницы — 10 %; место 2,5×5,5 м (вдоль тротуара 2,5×6,0 м); для микроавтобуса 3,35×5,5 м (DBC, C.6.4)',[l('DBC 2021, C.6.4',DBC)],
 [dq('C.6.4.1, табл. C.17–C.18',Q('dbc','Public or private parking areas associated with a public street, open space or building shall have accessible parking spaces.','Table C.18 Parking dimensions'),
   'Общественные и частные парковки при улице, открытом пространстве или здании должны иметь доступные места, зарезервированные для обладателей соответствующих стикеров. Число мест — по табл. C.17: все здания, кроме частного жилья, при 25–500 местах — 2 % (минимум одно место), свыше 500 — 1 % от добавочных; для больниц рекомендуется 10 %; микроавтобусные места — 10 % от числа доступных. Размеры (табл. C.18): легковой автомобиль под углом и перпендикулярно — 2,5 × 5,5 м; вдоль тротуара — 2,5 × 6,0 м; микроавтобус — 3,35 × 5,5 м.')])
e('A','ubornye','Доступные туалеты: коридор в блоке ≥1050 мм, площадка разворота ⌀1500 мм; пеленальный столик в мужских и женских туалетах, расстояние между ними ≤150 м; семейные туалеты (DBC, C.8)',[l('DBC 2021, C.8.3',DBC)],
 [dq('C.8.3.1–C.8.3.2',Q('dbc','Minimum dimensions for accessible toilets shall be in accordance with Table C.22.','Manoeuvring space diameter 1,500 mm')+' … '+Q('dbc','Both male and female toilet facilities shall include at least one baby changing table','shall be 150 m.'),
   'Минимальные размеры доступных туалетов — по табл. C.22: ширина коридоров в туалетах, душевых и раздевалках — 1 050 мм; площадка для разворота диаметром 1 500 мм; боковое пространство — не менее одного, слева или справа от унитаза. Baby changing stations: и в мужских, и в женских туалетах — не менее одного пеленального стола с подписью на английском и арабском; расстояние между пеленальными станциями в здании — не более 150 м.')])
e('A','zhile','Новые жилые комплексы >10 квартир: не менее 2 % адаптируемых квартир и все общие помещения; доступный путь к зданию и общим удобствам (DBC, C.10.3)',[l('DBC 2021, C.10.3',DBC)],
 [dq('C.10.3.2',Q('dbc','For new housing developments with more than ten units','persons of determination.'),
   'Для новых жилых комплексов более чем с десятью квартирами не менее 2 % общего числа квартир и все общие помещения здания должны быть адаптируемыми и отвечать требованиям Part C. Это позволяет при низких затратах переоборудовать квартиру под нужды будущих жильцов — «людей с решимостью» (persons of determination, официальный термин ОАЭ).')])
def apply(TOP,HT,GT,ACC):
    for grp,L in (('F',TOP),('H',HT),('G',GT),('A',ACC)):
        for t in L:
            k=(grp,t['slug'])
            if k not in AE: continue
            short,src,items=AE[k]
            t['keys']=['ru','rs','eu','uk','ae']
            t['cells']['ae']=(short,src)
            if items: t['tabs']['ae']=list(items)+[x for x in t['tabs'].get('ae',[]) if x[0]=='q' and grp=='A']
            else: t['tabs']['ae']=t['tabs'].get('ae') or []
