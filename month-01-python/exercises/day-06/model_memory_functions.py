"""Dzień 6: funkcje szacujące pamięć modelu.

Napisz funkcje dla FP16, INT8 i INT4. Każda przyjmuje liczbę parametrów w B
i zwraca rozmiar wag w GiB. Dodaj argument domyślny na narzut pamięci.
"""


def estimate_vram(parameters_b: float, bits: int, overhead: float = 1.2) -> float:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    pass
