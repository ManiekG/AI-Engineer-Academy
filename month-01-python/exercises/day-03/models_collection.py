"""Dzień 3: kolekcja modeli AI.

Utwórz słownik modeli: nazwa -> liczba parametrów w B oraz wymagany VRAM w GiB.
Wypisz każdy model, znajdź największy i zbuduj zbiór unikalnych wartości VRAM.
"""

MODELS = {
    "Llama-3.2-3B": {"parameters_b": 3, "vram_gib": 6},
    "Mistral-7B": {"parameters_b": 7, "vram_gib": 14},
    "Llama-3.1-8B": {"parameters_b": 8, "vram_gib": 16},
}


def largest_model(models: dict[str, dict[str, int]]) -> str:
    """Zwróć nazwę modelu o największej liczbie parametrów."""
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    pass
