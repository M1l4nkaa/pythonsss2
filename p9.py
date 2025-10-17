diakok = {
    "Ádám": 4,
    "Éva": 5,
    "Noé": 3
}

nev = input("Adj meg egy diák nevét: ")

if nev in diakok:
    uj_jegy = int(input("Add meg az új jegyet (1-5): "))
    diakok[nev] = uj_jegy
    print("Frissített jegyek:", diakok)
else:
    print("Nincs ilyen nevű diák!")