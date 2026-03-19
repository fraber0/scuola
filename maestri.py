# =============================================================================
#  GUIDA COMPLETA PYTHON - STRINGHE, LISTE, TUPLE, DIZIONARI, SET
#  Tutto quello che ti serve per la verifica
# =============================================================================


# =============================================================================
# 1. STRINGHE (str)
# =============================================================================
# Una stringa è una sequenza di caratteri, immutabile (non si può modificare
# direttamente). Si dichiara con apici singoli, doppi o tripli.

# --- Dichiarazione ---
nome = "Mario"
cognome = 'Rossi'
testo_lungo = """Questo è un testo
su più righe"""

# --- Accesso ai caratteri (indexing) ---
# Gli indici partono da 0
# Indici negativi partono dalla fine
s = "Python"
print(s[0])    # P  (primo carattere)
print(s[-1])   # n  (ultimo carattere)
print(s[2])    # t

# --- Slicing (sottostringa) ---
# stringa[inizio:fine:passo]  ->  fine è ESCLUSO
s = "Python"
print(s[0:3])   # Pyt  (caratteri 0, 1, 2)
print(s[2:])    # thon (dal 2 alla fine)
print(s[:4])    # Pyth (dall'inizio al 3)
print(s[::-1])  # nohtyP (stringa invertita)

# --- Lunghezza ---
print(len("ciao"))  # 4

# --- Concatenazione e ripetizione ---
a = "Hello"
b = " World"
print(a + b)    # Hello World
print(a * 3)    # HelloHelloHello

# --- Formattazione (f-string) ---
# Il modo moderno e più usato per inserire variabili nelle stringhe
nome = "Luca"
eta = 20
print(f"Mi chiamo {nome} e ho {eta} anni")
print(f"Tra 5 anni avrò {eta + 5} anni")  # si possono fare calcoli dentro {}

# --- Formattazione con .format() ---
print("Mi chiamo {} e ho {} anni".format(nome, eta))

# --- Metodi più importanti delle stringhe ---

testo = "  Ciao Mondo!  "

# Rimozione spazi
print(testo.strip())    # "Ciao Mondo!"  (rimuove spazi all'inizio e alla fine)
print(testo.lstrip())   # "Ciao Mondo!  " (solo a sinistra)
print(testo.rstrip())   # "  Ciao Mondo!" (solo a destra)

testo = "Ciao Mondo"

# Maiuscolo / minuscolo
print(testo.upper())       # CIAO MONDO
print(testo.lower())       # ciao mondo
print(testo.capitalize())  # Ciao mondo (solo prima lettera maiuscola)
print(testo.title())       # Ciao Mondo (prima lettera di ogni parola maiuscola)
print(testo.swapcase())    # cIAO mONDO (inverte maiuscole e minuscole)

# Ricerca
print(testo.find("Mondo"))     # 5  (indice dove inizia, -1 se non trovato)
print(testo.count("o"))        # 2  (quante volte appare)
print(testo.startswith("Ciao"))  # True
print(testo.endswith("Mondo"))   # True
print("Mondo" in testo)          # True (operatore in)

# Sostituzione
print(testo.replace("Mondo", "Python"))  # Ciao Python

# Divisione e unione
frase = "mela,pera,banana"
lista = frase.split(",")        # ['mela', 'pera', 'banana']
print(lista)

parole = ["uno", "due", "tre"]
print(" - ".join(parole))       # uno - due - tre

# Controlli sul contenuto
print("123".isdigit())    # True  (solo cifre)
print("abc".isalpha())    # True  (solo lettere)
print("abc123".isalnum()) # True  (lettere o cifre)
print("   ".isspace())    # True  (solo spazi)

# Allineamento e riempimento
print("ciao".center(10))        # "   ciao   "
print("ciao".ljust(10, "-"))    # "ciao------"
print("ciao".rjust(10, "-"))    # "------ciao"
print("7".zfill(4))             # "0007"


# =============================================================================
# 2. LISTE (list)
# =============================================================================
# Una lista è una sequenza ORDINATA e MUTABILE di elementi.
# Può contenere elementi di tipo diverso.
# Si dichiara con le parentesi quadre [ ]

# --- Dichiarazione ---
lista_vuota = []
numeri = [1, 2, 3, 4, 5]
mista = [1, "ciao", 3.14, True]
lista_di_liste = [[1, 2], [3, 4], [5, 6]]

# --- Accesso agli elementi (come le stringhe) ---
frutti = ["mela", "pera", "banana", "kiwi"]
print(frutti[0])    # mela
print(frutti[-1])   # kiwi
print(frutti[1:3])  # ['pera', 'banana']

# --- Modifica elementi (le liste sono mutabili!) ---
frutti[0] = "arancia"
print(frutti)  # ['arancia', 'pera', 'banana', 'kiwi']

# --- Lunghezza ---
print(len(frutti))  # 4

# --- Metodi principali ---

# Aggiunta
frutti.append("uva")         # aggiunge in fondo
frutti.insert(1, "limone")   # inserisce all'indice 1

# Rimozione
frutti.remove("pera")        # rimuove il primo elemento con quel valore
elemento = frutti.pop()      # rimuove e restituisce l'ultimo elemento
elemento = frutti.pop(0)     # rimuove e restituisce l'elemento all'indice 0
del frutti[0]                # elimina l'elemento all'indice 0
frutti.clear()               # svuota tutta la lista

# Ricerca
numeri = [3, 1, 4, 1, 5, 9, 2, 6]
print(numeri.index(4))   # 2  (indice della prima occorrenza di 4)
print(numeri.count(1))   # 2  (quante volte appare 1)
print(5 in numeri)       # True

# Ordinamento
numeri.sort()             # ordina in-place (modifica la lista originale)
print(numeri)             # [1, 1, 2, 3, 4, 5, 6, 9]

numeri.sort(reverse=True) # ordina in ordine decrescente
print(numeri)             # [9, 6, 5, 4, 3, 2, 1, 1]

numeri_originale = [3, 1, 4, 1, 5]
ordinata = sorted(numeri_originale)  # restituisce NUOVA lista, non modifica l'originale
print(numeri_originale)  # [3, 1, 4, 1, 5]  <- invariata
print(ordinata)          # [1, 1, 3, 4, 5]

numeri.reverse()  # inverte la lista in-place

# Copia
lista1 = [1, 2, 3]
lista2 = lista1.copy()   # copia corretta
lista3 = lista1          # ATTENZIONE: non è una copia, puntano alla stessa lista!

# Unione
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)        # [1, 2, 3, 4, 5, 6]
a.extend(b)         # aggiunge tutti gli elementi di b in a
print(a)            # [1, 2, 3, 4, 5, 6]

# --- List comprehension (modo compatto per creare liste) ---
quadrati = [x**2 for x in range(1, 6)]
print(quadrati)  # [1, 4, 9, 16, 25]

pari = [x for x in range(10) if x % 2 == 0]
print(pari)  # [0, 2, 4, 6, 8]

# --- Funzioni utili con le liste ---
numeri = [3, 1, 4, 1, 5, 9]
print(sum(numeri))   # 23
print(min(numeri))   # 1
print(max(numeri))   # 9

# --- Iterazione ---
frutti = ["mela", "pera", "banana"]
for frutto in frutti:
    print(frutto)

# Con indice
for i, frutto in enumerate(frutti):
    print(f"{i}: {frutto}")
# 0: mela
# 1: pera
# 2: banana


# =============================================================================
# 3. TUPLE (tuple)
# =============================================================================
# Una tupla è una sequenza ORDINATA e IMMUTABILE di elementi.
# Simile alla lista, ma non si può modificare dopo la creazione.
# Si dichiara con le parentesi tonde ( )
# Usata quando i dati non devono cambiare (coordinate, date, ecc.)

# --- Dichiarazione ---
tupla_vuota = ()
coordinate = (10, 20)
colori = ("rosso", "verde", "blu")
tupla_un_elemento = (42,)  # ATTENZIONE: la virgola è obbligatoria per tuple da 1 elemento
senza_parentesi = 1, 2, 3  # le parentesi sono opzionali

# --- Accesso (come liste e stringhe) ---
colori = ("rosso", "verde", "blu")
print(colori[0])    # rosso
print(colori[-1])   # blu
print(colori[0:2])  # ('rosso', 'verde')

# --- Le tuple sono IMMUTABILI ---
# colori[0] = "giallo"  # ERRORE! TypeError: object does not support item assignment

# --- Lunghezza ---
print(len(colori))  # 3

# --- Metodi (solo due, perché non si può modificare) ---
numeri = (1, 2, 3, 2, 4, 2)
print(numeri.count(2))   # 3  (quante volte appare 2)
print(numeri.index(3))   # 2  (indice della prima occorrenza di 3)

# --- Operatori ---
print((1, 2) + (3, 4))   # (1, 2, 3, 4)
print((1, 2) * 3)        # (1, 2, 1, 2, 1, 2)
print(3 in (1, 2, 3))    # True

# --- Unpacking (assegnazione multipla) ---
punto = (10, 20)
x, y = punto
print(x)  # 10
print(y)  # 20

a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3

# Unpacking con * (cattura il resto)
primo, *resto = (1, 2, 3, 4, 5)
print(primo)  # 1
print(resto)  # [2, 3, 4, 5]

# --- Conversione lista <-> tupla ---
lista = [1, 2, 3]
tupla = tuple(lista)   # lista -> tupla
lista2 = list(tupla)   # tupla -> lista

# --- Perché usare le tuple invece delle liste? ---
# 1. Sono più veloci
# 2. Proteggono i dati dalla modifica accidentale
# 3. Possono essere usate come chiavi dei dizionari (le liste no)


# =============================================================================
# 4. DIZIONARI (dict)
# =============================================================================
# Un dizionario è una collezione di coppie CHIAVE: VALORE.
# È MUTABILE, ORDINATO (da Python 3.7+) e non ammette chiavi duplicate.
# Si dichiara con le parentesi graffe { }
# Accesso ai valori tramite chiave, non tramite indice numerico.

# --- Dichiarazione ---
dizionario_vuoto = {}
persona = {"nome": "Mario", "età": 30, "città": "Roma"}
misto = {"id": 1, "attivo": True, "punteggi": [10, 20, 30]}

# --- Accesso ai valori ---
print(persona["nome"])         # Mario
print(persona.get("età"))      # 30
print(persona.get("email"))    # None  (non dà errore se la chiave non esiste)
print(persona.get("email", "non trovato"))  # "non trovato" (valore di default)

# ATTENZIONE: persona["email"] darebbe KeyError se la chiave non esiste!

# --- Modifica e aggiunta ---
persona["età"] = 31            # modifica un valore esistente
persona["email"] = "m@m.it"   # aggiunge una nuova coppia chiave-valore
print(persona)

# --- Rimozione ---
del persona["email"]           # elimina la chiave "email"
eta = persona.pop("età")       # rimuove e restituisce il valore
print(eta)                     # 31
persona.popitem()              # rimuove e restituisce l'ultima coppia inserita
persona.clear()                # svuota il dizionario

# --- Verifica esistenza chiave ---
persona = {"nome": "Mario", "età": 30}
print("nome" in persona)       # True
print("email" in persona)      # False

# --- Metodi principali ---
persona = {"nome": "Mario", "età": 30, "città": "Roma"}

# Viste (oggetti che riflettono il dizionario in tempo reale)
print(persona.keys())    # dict_keys(['nome', 'età', 'città'])
print(persona.values())  # dict_values(['Mario', 30, 'Roma'])
print(persona.items())   # dict_items([('nome', 'Mario'), ('età', 30), ...])

# Conversione in lista
lista_chiavi = list(persona.keys())
lista_valori = list(persona.values())

# Aggiornamento con un altro dizionario
extra = {"email": "m@m.it", "età": 31}
persona.update(extra)    # aggiunge o sovrascrive le chiavi
print(persona)

# Copia
copia = persona.copy()

# --- Iterazione ---
persona = {"nome": "Mario", "età": 30, "città": "Roma"}

# Solo chiavi
for chiave in persona:
    print(chiave)

# Solo valori
for valore in persona.values():
    print(valore)

# Chiavi e valori insieme
for chiave, valore in persona.items():
    print(f"{chiave}: {valore}")

# --- Lunghezza ---
print(len(persona))  # 3 (numero di coppie chiave-valore)

# --- Dict comprehension ---
quadrati = {x: x**2 for x in range(1, 6)}
print(quadrati)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# --- Dizionari annidati ---
studenti = {
    "Mario": {"voto": 8, "materia": "matematica"},
    "Luca":  {"voto": 7, "materia": "italiano"},
}
print(studenti["Mario"]["voto"])  # 8

# --- setdefault: aggiunge la chiave solo se non esiste ---
persona.setdefault("email", "non_disponibile")


# =============================================================================
# 5. SET (set)
# =============================================================================
# Un set è una collezione NON ORDINATA di elementi UNICI.
# È MUTABILE ma non ammette duplicati.
# Non si può accedere agli elementi tramite indice.
# Utilissimo per rimuovere duplicati e fare operazioni insiemistiche.
# Si dichiara con le parentesi graffe { } oppure con set()

# --- Dichiarazione ---
set_vuoto = set()          # ATTENZIONE: {} crea un dizionario vuoto, non un set!
numeri = {1, 2, 3, 4, 5}
lettere = {"a", "b", "c", "a", "b"}  # i duplicati vengono ignorati
print(lettere)  # {'a', 'b', 'c'}  (ordine non garantito)

# Creare un set da una lista (ottimo per rimuovere duplicati)
lista_con_duplicati = [1, 2, 2, 3, 3, 3, 4]
senza_duplicati = set(lista_con_duplicati)
print(senza_duplicati)  # {1, 2, 3, 4}

# --- Accesso ---
# Non si può accedere per indice (set["chiave"] -> ERRORE)
# Si può solo iterare o verificare la presenza
numeri = {1, 2, 3, 4, 5}
print(3 in numeri)   # True
print(6 in numeri)   # False

# --- Lunghezza ---
print(len(numeri))  # 5

# --- Metodi principali ---

# Aggiunta
numeri.add(6)         # aggiunge un elemento
print(numeri)

# Rimozione
numeri.remove(6)      # rimuove l'elemento (KeyError se non esiste)
numeri.discard(99)    # rimuove se esiste, altrimenti non fa nulla (no errore)
elemento = numeri.pop()  # rimuove e restituisce un elemento casuale
numeri.clear()        # svuota il set

# --- Operazioni insiemistiche (le più importanti!) ---
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unione: tutti gli elementi di A e B
print(A | B)            # {1, 2, 3, 4, 5, 6}
print(A.union(B))       # stesso risultato

# Intersezione: solo gli elementi in comune
print(A & B)                  # {3, 4}
print(A.intersection(B))      # stesso risultato

# Differenza: elementi in A ma NON in B
print(A - B)                  # {1, 2}
print(A.difference(B))        # stesso risultato

# Differenza simmetrica: elementi in A o B ma NON in entrambi
print(A ^ B)                           # {1, 2, 5, 6}
print(A.symmetric_difference(B))       # stesso risultato

# --- Relazioni tra insiemi ---
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {7, 8}

print(A.issubset(B))    # True  (A è sottoinsieme di B, A ⊆ B)
print(B.issuperset(A))  # True  (B contiene A, B ⊇ A)
print(A.isdisjoint(C))  # True  (A e C non hanno elementi in comune)

# --- Iterazione (l'ordine non è garantito) ---
frutti = {"mela", "pera", "banana"}
for frutto in frutti:
    print(frutto)

# --- Frozenset: set immutabile ---
# Come il set ma non si può modificare dopo la creazione
# Può essere usato come chiave di un dizionario
fs = frozenset([1, 2, 3])
# fs.add(4)  # ERRORE


# =============================================================================
# RIEPILOGO - QUANDO USARE COSA
# =============================================================================

# str   -> testo, dati testuali immutabili
# list  -> sequenza ordinata modificabile, elementi anche duplicati
# tuple -> sequenza ordinata NON modificabile, più veloce della lista
# dict  -> coppie chiave-valore, accesso rapido per chiave
# set   -> elementi unici, operazioni insiemistiche, rimozione duplicati

# =============================================================================
# CONVERSIONI TRA TIPI
# =============================================================================

lista  = [1, 2, 3, 2, 1]

in_tupla = tuple(lista)          # [1,2,3,2,1] -> (1,2,3,2,1)
in_set   = set(lista)            # [1,2,3,2,1] -> {1,2,3}
in_str   = str(lista)            # [1,2,3,2,1] -> "[1, 2, 3, 2, 1]"

tupla = (1, 2, 3)
in_lista = list(tupla)           # (1,2,3) -> [1,2,3]

s = {4, 5, 6}
in_lista2 = list(s)             # {4,5,6} -> [4,5,6]  (ordine non garantito)
in_tupla2 = tuple(s)            # {4,5,6} -> (4,5,6)
