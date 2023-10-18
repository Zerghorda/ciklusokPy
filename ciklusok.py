def szam1():
    cv: int = 1
    while cv <= 10:
        print(f"{cv}Nem fogok késni,mert lemaradni fontos informáciokrol!")
        cv += 1


def szam2():
    szam: int = int(input("Adjon meg egy 10-nél nagyobb számot!"))
    while szam < 10:
        szam: int = int(input("Adjon meg egy 10-nél nagyobb számot!"))


def fel1():
    szam: int = 1
    print("fel1")
    while szam < 10:
        print(f"{szam}", end=", ")
        szam += 1
        if szam == 10:
            print(f"{szam}", end="")


def fel2():
    szam: int = 20
    print("\nfel2")
    while szam < 30:
        if 20 < szam < 30:
            print(f"{szam}", end=", ")
            if szam == 29:
                print(f"{szam}", end="")
        szam += 1


def fel3():
    szam: int = 1
    print("\nfel3")
    while szam < 25:
        if 15 < szam < 25 and szam % 2 == 0:
            print(f"{szam}", end=", ")
            if szam == 24:
                print(f"{szam}", end="")
        szam += 1


def fel4():
    print("\nfel4")
    szam: int = 1
    while szam < 30:
        if 12 < szam < 30:
            print(f"{szam}", end=", ")
            if szam == 29:
                print(f"{szam}", end="")
        szam += 1
