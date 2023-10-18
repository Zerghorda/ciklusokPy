def szamolas(szam1: int, szam2: int):
    if szam2 == 0:
        print("0-val akartál osztani!")
    else:
        osszeg: float = szam1 / szam2
        print(f"{szam1} / {szam2} = {osszeg:.2f}")

