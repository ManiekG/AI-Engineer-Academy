"""Dzień 3 — listy, krotki, zbiory i słowniki.

1. W liście models zapisz trzy nazwy modeli.
2. W krotce llama_data zapisz: nazwę, liczbę parametrów i VRAM.
3. W zbiorze supported_quantizations zapisz co najmniej trzy unikalne kwantyzacje.
4. W słowniku model_info zapisz nazwę, parametry i VRAM dla jednego modelu.
5. Wypisz pierwszy i ostatni model, fragment listy oraz wartość "vram_gib" ze słownika.
"""

models = ["TinyLlama", "Phi-3", "Mistral-7B"]
llama_data = ("Llama-3.1-8B", 8, 16)
supported_quantizations = {"FP16", "INT8", "INT4"}
model_info = {"name": "Mistral-7B", "parameters_b": 7, "vram_gib": 14}

# TODO: użyj indeksowania, slicing oraz wartości ze słownika i wypisz wyniki.
