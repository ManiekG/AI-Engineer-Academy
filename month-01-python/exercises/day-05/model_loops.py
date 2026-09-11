"""Dzień 5 — pętle.

Przejdź przez listę modeli pętlą for. Wypisz indeks i nazwę przez enumerate,
pomijaj modele wymagające ponad 12 GiB przez continue, a na końcu policz sumę
parametrów modeli, które się mieszczą. Bonus: użyj while do pytania o limit.
"""

models = [("TinyLlama", 1.1, 3), ("Mistral-7B", 7, 14), ("Phi-3", 3.8, 8)]
vram_limit_gib = 12

# TODO: for + enumerate + if + continue; wydrukuj pasujące modele i sumę parametrów.
