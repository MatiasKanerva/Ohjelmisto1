def Calc(Numerot: list):
    summa = 0
    for x in Numerot:
        summa += x
    return summa

Tulos = Calc([3,2,3])
print(f"Summa on: {Tulos}")