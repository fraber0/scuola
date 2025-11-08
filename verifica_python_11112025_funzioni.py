"""
# ============================================================
# 🐍 LE 33 KEYWORDS DI PYTHON - spiegate con commenti
# ============================================================

# --- CONTROLLO DI FLUSSO ---
if True:  # Esegue un blocco di codice se la condizione è vera
    pass

elif False:  # "else if" – controlla un’altra condizione
    pass

else:  # Esegue questo blocco se nessuna condizione precedente è vera
    pass

for i in range(3):  # Ciclo che itera su una sequenza (es. range, lista)
    pass

while condizione:  # Ciclo che continua finché la condizione è vera
    pass

break  # Interrompe un ciclo "for" o "while" prima che finisca
continue  # Salta al prossimo giro del ciclo senza eseguire il resto del blocco

# --- FUNZIONI E CLASSI ---
def funzione():  # Definisce una funzione
    pass

return  # Restituisce un valore da una funzione

class MiaClasse:  # Definisce una classe (per creare oggetti)
    pass

# --- VARIABILI E SCOPE ---
global x  # Indica che "x" è una variabile globale
nonlocal x  # Usa una variabile di un livello esterno (nelle funzioni annidate)

# --- VALORI SPECIALI ---
True  # Valore booleano vero
False  # Valore booleano falso
None  # Indica assenza di valore o "null"

# --- GESTIONE ECCEZIONI ---
try:  # Blocco dove può verificarsi un errore
    pass
except Exception:  # Cattura l’errore e permette di gestirlo
    pass
else:  # Eseguito solo se nel blocco "try" non avvengono errori
    pass
finally:  # Eseguito sempre, con o senza errore
    pass
raise Exception("errore")  # Lancia un’eccezione manualmente
assert 2 + 2 == 4  # Verifica una condizione, altrimenti genera AssertionError

# --- OPERATORI LOGICI ---
and True  # Restituisce True solo se entrambe le condizioni sono vere
or False  # Restituisce True se almeno una condizione è vera
not True  # Inverte il valore booleano (da True a False, e viceversa)

# --- TEST DI APPARTENENZA / IDENTITÀ ---
x = [1, 2, 3]
2 in x  # Controlla se un elemento è contenuto in una sequenza
4 not in x  # Controlla se NON è contenuto

a = [1, 2]
b = a
a is b  # True se i due oggetti sono lo stesso in memoria
a is not [1, 2]  # True se sono oggetti diversi

# --- LAMBDA, PASS, DEL, WITH, YIELD ---
lambda x: x * 2  # Crea una funzione anonima (una sola espressione)
pass  # Segnaposto: indica “non fare nulla” (usato per blocchi vuoti)

del x  # Elimina una variabile o elemento da una lista/dizionario

with open("file.txt", "w") as f:  # Gestisce automaticamente risorse (es. file)
    f.write("ciao")

def gen():
    yield 1  # "yield" trasforma la funzione in un generatore (restituisce valori uno per volta)
"""