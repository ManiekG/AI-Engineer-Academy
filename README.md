# AI Engineer Academy

Praktyczna 6-miesięczna ścieżka nauki AI/LLM Engineer — od Pythona, pracy z danymi i FastAPI, przez Machine Learning, PyTorch, Transformers i RAG, po fine-tuning, Docker, deployment i MLOps.

## Główne technologie

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

## Program

| Miesiąc | Obszar | Projekt |
| --- | --- | --- |
| 01 | Python, Git, dane, API | Document Analyzer API |
| 02 | Machine Learning i PyTorch | Model klasyfikacyjny z API |
| 03 | Transformers i lokalne LLM | Lokalny chatbot LLM |
| 04 | RAG | Chat with Documents |
| 05 | Fine-tuning | Dostrojony lokalny LLM |
| 06 | Produkcja i MLOps | Private AI Knowledge Server |

Szczegółowy harmonogram i status nauki znajdują się w [`m.md`](m.md).

## Struktura repozytorium

- `month-01-python/` — Python, Git, pliki, dane, FastAPI, testy i Docker
- `month-02-ml-pytorch/` — podstawy ML i PyTorch
- `month-03-llm/` — Transformers, Hugging Face i lokalne modele
- `month-04-rag/` — embeddingi, vector DB, retrieval, reranking i evals
- `month-05-finetuning/` — SFT, LoRA, QLoRA i PEFT
- `month-06-production/` — deployment, monitoring, bezpieczeństwo i MLOps

## Sposób pracy

Zakładany rytm to około 60–120 minut dziennie. Każdy dzień kończy się małym ćwiczeniem lub fragmentem projektu oraz commitem do repozytorium. Po wykonaniu dnia jego status w `m.md` zmieniamy z `[ ]` na `[x]`.

## Cel końcowy

Zbudować kompletny **Private AI Knowledge Server**: system ingestujący dokumenty, indeksujący je, wyszukujący kontekst, generujący odpowiedzi przez LLM i działający jako wdrożona aplikacja API z testami, logowaniem i monitoringiem.
