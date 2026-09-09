# AI Engineer Academy — plan nauki

## Cel

Celem jest osiągnięcie praktycznych kompetencji AI/LLM Engineer: budowa aplikacji AI od danych wejściowych, przez modele, RAG i API, po konteneryzację, deployment i monitoring.

Główne technologie:

- Python
- Git
- NumPy
- Pandas
- scikit-learn
- PyTorch
- Hugging Face
- FastAPI
- Pydantic
- Ollama
- llama.cpp
- Qdrant
- PostgreSQL / pgvector
- Docker
- pytest
- LoRA / QLoRA / PEFT

---

# Plan 6 miesięcy

## Miesiąc 1 — Python, Git, API

Cel:
- swobodny Python
- praca z plikami i danymi
- Git
- REST
- FastAPI
- testy
- Docker

Projekt końcowy: **Document Analyzer API**

## Miesiąc 2 — Machine Learning i PyTorch

Tematy:
- supervised learning
- unsupervised learning
- regresja
- klasyfikacja
- clustering
- train / validation / test
- overfitting
- regularization
- metryki
- scikit-learn
- PyTorch
- training loop
- loss
- optimizer
- backpropagation

Projekt: **Model klasyfikacyjny z API**

## Miesiąc 3 — Transformers i LLM

Tematy:
- tokenizacja
- embeddings
- attention
- Transformer
- Hugging Face
- Ollama
- llama.cpp
- context window
- VRAM
- FP16 / BF16
- INT8 / INT4
- GGUF
- GPTQ
- AWQ

Projekt: **Lokalny chatbot LLM**

## Miesiąc 4 — RAG

Tematy:
- document parsing
- chunking
- embeddings
- vector database
- Qdrant
- pgvector
- semantic search
- hybrid search
- reranking
- metadata filtering
- evaluation

Projekt: **Chat with Documents**

## Miesiąc 5 — Fine-tuning

Tematy:
- SFT
- LoRA
- QLoRA
- PEFT
- dataset preparation
- evaluation
- quantization
- inference

Projekt: **Dostrojony lokalny LLM**

## Miesiąc 6 — Produkcja i MLOps

Tematy:
- Docker
- Docker Compose
- deployment
- PostgreSQL
- monitoring
- logging
- auth
- secrets
- CI/CD
- backup
- bezpieczeństwo

Projekt końcowy: **Private AI Knowledge Server**

---

# Miesiąc 1 — szczegółowo

Założenie: około 1–2 godziny dziennie.

## Pierwsze 10 dni — wersja z darmowymi lekcjami po polsku

### Dzień 1 — instalacja, venv, pierwszy program

**Tematy**
- instalacja i sprawdzenie Pythona
- `python --version`
- `pip`
- `venv`
- uruchamianie skryptów
- `print()`
- zmienne
- podstawowe typy

**Darmowa lekcja PL**
- CodeBucket — Kurs Pythona dla początkujących, rozdziały 00:00–08:33: https://www.youtube.com/watch?v=_6014HB3SMk

**Ćwiczenie**
Utwórz `day01_system_info.py`, który wypisze:
- imię użytkownika,
- system operacyjny,
- wersję Pythona,
- krótkie zdanie „Rozpoczynam naukę AI Engineer”.

**Rezultat do repo**
`month-01-python/exercises/day-01/day01_system_info.py`

---

### Dzień 2 — typy danych i operatory

**Tematy**
- `int`
- `float`
- `str`
- `bool`
- konwersje typów
- operatory matematyczne
- operatory porównania

**Darmowa lekcja PL**
- CodeBucket — ten sam kurs, rozdziały 05:09–15:02: https://www.youtube.com/watch?v=_6014HB3SMk

**Ćwiczenie**
Zbuduj prosty kalkulator pamięci modelu AI. Program przyjmuje liczbę parametrów w miliardach oraz liczbę bajtów na parametr i szacuje zapotrzebowanie pamięci w GB.

Przykład: 7B × 2 bajty ≈ 14 GB.

**Rezultat do repo**
`month-01-python/exercises/day-02/model_memory_calculator.py`

---

### Dzień 3 — listy, krotki, zbiory, słowniki

**Tematy**
- `list`
- `tuple`
- `set`
- `dict`
- indeksowanie
- slicing

**Darmowe lekcje PL**
- CodeBucket — rozdziały o listach, zbiorach, krotkach i słownikach 22:45–47:46: https://www.youtube.com/watch?v=_6014HB3SMk
- Maciej Komosiński — przegląd kolekcji Pythona: https://www.youtube.com/watch?v=y9eS0kuuxoI

**Ćwiczenie**
Utwórz słownik modeli AI z nazwą, liczbą parametrów i wymaganym VRAM. Wyświetl wszystkie modele i osobno te, które mieszczą się w zadanym limicie pamięci.

**Rezultat do repo**
`month-01-python/exercises/day-03/models_collection.py`

---

### Dzień 4 — instrukcje warunkowe

**Tematy**
- `if`
- `elif`
- `else`
- `and`
- `or`
- `not`
- porównania

**Darmowa lekcja PL**
- CodeBucket — instrukcje warunkowe, od ok. 15:02: https://www.youtube.com/watch?v=_6014HB3SMk

**Ćwiczenie**
Program ma zapytać o ilość VRAM i zaproponować klasę modelu:
- do 8 GB — mały model,
- 9–16 GB — średni model,
- 17–24 GB — duży model lokalny,
- powyżej 24 GB — większe modele / większy kontekst.

**Rezultat do repo**
`month-01-python/exercises/day-04/model_selector.py`

---

### Dzień 5 — pętle

**Tematy**
- `for`
- `while`
- `range`
- `enumerate`
- `zip`
- `break`
- `continue`

**Darmowe lekcje PL**
- CodeBucket — pętle `while` i `for`, od 19:03: https://www.youtube.com/watch?v=_6014HB3SMk
- Maciej Komosiński — pętle i kolekcje: https://www.youtube.com/watch?v=y9eS0kuuxoI

**Ćwiczenie**
Przejdź po liście modeli AI i wypisz numer, nazwę i liczbę parametrów. Następnie policz, ile modeli spełnia zadane kryterium VRAM.

**Rezultat do repo**
`month-01-python/exercises/day-05/model_loops.py`

---

### Dzień 6 — funkcje

**Tematy**
- `def`
- argumenty
- `return`
- argumenty domyślne
- `*args`
- `**kwargs`

**Darmowa lekcja PL**
- CodeBucket — funkcje, `*args`, `**kwargs`, `return`, od 1:03:10: https://www.youtube.com/watch?v=_6014HB3SMk

**Ćwiczenie**
Napisz funkcje:
- `memory_fp16(params_b)`
- `memory_int8(params_b)`
- `memory_int4(params_b)`

Każda ma zwracać przybliżone zapotrzebowanie pamięci dla modelu o podanej liczbie parametrów.

**Rezultat do repo**
`month-01-python/exercises/day-06/model_memory_functions.py`

---

### Dzień 7 — mini projekt: Text Analyzer CLI

**Tematy**
- powtórka dni 1–6
- łączenie funkcji, pętli, słowników i stringów

**Darmowa lekcja PL**
- CodeBucket — operacje na stringach 47:46–1:03:10 oraz funkcje od 1:03:10: https://www.youtube.com/watch?v=_6014HB3SMk

**Mini projekt**
Program pobiera tekst i zwraca:
- liczbę znaków,
- liczbę słów,
- liczbę zdań,
- pięć najczęstszych słów.

**Rezultat do repo**
`month-01-python/exercises/day-07/text_analyzer.py`

---

### Dzień 8 — moduły, import i pakiety

**Tematy**
- `import`
- własne moduły
- pakiety
- `pip`
- `if __name__ == "__main__"`

**Darmowa lekcja PL**
- CodeBucket — Moduły i Pakiety w Pythonie, pełny kurs: https://www.youtube.com/watch?v=dlm9x0h35bc

**Ćwiczenie**
Podziel Text Analyzer z dnia 7 na dwa pliki:
- `analyzer.py` — funkcje analityczne,
- `main.py` — uruchomienie programu.

**Rezultat do repo**
`month-01-python/exercises/day-08/`

---

### Dzień 9 — OOP: klasy i obiekty

**Tematy**
- `class`
- `__init__`
- obiekt
- atrybuty
- metody
- podstawy dziedziczenia

**Darmowa lekcja PL**
- CodeBucket — Programowanie Obiektowe w Pythonie, pełny kurs: https://www.youtube.com/watch?v=GlRvUX9nCPM

**Ćwiczenie**
Zbuduj klasę `AIModel` z polami:
- `name`
- `parameters_b`
- `quantization`
- `vram_required`

i metodą `describe()`.

**Rezultat do repo**
`month-01-python/exercises/day-09/ai_model.py`

---

### Dzień 10 — type hints i dataclasses

**Tematy**
- adnotacje typów
- `str`, `int`, `float`, `bool`
- `list[str]`
- `dict[str, int]`
- `Optional`
- `@dataclass`

**Materiały**
- Powtórka OOP z dnia 9: https://www.youtube.com/watch?v=GlRvUX9nCPM
- Oficjalna dokumentacja Python — `dataclasses`: https://docs.python.org/3/library/dataclasses.html
- Oficjalna dokumentacja Python — `typing`: https://docs.python.org/3/library/typing.html

**Ćwiczenie**
Przerób klasę `AIModel` z dnia 9 na `@dataclass` i dodaj type hints do wszystkich pól oraz metod.

**Rezultat do repo**
`month-01-python/exercises/day-10/ai_model_dataclass.py`

---

## Dni 11–30 — zakres dalszy

### Dzień 11
- pliki TXT
- `open`
- `with`
- encoding

### Dzień 12
- JSON
- `json.load`
- `json.dump`
- serializacja

### Dzień 13
- wyjątki
- `try`
- `except`
- `finally`
- własne wyjątki

### Dzień 14
Mini projekt: **CSV Analyzer**

Funkcje:
- odczyt CSV
- liczba rekordów
- średnie
- min/max
- brakujące dane

### Dzień 15
- NumPy
- `ndarray`
- `shape`
- `dtype`
- operacje wektorowe

### Dzień 16
- Pandas
- `Series`
- `DataFrame`
- `read_csv`
- `head`
- `describe`

### Dzień 17
- filtrowanie
- sortowanie
- `groupby`
- missing values

### Dzień 18
- HTTP
- GET
- POST
- PUT
- DELETE
- status codes
- JSON API

### Dzień 19
- FastAPI
- pierwszy endpoint
- uvicorn
- Swagger UI

### Dzień 20
- Pydantic
- `BaseModel`
- walidacja danych
- request body

### Dzień 21
- upload plików
- obsługa błędów
- status codes

### Dzień 22
- logging
- konfiguracja logów
- poziomy logowania

### Dzień 23
- pytest
- `assert`
- testy funkcji
- fixtures

### Dzień 24
- testowanie FastAPI
- `TestClient`
- test endpointów

### Dzień 25
- Git
- `git init`
- `git add`
- `git commit`
- `git status`
- `git log`

### Dzień 26
- branch
- merge
- konflikty
- pull request

### Dzień 27
- Docker
- Dockerfile
- image
- container
- `docker build`
- `docker run`

### Dzień 28
- Docker Compose
- environment variables
- `.env`

### Dzień 29
Składanie projektu końcowego: **Document Analyzer API**

Funkcje:
- upload TXT / CSV / JSON
- analiza dokumentu
- statystyki
- walidacja
- API REST
- testy
- logowanie
- Docker

### Dzień 30

Egzamin praktyczny. Bez kopiowania gotowego rozwiązania zbudować małe API, które:

1. przyjmuje plik,
2. analizuje jego zawartość,
3. zwraca wynik w JSON,
4. obsługuje błędy,
5. posiada test,
6. działa w Dockerze.

---

# Zasady pracy

Każdego dnia:
- 20–40 min materiału,
- 40–80 min kodowania,
- ćwiczenie zapisane w repo,
- commit po zakończeniu dnia.

Po wykonaniu dnia zmieniamy status z `- [ ]` na `- [x]`.

---

# Status

## Miesiąc 1

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
