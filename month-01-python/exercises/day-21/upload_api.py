"""Dzień 21: endpoint uploadu TXT z walidacją rozszerzenia i błędami HTTP."""

from fastapi import FastAPI

app = FastAPI()


@app.post("/documents")
def upload_document():
    # TODO: użyj UploadFile, HTTPException i sprawdź typ/rozszerzenie pliku.
    raise NotImplementedError
