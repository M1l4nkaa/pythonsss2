mondat = input("Adj meg egy mondatot: ")
szavak = mondat.split()

gyakorisag = {}
for szo in szavak:
    gyakorisag[szo] = gyakorisag.get(szo, 0) + 1

print(gyakorisag)
