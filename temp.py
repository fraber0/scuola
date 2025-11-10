"""
dim = input("Inserire la dimensione: ")
while dim.isdigit == False:
    print("Numero non valido.")
    dim = input("Inserire la dimensione: ")
dim = int(dim)

lista_numeri = []
lista_numeri_pari = []
sum_dispari = 0
for i in range(dim):
    x = input("Inserire un elemnto: ")
    while x.isdigit == False:
        print("Numero non valido.")
        x = input("Inserire un elemento: ")
    x = int(x)
    
    if x % 2 == 0:
        lista_numeri_pari.append(x)
    else:
        sum_dispari += x

    lista_numeri.append(x)

numeri = tuple(lista_numeri)
numeri_pari = tuple(lista_numeri_pari)

print(lista_numeri)
print(lista_numeri_pari)
print(sum_dispari)
"""

"""
frase = input("Inserisci una frase: ")
parole = list(frase.split())

def palindroma(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

parole_palindrome = []
for p in parole:
    if palindroma(p):
        parole_palindrome.append(p)

print(parole)
print(parole_palindrome)
print(len(parole_palindrome))
"""