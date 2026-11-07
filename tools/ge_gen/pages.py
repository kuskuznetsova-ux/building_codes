# -*- coding: utf-8 -*-
"""Страница «Грузия — правовая основа и стадии» (RU и EN): docs/normy/ge.md, docs/normy/ge.en.md."""
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import gedata
from gedata import Q,FAIL
from qlib import pair
DOCS=os.path.normpath(os.path.join(HERE,'..','..','docs'))
Q94=Q('gecode','1. Строительство зданий и сооружений I класса, за исключением случаев','подлежит обязательству по получению разрешения на строительство.')
Q104=Q('gecode','2. Решение об утверждении условий использования земельного участка под строительство, кроме случая','после приема заявления.')
Q108=Q('gecode','3. Решение о согласовании архитектурного проекта, кроме случая, предусмотренного статьей 109','5 лет со дня его утверждения.')
Q107=Q('gecode','3. Административный орган, выдающий разрешение на строительство, обязан, кроме случая','должно быть принято в течение 5 рабочих дней.')
Q106=Q('gecode','1. Заявка на выдачу разрешения должна включать в себя:','з) в случаях, предусмотренных законодательством Грузии, – заключение аккредитованного органа инспектирования или (и) сертифицированного эксперта')
Q34=Q('ge255','3. წინასწარ გადაწყვეტილებას ესკიზის შეთანხმების თაობაზე','10 სამუშაო დღის ვადაში.')
Q21=Q('ge255','2. სავალდებულო საექსპერტო შეფასებას ექვემდებარება სანებართვო დოკუმენტების პროექტები:','დ) ტექნოლოგიური')
Q31=Q('ge255','3. გადაწყვეტილება ამ წესით განსაზღვრული შენობა-ნაგებობების ექსპლუატაციაში მიღებისათვის ვარგისად აღიარების შესახებ მიიღება:','IV კლასის შენობა-ნაგებობის შემთხვევაში – 30 სამუშაო დღის ვადაში.')
if FAIL: raise SystemExit(FAIL)
L={'ru':dict(
 h='# 4.2 Грузия — правовая основа и стадии проектирования',
 st='Статус: черновик',
 stt='Текст составлен по Кодексу № 3213 (русский перевод на matsne) и первичным редакциям Постановлений № 255 и № 41. Консолидированные (текущие) версии постановлений на matsne платные — последующие изменения не учтены. ⏳ — не сверено.',
 s1='## Правовая основа',
 t1=['| Уровень | Документ |','|---|---|',
  '| Кодекс | [Кодекс о пространственном планировании, архитектурной и строительной деятельности № 3213 от 20.07.2018](https://matsne.gov.ge/ru/document/view/4276845) (с 03.06.2019) |',
  '| Порядок разрешений | [Пост. Правительства № 255 от 31.05.2019](https://matsne.gov.ge/ka/document/view/4578072) — классы зданий, предпроектные исследования, состав документов, экспертиза, уведомления, разрешение, приёмка |',
  '| Безопасность зданий | [Пост. № 41 от 28.01.2016](https://matsne.gov.ge/ka/document/view/3176389) — технический регламент «Правила безопасности здания» (на основе IBC), в силе с 01.01.2017 для классов III–V |',
  '| Пожарная безопасность (общая) | [Закон об общественной безопасности № 2608](https://matsne.gov.ge/en/document/view/4243170), ст. 25; регламент «Условия пожарной безопасности» ⏳ не найден. Закон «О пожарной безопасности» 1998 г. утратил силу 02.04.2017 |'],
 s2='## Классы зданий и вид процедуры',
 p2='Здания делятся на 5 классов по риску (Кодекс, ст. 96); пороги по площади, высоте и т. п. — прил. 1 к Пост. № 255 (⏳ таблица не разобрана). От класса зависит процедура:',
 b2=['**I класс** — простое уведомление о строительстве (решение за 5 рабочих дней); муниципалитет вправе потребовать детальное уведомление или разрешение.','**II класс** — разрешение; муниципалитет вправе заменить его детальным уведомлением (решение за 10 рабочих дней).','**III–IV классы** — разрешение, обязательная экспертиза; Пост. № 41 действует для классов III–V.'],
 s3='## Последовательность стадий',
 p3='Разрешение выдаётся в одно-, двух- или **трёхстадийном** административном производстве (Кодекс, ст. 104–108). Стадии I и II — условия использования участка и согласование архитектурного проекта — можно пройти заранее.',
 th=['| № | Стадия | Что это | Основание | Срок |','|--:|---|---|---|---|'],
 rows=[
 ('1','Предпроектное исследование (წინასაპროექტო კვლევა)','топография, состояние здания, застройка, документальное, влияние на соседей, инженерная геология (обязательность зависит от класса)','Пост. № 255, ст. 6–7','—'),
 ('2','**Стадия I**: условия использования участка','функциональная зона, вид использования, параметры и линии застройки, максимальная высота','Кодекс, ст. 103–105; № 255, ст. 8–9','10 раб. дней; действуют 3 года'),
 ('3','Архитектурный эскиз и предварительное решение (необязательно)','схема участка и фасадов, ТЭП; «концепция строительства»','Кодекс, ст. 113–114; № 255, ст. 12, 34','10 раб. дней'),
 ('4','**Стадия II**: согласование архитектурного проекта','титул, записка, ТЭП (К1, К2, К3), планы, разрезы, фасады','Кодекс, ст. 106, 108; № 255, ст. 13','17 раб. дней; действует 5 лет'),
 ('5','Конструктивные части, проект организации строительства','инженерно-геологические изыскания, конструктивная схема/проект, технологическая схема, проект организации строительства','Кодекс, ст. 106; № 255, ст. 11, 15–18','—'),
 ('6','Экспертиза','детальный архитектурный проект — III–IV классы; инженерно-геологический и конструктивный — II–IV','№ 255, ст. 21','—'),
 ('7','**Стадия III**: разрешение на строительство','детальный архитектурный проект; в разрешении — класс, этапы, строительные условия','Кодекс, ст. 107, 111; № 255, ст. 14, 25','20 раб. дней (при трёх стадиях — 5); при молчании считается выданным'),
 ('8','Строительство по этапам','проект организации строительства: подготовительные и основные работы; протоколы завершения этапов','№ 255, ст. 20, 26','—'),
 ('9','Приёмка: признание пригодным к эксплуатации','этапные протоколы, обмерный план, кадастровый чертёж','№ 255, ст. 29–31','15–30 раб. дней по классам'),
 ],
 s4='## Дословно',
 qs=[('Кодекс № 3213, ст. 94, ч. 1–2',Q94,'ru (офиц. перевод)','Класс I — простое уведомление; классы I–IV — разрешение.'),
  ('Кодекс № 3213, ст. 104, ч. 2',Q104,'ru (офиц. перевод)','Условия использования участка — решение за 10 рабочих дней.'),
  ('Кодекс № 3213, ст. 108, ч. 3, 5, 6',Q108,'ru (офиц. перевод)','Согласование архитектурного проекта — 17 рабочих дней; при молчании проект считается согласованным; срок действия 5 лет.'),
  ('Кодекс № 3213, ст. 107, ч. 3',Q107,'ru (офиц. перевод)','Разрешение — 20 рабочих дней, при трёх стадиях — 5.'),
  ('Пост. № 255, ст. 34, п. 3 (первичная редакция)',Q34,'ka','Предварительное решение (согласование эскиза) — 10 рабочих дней.'),
  ('Пост. № 255, ст. 21, п. 2 (первичная редакция)',Q21,'ka','Обязательная экспертиза: детальный архитектурный проект (III–IV), инженерно-геологический и конструктивный (II–IV), технологический — при необходимости.'),
  ('Пост. № 255, ст. 31, п. 3 (первичная редакция)',Q31,'ka','Решение о пригодности к эксплуатации: II класс — 15 раб. дней; III до 1500 м² — 15; свыше — 20; IV — 30.')],
 s5='## Что осталось',
 b5=['Прил. 1 к Пост. № 255 (пороги классов) — разобрать по PDF.','Консолидированные редакции Пост. № 41 и № 255; сроки по Кодексу для классов.','Стадии «передача заказчику» и «эксплуатация» — документы не найдены.','Градостроительные нормы (К1, К2, К3, линии регулирования), инсоляция.'],
 note='Тема связана со [стадиями проектирования](../sravnenie/stadii.md) и [пожарной безопасностью](../pozharnaya/index.md) (вкладки «🇬🇪 Грузия»).'),
 'en':dict(
 h='# 4.2 Georgia — legal framework and design stages',
 st='Status: draft',
 stt='Compiled from Code No. 3213 (Russian translation on matsne) and the original editions of Resolutions No. 255 and No. 41. Current consolidated versions of the resolutions are paywalled on matsne, so later amendments are not reflected. ⏳ = not verified.',
 s1='## Legal framework',
 t1=['| Level | Document |','|---|---|',
  '| Code | [Code of Georgia on Spatial Planning, Architectural and Construction Activities No. 3213 of 20.07.2018](https://matsne.gov.ge/en/document/view/4276845) (in force from 03.06.2019) |',
  '| Permit procedure | [Government Resolution No. 255 of 31.05.2019](https://matsne.gov.ge/ka/document/view/4578072) — building classes, pre-design surveys, documents, expert review, notifications, permit, acceptance |',
  '| Building safety | [Resolution No. 41 of 28.01.2016](https://matsne.gov.ge/ka/document/view/3176389) — technical regulation “Building Safety Rules” (IBC-based), in force since 01.01.2017 for classes III–V |',
  '| Fire safety (general) | [Law on Public Safety No. 2608](https://matsne.gov.ge/en/document/view/4243170), Art. 25; the “Fire Safety Conditions” regulation ⏳ not found. The 1998 Law on Fire Safety ceased to be in force on 02.04.2017 |'],
 s2='## Building classes and type of procedure',
 p2='Buildings fall into 5 risk classes (Code, Art. 96); thresholds for area, height etc. are in Annex 1 to Resolution No. 255 (⏳ table not parsed). The class determines the procedure:',
 b2=['**Class I** — simple construction notification (decision within 5 working days); a municipality may require a detailed notification or a permit.','**Class II** — permit; a municipality may replace it with a detailed notification (decision within 10 working days).','**Classes III–IV** — permit and mandatory expert review; Resolution No. 41 applies to classes III–V.'],
 s3='## Sequence of stages',
 p3='A permit is issued in a one-, two- or **three-stage** administrative procedure (Code, Arts. 104–108). Stages I and II — site development conditions and approval of the architectural project — can be completed in advance.',
 th=['| № | Stage | What it is | Basis | Time limit |','|--:|---|---|---|---|'],
 rows=[
 ('1','Pre-design survey (წინასაპროექტო კვლევა)','topographic, condition of existing building, built-up area, documentary, impact on neighbours, engineering-geological (mandatory depending on class)','Res. 255, Arts. 6–7','—'),
 ('2','**Stage I**: site development conditions','functional zone, use, development parameters and lines, maximum height','Code, Arts. 103–105; Res. 255, Arts. 8–9','10 working days; valid 3 years'),
 ('3','Architectural sketch and preliminary decision (optional)','site and façade schemes, key figures; “construction concept”','Code, Arts. 113–114; Res. 255, Arts. 12, 34','10 working days'),
 ('4','**Stage II**: approval of the architectural project','title, explanatory note, indicators (K1, K2, K3), plans, sections, façades','Code, Arts. 106, 108; Res. 255, Art. 13','17 working days; valid 5 years'),
 ('5','Structural parts, construction organisation project','engineering-geological survey, structural scheme/project, technological scheme, construction organisation project','Code, Art. 106; Res. 255, Arts. 11, 15–18','—'),
 ('6','Expert review','detailed architectural project — classes III–IV; engineering-geological and structural — II–IV','Res. 255, Art. 21','—'),
 ('7','**Stage III**: building permit','detailed architectural project; the permit states class, stages and construction conditions','Code, Arts. 107, 111; Res. 255, Arts. 14, 25','20 working days (5 for three-stage); deemed issued if the authority is silent'),
 ('8','Construction in stages','construction organisation project: preparatory and main works; stage completion records','Res. 255, Arts. 20, 26','—'),
 ('9','Acceptance: recognition as fit for use','stage records, as-built survey, cadastral drawing','Res. 255, Arts. 29–31','15–30 working days by class'),
 ],
 s4='## Verbatim',
 qs=[('Code No. 3213, Art. 94(1)–(2)',Q94,'ru (official translation)','Class I — simple notification; classes I–IV — permit.'),
  ('Code No. 3213, Art. 104(2)',Q104,'ru (official translation)','Site development conditions — decision within 10 working days.'),
  ('Code No. 3213, Art. 108(3), (5), (6)',Q108,'ru (official translation)','Approval of the architectural project — 17 working days; deemed approved if no decision; valid for 5 years.'),
  ('Code No. 3213, Art. 107(3)',Q107,'ru (official translation)','Permit — 20 working days, 5 for the three-stage procedure.'),
  ('Res. 255, Art. 34(3) (original edition)',Q34,'ka','Preliminary decision (approval of the sketch) — 10 working days.'),
  ('Res. 255, Art. 21(2) (original edition)',Q21,'ka','Mandatory expert review: detailed architectural project (III–IV), engineering-geological and structural (II–IV), technological — if needed.'),
  ('Res. 255, Art. 31(3) (original edition)',Q31,'ka','Decision on fitness for use: class II — 15 working days; class III up to 1500 m² — 15; above — 20; class IV — 30.')],
 s5='## Still to do',
 b5=['Annex 1 to Resolution No. 255 (class thresholds) — parse from the PDF.','Consolidated editions of Resolutions No. 41 and No. 255; Code time limits by class.','Stages “handover to the client” and “operation” — no documents found.','Urban planning norms (K1, K2, K3, building lines), insolation.'],
 note='See also the [design stages](../sravnenie/stadii.md) and [fire safety](../pozharnaya/index.md) pages (tab “🇬🇪 Georgia”).')}
def build(lang):
    d=L[lang]; o=[d['h'],'','!!! warning "'+d['st']+'"','    '+d['stt'],'',d['s1'],'']+d['t1']+['',d['s2'],'',d['p2'],'']+['- '+b for b in d['b2']]+['',d['s3'],'',d['p3'],'']+d['th']
    for r in d['rows']: o.append('| '+' | '.join(r)+' |')
    o+=['',d['s4'],'']
    for lab,q,lg,ru in d['qs']:
        # pair() даёт отступ 4 — снимаем
        o+=[x[4:] if x.startswith('    ') else x for x in pair(lab,q,ru,lg)]
    o+=[d['s5'],'']+['- [ ] '+b for b in d['b5']]+['',d['note'],'']
    return '\n'.join(o)
for lang,fn in (('ru','ge.md'),('en','ge.en.md')):
    open(os.path.join(DOCS,'normy',fn),'w',encoding='utf-8').write(build(lang))
print('ok')
