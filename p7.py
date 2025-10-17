szo = input("Adj meg egy szót: ")

betuk = {}
for betu in szo:
    betuk[betu] = betuk.get(betu, 0) + 1

print(betuk)