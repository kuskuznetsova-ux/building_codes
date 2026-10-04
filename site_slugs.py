"""Латинские идентификаторы вкладок стран, чтобы на них можно было ссылаться как #rs, #eu."""
from pymdownx.slugs import slugify

_TABS = {'россия': 'ru', 'сербия': 'rs', 'ес': 'eu', 'англия': 'uk'}


def tab_slugify(value, separator):
    key = value.lower()
    for word, code in _TABS.items():
        if word in key:
            return code
    return slugify(case='lower')(value, separator)
