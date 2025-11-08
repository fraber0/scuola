"""
2025, verifica python su stringhe, tuple, liste.
Francesco Berra - 5O
Il file è di uso pubblico.
"""

# ================================================================
# 📘 PYTHON – Librerie utili per stringhe, liste e tuple
# ================================================================

# -------------------------------
# 🔤 STRINGHE
# -------------------------------

# Il modulo "string" contiene costanti predefinite con caratteri utili.
import string
print("Alfabeto minuscolo:", string.ascii_lowercase)  # tutte le lettere a-z
print("Cifre:", string.digits)                        # '0123456789'

# Il modulo "re" serve per lavorare con espressioni regolari (pattern di testo).
import re
testo = "La mia email è esempio123@mail.com"
email = re.findall(r"\S+@\S+", testo)  # cerca parole che contengono '@'
print("Email trovate:", email)

# "textwrap" formatta testi lunghi andando a capo automaticamente.
import textwrap
paragrafo = "Python è un linguaggio di programmazione potente e semplice da imparare."
print("\nTesto formattato:")
print(textwrap.fill(paragrafo, width=30))  # va a capo ogni 30 caratteri

# "difflib" confronta stringhe e misura quanto sono simili (da 0 a 1).
import difflib
s1, s2 = "ciao", "ciau"
print("\nSomiglianza tra stringhe:", difflib.SequenceMatcher(None, s1, s2).ratio())


# -------------------------------
# 📋 LISTE
# -------------------------------

# "itertools" fornisce strumenti per combinare o iterare su liste in modo avanzato.
import itertools
numeri = [1, 2, 3]
print("\nPermutazioni di [1, 2, 3]:", list(itertools.permutations(numeri)))
# -> restituisce tutte le possibili disposizioni degli elementi

# "functools" e "operator" permettono di applicare funzioni a liste in modo funzionale.
import functools, operator
somma = functools.reduce(operator.add, numeri)
# reduce applica una funzione cumulativamente: ((((1+2)+3)))
print("Somma con reduce:", somma)

# "collections" offre strutture dati avanzate simili alle liste
import collections
conta = collections.Counter(["a", "b", "a", "c", "b", "a"])
# Conta quanti elementi uguali ci sono
print("Conteggio elementi:", conta)

# "deque" è una lista ottimizzata per aggiungere/togliere elementi da entrambi i lati
from collections import deque
coda = deque(["x", "y", "z"])
coda.append("w")
print("Coda con deque:", coda)

# "heapq" trasforma una lista in una coda di priorità (heap)
import heapq
lista = [5, 1, 3, 7, 2]
heapq.heapify(lista)  # riordina la lista per avere il minimo in testa
print("Heap minimo:", lista)
print("Minimo estratto:", heapq.heappop(lista))  # estrae il più piccolo elemento


# -------------------------------
# 🧮 TUPLE
# -------------------------------

# "namedtuple" crea tuple con nomi ai campi (invece di usare solo indici)
from collections import namedtuple
Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)
print("\nAccesso con nome:", p.x, p.y)  # invece di p[0], p[1]

# "operator.itemgetter" è utile per ordinare o estrarre elementi da tuple o liste
from operator import itemgetter
dati = [(2, "b"), (1, "a"), (3, "c")]
ordinati = sorted(dati, key=itemgetter(0))  # ordina per il primo elemento
print("Ordinati per primo elemento:", ordinati)

# "typing" permette di annotare tipi, utile per chiarezza e autocompletamento
from typing import Tuple
def coord() -> Tuple[int, int]:
    return (10, 20)
print("Tuple annotate:", coord())


# -------------------------------
# ⚙️ ALTRE LIBRERIE UTILI
# -------------------------------

# "copy" serve per fare copie di liste o tuple.
# deepcopy crea una copia completa, anche di liste annidate.
import copy
lista_originale = [[1, 2], [3, 4]]
lista_copia = copy.deepcopy(lista_originale)
lista_copia[0][0] = 99
print("\nCopia profonda (deepcopy):", lista_originale, lista_copia)

# "statistics" fornisce funzioni statistiche base su liste di numeri
import statistics
numeri = [10, 20, 30]
print("Media:", statistics.mean(numeri), "Varianza:", statistics.variance(numeri))

# ================================================================
# ✅ FINE - Mini bignami per la verifica su stringhe, liste, tuple
# ================================================================

import math

# ================================================================
# 📘 COSTANTI MATEMATICHE
# ================================================================
print("pi:", math.pi)                # 3.141592653589793
print("e:", math.e)                  # 2.718281828459045
print("tau:", math.tau)              # 6.283185307179586 (2*pi)
print("inf:", math.inf)              # infinito positivo
print("nan:", math.nan)              # Not a Number

# ================================================================
# 🔢 FUNZIONI DI BASE
# ================================================================
print("\n--- Funzioni di base ---")
print("sqrt(16):", math.sqrt(16))                    # Radice quadrata
print("pow(2, 3):", math.pow(2, 3))                  # Potenza (2³)
print("fabs(-5):", math.fabs(-5))                    # Valore assoluto float
print("factorial(5):", math.factorial(5))            # Fattoriale
print("ceil(4.3):", math.ceil(4.3))                  # Arrotonda per eccesso
print("floor(4.7):", math.floor(4.7))                # Arrotonda per difetto
print("trunc(4.7):", math.trunc(4.7))                # Tronca la parte decimale
print("remainder(7, 3):", math.remainder(7, 3))      # Resto con segno

# ================================================================
# 📈 LOGARITMI ED ESPONENZIALI
# ================================================================
print("\n--- Logaritmi ed esponenziali ---")
print("exp(1):", math.exp(1))                        # e^1
print("log(8, 2):", math.log(8, 2))                  # log in base 2
print("log10(1000):", math.log10(1000))              # log in base 10
print("log2(16):", math.log2(16))                    # log base 2
print("expm1(1):", math.expm1(1))                    # e^x - 1, più preciso per x piccoli
print("log1p(1):", math.log1p(1))                    # log(1 + x), più preciso per x piccoli

# ================================================================
# 📏 FUNZIONI TRIGONOMETRICHE
# ================================================================
print("\n--- Funzioni trigonometriche ---")
print("sin(pi/2):", math.sin(math.pi / 2))
print("cos(pi):", math.cos(math.pi))
print("tan(pi/4):", math.tan(math.pi / 4))
print("asin(1):", math.asin(1))
print("acos(0):", math.acos(0))
print("atan(1):", math.atan(1))
print("atan2(1, 1):", math.atan2(1, 1))  # atan(y/x) con controllo sul segno
print("degrees(pi):", math.degrees(math.pi))  # converte radianti → gradi
print("radians(180):", math.radians(180))    # converte gradi → radianti

# ================================================================
# 🌈 FUNZIONI IPERBOLICHE
# ================================================================
print("\n--- Funzioni iperboliche ---")
print("sinh(1):", math.sinh(1))
print("cosh(1):", math.cosh(1))
print("tanh(1):", math.tanh(1))
print("asinh(1):", math.asinh(1))
print("acosh(2):", math.acosh(2))
print("atanh(0.5):", math.atanh(0.5))

# ================================================================
# 📏 DISTANZE, ANGOLI E GEOMETRIA
# ================================================================
print("\n--- Distanze e geometria ---")
print("hypot(3, 4):", math.hypot(3, 4))           # √(3² + 4²)
print("dist([1, 2], [4, 6]):", math.dist([1, 2], [4, 6]))  # distanza euclidea
print("degrees(math.pi):", math.degrees(math.pi))  # radianti → gradi
print("radians(180):", math.radians(180))          # gradi → radianti

# ================================================================
# ⚙️ FUNZIONI DI PRECISIONE E MISCELLANEA
# ================================================================
print("\n--- Funzioni di precisione e varie ---")
print("copysign(3, -1):", math.copysign(3, -1))   # copia il segno
print("isfinite(5):", math.isfinite(5))           # è finito?
print("isinf(math.inf):", math.isinf(math.inf))   # è infinito?
print("isnan(math.nan):", math.isnan(math.nan))   # è NaN?
print("prod([1, 2, 3, 4]):", math.prod([1, 2, 3, 4]))  # prodotto di tutti gli elementi
print("comb(5, 2):", math.comb(5, 2))             # combinazioni (n su k)
print("perm(5, 2):", math.perm(5, 2))             # permutazioni (nPk)
print("gcd(12, 18):", math.gcd(12, 18))           # massimo comune divisore
print("lcm(12, 18):", math.lcm(12, 18))           # minimo comune multiplo
print("fmod(7, 3):", math.fmod(7, 3))             # resto in floating point
print("nextafter(1.0, 2.0):", math.nextafter(1.0, 2.0)) # prossimo float dopo 1 verso 2
print("ulp(1.0):", math.ulp(1.0))                 # unità di differenza del float