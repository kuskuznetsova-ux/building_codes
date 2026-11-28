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


def first_pair(block):
    for orig, ru in PAIR.findall(block):
        if "|" in orig or "|" in ru:  # таблицы в сообщении не читаются
            continue
        orig, ru = clean(orig), clean(ru)
        m = LABEL.match(orig)
        label, body = (m.group(1), orig[m.end():]) if m else ("", orig)
        if len(body) < 40 or len(ru) < 20:
            continue
        return {"label": label.strip(), "orig": body.strip(), "ru": re.sub(r"^\*Пояснение:\*\s*", "", ru)}
    return None


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
        pairs = {k: first_pair(blocks.get(k, "")) for k in TABS}
        if not pairs["ru"] or not (pairs["ae"] or pairs["ge"]):
            continue
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
