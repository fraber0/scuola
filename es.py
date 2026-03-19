# ============================================================
# ESERCIZIO 1
# ============================================================
"""
numero = input("Inserisci un numero: ")

while numero.isdigit() == False:
    print("Numero non valido.\n")
    numero = input("Inserisci un numero: ")

def somma_cifre(n):
    somma = 0
    for c in n:
        somma += int(c)

    return somma


sommaCifre = somma_cifre(numero)
print(sommaCifre)
"""

# ============================================================
# ESERCIZIO 1.1
# ============================================================
"""
numero = input("Inserisci un numero: ")

while numero.isdigit() == False:
    print("Numero non valido.\n")
    numero = input("Inserisci un numero: ")

def somma_cifre(n):
    somma = 0
    for c in n:
        somma += int(c)

    return str(somma)


while len(numero) > 1:
    numero = somma_cifre(numero)
    print(numero)
"""

# ============================================================
# ESERCIZIO 2
# ============================================================
"""
tupla_numeri = tuple(map(int, input("Inserisci 6 numeri separati da spazi: ").split()))

numeri = []

for i in range(6):
    n = int(input(f"Inserisci il numero {i+1}: "))
    numeri.append(n) 

tupla_numeri = tuple(numeri)

massimo = max(tupla_numeri)
minimo = min(tupla_numeri)
media = sum(tupla_numeri) / len(tupla_numeri)

numeri_maggiori_della_media = []

for n in tupla_numeri:
    if n > media:
        numeri_maggiori_della_media.append(n)

print("\nTupla originale:", tupla_numeri)
print("Valore massimo:", massimo)
print("Valore minimo:", minimo)
print("Media:", media)
print("Valori maggiori della media:", numeri_maggiori_della_media)
"""

# ============================================================
# ESERCIZIO 3
# ============================================================
"""
stringa = input("Inserisci una stringa: ")
nuova_stringa = ""
vocali = "aAeEiIoOuU"

for c in stringa:
    if c not in vocali:
        nuova_stringa += c

print("Stringa originale: ", stringa)
print("Nuova stringa: ", nuova_stringa)
"""

# ============================================================
# ESERCIZIO 4
# ============================================================
"""
def estrai_colonna(matrice, j, n):
    colonna = []
    for i in range(int(n)):
        colonna.append(matrice[i][j])
    return colonna

n = input("Inserire la dimensione della matrice NxN: ")
while n.isdigit == False and int(n) <= 0:
    print("Numero non valido.")
    n = input("Inserire la dimensione della matrice NxN: ")

matrice = []

for i in range(int(n)):
    riga = []
    for j in range(int(n)):
        val = int(input(f"Inserisci l'elemento [{i},{j}]: "))
        riga.append(val)
    matrice.append(riga)

j = input("Inserire il numero della colonna da estrarre: ")
while j.isdigit == False and int(j) <= 0 and int(j) >= int(n):
    print("Numero non valido.")
    j = input("Inserire il numero della colonna da estrarre: ")

print(estrai_colonna(matrice, int(j), n))
"""

# ============================================================
# ESERCIZIO 5
# ============================================================
"""
stringa = input("Inserisci una stringa: ")
vocali = "aAeEiIoOuU"
numero_vocali = 0
consonanti = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"
numero_consonanti = 0

for c in stringa:
    if c in vocali:
        numero_vocali += 1
    elif c in consonanti:
        numero_consonanti += 1

print("Numero di vocali: ", numero_vocali)
print("Numero di consonanti: ", numero_consonanti)
"""