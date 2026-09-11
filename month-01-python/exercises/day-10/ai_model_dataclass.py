"""Dzień 10: zamień AIModel na dataclass z pełnymi type hints."""

from dataclasses import dataclass


@dataclass
class AIModel:
    name: str
    parameters_b: float
    quantization: str
    vram_required: float

    def describe(self) -> str:
        # TODO
        raise NotImplementedError
