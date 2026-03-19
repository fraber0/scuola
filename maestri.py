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




# =============================================================================
#  GUIDA COMPLETA PYTHON - GESTIONE ERRORI E FILE
#  Tutto quello che ti serve per la verifica
# =============================================================================


# =============================================================================
# 1. GESTIONE DEGLI ERRORI (Exceptions)
# =============================================================================
# Quando Python incontra un errore, "lancia" (raise) un'eccezione.
# Se non viene gestita, il programma si blocca.
# Con try/except possiamo gestire gli errori e continuare l'esecuzione.

# --- Errori più comuni ---
# TypeError        -> operazione su tipo sbagliato  ("ciao" + 5)
# ValueError       -> valore non valido             (int("abc"))
# ZeroDivisionError-> divisione per zero            (10 / 0)
# IndexError       -> indice fuori range            ([1,2,3][10])
# KeyError         -> chiave non presente           ({"a":1}["b"])
# FileNotFoundError-> file non trovato              (open("x.txt"))
# AttributeError   -> attributo/metodo non esiste  ("ciao".vola())
# NameError        -> variabile non definita        (print(x))
# ImportError      -> modulo non trovato            (import pippo)
# RecursionError   -> troppe chiamate ricorsive


# --- Struttura base: try / except ---
try:
    risultato = 10 / 0          # questa riga lancia ZeroDivisionError
    print(risultato)            # questa non viene eseguita
except ZeroDivisionError:
    print("Errore: divisione per zero!")

# --- Catturare più eccezioni ---

# Modo 1: except separati (consigliato, gestione diversa per ogni errore)
try:
    numero = int("abc")
except ValueError:
    print("Errore: il valore non è un numero")
except TypeError:
    print("Errore: tipo non valido")

# Modo 2: più eccezioni in un unico except
try:
    numero = int("abc")
except (ValueError, TypeError):
    print("Errore di valore o di tipo")

# --- Catturare qualsiasi eccezione ---
try:
    x = 1 / 0
except Exception as e:          # 'e' contiene il messaggio di errore
    print(f"Errore generico: {e}")

# --- Accedere al messaggio di errore ---
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError as e:
    print(f"Tipo errore: {type(e).__name__}")  # IndexError
    print(f"Messaggio:   {e}")                 # list index out of range

# --- else: eseguito solo se NON ci sono stati errori ---
try:
    numero = int("42")
except ValueError:
    print("Non è un numero valido")
else:
    print(f"Conversione riuscita: {numero}")   # viene eseguito

# --- finally: eseguito SEMPRE, con o senza errori ---
# Usato tipicamente per chiudere file, connessioni, ecc.
try:
    risultato = 10 / 2
except ZeroDivisionError:
    print("Divisione per zero")
finally:
    print("Questo viene eseguito sempre")      # viene sempre stampato

# --- Struttura completa ---
try:
    valore = int(input("Inserisci un numero: "))
    risultato = 100 / valore
except ValueError:
    print("Devi inserire un numero intero!")
except ZeroDivisionError:
    print("Non puoi dividere per zero!")
except Exception as e:
    print(f"Errore imprevisto: {e}")
else:
    print(f"Risultato: {risultato}")
finally:
    print("Operazione terminata")

# --- Lanciare un'eccezione manualmente: raise ---
def dividi(a, b):
    if b == 0:
        raise ValueError("Il divisore non può essere zero")
    return a / b

try:
    print(dividi(10, 0))
except ValueError as e:
    print(f"Errore: {e}")

# --- raise senza argomenti: rilancia l'eccezione corrente ---
try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Gestito internamente, ma rilanciato")
        raise                   # rilancia lo stesso errore al livello superiore
except ZeroDivisionError:
    print("Gestito esternamente")


# =============================================================================
# 2. ECCEZIONI PERSONALIZZATE (Custom Exceptions)
# =============================================================================
# Puoi creare eccezioni personalizzate ereditando dalla classe Exception.
# Utile per dare errori più significativi nella tua applicazione.

# --- Eccezione base personalizzata ---
class MioErrore(Exception):
    pass

try:
    raise MioErrore("Qualcosa è andato storto")
except MioErrore as e:
    print(f"Errore personalizzato: {e}")

# --- Eccezione con messaggio di default ---
class ErroreVotoNonValido(Exception):
    def __init__(self, voto, messaggio="Il voto deve essere tra 0 e 10"):
        self.voto = voto
        self.messaggio = messaggio
        super().__init__(self.messaggio)    # passa il messaggio alla classe padre

    def __str__(self):
        return f"{self.messaggio} (ricevuto: {self.voto})"

try:
    voto = 15
    if voto > 10 or voto < 0:
        raise ErroreVotoNonValido(voto)
except ErroreVotoNonValido as e:
    print(e)   # Il voto deve essere tra 0 e 10 (ricevuto: 15)

# --- Gerarchia di eccezioni personalizzate ---
# Utile per creare famiglie di errori correlati

class ErroreApplicazione(Exception):
    """Errore base dell'applicazione"""
    pass

class ErroreDatabase(ErroreApplicazione):
    """Errore relativo al database"""
    pass

class ErroreConnessione(ErroreDatabase):
    """Errore di connessione al database"""
    pass

class ErroreAutenticazione(ErroreApplicazione):
    """Errore di autenticazione"""
    def __init__(self, utente):
        self.utente = utente
        super().__init__(f"Autenticazione fallita per l'utente: {utente}")

# Posso catturare il genitore per gestire tutti gli errori figli
try:
    raise ErroreConnessione("Impossibile connettersi al database")
except ErroreApplicazione as e:       # cattura anche ErroreDatabase ed ErroreConnessione
    print(f"Errore nell'app: {e}")

try:
    raise ErroreAutenticazione("mario_rossi")
except ErroreAutenticazione as e:
    print(e)                          # Autenticazione fallita per l'utente: mario_rossi
    print(f"Utente: {e.utente}")      # mario_rossi

# --- assert: verifica una condizione, lancia AssertionError se falsa ---
# Usato per controllare condizioni che "devono" essere vere
def calcola_media(voti):
    assert len(voti) > 0, "La lista dei voti non può essere vuota"
    return sum(voti) / len(voti)

try:
    print(calcola_media([]))
except AssertionError as e:
    print(f"Assertion fallita: {e}")


# =============================================================================
# 3. LETTURA E SCRITTURA DI FILE
# =============================================================================
# Per aprire un file si usa open().
# È sempre buona pratica usare 'with' che chiude il file automaticamente.

# --- Modalità di apertura ---
# "r"  -> read       - lettura (default), errore se il file non esiste
# "w"  -> write      - scrittura, SOVRASCRIVE il file se esiste, lo crea se no
# "a"  -> append     - aggiunge in fondo, lo crea se non esiste
# "x"  -> exclusive  - crea il file, errore se esiste già
# "r+" -> read+write - lettura e scrittura, il file deve esistere
# "b"  -> binary     - modalità binaria (es. "rb", "wb") per immagini, ecc.

# =============================================================================
# 3.1 SCRITTURA DI FILE
# =============================================================================

# --- Scrittura base con write() ---
with open("esempio.txt", "w") as file:
    file.write("Prima riga\n")         # \n va a capo manualmente
    file.write("Seconda riga\n")
    file.write("Terza riga\n")
# Il file viene chiuso automaticamente all'uscita dal blocco with

# --- Scrittura con writelines() ---
# Scrive una lista di stringhe (devi aggiungere \n manualmente)
righe = ["Prima riga\n", "Seconda riga\n", "Terza riga\n"]
with open("esempio.txt", "w") as file:
    file.writelines(righe)

# --- Aggiungere in fondo con append ---
with open("esempio.txt", "a") as file:
    file.write("Quarta riga aggiunta dopo\n")

# --- Scrittura con print() su file ---
with open("esempio.txt", "w") as file:
    print("Prima riga", file=file)     # print gestisce \n automaticamente
    print("Seconda riga", file=file)

# =============================================================================
# 3.2 LETTURA DI FILE
# =============================================================================

# --- Leggere tutto il file in una stringa con read() ---
with open("esempio.txt", "r") as file:
    contenuto = file.read()
print(contenuto)

# --- Leggere tutte le righe in una lista con readlines() ---
with open("esempio.txt", "r") as file:
    righe = file.readlines()           # ['Prima riga\n', 'Seconda riga\n', ...]
print(righe)

# Rimuovere il \n finale da ogni riga
righe_pulite = [riga.strip() for riga in righe]
print(righe_pulite)                    # ['Prima riga', 'Seconda riga', ...]

# --- Leggere una riga alla volta con readline() ---
with open("esempio.txt", "r") as file:
    riga = file.readline()             # legge solo la prima riga
    print(riga)

# --- Iterare riga per riga (modo più efficiente per file grandi) ---
with open("esempio.txt", "r") as file:
    for riga in file:
        print(riga.strip())            # strip() rimuove \n e spazi

# --- Gestire il caso in cui il file non esiste ---
try:
    with open("file_inesistente.txt", "r") as file:
        contenuto = file.read()
except FileNotFoundError:
    print("Il file non esiste!")

# =============================================================================
# 3.3 LETTURA E SCRITTURA DI FILE CSV
# =============================================================================
import csv

# --- Scrittura CSV ---
studenti = [
    ["Nome", "Cognome", "Voto"],
    ["Mario", "Rossi", 8],
    ["Luca", "Bianchi", 7],
    ["Anna", "Verdi", 9],
]

with open("studenti.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(studenti)         # scrive tutte le righe

# Scrittura con dizionari
studenti_dict = [
    {"nome": "Mario", "voto": 8},
    {"nome": "Luca",  "voto": 7},
]
with open("studenti_dict.csv", "w", newline="") as file:
    campi = ["nome", "voto"]
    writer = csv.DictWriter(file, fieldnames=campi)
    writer.writeheader()               # scrive la riga di intestazione
    writer.writerows(studenti_dict)

# --- Lettura CSV ---
with open("studenti.csv", "r") as file:
    reader = csv.reader(file)
    for riga in reader:
        print(riga)                    # ogni riga è una lista

# Lettura con dizionari (usa la prima riga come intestazione)
with open("studenti_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for riga in reader:
        print(riga["nome"], riga["voto"])

# =============================================================================
# 3.4 LETTURA E SCRITTURA DI FILE JSON
# =============================================================================
import json

# --- Scrittura JSON ---
dati = {
    "nome": "Mario",
    "età": 30,
    "hobby": ["calcio", "lettura"],
    "attivo": True
}

with open("dati.json", "w") as file:
    json.dump(dati, file, indent=4)    # indent=4 per formattazione leggibile

# --- Lettura JSON ---
with open("dati.json", "r") as file:
    dati_letti = json.load(file)
print(dati_letti["nome"])             # Mario
print(dati_letti["hobby"])            # ['calcio', 'lettura']

# --- Conversione stringa <-> JSON (senza file) ---
stringa_json = json.dumps(dati)       # dizionario -> stringa JSON
dizionario   = json.loads(stringa_json)  # stringa JSON -> dizionario

# =============================================================================
# 3.5 FORMATTAZIONE DELL'OUTPUT SU FILE E A SCHERMO
# =============================================================================

# --- Formattazione con f-string (già vista nelle stringhe) ---
nome = "Mario"
voto = 8.5
print(f"Studente: {nome}, Voto: {voto}")

# --- Formattazione numeri ---
pi = 3.14159265358979

print(f"{pi:.2f}")        # 3.14     (2 decimali)
print(f"{pi:.4f}")        # 3.1416   (4 decimali)
print(f"{pi:10.2f}")      # "      3.14" (larghezza 10, 2 decimali)
print(f"{pi:<10.2f}")     # "3.14      " (allineato a sinistra)
print(f"{pi:>10.2f}")     # "      3.14" (allineato a destra)
print(f"{pi:^10.2f}")     # "   3.14   " (centrato)

numero = 1000000
print(f"{numero:,}")      # 1,000,000  (separatore migliaia)
print(f"{numero:_}")      # 1_000_000  (separatore con underscore)

# --- Formattazione interi ---
n = 42
print(f"{n:05d}")         # 00042   (padding con zeri, larghezza 5)
print(f"{n:b}")           # 101010  (binario)
print(f"{n:o}")           # 52      (ottale)
print(f"{n:x}")           # 2a      (esadecimale minuscolo)
print(f"{n:X}")           # 2A      (esadecimale maiuscolo)

# --- Tabelle formattate ---
print(f"{'Nome':<10} {'Voto':>5} {'Media':>8}")
print("-" * 25)
print(f"{'Mario':<10} {8:>5} {8.33:>8.2f}")
print(f"{'Luca':<10} {7:>5} {7.67:>8.2f}")
print(f"{'Anna':<10} {9:>5} {9.00:>8.2f}")

# Output:
# Nome        Voto    Media
# -------------------------
# Mario          8     8.33
# Luca           7     7.67
# Anna           9     9.00

# --- Scrivere output formattato su file ---
studenti = [("Mario", 8, 8.33), ("Luca", 7, 7.67), ("Anna", 9, 9.00)]

with open("report.txt", "w") as file:
    file.write(f"{'Nome':<10} {'Voto':>5} {'Media':>8}\n")
    file.write("-" * 25 + "\n")
    for nome, voto, media in studenti:
        file.write(f"{nome:<10} {voto:>5} {media:>8.2f}\n")

# =============================================================================
# 3.6 LAVORARE CON I PERCORSI - modulo os e pathlib
# =============================================================================
import os

# Percorso corrente
print(os.getcwd())                         # /home/utente/Desktop/...

# Verificare se un file/cartella esiste
print(os.path.exists("esempio.txt"))       # True o False
print(os.path.isfile("esempio.txt"))       # True se è un file
print(os.path.isdir("cartella"))           # True se è una cartella

# Costruire percorsi in modo sicuro (funziona su tutti i sistemi operativi)
percorso = os.path.join("cartella", "sottocartella", "file.txt")
print(percorso)   # cartella/sottocartella/file.txt (su Mac/Linux)

# Informazioni sul file
print(os.path.basename("/cartella/file.txt"))  # file.txt
print(os.path.dirname("/cartella/file.txt"))   # /cartella
print(os.path.splitext("file.txt"))            # ('file', '.txt')

# Creare/eliminare cartelle
os.makedirs("nuova_cartella", exist_ok=True)   # crea cartella (exist_ok evita errore se esiste)
os.rmdir("nuova_cartella")                     # elimina cartella vuota

# Listare file in una cartella
for file in os.listdir("."):
    print(file)

# --- pathlib (modo moderno, da Python 3.4+) ---
from pathlib import Path

p = Path("esempio.txt")
print(p.exists())           # True/False
print(p.stem)               # "esempio" (nome senza estensione)
print(p.suffix)             # ".txt"
print(p.parent)             # cartella padre

# Leggere e scrivere con pathlib
testo = p.read_text()                          # legge tutto il file
p.write_text("nuovo contenuto")               # sovrascrive il file

# =============================================================================
# RIEPILOGO
# =============================================================================

# try/except/else/finally  -> gestione errori
# raise                    -> lancia un'eccezione
# class MioErrore(Exception) -> eccezione personalizzata

# open("file", "r")  -> lettura
# open("file", "w")  -> scrittura (sovrascrive)
# open("file", "a")  -> aggiunta in fondo

# file.read()        -> tutto il file in una stringa
# file.readlines()   -> tutte le righe in una lista
# file.readline()    -> una riga alla volta
# file.write()       -> scrive una stringa
# file.writelines()  -> scrive una lista di stringhe

# json.dump/load     -> scrittura/lettura JSON su file
# json.dumps/loads   -> conversione JSON <-> stringa
# csv.writer/reader  -> scrittura/lettura CSV

