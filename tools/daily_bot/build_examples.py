"""Собирает examples.json из страниц портала «Строительные нормы».

Запуск: python tools/daily_bot/build_examples.py [docs]  (по умолчанию ./docs)
Для каждой страницы темы берёт цитату из вкладки «Россия» и ближайшие по теме
цитаты из вкладок «ОАЭ (Дубай)» и «Грузия» (с русским переводом).
Тексты переносятся как есть: в бот попадают только процитированные нормы.
"""
import json
import re
import sys
from pathlib import Path

SITE = "https://kuskuznetsova-ux.github.io/building_codes/"
TABS = {"ru": "Россия", "ae": "ОАЭ", "ge": "Грузия"}
PAIR = re.compile(
    r'<div class="orig" markdown>\s*(.*?)\s*</div>\s*<div class="ru" markdown>\s*(.*?)\s*</div>\s*</div>', re.S)
LABEL = re.compile(r"^\*([^*]+?):\*\s*")


def clean(s):
    s = re.sub(r'<small class="actual">.*?</small>\s*', "", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[ \t]+", " ", s).strip()
    # служебные пометки о происхождении текста в сообщения не попадают
    s = re.sub(r"\s*Цитата сверен.*?предоставлен пользователем\)\.?", "", s)
    return s


def tab_blocks(text):
    """{'ru': текст вкладки, ...} — вкладки идут с отступом в 4 пробела."""
    out, cur, name = {}, [], None
    for line in text.split("\n"):
        m = re.match(r'^=== "([^"]+)"', line)
        if m:
            if name:
                out[name] = "\n".join(cur)
            name = next((k for k, v in TABS.items() if m.group(1).startswith(v)), "other")
            cur = []
        elif name:
            cur.append(line[4:] if line.startswith("    ") else line)
    if name:
        out[name] = "\n".join(cur)
    return out


def pairs_of(block):
    """Все пары «оригинал — русский» вкладки (без таблиц, они в сообщении не читаются)."""
    out = []
    for orig, ru in PAIR.findall(block):
        if "|" in orig or "|" in ru:
            continue
        orig, ru = clean(orig), clean(ru)
        m = LABEL.match(orig)
        label, body = (m.group(1), orig[m.end():]) if m else ("", orig)
        if len(body) < 40 or len(ru) < 20:
            continue
        out.append({"label": label.strip(), "orig": body.strip(),
                    "ru": re.sub(r"^\*Пояснение:\*\s*", "", ru)})
    return out


def stems(text):
    return {w[:5] for w in re.findall(r"[а-яё]{5,}", text.lower())}


# слова, общие почти для любой нормы: совпадение по ним ничего не говорит о теме
COMMON = {"здани", "помещ", "должн", "требо", "допус", "предус", "соотв", "устан", "этаже", "случа",
          "каждо", "кроме", "наруж", "этажа", "пожар", "более", "менее", "выше", "ниже", "между", "норма", "прави", "порядо", "свод", "пункт"}
MIN_SHARED = 2


def best_pair(candidates, ru_pair, topic):
    """Ближайшая по смыслу цитата страны к российской. weak=True — подходящей нет."""
    if not candidates:
        return None
    ref = stems(ru_pair["ru"]) - COMMON  # заголовок темы не учитываем: общий для всех цитат страницы
    scored = [(len(ref & (stems(c["ru"]) - COMMON)), i, c) for i, c in enumerate(candidates)]
    score, _, best = max(scored, key=lambda t: (t[0], -t[1]))
    return {**best, "weak": score < (1 if len(ref) <= 6 else MIN_SHARED)}


def main(docs):
    docs = Path(docs)
    items = []
    for md in sorted(docs.rglob("*.md")):
        if md.name.endswith(".en.md"):
            continue
        text = md.read_text(encoding="utf-8")
        if '=== "Россия"' not in text:
            continue
        title = re.search(r"^# (.+)$", text, re.M)
        blocks = tab_blocks(text)
        allp = {k: pairs_of(blocks.get(k, "")) for k in TABS}
        if not allp["ru"] or not (allp["ae"] or allp["ge"]):
            continue
        topic = title.group(1) if title else md.stem
        pairs = {"ru": allp["ru"][0],
                 "ae": best_pair(allp["ae"], allp["ru"][0], topic),
                 "ge": best_pair(allp["ge"], allp["ru"][0], topic)}
        rel = md.relative_to(docs).with_suffix("")
        url = SITE + (str(rel.parent) + "/" if rel.name == "index" else str(rel) + "/")
        items.append({"id": str(rel.parent if rel.name == "index" else rel),
                      "topic": title.group(1) if title else rel.name,
                      "url": url.replace("./", ""), **pairs})
    out = Path(__file__).resolve().parent / "examples.json"
    out.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(items), "примеров ->", out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "docs")
