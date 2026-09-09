# Miesiąc 1 — Python, Git i API

Założenie: około 1–2 godziny dziennie.

## Pierwsze 10 dni

### Dzień 1 — instalacja, venv, pierwszy program
Tematy: instalacja i sprawdzenie Pythona, `python --version`, `pip`, `venv`, uruchamianie skryptów, `print()`, zmienne, podstawowe typy.

Darmowa lekcja PL:
- CodeBucket — Kurs Pythona dla początkujących, rozdziały 00:00–08:33: https://www.youtube.com/watch?v=_6014HB3SMk

Ćwiczenie: utwórz `day01_system_info.py`, który wypisze imię użytkownika, system operacyjny, wersję Pythona i zdanie „Rozpoczynam naukę AI Engineer”.

Rezultat: `month-01-python/exercises/day-01/day01_system_info.py`

### Dzień 2 — typy danych i operatory
Tematy: `int`, `float`, `str`, `bool`, konwersje typów, operatory matematyczne i porównania.

Darmowa lekcja PL:
- CodeBucket — 05:09–15:02: https://www.youtube.com/watch?v=_6014HB3SMk

Ćwiczenie: kalkulator pamięci modelu AI.

Rezultat: `month-01-python/exercises/day-02/model_memory_calculator.py`

### Dzień 3 — listy, krotki, zbiory, słowniki
Tematy: `list`, `tuple`, `set`, `dict`, indeksowanie, slicing.

Darmowe lekcje PL:
- CodeBucket — 22:45–47:46: https://www.youtube.com/watch?v=_6014HB3SMk
- Maciej Komosiński — kolekcje Pythona: https://www.youtube.com/watch?v=y9eS0kuuxoI

Ćwiczenie: słownik modeli AI z liczbą parametrów i VRAM.

Rezultat: `month-01-python/exercises/day-03/models_collection.py`

### Dzień 4 — instrukcje warunkowe
Tematy: `if`, `elif`, `else`, `and`, `or`, `not`, porównania.

Darmowa lekcja PL:
- CodeBucket — od ok. 15:02: https://www.youtube.com/watch?v=_6014HB3SMk

Ćwiczenie: program dobierający klasę modelu do ilości VRAM.

Rezultat: `month-01-python/exercises/day-04/model_selector.py`

### Dzień 5 — pętle
Tematy: `for`, `while`, `range`, `enumerate`, `zip`, `break`, `continue`.

Darmowe lekcje PL:
- CodeBucket — od 19:03: https://www.youtube.com/watch?v=_6014HB3SMk
- Maciej Komosiński — pętle i kolekcje: https://www.youtube.com/watch?v=y9eS0kuuxoI

Ćwiczenie: analiza listy modeli AI i filtrowanie po VRAM.

Rezultat: `month-01-python/exercises/day-05/model_loops.py`

### Dzień 6 — funkcje
Tematy: `def`, argumenty, `return`, argumenty domyślne, `*args`, `**kwargs`.

Darmowa lekcja PL:
- CodeBucket — od 1:03:10: https://www.youtube.com/watch?v=_6014HB3SMk

Ćwiczenie: funkcje szacujące pamięć modeli FP16, INT8 i INT4.

Rezultat: `month-01-python/exercises/day-06/model_memory_functions.py`

### Dzień 7 — mini projekt: Text Analyzer CLI
Tematy: powtórka dni 1–6, łączenie funkcji, pętli, słowników i stringów.

Darmowa lekcja PL:
- CodeBucket — stringi 47:46–1:03:10 oraz funkcje od 1:03:10: https://www.youtube.com/watch?v=_6014HB3SMk

Projekt: liczba znaków, słów, zdań oraz 5 najczęstszych słów.

Rezultat: `month-01-python/exercises/day-07/text_analyzer.py`

### Dzień 8 — moduły, import i pakiety
Tematy: `import`, własne moduły, pakiety, `pip`, `if __name__ == "__main__"`.

Darmowa lekcja PL:
- CodeBucket — Moduły i Pakiety w Pythonie: https://www.youtube.com/watch?v=dlm9x0h35bc

Ćwiczenie: podziel Text Analyzer na `analyzer.py` i `main.py`.

Rezultat: `month-01-python/exercises/day-08/`

### Dzień 9 — OOP
Tematy: `class`, `__init__`, obiekty, atrybuty, metody, podstawy dziedziczenia.

Darmowa lekcja PL:
- CodeBucket — Programowanie Obiektowe w Pythonie: https://www.youtube.com/watch?v=GlRvUX9nCPM

Ćwiczenie: klasa `AIModel` z polami `name`, `parameters_b`, `quantization`, `vram_required` i metodą `describe()`.

Rezultat: `month-01-python/exercises/day-09/ai_model.py`

### Dzień 10 — type hints i dataclasses
Tematy: adnotacje typów, `Optional`, `list[str]`, `dict[str, int]`, `@dataclass`.

Materiały:
- OOP: https://www.youtube.com/watch?v=GlRvUX9nCPM
- `dataclasses`: https://docs.python.org/3/library/dataclasses.html
- `typing`: https://docs.python.org/3/library/typing.html

Ćwiczenie: przerób klasę `AIModel` na `@dataclass` i dodaj type hints.

Rezultat: `month-01-python/exercises/day-10/ai_model_dataclass.py`

## Dni 11–30 — zakres
11. pliki TXT
12. JSON
13. wyjątki
14. mini projekt CSV Analyzer
15. NumPy
16. Pandas
17. filtrowanie, sortowanie, groupby, missing values
18. HTTP i REST
19. FastAPI
20. Pydantic
21. upload plików i błędy HTTP
22. logging
23. pytest
24. testowanie FastAPI
25. Git — podstawy
26. branch, merge, PR
27. Docker
28. Docker Compose
29. składanie Document Analyzer API
30. egzamin praktyczny

## Zasady pracy
Każdego dnia: 20–40 min materiału, 40–80 min kodowania, ćwiczenie zapisane w repo i commit.

## Status
- [ ] Dzień 1
- [ ] Dzień 2
- [ ] Dzień 3
- [ ] Dzień 4
- [ ] Dzień 5
- [ ] Dzień 6
- [ ] Dzień 7
- [ ] Dzień 8
- [ ] Dzień 9
- [ ] Dzień 10
- [ ] Dzień 11
- [ ] Dzień 12
- [ ] Dzień 13
- [ ] Dzień 14
- [ ] Dzień 15
- [ ] Dzień 16
- [ ] Dzień 17
- [ ] Dzień 18
- [ ] Dzień 19
- [ ] Dzień 20
- [ ] Dzień 21
- [ ] Dzień 22
- [ ] Dzień 23
- [ ] Dzień 24
- [ ] Dzień 25
- [ ] Dzień 26
- [ ] Dzień 27
- [ ] Dzień 28
- [ ] Dzień 29
- [ ] Dzień 30
