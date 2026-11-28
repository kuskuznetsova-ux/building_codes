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
START = date(2026, 1, 1)
LIMIT = 4000


def cut(s, n):
    """Обрезка по границе предложения или слова."""
    s = " ".join(s.split())
    if len(s) <= n:
        return s
    head = s[:n]
    p = max(head.rfind(". "), head.rfind("; "))
    return (head[:p + 1] if p > n * 0.5 else head.rsplit(" ", 1)[0]) + " …"


def pick(items, today=None, index=None):
    ordered = sorted(items, key=lambda x: (not (x["ae"] and x["ge"]), x["url"]))
    i = index if index is not None else ((today or date.today()) - START).days
    return ordered[i % len(ordered)]


def format_example(ex):
    esc = lambda s: html.escape(s, quote=False)
    lines = [f"<b>Норма дня · {esc(ex['topic'])}</b>", ""]
    ru = ex["ru"]
    lines += [f"<b>Россия</b> — {esc(ru['label'].split(' · ', 1)[-1])}",
              f"<i>{esc(cut(ru['orig'], 450))}</i>", "",
              esc(cut(ru["ru"], 400)), ""]
    for key, name in (("ae", "ОАЭ (Дубай)"), ("ge", "Грузия")):
        p = ex[key]
        if p:
            lines += [f"<b>{name}</b> — {esc(p['label'].split(' · ', 1)[-1])}", esc(cut(p["ru"], 500)), ""]
        else:
            lines += [f"<b>{name}</b> — в портале по этой теме пока нет (⏳)", ""]
    lines += ["Сопоставление — по теме страницы; перед использованием сверяйте с первоисточником.",
              f'<a href="{ex["url"]}">Открыть тему на портале</a>']
    return "\n".join(lines)[:LIMIT]


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
    text = format_example(pick(items, index=a.index))
    if a.dry_run:
        print(text)
    else:
        send(text)
        print("отправлено")


if __name__ == "__main__":
    main()
