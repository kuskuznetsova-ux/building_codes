# Источники текстов (ключ в `qlib.FILES` → файл в `tools/src/` → откуда брать)

Тексты в репозиторий не кладём. Скачать, сохранить как .txt (HTML → текст, PDF → `pdftotext`), положить по указанным путям.

| Ключ | Файл | Источник |
|---|---|---|
| sp1 | fire/sp1.txt | СП 1.13130.2020 — https://www.consultant.ru/document/cons_doc_LAW_351940/ |
| sp4 | fire/sp4.txt | СП 4.13130.2013 — https://base.garant.ru/70398302/ |
| fz | fire/fz123.txt | ФЗ-123 — официальная редакция из «Техэксперт» (от пользователя) или https://sudact.ru/law/federalnyi-zakon-ot-22072008-n-123-fz-tekhnicheskii/ |
| sp2 | up/sp2r.txt | СП 2.13130.2020 (изм. 1, 2) — PDF от пользователя (Техэксперт) |
| sp486 | sp/sp486.txt | СП 486.1311500.2020 с изм. 1 — https://www.consultant.ru/document/cons_doc_LAW_507782/ (изменение), PDF от пользователя |
| sp267, sp477 | hr/sp267.txt, hr/sp477.txt | https://meganorm.ru/ (СП 267.1325800.2016, СП 477.1325800.2020) |
| sp42 | ins/sp42.txt | СП 42.13330.2026 — https://meganorm.ru/mega_doc/norm_update_01092026/pravila/0/sp_42_13330_2026_svod_pravil_gradostroitelstvo_planirovka_i.html (или официальный текст от пользователя) |
| san | ins/san_all.txt | СанПиН 1.2.3685-21, табл. 5.58–5.60 и п. 165–168 — https://sudact.ru/law/postanovlenie-glavnogo-gosudarstvennogo-sanitarnogo-vracha-rf-ot_1430/sanpin-1.2.3685-21/ |
| rs22 | fire/rs22b.txt | Правилник 22/2019 — https://www.paragraf.rs/propisi/pravilnik-tehnickim-normativima-zastitu-pozara-stambenih-poslovnih-objekata-objekata.html (копия PDF thoriumaplus.com) |
| rs80 | fire/rs22.txt | Правилник 80/2015 (высокие объекты) — http://antiplam.rs/ (копия PDF) |
| rspar | ins/rs_par.txt | Правилник 22/2015 о парцелацији, регулацији и изградњи — https://www.paragraf.rs/propisi/pravilnik_o_opstim_pravilima_za_parcelaciju_regulaciju_i_izgradnju.html |
| cpr | fire/cpr_uk.txt | https://www.legislation.gov.uk/eur/2011/305/annex/I |
| mbo | hr/mbo.txt | https://bvpi.de/bvpi/downloads/MBO.pdf |
| mhhr | hr/mhhr2.txt | https://bau.bremen.de/sixcms/media.php/13/MHHR.pdf |
| msb | hr/msb2.txt | Muster-Schulbau-Richtlinie, wirtschaft.hessen.de |
| garv | sp/garstvo.txt | https://bauministerkonferenz.de/Dokumente/42323132.pdf |
| adb1, adb2 | fire/adb1_26.txt, fire/adb2_26.txt | AD B Vol 1/2 (2019 + поправки 2025–2029) — https://www.gov.uk/government/publications/fire-safety-approved-document-b |
| adb2_06 | uk2/adb2_2006b.txt | AD B Vol 2, 2006 — https://www.gov.uk/government/publications/historical-documents-relating-to-approved-document-b-fire-safety |
| bb100 | uk2/bb100f2.txt | https://www.gov.uk/government/publications/building-bulletin-100-design-for-fire-safety-in-schools |
| bsa, hrb2, hrb6 | hr/bsa65_c.txt и др. | legislation.gov.uk: ukpga/2022/30/section/65; uksi/2023/275/regulation/5 и /6 |
| ba1, ba6, ba7 | uk2/ba_s1.txt и др. | legislation.gov.uk/ukpga/1984/55/section/1, /6, /7 |
| br7, br12, br16, br17, br11a/e/f, brs1 | uk2/br_*.txt | legislation.gov.uk/uksi/2010/2214/regulation/… и /schedule/1 |
| hp3, hp4, hp5, hp9, hp41, hp44 | uk2/hp_*.txt | legislation.gov.uk/uksi/2023/909/regulation/… |
| dmpo4 | uk2/dmpo_s4.txt | legislation.gov.uk/uksi/2015/595/schedule/4 |
| lich | ins/lich.txt | https://lichfields.uk/blog/2022/june/10/is-your-planning-application-at-risk-new-bre-report-209-guidance-fundamental-changes-to-daylight-and-sunlight-assessments (пересказ BRE 209 и EN 17037) |

Для генератора стадий (`tools/stages_gen`): `rs/` (Правилник 96/2023, Закон о планировании и строительстве — paragraf.rs), `st/` (RIBA Plan of Work 2020, ACE 2013, ПП РФ № 87), `eu/cka.txt`, `uk/gw.txt` — ссылки в `tools/stages_gen/data.py`.

## Страны ЕС (Франция, Австрия, Испания) — eudata.py
| key | file | URL |
|---|---|---|
| es | eu5/es_n.txt | https://www.codigotecnico.org/pdf/Documentos/SI/DBSI.pdf |
| at | eu5/at_n.txt | https://www.propellets.at/assets/upload/pelletlagerung/oib-rl-2-ausgabe-mai-2023.pdf (OIB-RL 2) |
| atb | eu5/atb_n.txt | https://din-notlicht.com/wp-content/uploads/oib-rl-begriffsbestimmungen-ausgabe-mai-2023.pdf |
| at23 | eu5/at23o_n.txt | https://din-notlicht.com/wp-content/uploads/oib-rl-2.3-ausgabe-mai-2023.pdf |
| at22 | eu5/at22_n.txt | https://din-notlicht.com/wp-content/uploads/oib-rl-2.2-ausgabe-mai-2023.pdf |
| at4 | eu5/at4_n.txt | https://glas-gasperlmair.at/wp-content/uploads/2023/10/oib-rl_4_ausgabe_mai_2023.pdf |
| fr | eu5/fr_n.txt | https://medias.amf.asso.fr/docs/DOCUMENTS/AMF_20070607_arrete_31_01_86_incendie.pdf (Légifrance недоступен) |

## Доступная среда (adata.py)
| key | file | URL |
|---|---|---|
| sp59 | acc/sp59.txt | СП 59.13330.2020 — PDF «Техэксперт», предоставлен пользователем (pdftotext -layout) |
| adm2 | acc/adm2.txt | https://assets.publishing.service.gov.uk/media/66f6c5eec71e42688b65ee11/ADM__V2_with_2024_amendments.pdf (pdftotext БЕЗ -layout: двухколоночная вёрстка) |
| sua | acc/sua.txt | https://www.codigotecnico.org/pdf/Documentos/SUA/DBSUA.pdf |
| rsa | acc/rs.txt | https://www.paragraf.rs/propisi_download/pravilnik_o_tehnickim_standardima_planiranja_projektovanja_i_izgradnje_objekata_kojima_se_osigurava_nesmetano_kretanje_i_pristup_osobama_sa_invaliditetom_deci_i_starim_osobama.pdf |
| uae | ae/ud.txt | https://dmpmedia.dm.gov.ae/uploads/2025/12/DUBAI-GUIDE-for-build-environment-Universal-Design.pdf |
