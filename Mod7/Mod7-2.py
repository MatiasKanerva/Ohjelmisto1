import random

def Noppa(Tahkot: int):
    return random.randint(1,Tahkot)

Luku = 0
Tahkoja = int(input("Kunka monta tahkoa on nopassa?: "))

while Luku != Tahkoja:
    Luku = Noppa(Tahkoja)
    print(Luku)