filmek = {
    "Inception": 2010,
    "Titanic": 1997,
    "Matrix": 1999
}

film = input("Adj meg egy filmcímet: ")

if film in filmek:
    print(f"A(z) {film} {filmek[film]}-ben jelent meg.")
else:
    print("Nincs ilyen film az adatbázisban.")