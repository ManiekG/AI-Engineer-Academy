"""Dzień 19: pierwsze API FastAPI. Uruchom: uvicorn main:app --reload."""

from fastapi import FastAPI

app = FastAPI(title="Document Analyzer")


@app.get("/health")
def health() -> dict[str, str]:
    # TODO: dodaj status aplikacji.
    return {"status": "TODO"}
