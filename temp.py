messaggio = "oggi ho giocato alla play fino a tardi e poi sono uscito tardi"
parole_bannate = {"tardi", "play"}
l = messaggio.split()
for p in l:
    if p in parole_bannate:
        l.remove(p)

print(" ".join(l))