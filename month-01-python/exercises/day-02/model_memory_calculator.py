"""Dzień 2 — typy danych i operatory: kalkulator pamięci modelu AI.

Cel lekcji: przećwicz int, float, str, bool, int()/float(), operatory
matematyczne (+, -, *, /, **), porównania (<=, >) oraz if/else.

Zadanie główne
--------------
Napisz program, który pyta użytkownika o:
1. nazwę modelu (str), np. Llama-3.1-8B;
2. liczbę parametrów w miliardach (float), np. 8;
3. liczbę bitów na parametr (int), np. 16 dla FP16 albo 4 dla INT4;
4. dostępny VRAM w GiB (float), np. 12.

Następnie oblicz:
- liczbę parametrów: parameters_b * 1_000_000_000;
- liczbę bajtów na parametr: bits_per_parameter / 8;
- rozmiar samych wag w GiB: bytes / 1024 ** 3;
- bool fits_in_vram: czy model mieści się w dostępnym VRAM.

Na końcu wypisz czytelny raport i użyj if/else, aby powiedzieć, czy model
mieści się w pamięci. Wynik dla 8B parametrów w FP16 powinien wynosić około
14.90 GiB (bez narzutu na kontekst i runtime).

Bonus: policz o ile GiB brakuje pamięci, gdy model się nie mieści.
"""

# Krok 1: odkomentuj inputy i zamień tekst na odpowiedni typ danych.
# model_name = input("Nazwa modelu: ")
# parameters_b = float(input("Parametry modelu [B]: "))
# bits_per_parameter = int(input("Bity na parametr: "))
# available_vram_gib = float(input("Dostępny VRAM [GiB]: "))

# Krok 2: podczas testowania możesz użyć tych wartości przykładowych.
model_name = "Llama-3.1-8B"
parameters_b = 8.0
bits_per_parameter = 16
available_vram_gib = 12.0

# Krok 3: zastąp None własnymi obliczeniami.
parameter_count = None
bytes_per_parameter = None
model_size_gib = None
fits_in_vram = None

# Krok 4: wydrukuj raport. Użyj f-stringa oraz if/else.
# print(f"Model: {model_name}")
# print(f"Rozmiar wag: {model_size_gib:.2f} GiB")
# if fits_in_vram:
#     print("Model mieści się w VRAM.")
# else:
#     print("Model nie mieści się w VRAM.")
