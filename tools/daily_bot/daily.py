"""Утренний пример из портала: норма России и ближайшие требования ОАЭ (Дубай) и Грузии.

Запуск: python -m norm_monitor.daily [--dry-run] [--index N]
Примеры лежат в examples.json (собираются build_examples.py из страниц портала).
Номер примера считается по дате, поэтому состояние хранить не нужно.
"""
import argparse
import html
import json
from datetime import date
from pathlib import Path

import os
import urllib.request

EXAMPLES = Path(__file__).resolve().parent / "examples.json"
ENGLISH = Path(__file__).resolve().parent / "en.json"
START = date(2026, 11, 30)  # в этот день уходит первый пример
LIMIT = 4000


def cut(s, n):
    """Обрезка по границе предложения или слова."""
    s = " ".join(s.split())
    if len(s) <= n:
        return s
    head = s[:n]
    p = max(head.rfind(". "), head.rfind("; "))
    return (head[:p + 1] if p > n * 0.5 else head.rsplit(" ", 1)[0]) + " …"


def rank(x):
    """0 — пожарные нормы, 1 — высотные здания, 2 — остальное."""
    i = x["id"]
    if i.startswith("vysotnye-") or i.startswith("pozharnaya/vysotnye"):
        return 1
    return 0 if i.startswith("pozharnaya/") else 2


def pick(items, today=None, index=None):
    ordered = sorted(items, key=lambda x: (rank(x), not (x["ae"] and x["ge"]), x["id"]))
    i = index if index is not None else max(0, ((today or date.today()) - START).days)
    return ordered[i % len(ordered)]


def format_example(ex, en=None, scale=1.0):
    esc = lambda s: html.escape(s, quote=False)
    en = (en or {}).get(ex["id"], {})
    n = lambda k: int(k * scale)
    lines = [f"<b>Норма дня · {esc(ex['topic'])}</b>", ""]
    ru = ex["ru"]
    lines += [f"<b>Россия</b> — {esc(ru['label'].split(' · ', 1)[-1])}",
              f"<i>{esc(cut(ru['orig'], n(380)))}</i>", "",
              esc(cut(ru["ru"], n(330)))]
    if en.get("ru"):
        lines += ["", "EN: " + esc(cut(en["ru"], n(330)))]
    lines.append("")
    for key, name in (("ae", "ОАЭ (Дубай)"), ("ge", "Грузия")):
        p = ex[key]
        if not p:
            lines += [f"<b>{name}</b> — в портале по этой теме пока нет (⏳)", ""]
            continue
        lines += [f"<b>{name}</b> — {esc(p['label'].split(' · ', 1)[-1])}", esc(cut(p["ru"], n(330)))]
        english = p["orig"] if key == "ae" else en.get("ge")  # ОАЭ: оригинал DBC уже на английском
        if english:
            lines += ["EN: " + esc(cut(english, n(330)))]
        lines.append("")
    lines += ["Сопоставление — по теме страницы; перед использованием сверяйте с первоисточником.",
              f'<a href="{ex["url"]}">Открыть тему на портале</a>']
    text = "\n".join(lines)
    if len(text) > LIMIT and scale > 0.3:  # не обрезаем тегами: сжимаем цитаты и пересобираем
        return format_example(ex, {ex["id"]: en}, scale * 0.8)
    return text


def send(text):
    token, chat = os.environ["DAILY_BOT_TOKEN"], os.environ["DAILY_CHAT_ID"]
    body = json.dumps({"chat_id": chat, "text": text, "parse_mode": "HTML",
                       "disable_web_page_preview": True}).encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage",
                                 data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        resp = json.load(r)
    if not resp.get("ok"):
        raise RuntimeError(f"Telegram: {resp}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--index", type=int)
    a = ap.parse_args()
    items = json.loads(EXAMPLES.read_text(encoding="utf-8"))
    en = json.loads(ENGLISH.read_text(encoding="utf-8")) if ENGLISH.exists() else {}
    text = format_example(pick(items, index=a.index), en)
    if a.dry_run:
        print(text)
    else:
        send(text)
        print("отправлено")


if __name__ == "__main__":
    main()
