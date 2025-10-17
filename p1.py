szemelyek = {
    "Milán": 19,
    "Imre": 20,
    "Sanyi": 17
}

for nev, eletkor in szemelyek.items():
    print(f"{nev}: {eletkor} éves")

legidosebb = max(szemelyek, key=lambda nev: szemelyek[nev])
print(f"A legidősebb: {legidosebb}")