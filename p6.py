kedvencek = {
    "Zsófi": "matek",
    "Peti": "töri",
    "Lili": "biológia"
}

nev = input("Adj meg egy tanuló nevét: ")

if nev in kedvencek:
    print(f"{nev} kedvenc tantárgya: {kedvencek[nev]}")
else:
    print("Nincs ilyen tanuló!")