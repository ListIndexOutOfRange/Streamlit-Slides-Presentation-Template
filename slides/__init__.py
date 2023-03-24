from __future__ import annotations
from typing import Iterable
import re
from pathlib import Path
from importlib import import_module
import toml


HERE = Path(__file__).resolve().parent

CONFIG = toml.load(HERE.parent / "config.toml")


def alphanumeric_sort(iterable: Iterable) -> Iterable:
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(iterable, key=alphanum_key)


def get_pages() -> list[str]:
    python_files = HERE.glob("*.py")
    python_files = filter(lambda x: not x.stem.startswith('_'), python_files)
    modules = list()
    for file in python_files:
        import_module(f"{file.parent.stem}.{file.stem}")
        modules.append(file.stem)
    return alphanumeric_sort(modules)


pages = get_pages()


__all__ = (CONFIG, pages)
