def Calc(Lista=[]):
    summa = 0
    Luku = input("Kirjoita kokonais lukuja: ")
    while Luku != "":
        Luku = int(Luku)
        Lista.append(Luku)
        print(Lista, Luku)
        summa = summa + Luku
        Luku = input("Kirjoita kokonais lukuja: ")
    print(f"Summa on: {summa}")
    return

Calc()