"""Dzień 20: modele wejścia i wyjścia Pydantic dla analizy dokumentu."""

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    text: str = Field(min_length=1, description="Tekst do analizy")


class AnalysisResponse(BaseModel):
    # TODO: dodaj fields word_count i character_count.
    pass
