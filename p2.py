jegyek = {
    "matek": 3,
    "magyar": 5,
    "töri": 4,
    "angol": 4,
    "tesi": 5
}

atlag = sum(jegyek.values()) / len(jegyek)
print(f"Az átlagom: {atlag:.1f}")
