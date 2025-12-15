# resituisce il tipo di una variabile
def definisci_tipo(var):
    return type(var)

#prendo in input una lista di lunghezza n
def input_lista(lista, n):
    for i in range(n):
        x = input("Inserisci un numero: ")
        while x.isdigit == False:
            print("Numero non valido.")
            x = input("Inserisci un numero: ")
        lista.append(int(x))

    return lista

# calcolare massimo, minimo e media di una sequenza
def statistiche(seq: list | tuple):
    massimo = max(seq)
    minimo = min(seq)
    media = sum(seq) / len(seq)
    return massimo, minimo, media

# creare una matrice NxN da input
def input_matrice():
    while True:
        n_str = input("Inserire la dimensione della matrice NxN: ")
        if n_str.isdigit() and int(n_str) > 0:
            n = int(n_str)
            break
        print("Numero non valido. Inserisci un intero positivo.")
    
    matrice = []
    for i in range(n):
        riga = [int(input(f"[{i},{j}]: ")) for j in range(n)]
        matrice.append(riga)
    return matrice

# calcolare la somma di una riga o colonna di una matrice
def somma_riga(matrice, riga):
    return sum(matrice[riga])

def somma_colonna(matrice, colonna):
    return sum(riga[colonna] for riga in matrice)

# trovare i numeri pari/dispari in una sequenza
def numeri_pari(seq):
    return [x for x in seq if x % 2 == 0]

def numeri_dispari(seq):
    return [x for x in seq if x % 2 != 0]

# verificare se una parola è palindroma
def palindroma(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# stampare una matrice in modo ordinato
def stampa_matrice(matrice):
    for riga in matrice:
        print(" ".join(str(x) for x in riga))

# controllo se una stringa è anagramma di un'altra
def controlla_anagramma(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

# \\ - scrive un backslash (\)
# \b - scrive uno spazio
# \n - inserisce un a capo
# \t - sposta di una tabulazione

# SOTTOSTRINGHE
# frase[:1] - sottostringa dall'inizio a 1 (escluso)
# frase[2:4] - sottostringa da 2 (incluso) a 4 (escluso)
# frase[5:] - sottostringa da 5 (incluso) alla fine

# le stringhe sono immutabili
# per modificare una stringa nella posizione x: stringa = stringa[:x] + "A" + stringa[x+1:]

# ======================================
# 🧩 MANIPOLAZIONE DELLE STRINGHE
# ======================================

s = "  Ciao mondo  "

# --- Lunghezza e conversione ---
len(s)                 # → 13: lunghezza della stringa
str(123)               # → "123": converte un numero in stringa

# --- Rimozione spazi ---
s.strip()              # → "Ciao mondo": toglie spazi all'inizio e alla fine
s.lstrip()             # → "Ciao mondo  ": toglie spazi solo a sinistra
s.rstrip()             # → "  Ciao mondo": toglie spazi solo a destra

# --- Maiuscole/minuscole ---
s.lower()              # → "  ciao mondo  "
s.upper()              # → "  CIAO MONDO  "
s.capitalize()         # → "  ciao mondo  " (solo prima lettera maiuscola)
s.title()              # → "  Ciao Mondo  " (ogni parola con iniziale maiuscola)
s.swapcase()           # → "  cIAO MONDO  "

# --- Suddivisione e unione ---
s.split()              # → ['Ciao', 'mondo']: divide in parole
s.split("o")           # → ['  Cia', ' m', 'nd', '  ']: divide su 'o'
",".join(['uno','due','tre'])  # → "uno,due,tre": unisce lista in stringa

# --- Ricerca e conteggio ---
s.find("mondo")        # → 7: posizione della sottostringa
s.rfind("o")           # → 10: ultima occorrenza
s.count("o")           # → 2: quante volte appare "o"
s.index("Ciao")        # → 2: come find(), ma errore se non trova
"mondo" in s           # → True: verifica presenza di sottostringa

# --- Sostituzione ---
s.replace("mondo", "universo")  # → "  Ciao universo  "

# --- Controllo del contenuto ---
s.isalpha()            # True se solo lettere
s.isdigit()            # True se solo numeri
s.isalnum()            # True se lettere o numeri
s.isspace()            # True se solo spazi
s.islower()            # True se tutte minuscole
s.isupper()            # True se tutte maiuscole

# --- Allineamento e formattazione ---
s.center(20, "-")      # → "----  Ciao mondo  ----"
s.ljust(20, ".")       # → "  Ciao mondo  ......."
s.rjust(20, ".")       # → ".......  Ciao mondo  "

# --- Inizio e fine ---
s.startswith("Ciao")   # True se inizia così
s.endswith("mondo")    # True se finisce così

# --- Ordinamento e inversione ---
"".join(sorted("banana"))  # → "aaabnn"
"banana"[::-1]             # → "ananab" (stringa invertita)

# --- Esempio combinato ---
s = " Ciao Python "
s.strip().lower().replace("python", "mondo")  # → "ciao mondo"

# dichiarazione tupla
tupla = ()
tupla_singola = (5,)    # ✅ tupla
non_tupla = (5)         # ❌ non è una tupla → è un int

# ======================================
# 🧱 MANIPOLAZIONE DELLE TUPLE (immutabili)
# ======================================

tupla = (5, 2, 8, 1, 3)

# Le tuple sono immutabili (non si modificano direttamente)
# Ma puoi eseguire molte operazioni di lettura:

len(tupla)             # Numero di elementi
max(tupla)             # Massimo
min(tupla)             # Minimo
sum(tupla)             # Somma (solo numeri)
tupla.count(2)         # Quante volte compare 2
tupla.index(8)         # Posizione di 8
tupla[0]               # Accesso per indice
tupla[-1]              # Ultimo elemento
tupla[1:3]             # Slice (porzione)

# Concatenazione e conversione
tupla2 = (10, 20)
tupla3 = tupla + tupla2  # Concatenazione

# Conversione lista ↔ tupla
lista = list(tupla)       # Converte tupla in lista (modificabile)
tupla = tuple(lista)      # Converte lista in tupla (fissa)

# Ordinare una tupla (crea una nuova lista ordinata)
tupla_ordinata = tuple(sorted(tupla))

# Esempio pratico:
numeri = (10, 20, 30, 40, 50)
media = sum(numeri) / len(numeri)
sopra_media = tuple(x for x in numeri if x > media)

# ======================================
# 📋 MANIPOLAZIONE DELLE LISTE (mutabili)
# ======================================

lista = [5, 2, 8, 1, 3]

# --- Aggiunta e rimozione ---
lista.append(10)       # Aggiunge un elemento in fondo
lista.insert(2, 99)    # Inserisce 99 all’indice 2
lista.remove(8)        # Rimuove la prima occorrenza di 8
lista.pop()            # Rimuove e ritorna l’ultimo elemento
lista.pop(1)           # Rimuove elemento all’indice 1
del lista[0]           # Cancella elemento all’indice 0
lista.clear()          # Svuota completamente la lista

# --- Ordinamento e inversione ---
lista = [5, 2, 8, 1, 3]
lista.sort()           # Ordina in modo crescente
lista.sort(reverse=True)  # Ordina in modo decrescente
lista.reverse()        # Inverte l’ordine
sorted(lista)          # Restituisce una NUOVA lista ordinata

# --- Informazioni e conteggio ---
len(lista)             # Lunghezza
max(lista)             # Valore massimo
min(lista)             # Valore minimo
sum(lista)             # Somma degli elementi
lista.count(2)         # Quante volte compare il 2
lista.index(3)         # Posizione del 3 nella lista

# --- Concatenazione e slicing ---
lista1 = [1, 2, 3]
lista2 = [4, 5]
lista3 = lista1 + lista2     # [1, 2, 3, 4, 5]
lista1.extend(lista2)        # Aggiunge elementi di lista2 a lista1
lista[1:3]                   # Sotto-lista (dal secondo al terzo elemento)
lista[::-1]                  # Lista invertita

# --- Copia ---
copia = lista.copy()         # Crea una copia indipendente

# --- Controllo appartenenza ---
2 in lista                   # True se 2 è nella lista
10 not in lista               # True se 10 non è nella lista

# --- Esempio pratico ---
lista = [3, 7, 2, 9]
media = sum(lista) / len(lista)
sopra_media = [x for x in lista if x > media]


# ============================================================
# GUIDA COMPLETA AI DIZIONARI IN PYTHON
# ============================================================
# In questo file trovi:
# 1) Cos'è un dizionario
# 2) Come dichiararlo
# 3) Come accedere e modificare i valori
# 4) Le funzioni/metodi più usati
# 5) Iterazione sui dizionari
# 6) Dizionari annidati
# 7) Copia e confronto
# 8) Esempi pratici
# 9) Esercizi (con suggerimenti)


# ------------------------------------------------------------
# 1) COS'È UN DIZIONARIO
# ------------------------------------------------------------
# Un dizionario (dict) è una struttura dati che associa:
# CHIAVE -> VALORE
# Le chiavi sono uniche e immutabili (stringhe, numeri, tuple).
# I valori possono essere di qualsiasi tipo.


# Esempio concettuale:
# rubrica = {
# "Mario": "3331234567",
# "Luigi": "3339876543"
# }


# ------------------------------------------------------------
# 2) COME DICHIARARE UN DIZIONARIO
# ------------------------------------------------------------


# Dizionario vuoto
vuoto = {}


# Dizionario con valori iniziali
persona = {
"nome": "Luca",
"eta": 25,
"studente": True
}


# Altro modo per creare un dizionario
persona2 = dict(nome="Anna", eta=30, studente=False)


# ------------------------------------------------------------
# 3) ACCESSO E MODIFICA DEI VALORI
# ------------------------------------------------------------


# Accesso tramite chiave
print(persona["nome"]) # Luca


# Metodo get (più sicuro)
print(persona.get("eta")) # 25
print(persona.get("altezza", 0)) # 0 (valore di default)


# Modificare un valore
persona["eta"] = 26


# Aggiungere una nuova coppia chiave-valore
persona["citta"] = "Milano"


# Eliminare una chiave
persona.pop("studente")


# Eliminare l'ultima coppia inserita (Python 3.7+)
persona.popitem()


# Eliminare tutto il dizionario
persona.clear()


# ------------------------------------------------------------
# 4) FUNZIONI E METODI PIÙ USATI
# ------------------------------------------------------------
studente = {
"nome": "Marco",
"voti": [7, 8, 6]
}


# keys() -> tutte le chiavi
print(studente.keys())


# values() -> tutti i valori
print(studente.values())


# items() -> coppie (chiave, valore)
print(studente.items())


# update() -> unisce due dizionari
extra = {"eta": 20, "corso": "Informatica"}
studente.update(extra)


# len() -> numero di coppie chiave-valore
print(len(studente))

# ------------------------------------------------------------
# 5) ITERARE SU UN DIZIONARIO
# ------------------------------------------------------------


# Iterare sulle chiavi
for chiave in studente:
print(chiave)


# Iterare sui valori
for valore in studente.values():
print(valore)


# Iterare su chiavi e valori
for chiave, valore in studente.items():
print(f"{chiave} -> {valore}")


# ------------------------------------------------------------
# 6) DIZIONARI ANNIDATI
# ------------------------------------------------------------


classe = {
"studente1": {
"nome": "Luca",
"media": 7.5
},
"studente2": {
"nome": "Anna",
"media": 8.2
}
}


# Accesso a un dizionario annidato
print(classe["studente1"]["nome"]) # Luca


# ------------------------------------------------------------
# 7) COPIA E CONFRONTO
# ------------------------------------------------------------


# Copia (ATTENZIONE: shallow copy)
a = {"x": 1, "y": 2}
b = a.copy()


# Confronto
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2) # True (ordine non conta)


# ------------------------------------------------------------
# 8) ESEMPI PRATICI
# ------------------------------------------------------------


# Conteggio delle parole in una frase
frase = "python è facile python è potente"
conteggio = {}


for parola in frase.split():
conteggio[parola] = conteggio.get(parola, 0) + 1


print(conteggio)


# Rubrica telefonica
rubrica = {}


rubrica["Mario"] = "3331234567"
rubrica["Luigi"] = "3339876543"


# ============================================================
# GUIDA COMPLETA AI SET IN PYTHON
# ============================================================
# In questo file trovi:
# 1) Cos'è un set
# 2) Come dichiararlo
# 3) Operazioni fondamentali
# 4) Metodi più usati
# 5) Operazioni matematiche tra set
# 6) Iterazione
# 7) Conversioni (lista, stringa, set)
# 8) Esempi pratici
# 9) Esercizi finali


# ------------------------------------------------------------
# 1) COS'È UN SET
# ------------------------------------------------------------
# Un set è una collezione:
# - NON ordinata
# - di elementi UNICI
# - mutabile (può cambiare nel tempo)


# I set sono molto usati per:
# - eliminare duplicati
# - confrontare gruppi di dati
# - verificare appartenenza (veloce)


# ------------------------------------------------------------
# 2) COME DICHIARARE UN SET
# ------------------------------------------------------------


# Set vuoto (ATTENZIONE: {} crea un dizionario!)
set_vuoto = set()


# Set con valori
numeri = {1, 2, 3, 3, 2}
print(numeri) # {1, 2, 3}


# Da lista a set (elimina duplicati)
lista = [1, 2, 2, 3, 4]
set_da_lista = set(lista)


# ------------------------------------------------------------
# 3) OPERAZIONI FONDAMENTALI
# ------------------------------------------------------------


# Aggiungere un elemento
numeri.add(4)


# Aggiungere più elementi
numeri.update([5, 6])


# Rimuovere un elemento (errore se non esiste)
numeri.remove(2)


# Rimuovere un elemento (nessun errore)
numeri.discard(10)


# Svuotare il set
numeri.clear()


# ------------------------------------------------------------
# 4) METODI PIÙ USATI
# ------------------------------------------------------------


A = {1, 2, 3}
B = {3, 4, 5}


# Lunghezza
print(len(A))


# Appartenenza
print(2 in A)
print(10 in A)


# Copia
C = A.copy()


# ------------------------------------------------------------
# 5) OPERAZIONI MATEMATICHE TRA SET
# ------------------------------------------------------------


# Unione
print(A | B)
print(A.union(B))


# Intersezione
print(A & B)
print(A.intersection(B))


# Differenza
print(A - B)
print(A.difference(B))


# Differenza simmetrica
print(A ^ B)
print(A.symmetric_difference(B))


# Sottoinsiemi
print({1, 2}.issubset(A))
print(A.issuperset({1, 2}))


# ------------------------------------------------------------
# 6) ITERAZIONE SU UN SET
# ------------------------------------------------------------


for elemento in A:
print(elemento)


# ------------------------------------------------------------
# 7) CONVERSIONI
# ------------------------------------------------------------


# Set -> lista
lista_da_set = list(A)


# Lista -> set
set_da_lista = set(lista)


# Stringa -> set (caratteri unici)
parola = "banana"
set_lettere = set(parola)
print(set_lettere) # {'b', 'a', 'n'}


# Set -> stringa
stringa = "".join(set_lettere)
print(stringa)


# ------------------------------------------------------------
# 8) ESEMPI PRATICI
# ------------------------------------------------------------


# Eliminare duplicati da una lista
numeri = [1, 2, 2, 3, 4, 4, 5]
unici = list(set(numeri))
print(unici)


# Elementi in comune tra due liste
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
comuni = set(l1) & set(l2)
print(comuni)