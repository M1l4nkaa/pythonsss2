gyumolcsok = {
    "alma": 250,
    "banán": 300,
    "narancs": 400,
    "barack": 600,
    "meggy": 100,
    "körte": 150,
    "eper": 90
}

keresett = input("Írd be a kívánt gyümölcsnevet: ").lower()

if keresett in gyumolcsok:
    print(f"A(z) {keresett} ára: {gyumolcsok[keresett]} Ft")
else:
    print("Nincs ilyen gyümölcs!")