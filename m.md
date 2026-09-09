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

## Tydzień 1 — Python praktyczny

### Dzień 1
- instalacja i sprawdzenie Pythona
- `python --version`
- `pip`
- `venv`
- uruchamianie skryptów
- `print()`
- zmienne
- podstawowe typy

Ćwiczenie: utworzyć program wypisujący informacje o użytkowniku i systemie.

### Dzień 2
- `int`
- `float`
- `str`
- `bool`
- konwersje typów
- operatory

Ćwiczenie: kalkulator parametrów modelu AI.

### Dzień 3
- `list`
- `tuple`
- `set`
- `dict`
- indeksowanie
- slicing

Ćwiczenie: lista modeli AI z parametrami.

### Dzień 4
- `if`
- `elif`
- `else`
- operatory logiczne
- porównania

Ćwiczenie: program dobierający model na podstawie ilości VRAM.

### Dzień 5
- `for`
- `while`
- `range`
- `enumerate`
- `zip`

Ćwiczenie: analiza listy modeli i ich parametrów.

### Dzień 6
- funkcje
- argumenty
- `return`
- argumenty domyślne
- `*args`
- `**kwargs`

Ćwiczenie: funkcje liczące pamięć potrzebną na model.

### Dzień 7
- powtórka
- mini projekt

Projekt: **Text Analyzer CLI**

Funkcje:
- liczba znaków
- liczba słów
- liczba zdań
- najczęstsze słowa

---

## Tydzień 2 — Python dla danych

### Dzień 8
- moduły
- `import`
- własne moduły
- `__name__`

### Dzień 9
- OOP
- `class`
- `__init__`
- metody
- atrybuty

### Dzień 10
- dataclasses
- typing
- `Optional`
- `list[str]`
- `dict[str, int]`

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

---

## Tydzień 3 — NumPy, Pandas, REST, FastAPI

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

---

## Tydzień 4 — testy, Docker, projekt

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
- teoria
- małe ćwiczenie
- kod w repo
- commit

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
