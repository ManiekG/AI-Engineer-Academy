"""Dzień 2: kalkulator pamięci modelu AI.

Zadanie: pobierz liczbę parametrów (w miliardach) i liczbę bitów na parametr.
Oblicz rozmiar samych wag modelu w GiB i wyświetl czytelny raport.
Wskazówka: 1 parametr FP16 zajmuje 2 bajty, a 1 GiB = 1024**3 bajtów.
"""


def model_size_gib(parameters_b: float, bits_per_parameter: int) -> float:
    """Zwróć szacowany rozmiar wag modelu w GiB."""
    # TODO: zamień miliardy parametrów i bity na bajty, a potem na GiB.
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: zapytaj użytkownika o dane i wydrukuj wynik.
    pass
