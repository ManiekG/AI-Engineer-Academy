# Plan nauki: 6 miesięcy

Zakładany rytm: 5 dni nauki i 1 dzień projektu/retrospektywy tygodniowo, po 60–120 minut dziennie.

## Miesiąc 1 — Python i inżynieria dokumentów

Python, środowiska wirtualne, Git, typy, testy, HTTP, JSON/CSV/PDF oraz projekt `document-analyzer`. Rezultat: narzędzie CLI, które pobiera tekst z dokumentu, dzieli go na fragmenty i tworzy ustrukturyzowany raport.

## Miesiąc 2 — Machine Learning i PyTorch

NumPy, pandas, wizualizacja danych, walidacja, metryki, regresja/klasyfikacja oraz podstawy PyTorch. Rezultat: powtarzalny pipeline treningu i eksperyment dla wybranego zbioru danych.

## Miesiąc 3 — LLM

Tokenizacja, okno kontekstu, prompting, structured output, function calling, agenci i ocena odpowiedzi. Rezultat: asystent wykonujący zadanie z użyciem narzędzi i walidujący wynik.

## Miesiąc 4 — RAG

Chunking, embeddingi, wektorowe wyszukiwanie, reranking, cytowania oraz ewaluacja retrievalu i odpowiedzi. Rezultat: aplikacja Q&A nad własnym zbiorem dokumentów.

## Miesiąc 5 — Fine-tuning

Projektowanie zbioru instrukcji, czyszczenie danych, SFT/LoRA, eksperymenty, bezpieczeństwo i ewaluacja. Rezultat: dostrojony model lub adapter wraz z kartą modelu.

## Miesiąc 6 — Production

FastAPI, Docker, kolejki, cache, testy integracyjne, CI/CD, tracing, metryki, koszt i bezpieczeństwo. Rezultat: wdrożona usługa AI z dokumentacją operacyjną.

# Miesiąc 1: plan na 30 dni

| Dzień | Temat | Zadanie / rezultat |
| --- | --- | --- |
| 1 | Setup | Zainstaluj Python, Git i VS Code; utwórz środowisko `venv`. |
| 2 | Terminal i Git | Przećwicz status, add, commit, log i `.gitignore`. |
| 3 | Składnia | Napisz funkcje, warunki i pętle rozwiązujące 5 krótkich zadań. |
| 4 | Kolekcje | Przetwórz listę słowników za pomocą list/dict/set comprehension. |
| 5 | Funkcje | Dodaj argumenty domyślne, `*args`, `**kwargs` i docstringi. |
| 6 | Moduły | Podziel prosty skrypt na moduły i uruchom go jako pakiet. |
| 7 | Tydzień 1 | Zrób mini-projekt: CLI liczące statystyki tekstu. |
| 8 | Typy | Dodaj type hints i uruchom statyczne sprawdzanie typów. |
| 9 | Błędy | Obsłuż wyjątki, własne błędy i czytelne komunikaty CLI. |
| 10 | Pliki | Wczytaj i zapisz UTF-8: TXT, JSON oraz CSV. |
| 11 | `pathlib` | Zbuduj rekursywny skaner katalogu dokumentów. |
| 12 | Regex | Wydobądź e-maile, daty i numery z przykładowego tekstu. |
| 13 | Testy | Napisz testy `pytest` dla parsera tekstu. |
| 14 | Tydzień 2 | Zrefaktoruj mini-projekt, dodaj testy i README. |
| 15 | OOP | Zdefiniuj dataclass reprezentujący dokument i jego metadane. |
| 16 | Iteratory | Użyj generatorów do przetwarzania dużego pliku liniami. |
| 17 | HTTP | Pobierz dane z publicznego API, obsłuż timeout i błąd odpowiedzi. |
| 18 | HTML | Wyodrębnij tekst oraz linki z lokalnej strony HTML. |
| 19 | PDF/DOCX | Zbadaj bibliotekę ekstrakcji tekstu i porównaj wyniki. |
| 20 | Logowanie | Dodaj poziomy logów i konfigurację logowania. |
| 21 | Tydzień 3 | Zaprojektuj API i strukturę projektu Document Analyzer. |
| 22 | Projekt: wejście | Zaimplementuj odkrywanie plików i walidację rozszerzeń. |
| 23 | Projekt: ekstrakcja | Dodaj ekstraktory TXT, PDF i DOCX z jednolitym interfejsem. |
| 24 | Projekt: czyszczenie | Normalizuj whitespace, nagłówki i kodowanie tekstu. |
| 25 | Projekt: chunking | Podziel tekst na fragmenty z nakładaniem kontekstu. |
| 26 | Projekt: analiza | Oblicz statystyki, słowa kluczowe i wykryte encje regex. |
| 27 | Projekt: raport | Zapisz wynik jako JSON oraz czytelny Markdown. |
| 28 | Projekt: CLI | Dodaj komendę, flagi wejścia/wyjścia i `--help`. |
| 29 | Jakość | Uzupełnij testy, formatowanie, linting i obsługę błędów. |
| 30 | Domknięcie | Zademonstruj projekt na 3 dokumentach i napisz retrospektywę. |
