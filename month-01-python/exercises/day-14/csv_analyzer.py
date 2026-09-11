"""Dzień 14: mini-projekt CSV Analyzer.

Wczytaj CSV z kolumnami model, parameters_b, vram_gib i wypisz średni VRAM
oraz model o najwyższej liczbie parametrów.
"""

import csv
from pathlib import Path


def load_models(path: Path) -> list[dict[str, str]]:
    # TODO: użyj csv.DictReader.
    raise NotImplementedError
