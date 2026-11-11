# -*- coding: utf-8 -*-
"""Колонка «Индия». Источники: NBC 2016 Part 4 «Fire and Life Safety» (BIS; копия Nagpur Municipal Corporation),
DCPR 2034 (нормы застройки Большого Мумбаи, MCGM), Studio Matrx (вторичный пересказ NBC Part 8, daylighting).
Корпуса — вне репозитория: NORM_SRC/in/ (dcpr_c.txt, nbc4_r.txt, d430f3.txt).
IN[(папка, slug)] = (кратко, [источники], [элементы])."""
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','fire_gen'))
import qlib
qlib.FILES.update({'indcpr':'in/dcpr_c.txt','innbc4':'in/nbc4_r.txt','insm':'in/d430f3.txt'})
FAIL=[]
def Q(*a):
    try: return qlib.Q(*a)
    except AssertionError as e:
        FAIL.append(e.args[0]); return '⚠'
NA='⏳ не сверено'
DC='[DCPR 2034 (Большой Мумбаи), MCGM](https://portal.mcgm.gov.in/irj/go/km/docs/documents/MCGM%20Department%20List/Chief%20Engineer%20(Development%20Plan)/Docs/SANCTIONED%20DP2034/DCPR/DCPR%202034.pdf)'
NB='[NBC 2016, Part 4 «Fire and Life Safety» (копия NMC Нагпур)](https://nmcnagpur.gov.in/assets/300/2025/03/mediafiles/NBC2016-Part-IV.pdf)'
SM='[Studio Matrx: Daylighting, NBC 2016 Part 8 (вторичный источник)](https://www.studiomatrx.org/guides/daylight-factor-india)'
def dc(l,q,ru): return ('q','DCPR 2034, '+l,q,ru,'en')
def nb(l,q,ru): return ('q','NBC 2016 Part 4, '+l,q,ru,'en')
IN={}
def put(d,s,short,src,items): IN[(d,s)]=(short,src,items)
CAV=('n','Важно: NBC — модельный национальный кодекс (BIS), обязательным он становится через местные правила; DCPR 2034 действует только в Большом Мумбаи (редакция Gazette от 08.05.2018 — позднейшие изменения не учтены). По стороннему источнику (Studio Matrx, 10.2026) издание NBC 2016 BIS отозвано и заменено «SP 7:2026» — ⏳ не сверено. Копия NBC Part 4 — лицензионная копия BIS на сайте Nagpur Municipal Corporation, не официальная публикация BIS.')
P='pozharnaya'
put(P,'klassy','NBC 2016: группы по назначению A–J (A — жилые: A‑1 … A‑6; многоквартирные — A‑4), 4 типа конструкции по огнестойкости (Types 1–4); «высотное» — от 15 м (NBC) / выше 32 м (Мумбаи, DCPR)',[NB,DC],[
 nb('п. 3.1.2, A-4',Q('innbc4','d) Subdivision A-4 Apartment houses','mansions and Chawls.'),
  'Подгруппа A‑4 «Многоквартирные дома»: здания, где предусмотрены жилые помещения для трёх и более семей, живущих независимо друг от друга, с собственными кухнями (многоквартирные дома, особняки, «чхоулы»).'),
 nb('п. 3.3.1',Q('innbc4','For the purpose of the Code, the types of construction according to fire resistance shall be classified into four categories','Type 4 Construction.'),
  'Для целей Кодекса типы конструкции по огнестойкости делятся на четыре: Type 1, Type 2, Type 3 и Type 4.'),
 dc('п. 2(75)',Q('indcpr','“High Rise Building” means a building having height more than 32m','average surrounding ground level.'),
  'Высотное здание — здание высотой более 32 м над средним уровнем окружающей земли (по NBC — от 15 м).'),CAV])
put(P,'metodiki','Высота здания — от среднего уровня земли до верха террасы (плоская крыша); высотное по NBC — от 15 м; путь эвакуации — от наиболее удалённой точки этажа по естественному непрепятственному пути до двери выхода (NBC, п. 2.38, 4.4.2.2; DCPR, п. 2(73))',[NB,DC],[
 dc('п. 2(73)',Q('indcpr','"Height of a building" means the vertical distance measured, in the case of flat roofs','topmost terrace level'),
  'Высота здания — вертикальное расстояние для плоских крыш от среднего уровня земли вокруг здания, примыкающей к нему, до верхнего уровня террасы (для скатных крыш — до точки пересечения наружной стены с поверхностью ската).'),
 nb('п. 2.38',Q('innbc4','2.38 High Rise Building — A building 15 m or above','(irrespective of its occupancy).'),
  'Высотное здание — здание высотой 15 м и более (независимо от назначения).'),
 nb('п. 4.4.2.2(b)',Q('innbc4','b) Travel distance shall be measured from the most remote point within a storey or a mezzanine floor','door to an exit.'),
  'Путь движения измеряют от наиболее удалённой точки в пределах этажа или антресоли вдоль естественного непрепятственного пути горизонтальной или вертикальной эвакуации до двери выхода.')])
put(P,'pravovaya-sila','NBC — модельный кодекс (BIS), обязателен через местные нормы; в Мумбаи DCPR отсылает к NBC и добавляет Приложение I для высотных зданий; отступления — по решению начальника пожарной службы (NBC, п. 3.4.2; DCPR, п. 47)',[NB,DC],[
 dc('п. 47(1)',Q('indcpr','The planning, design and construction of any building shall be such as to ensure safety from fire.','shall also apply,'),
  'Планирование, проектирование и строительство любого здания должны обеспечивать пожарную безопасность; если иное не указано, применяется глава о пожарной безопасности Национального строительного кодекса в действующей редакции. Для высотных и особых зданий действует также Приложение I.'),
 nb('п. 3.4.2',Q('innbc4','Exceptions and deviations to the general provisions of','from the Code.'),
  'Исключения и отступления от общих положений даны для каждого вида назначения в пп. 6.1–6.9. В случае практической трудности или чтобы избежать необоснованных лишений, без ущерба разумной безопасности, местный начальник пожарной службы может рассмотреть освобождения от требований Кодекса.'),CAV])
put(P,'vyhody','Не менее двух лестниц во всех зданиях, охваченных п. 1.2; не менее половины лестниц выходят прямо наружу или через выходной проход (NBC, пп. 4.4.2.4.3.1, 4.2.10)',[NB],[
 nb('п. 4.4.2.4.3.1',Q('innbc4','All buildings, as mentioned in 1.2, shall have a minimum of two staircases.','At least 50 percent of the staircases shall discharge as per (a) and/or (b) above.'),
  'Все здания, указанные в п. 1.2, должны иметь не менее двух лестниц. Все эвакуационные лестницы на уровне выхода выводят наружу: прямо, через выходной проход или через большой вестибюль; не менее 50 % лестниц — прямо и/или через выходной проход.'),
 nb('п. 4.2.10',Q('innbc4','4.2.10 At least half of the required exit stairs from upper floors','through exit passageways.'),
  'Не менее половины необходимых эвакуационных лестниц с верхних этажей (с округлением вверх) выходят прямо наружу или через выходные проходы.')])
put(P,'rasstoyanie','Предельный путь до выхода (группа A, жилые): 30 м (Types 1–2) / 22,5 м (Types 3–4); в здании со спринклерами — на 50 % больше; тупик — до 15 м (6 м для учебных, лечебных, зрелищных) (NBC, табл. 5, п. 4.4.2.2)',[NB],[
 ('t','NBC 2016 Part 4, табл. 5 (выборка; воспроизведена вручную, м)','''| Occupancy Group | Types 1 and 2 | Types 3 and 4 |
|---|---|---|
| Residential (Group A) | 30.00 | 22.50 |
| Educational (Group B) | 30.00 | 22.50 |
| Business (Group E) | 30.00 | 30.00 |''','Максимальный путь движения до выхода. Примечание 1 к таблице: для здания, полностью оборудованного спринклерами, путь можно увеличить на 50 %.','en'),
 nb('п. 4.4.2.2(c)',Q('innbc4','c) The dead end corridor length in exit access','(see Fig. 6)'),
  'Длина тупикового коридора на пути к выходу не должна превышать 6 м для учебных, лечебных и зрелищных групп; для остальных — 15 м.')])
put(P,'shirina','Лестница: A‑2 — 1,00 м; A‑1, A‑3, A‑4 — 1,25 м (NBC); в Мумбаи — жилые 1,5 м (до 70 м) / 2,0 м (выше 70 м), ступенька ≤17,5 см, проступь ≥25 см; дверь выхода ≥1,0 × 2,0 м; единица ширины выхода — 500 мм',[NB,DC],[
 nb('п. 4.4.2.4.3.2(e)',Q('innbc4','e) Notwithstanding the detailed provision for exits in accordance with 4.2 and 4.3, the following minimum width shall be provided for staircases for respective occupancies:','All other occupancies : 1.50 m'),
  'Минимальная ширина лестниц: жилые A‑2 — 1,00 м; A‑1, A‑3 и A‑4 — 1,25 м (для двухэтажных рядовых домов — 0,75 м); гостиничные A‑5 и A‑6 — 1,50 м; зрелищные — 2,00 м (1,50 м при <150 человек); учебные — 1,50 м; лечебные — 2,00 м; прочие — 1,50 м.'),
 nb('п. 4.4.2.4.1(b)',Q('innbc4','b) No exit doorway shall be less than 1 000 mm','in height.'),
  'Дверь выхода — не менее 1000 мм по ширине (в зрелищных зданиях — 2000 мм) и не менее 2000 мм по высоте.'),
 ('t','DCPR 2034, табл. 16 (выборка; воспроизведена вручную, м)','''| Type of occupancy | buildings up to 70 m | buildings above 70 m |
|---|---|---|
| Residential — general | 1.50 | 2.00 |
| Residential — row housing (2 storeys) / duplex stair | 0.90 | — |
| Educational — up to 32 m / over 32 m | 1.50 / 2.0 | — |''','Минимальная ширина общих лестниц и коридоров. Для двухэтажных рядовых домов и внутриквартирных лестниц ширина ограничена 1,20 м.','en'),
 dc('п. 37(15)(ii)–(iv)',Q('indcpr','(ii)Flight- No flight shall contain more than 12 risers','shall be 30cm'),
  'В марше не более 12 подъёмов (в жилых зданиях на узких участках допускается одномаршевая лестница); высота подъёма — не более 17,5 см (внутри квартиры — 25 см); ширина проступи без носика — не менее 25 см в жилых зданиях и 30 см в остальных.')])
put(P,'ognestojkost','NBC: конструкции Types 1–4 с минимальными пределами по табл. 1 (значения таблицы ⏳ не вынесены); внутренние стены лестничных клеток — кирпич/ж/б ≥120 мин; DCPR, Прил. I: несущие конструкции — 3 ч, перекрытия — 2 ч',[NB,DC],[
 nb('п. 3.3.1',Q('innbc4','The minimum fire resistance ratings of structural and nonstructural members for various types of construction shall be as given in Table 1.','minimum of 120 min rating.'),
  'Минимальные пределы огнестойкости несущих и ненесущих элементов для разных типов конструкции — по табл. 1. Для зданий следует применять негорючие материалы, а внутренние стены лестничных клеток — из кирпичной кладки, железобетона или иного материала с пределом не менее 120 мин.'),
 dc('Прил. I, п. 2(2)',Q('indcpr','(2) Structural members such as supports and load bearing walls shall have fire resistance rating of 3 hour','at least 2 hours.'),
  'Несущие элементы (опоры, несущие стены) — предел огнестойкости 3 ч; ригели и потолки — не менее 2 ч.')])
put(P,'otseki','Этаж делится на отсеки ≤750 м² (больше — по табл. при спринклерах), граница — преграда 120 мин (NBC, п. 4.5.2); Мумбаи: противопожарные стены не менее 2 ч, стены коридоров 1 ч (DCPR, Прил. I)',[NB,DC],[
 nb('п. 4.5.2',Q('innbc4','4.5.2 All floors shall be compartmented/zoned with area of each compartment being not more than 750 m2.','in case of sprinklered basement/building:'),
  'Все этажи делятся на отсеки площадью каждый не более 750 м². Для зданий (подвалов) со спринклерами максимальный размер отсека задаётся таблицей по назначению (значения ⏳ не вынесены).'),
 nb('п. 4.5.2 (граница отсека)',Q('innbc4','Compartmentation shall be achieved by means of fire barrier having fire resistance rating of 120 min.','120 min.'),
  'Деление на отсеки выполняют противопожарной преградой с пределом огнестойкости 120 мин.'),
 dc('Прил. I, п. 2(3)',Q('indcpr','(3) Internal walls and partitions separating corridors from areas on floors','not less than two hours.'),
  'Стены и перегородки, отделяющие коридоры от помещений этажа, — предел не менее 1 ч, без проёмов, кроме дверей/люков с пределом не менее 0,5 ч; противопожарные стены (разделение на пожарные секции) — не менее 2 ч.')])
put(P,'razryvy','Табл. 1 NBC связывает пределы огнестойкости наружных стен с «fire separation» <3,7 м / 3,7–9 м / ≥9 м (значения ⏳); Мумбаи: для зданий 32–70 м — свободная полоса ≥6 м, выше 70 м — ≥9 м (DCPR, п. 47)',[NB,DC],[
 dc('п. 47(1)(A)(a)–(b)',Q('indcpr','a) In case of rehabilitation/composite buildings having height more than 32 m up to 70 m','accessible from road side.'),
  'Для реабилитационных/составных зданий высотой более 32 м до 70 м не менее одной стороны (кроме выходящей на дорогу) должна иметь свободное открытое пространство 6 м на уровне земли, доступное с дороги; для зданий выше 70 м — 9 м.'),
 ('n','Табл. 1 NBC (пределы огнестойкости элементов, в т. ч. наружных стен по расстоянию 3,7 / 9 м) прочитана не полностью ⏳.')])
put(P,'fasady','Фасады — из негорючих материалов; расстояние между верхом проёма нижнего этажа и подоконником верхнего ≥0,9 м; стеклянный фасад: открываемые противопожарные панели ≥1000×1000 мм не реже чем через 10 м (DCPR, Прил. I, п. 2(4); NBC, п. 3.4.10.2)',[NB,DC],[
 dc('Прил. I, п. 2(4)',Q('indcpr','(4) Facades excluding windows and doors shall consist of non-combustible building materials.','between storeys.'),
  'Фасады (кроме окон и дверей) выполняют из негорючих материалов. Минимальное расстояние между верхом проёма нижнего этажа и подоконником проёма этажом выше — 0,9 м, чтобы огню пришлось пройти не менее 0,9 м между этажами.'),
 nb('п. 3.4.10.2(c)',Q('innbc4','c) Openable panels shall be provided on each floor and shall be spaced not more than 10 m apart','opening outwards.'),
  'На каждом этаже стеклянного фасада предусматривают открываемые панели (противопожарный доступ) с шагом не более 10 м между центрами, на высоте 1,2–1,5 м от пола, размером не менее 1000 × 1000 мм, открывающиеся наружу.')])
put(P,'otdelka','Горючая отделка стен и потолков (включая фасады) ограничивается по скорости распространения пламени: 4 класса поверхностей (Class 1 — очень низкое … Class 4 — быстрое); допустимые классы по зонам — п. 3.4.11.3 (NBC)',[NB,DC],[
 nb('п. 3.4.11.2',Q('innbc4','3.4.11.2 The susceptibility of various types of wall surfaces to fire is determined in terms of the rate of spread of flame.','Class 4 Surfaces of rapid flame spread.'),
  'Восприимчивость стен к огню определяют по скорости распространения пламени; поверхности делятся на 4 класса: Class 1 — очень малое распространение пламени, Class 2 — малое, Class 3 — среднее, Class 4 — быстрое.'),
 dc('Прил. I, п. 2(1)(i)',Q('indcpr','(i) Load bearing elements of construction and elements of construction for which the required fire resistance','Ceiling linings shall be non-combustible or of plasterboard.'),
  'Несущие элементы и элементы с пределом огнестойкости 1 ч и более — из негорючих материалов; отделка стен и полов допускается с очень низким распространением пламени (Class I по IS 1642); потолочная отделка — негорючая или из гипсокартона.')])
put(P,'sprinklery','Спринклеры — «wherever required in terms of Table 7» NBC (значения таблицы ⏳ не разобраны); ложные потолки выше 800 мм — со спринклерами; в Мумбаи — по NBC (NBC, п. 5.1.3; DCPR, Прил. I, п. 13)',[NB,DC],[
 nb('п. 5.1.3(a)–(c)',Q('innbc4','a) Automatic sprinklers shall be installed wherever required in terms of Table 7 throughout the building','exceeding 800 mm in height.'),
  'Автоматические спринклеры устанавливают во всём здании везде, где это требует табл. 7, в соответствии с хорошей практикой; при выборочном спринклерном оборудовании возникает опасность распространения огня из неспринклерных зон; спринклеры нужны в пустотах ложных потолков высотой более 800 мм.'),
 dc('Прил. I, п. 13(1)',Q('indcpr','(1) Buildings shall be protected by wet riser, wet riser-cum-down corner, automatic sprinkler','as prescribed in sub-Regulations (2) to (6)'),
  'Здания защищают мокрым стояком, стояком-спуском, автоматическими спринклерами, водяным распылением или пенной системой — по подпунктам (2)–(6).'),
 ('n','Табл. 7 NBC («Minimum Requirements for Fire Fighting Installations») в копии PDF плохо читается ⏳ — пороги высоты/площади для спринклеров не вынесены.')])
put(P,'doo','Учебные здания (группа B): помещение на >45 человек — не менее двух дверей; лестница ≥1,5 м (в Мумбаи при высоте более 32 м — 2,0 м); класс ≥38 м² (или 0,8 м² на ученика) (NBC, п. 6.2.2; DCPR, табл. 14, 16)',[NB,DC],[
 nb('п. 6.2.2',Q('innbc4','Every room with a capacity of over 45 persons in area shall have at least two doorways.','panic bars'),
  'Каждое помещение вместимостью более 45 человек должно иметь не менее двух дверей. Двери выходов — с антипаническими ручками.'),
 ('t','DCPR 2034, табл. 14, строка 8 (воспроизведена вручную)','''| Occupancy | Minimum size, sq.m | Minimum width, m |
|---|---|---|
| Class room in an Educational building | 38.0 or 0.8 sq.m per student | 5.5 |''','Классная комната в образовательном здании: не менее 38,0 м² или 0,8 м² на ученика (или по решению правительства); ширина не менее 5,5 м.','en')])
put(P,'avtostoyanki','Мумбаи: место для автомобиля 2,5 × 5,5 м (до 50 % мест — 2,3 × 4,5 м); подвальные стоянки вентилируются отдельно, проёмы ≥2,5 % площади этажа; лестница подвала — отдельная, 2 ч (DCPR, п. 44, Прил. I, п. 7); NBC — Annex H ⏳',[DC],[
 dc('п. 44(1)(ii)',Q('indcpr','Type of Vehicle Minimum size/Area of parking space','upto 50 per cent of the prescribed space may be of the size of 2.3 m x 4.5 m.'),
  'Минимальные размеры места: автомобиль — 2,5 × 5,5 м; скутер/мотоцикл — 3 м²; велосипед — 1,4 м²; автобус — 3,75 × 7,5 м. До 50 % предписанных мест для автомобилей могут быть размером 2,3 × 4,5 м.'),
 dc('Прил. I, п. 7(1)',Q('indcpr','(1) Each basement shall be separately ventilated.','spread evenly around the perimeter of the basement'),
  'Каждый подвал вентилируется отдельно: суммарная площадь вентиляционных проёмов не менее 2,5 % площади этажа, равномерно по периметру подвала (решётки, разбиваемые плиты, световые люки, шахты) либо система приточных и вытяжных отверстий.'),
 ('n','NBC 2016 Part 4, Annex H «Car parking facilities» — не вынесен ⏳.')])
put(P,'dymoudalenie','Мумбаи: лестничная клетка проветривается на каждой площадке или при расположении в ядре — подпор 5 мм вод. ст.; постоянный проём вверху 5 % сечения; лифтовой холл — подпор 2,5–3 мм вод. ст. (DCPR, Прил. I, пп. 3, 4); NBC — п. 4.4.2.5, 4.6 ⏳',[DC,NB],[
 dc('Прил. I, п. 3(3)',Q('indcpr','(3) A permanent vent at the top equal to 5 per cent of the cross-sectional area of the enclosure','water gauge by an electrically operated blower shall be maintained.'),
  'Вверху клетки — постоянное отверстие, равное 5 % площади её сечения, и открываемые створки на каждой площадке не менее 0,5 м² на наружной стене; крыша шахты — не менее чем на 1 м выше окружающей кровли; остекление во внутренних стенах не допускается. Если клетка в ядре здания и не может проветриваться, электровентилятором поддерживают избыточное давление 5 мм вод. ст.'),
 dc('Прил. I, п. 4(4)',Q('indcpr','(4) If the lift shaft and lift lobby are in the core of the building, a positive pressure of not less than 2.5','shall be maintained in the lift shaft.'),
  'Если шахта и холл лифта находятся в ядре здания — в холле поддерживают избыточное давление 2,5–3 мм вод. ст., в шахте — не менее 5 мм вод. ст.; системы включаются автоматически и вручную при срабатывании извещателей.'),
 ('n','NBC 2016 Part 4: п. 4.4.2.5 (smoke control of exits) и 4.6 (smoke exhaust and pressurization) — не вынесены ⏳.')])
# ---- высотные здания
V=P+'/vysotnye'
RZ=nb('Annex E-4',Q('innbc4','Refuge area shall be provided in buildings of height more than 24 m.','at every 15 m or so.'),
  'Зона убежища (refuge area) предусматривается в зданиях выше 24 м; рассчитывается на жильцов двух смежных этажей из расчёта 0,3 м² на человека (плюс место для кресла-коляски 0,9 м² на каждые 200 человек), не менее 15 м²; по периметру этажа, открыта воздуху минимум с одной стороны, с ограждением; на уровне 24 м или выше и далее примерно через каждые 15 м.')
put(V,'porog','Высотное здание: NBC — от 15 м; Мумбаи (DCPR) — выше 32 м над средним уровнем земли; планы высотных зданий согласует Chief Fire Officer; лифт обязателен выше 16 м, два лифта — выше 24 м (NBC, п. 2.38; DCPR, пп. 2(75), 10(5), 37(17))',[NB,DC],[
 nb('п. 2.38; Annex E-1',Q('innbc4','2.38 High Rise Building — A building 15 m or above','(irrespective of its occupancy).'),
  'Высотное здание — здание высотой 15 м и более независимо от назначения. Annex E требует особого внимания к высотным зданиям: поэтапная эвакуация, эффект тяги при подпоре и дымоудалении, зонирование систем пожаротушения, доступ пожарных.'),
 dc('п. 2(75)',Q('indcpr','“High Rise Building” means a building having height more than 32m','average surrounding ground level.'),
  'Высотное здание (Мумбаи) — здание высотой более 32 м над средним уровнем окружающей земли.'),
 dc('п. 10(5)(ii)',Q('indcpr','(ii) Fire brigade scrutiny. -The plans for all high rise and special buildings shall also be subject to the scrutiny of the Chief Fire Officer','Chief Fire Officer.'),
  'Планы всех высотных и особых зданий проверяет Chief Fire Officer; разрешение на застройку выдаётся только после его согласования.'),CAV])
put(V,'lestnitsy','Не менее двух лестниц; шахта пожарных (firefighting shaft) — на каждую башню; стены лестничных клеток 2 ч, доступ через проветриваемый холл и самозакрывающиеся двери ≥0,5 ч, подпор 5 мм вод. ст. (NBC, п. 4.4.2.4.3, Annex E-2; DCPR, Прил. I, п. 3)',[NB,DC],[
 dc('Прил. I, п. 3(1)',Q('indcpr','(1) The internal enclosing walls of staircase shall be of brick or R.C.C. construction','shall not form part of common corridor.'),
  'Внутренние стены лестничной клетки — из кирпича или железобетона с пределом не менее 2 ч. Клетки доступны через проветриваемый холл, через самозакрывающиеся одностворчатые двери с пределом не менее 0,5 ч, открывающиеся по направлению эвакуации, с доводчиками. Площадка лестницы не должна быть частью общего коридора.'),
 nb('Annex E-2',Q('innbc4','One firefighting shaft shall be planned for each residential building/tower','for each compartment of institutional, assembly, business and mercantile occupancy types.'),
  'Одна шахта пожарных (firefighting shaft) предусматривается на каждое жилое здание/башню, учебное здание/блок и на каждый отсек лечебных, зрелищных, деловых и торговых зданий.')])
put(V,'puti','Путь до выхода — 30 м (Types 1–2) / 22,5 м (Types 3–4), +50 % в здании со спринклерами; тупик ≤15 м (NBC, табл. 5, п. 4.4.2.2); в Мумбаи при подвале — доп. лестницы, если путь превышает нормы (DCPR, Прил. I, п. 7)',[NB,DC],[
 ('t','NBC 2016 Part 4, табл. 5 (выборка; воспроизведена вручную, м)','''| Occupancy Group | Types 1 and 2 | Types 3 and 4 |
|---|---|---|
| Residential (Group A) | 30.00 | 22.50 |
| Business (Group E) | 30.00 | 30.00 |''','Максимальный путь до выхода; для полностью спринклерного здания — на 50 % больше.','en'),
 nb('п. 4.4.2.2(c)',Q('innbc4','c) The dead end corridor length in exit access','(see Fig. 6)'),
  'Тупики коридоров на пути к выходу — до 15 м (до 6 м для учебных, лечебных, зрелищных).')])
put(V,'lifty','Лифт обязателен при высоте >16 м; выше 24 м — не менее двух, один из них пожарный; пожарный лифт: площадь ≥1,4 м², грузоподъёмность ≥545 кг, подъём на верхний этаж за ≤1 мин; в жилых выше 70 м — грузовой лифт-носилки (DCPR, пп. 37(17), Прил. I, п. 6)',[DC,NB],[
 dc('п. 37(17)(i)',Q('indcpr','(i)At least one lift shall be provided in every building more than 16m in height.','may also extend up to terrace floor'),
  'В каждом здании выше 16 м — не менее одного лифта; в зданиях выше 24 м — не менее двух лифтов для обслуживания каждой жилой единицы, один из которых пожарный. Не менее одного лифта должно обслуживать самый нижний уровень подвала и может доходить до террасы.'),
 dc('Прил. I, п. 6(b), (g)',Q('indcpr','(b) The lift shall have a floor area of not less than 1.4 sq. m. with a minimum dimension of 1.12 m.','(8 persons lift) with automatic closing doors.'),
  'Пожарный лифт: площадь кабины не менее 1,4 м² при минимальном размере 1,12 м; грузоподъёмность не менее 545 кг (на 8 человек); автоматически закрывающиеся двери. Скорость такова, чтобы кабина доходила с первого этажа до верхнего за одну минуту (п. 6(g)).'),
 dc('п. 37(17)(ii)(e)',Q('indcpr','e. In high rise residential buildings having height more than 70m','stretcher lift also.'),
  'В жилых высотных зданиях выше 70 м один из лифтов — грузовой; он проектируется так, чтобы служить и лифтом для носилок.'),
 ('n','NBC, Annex E-3: требования к лифтам высотных зданий — Part 8, Section 5 (не прочитан ⏳).')])
put(V,'ognestojkost','Несущие конструкции — 3 ч, перекрытия — 2 ч; стены шахт лифтов, служебных каналов, мусоропровода — 2 ч; зоны убежища выше 24 м: на уровне 24 м и далее примерно через каждые 15 м (DCPR, Прил. I; NBC, Annex E-4)',[DC,NB],[
 dc('Прил. I, п. 2(2)',Q('indcpr','(2) Structural members such as supports and load bearing walls shall have fire resistance rating of 3 hour','at least 2 hours.'),
  'Несущие элементы (опоры, несущие стены) — 3 ч; ригели и потолки — не менее 2 ч.'),
 RZ,
 dc('Прил. I, п. 18(i)',Q('indcpr','a) The refuge area shall be so located that it shall preferably face the access road/s','h) The refuge area provided within building line shall be accessible from common passage/ staircase.'),
  'Зона убежища предпочтительно обращена к подъездной дороге; консольная — только на промежуточной площадке лестницы, железобетонная, с ограждением 1,20 м; дверь с надписью «REFUGE AREA»; лифты в зону убежища не открываются; доступ из общего прохода/лестницы.')])
put(V,'fasady','Фасады из негорючих материалов; 0,9 м между проёмами этажей; стеклянные фасады — по NBC/типовым правилам (DCPR, Прил. I, пп. 2(4), 19; NBC, п. 3.4.10.2)',[DC,NB],[
 dc('Прил. I, п. 19',Q('indcpr','All the buildings having glass façade shall comply with fire safety requirements as per Model Building','Bye Laws/NBC'),
  'Все здания со стеклянным фасадом должны отвечать требованиям пожарной безопасности по Model Building Bye Laws / NBC.'),
 nb('п. 3.4.10.2(c)',Q('innbc4','c) Openable panels shall be provided on each floor and shall be spaced not more than 10 m apart','opening outwards.'),
  'Открываемые противопожарные панели — на каждом этаже через не более 10 м, на высоте 1,2–1,5 м, не менее 1000×1000 мм, наружу.')])
put(V,'sprinklery','Спринклеры, мокрые стояки, стояки-спуски — по NBC и таблице DCPR (ёмкость баков и насосов зависит от высоты: до 70 м и выше 70 м); открываемые окна — не менее 2,5 % площади этажа (DCPR, Прил. I, пп. 5, 13)',[DC,NB],[
 dc('Прил. I, п. 5',Q('indcpr','The area of the open able external windows on a floor shall be not less than 2 1/2 per cent of the floor','area.'),
  'Площадь открываемых наружных окон на этаже — не менее 2,5 % площади этажа; замки окон — с «аварийным» ключом (открываются остриём пожарного топора).'),
 dc('Прил. I, п. 13(1)',Q('indcpr','(1) Buildings shall be protected by wet riser, wet riser-cum-down corner, automatic sprinkler','as prescribed in sub-Regulations (2) to (6)'),
  'Здания защищают мокрым стояком, стояком-спуском, автоматическими спринклерами, водяным распылением или пенной системой.'),
 ('n','Таблица ёмкостей баков и насосов (DCPR, Прил. I, п. 13(2)) и табл. 7 NBC — не вынесены ⏳.')])
# ---- стадии
S='stadii'
put(S,'01-strategiya','⏳ отдельной стадии в читанных актах нет (DCPR 2034 начинается с уведомления о намерении застройки)',[DC],[('n','⏳ Нужно найти: правила предпроектных обоснований (zoning/FSI — DCPR Part V, Part VII); в DCPR прочитаны разд. 10–12 (процедура).')])
put(S,'02-zadanie','◐ уведомление о намерении (Notice of Intention): письменное заявление Commissioner по форме Прил. II с планами и сведениями; условия участка — зонирование и FSI по DCPR (Part V, VII ⏳) (DCPR, п. 10(1))',[DC],[
 dc('п. 10(1)',Q('indcpr','(1) Notice of intention: Every person who intends to carry out development or redevelopment','sub-Regulations (2) and (3) hereunder.'),
  'Каждое лицо, намеренное выполнить застройку или реконструкцию, возвести или перестроить здание, подаёт Commissioner письменное уведомление по форме Приложения II с планами и сведениями в нужном числе экземпляров (по п. 10(2)–(3)).')])
put(S,'03-koncepciya','⏳ отдельной стадии концепции в DCPR нет',[],[('n','⏳ Нужно найти: правила предварительного согласования концепции (IOD/«intimation of disapproval» и т. п. — DCPR текст такой стадии не называет).')])
put(S,'04-eskiz','⏳ не найдено',[],[('n','⏳ Нужно найти: требования к эскизным материалам (в DCPR прочитан состав планов и сведений, п. 10(2)–(3) — не вынесен).')])
put(S,'05-ago-agr','◐ согласование Chief Fire Officer для высотных и особых зданий; специальные NOC (DCPR, п. 10(5)(ii), Прил. III)',[DC],[
 dc('п. 10(5)(ii)',Q('indcpr','(ii) Fire brigade scrutiny. -The plans for all high rise and special buildings shall also be subject to the scrutiny of the Chief Fire Officer','Chief Fire Officer.'),
  'Планы всех высотных и особых зданий дополнительно проверяет Chief Fire Officer; разрешение выдаётся только после его согласования.')])
put(S,'06-proekt-razresheniya','≈ планы и сведения, подписанные владельцем и лицензированным специалистом/архитектором (Professional on Record) (DCPR, п. 10(2)–(4), Прил. 10)',[DC],[
 dc('п. 10(4)(i)',Q('indcpr','(i) Signing of Plans - All the plans shall be signed by the owner and the licensed','Professional on Record as the case may be'),
  'Все планы подписывают владелец и лицензированный геодезист/инженер/инженер-конструктор/технадзор или архитектор (Professional on Record), с указанием фамилий, адресов и номеров лицензий.')])
put(S,'07-ekspertiza','≈ проверка и решение Commissioner (утвердить, отказать или утвердить с изменениями); для высотных — согласование Chief Fire Officer; отдельной независимой экспертизы в читанных нормах нет (DCPR, п. 10(5))',[DC],[
 dc('п. 10(5)(i)',Q('indcpr','(i) Grant of permission or refusal. - The Commissioner may either sanction or refuse to sanction the plans and specifications','in the formats specified in Annexure 11 and 12'),
  'Commissioner может утвердить или отказать в утверждении планов и спецификаций либо утвердить с изменениями или указаниями и сообщает решение по форме Приложений 11 и 12.')])
put(S,'08-razreshenie','≈ разрешение на застройку (Development Permission / Commencement Certificate): считается выданным, если за 60 дней нет ответа; действует 4 года (продление ежегодно) (DCPR, п. 10(5)(iii), 10(6))',[DC],[
 dc('п. 10(5)(iii)',Q('indcpr','(iii) Deemed permission.-If within sixty days of the receipt of the notice under sub-Regulations (1) of','shall be deemed to have been sanctioned'),
  'Если в течение 60 дней со дня получения уведомления Commissioner не сообщил письменно об отказе, утверждении или утверждении с изменениями, уведомление с планами считается утверждённым (это не даёт права действовать вразрез с условиями аренды, генпланом, нормами или законом).'),
 dc('п. 10(6)',Q('indcpr','A development permission/commencement certificate shall remain valid for four years in the aggregate','three consecutive terms of one year each'),
  'Разрешение/свидетельство о начале работ действует четыре года суммарно, но подлежит ежегодному продлению (до истечения года со дня выдачи, если работы не начаты); продление возможно на три последовательных срока по году.')])
put(S,'09-rabochaya','⏳ отдельной стадии рабочей документации в читанных нормах нет (Прил. 5–8: заключения конструктора, сантехника, технадзора)',[],[('n','⏳ Нужно найти: требования к рабочей документации; в DCPR — Annexure 5–9 (формы заключений) не вынесены.')])
put(S,'10-stroitelstvo','◐ уведомление о начале работ (работы можно начинать через 7 дней), проверка до уровня цоколя (инспекция за 15 дней, иначе считается разрешённым), согласование отступлений, инспекции (DCPR, пп. 11(2)–(5), 12)',[DC],[
 dc('п. 11(2)',Q('indcpr','(2) Notice to start of work: The owner shall give notice to the Commissioner of his intention to start','earlier, if so permitted.'),
  'Владелец уведомляет Commissioner о намерении начать работы (форма Приложения 13) и может начать работы через 7 дней со дня вручения уведомления или раньше, если разрешено.'),
 dc('п. 11(4)',Q('indcpr','(4) Checking of plinth columns up to plinth level: The owner through his licensed surveyor, or his architect shall give notice','shall be deemed to have been given provided the work is carried out according to the sanctioned plans.'),
  'По завершении работ до уровня цоколя владелец через лицензированного специалиста уведомляет Commissioner; Commissioner инспектирует работы в течение 15 дней и разрешает или не разрешает дальнейшее строительство; если отказа в этот срок нет — разрешение считается данным.')])
put(S,'11-ispolnitelnaya','≈ свидетельства о завершении: водоотведения (Прил. 17), здания (Прил. 18) с тремя комплектами планов построенного объекта; принятие завершения (Прил. 19) (DCPR, п. 11(6))',[DC],[
 dc('п. 11(6)',Q('indcpr','(6) Completion certificate: The owner, through his licensed plumber, shall furnish a drainage completion','accompanied by three sets of plans of the completed development.'),
  'Владелец через лицензированного сантехника представляет свидетельство о завершении водоотведения (Прил. 17), а через лицензированного специалиста/архитектора — свидетельство о завершении здания (Прил. 18) с тремя комплектами планов построенного объекта.')])
put(S,'12-priemka-vvod','≈ Occupancy Certificate: Commissioner выдаёт или отказывает в течение 21 дня, иначе объект считается принятым для заселения; для высотных — только после согласования Chief Fire Officer; возможен частичный OC (DCPR, пп. 11(7)–(8), 12(2))',[DC],[
 dc('п. 11(7)',Q('indcpr','(7) Occupancy certificate: On receipt of the acceptance of completion certificate in the form given at','falling which the work shall be deemed to have been approved for occupation'),
  'После принятия завершения владелец представляет свидетельство о завершении застройки (Прил. 16) с тремя копиями исполнительных планов; Commissioner выдаёт Occupancy Certificate (Прил. 20) или отказывает в течение 21 дня со дня получения, иначе работы считаются принятыми для заселения (если построено по утверждённым планам).'),
 dc('п. 12(2)',Q('indcpr','(2) Inspection by Fire Departmental: For all high-rise and special buildings, the work shall also be subject to inspection by the Chief Fire Officer','Chief Fire Officer.'),
  'Для всех высотных и особых зданий работы также подлежат инспекции Chief Fire Officer; Occupancy Certificate (принятие завершения) выдаётся только после его согласования.')])
put(S,'13-peredacha','⏳ не найдено',[],[('n','⏳ Нужно найти: порядок передачи объекта и гарантийные обязательства (в DCPR не рассматриваются).')])
put(S,'14-ekspluatatsiya','⏳ не найдено: в DCPR — только положения о небезопасных зданиях и ремонте (разд. 12, Прил. IV)',[],[('n','⏳ Нужно найти: правила эксплуатации, обследования и ремонта зданий.')])
# ---- прочие разделы
PK='parkovki'
put(PK,'razmery','Мумбаи: место для автомобиля 2,5 × 5,5 м (до 50 % мест — 2,3 × 4,5 м); мотоцикл — 3 м²; велосипед — 1,4 м²; автобус — 3,75 × 7,5 м (DCPR, п. 44(1)(ii))',[DC],[
 dc('п. 44(1)(ii)',Q('indcpr','Type of Vehicle Minimum size/Area of parking space','upto 50 per cent of the prescribed space may be of the size of 2.3 m x 4.5 m.'),
  'Минимальные размеры места: автомобиль — 2,5 × 5,5 м; скутер/мотоцикл — 3 м²; велосипед — 1,4 м²; автобус — 3,75 × 7,5 м; до 50 % мест для автомобилей могут быть 2,3 × 4,5 м.')])
D='dostupnaya'
put(D,'pandusy','Мумбаи: уклон пандуса для пешеходов — не круче 1:12 (для транспорта — по DCPR); поручни с обеих сторон высотой 0,90 м; пандус в больнице — не уже 2,25 м (DCPR, п. 37(16))',[DC],[
 dc('п. 37(16)(i)',Q('indcpr','(i) Ramps for pedestrians-','Handrail- A handrail shall be provided on both the sides of the ramp with minimum height of 0.90 m'),
  'Для пандусов применяются положения о лестницах; пандус в больнице — не уже 2,25 м; уклон — не менее 1:8 для транспорта и 1:12 для пешеходов (в тексте DCPR; формулировка требует сверки ⏳), нескользкое покрытие; поручни с обеих сторон высотой не менее 0,90 м.')])
O='obshchestvennye'
put(O,'vysota','Мумбаи: высота помещений — от 2,75 м (общие помещения), 3,6 м (зрелищные, учебные, лечебные, производственные), 2,4 м (с кондиционированием), 2,2 м (санузлы); макс. 4,2 м (DCPR, табл. 15)',[DC],[
 ('t','DCPR 2034, табл. 15 (выборка; воспроизведена вручную, м)','''| Occupancy | Minimum height | Maximum height |
|---|---|---|
| Any habitable room (flat roof) | 2.75 | 4.2 |
| Bathrooms, WC | 2.2 | 4.2 |
| Air-conditioned habitable room | 2.4 | 4.2 |
| Assembly halls, institutional, educational, industrial, storage, malls | 3.6 | 6.0 |
| IT buildings, office buildings | 2.75 | 4.2 |''','Высота — от поверхности пола до низшей точки потолка. Высота сверх 4,2 м засчитывается как дополнительный FSI 50 % площади (кроме отдельных назначений).','en')])
put(O,'lestnitsy','Мумбаи: ширина лестниц — по табл. 16 (учебные — 1,5 м до 32 м и 2,0 м выше; зрелищные — 2,0 м); ступенька ≤17,5 см; проступь ≥30 см (кроме жилых — 25 см) (DCPR, п. 37(15))',[DC],[
 dc('п. 37(15)(ii)–(iv)',Q('indcpr','(ii)Flight- No flight shall contain more than 12 risers','shall be 30cm'),
  'В марше не более 12 подъёмов; высота подъёма — не более 17,5 см; проступь — не менее 25 см в жилых зданиях и 30 см в остальных.')])
put(O,'lifty','Мумбаи: лифт обязателен в зданиях выше 16 м; выше 24 м — не менее двух, один пожарный (DCPR, п. 37(17))',[DC],[
 dc('п. 37(17)(i)',Q('indcpr','(i)At least one lift shall be provided in every building more than 16m in height.','may also extend up to terrace floor'),
  'В каждом здании выше 16 м — не менее одного лифта; в зданиях выше 24 м — не менее двух, один из них пожарный; не менее одного лифта обслуживает нижний уровень подвала.')])
Z='zhile-do-75'
put(Z,'komnaty','Мумбаи: любая жилая комната — ширина ≥2,4 м; кухня — ширина ≥1,8 м (в однокомнатной квартире — 2,1 м); многофункциональная комната с альковом ≥12,5 м²; ванная ≥1,50 м², WC ≥1,10 м² (DCPR, табл. 14)',[DC],[
 ('t','DCPR 2034, табл. 14 (выборка; воспроизведена вручную)','''| Occupancy | Minimum size, sq.m | Minimum width, m |
|---|---|---|
| Any habitable room | — | 2.4 |
| Kitchen (two-room and above tenement) | — | 1.8 |
| Kitchen (one-room tenement) | — | 2.1 |
| Multipurpose room (with alcove) | 12.5 | 2.4 |
| Bathroom | 1.50 | 1.10 |
| Water closet (W.C.) | 1.10 | 0.90 |''','Минимальные размеры и ширина жилых и вспомогательных помещений (Мумбаи).','en')])
put(Z,'vysota-potolka','Мумбаи: любая жилая комната (плоская крыша) — высота ≥2,75 м, макс. 4,2 м; помещение с кондиционированием — ≥2,4 м; ванные и WC — ≥2,2 м (DCPR, табл. 15)',[DC],[
 ('t','DCPR 2034, табл. 15 (выборка; воспроизведена вручную, м)','''| Occupancy | Minimum height | Maximum height |
|---|---|---|
| Any habitable room (flat roof) | 2.75 | 4.2 |
| Bathrooms, WC, combined bath & WC | 2.2 | 4.2 |
| Air-conditioned habitable room | 2.4 | 4.2 |''','Измеряется от поверхности пола до низшей точки потолка. Для скатной крыши — средняя высота 2,75 м при 2,4 м у низшей точки.','en')])
put(Z,'lifty','Мумбаи: лифт — в каждом здании выше 16 м; выше 24 м — не менее двух, один пожарный (DCPR, п. 37(17))',[DC],[
 dc('п. 37(17)(i)',Q('indcpr','(i)At least one lift shall be provided in every building more than 16m in height.','may also extend up to terrace floor'),
  'В каждом здании выше 16 м — не менее одного лифта; в зданиях выше 24 м — не менее двух, один из них пожарный.')])
put(Z,'lestnitsy','Мумбаи: ширина лестниц жилых — 1,5 м (до 70 м) / 2,0 м (выше 70 м); не более 12 подъёмов в марше; ступенька ≤17,5 см; проступь ≥25 см; поручень 0,9 м (DCPR, п. 37(15))',[DC],[
 dc('п. 37(15)(vii)',Q('indcpr','(vii) Hand rail- Handrails with a minimum height of 0.9m','shall be provided.'),
  'Поручни — минимальной высотой 0,9 м от середины проступей.'),
 dc('п. 37(15)(ii)–(iv)',Q('indcpr','(ii)Flight- No flight shall contain more than 12 risers','shall be 30cm'),
  'В марше не более 12 подъёмов; высота подъёма ≤17,5 см; проступь ≥25 см в жилых зданиях.')])
G='gradostroitelstvo'
put(G,'insolyatsiya','Нормы по часам инсоляции не найдены ⏳; дневной свет: по NBC 2016 Part 8 (пересказ Studio Matrx) — отношение окон к полу не менее 10 % (жилые комнаты, кухни), 5 % (санузлы), 20 % для классов — вторичный источник',[SM],[
 ('n','Studio Matrx пересказывает NBC 2016 Part 8: минимальное отношение площади окон к площади пола для жилой комнаты — 10 % (не менее 50 % открываемых), кухни — 10 %, санузла — 5 %, лестницы/коридора — 7,5 %, классов — 20 % (по правилам штатов). Это вторичный источник; по самому NBC Part 8 и по IS 2440 ⏳ не сверено. Studio Matrx также сообщает, что издание NBC 2016 BIS отозвано (актуальное — SP 7:2026).')])
NORMY={
 'Закон / кодекс':'Национальный строительный кодекс Индии (NBC 2016, BIS; Part 4 «Fire and Life Safety») — модельный кодекс; в Мумбаи — DCPR 2034 по Maharashtra Regional and Town Planning Act 1966 ([DCPR](https://portal.mcgm.gov.in/irj/go/km/docs/documents/MCGM%20Department%20List/Chief%20Engineer%20(Development%20Plan)/Docs/SANCTIONED%20DP2034/DCPR/DCPR%202034.pdf))',
 'Технический регламент':'NBC 2016 Part 4 ([копия NMC Нагпур](https://nmcnagpur.gov.in/assets/300/2025/03/mediafiles/NBC2016-Part-IV.pdf)); DCPR 2034, п. 47 и Приложение I (высотные и особые здания)',
 'Состав документации / стадии':'DCPR 2034, пп. 10–12 (уведомление, разрешение, Commencement/Occupancy Certificate)',
 'Градостроительство (планировка, инсоляция)':'DCPR 2034 (Part V FSI, Part VII зонирование) ⏳ не вынесены; NBC Part 8 (дневной свет) — по вторичному источнику',
 'Пожарная безопасность':'NBC 2016 Part 4; DCPR 2034, п. 47, Прил. I',
 'Процедура разрешений':'DCPR 2034, пп. 10–12 (Commissioner MCGM; Chief Fire Officer для высотных зданий)'}
