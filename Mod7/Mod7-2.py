import random

def Noppa():
    Heitto = int(input("Kerro minkä sivuista noppaa heität: "))
    Luku = 0
    while Luku != Heitto:
        Luku = random.randint(1,Heitto)
        print(Luku)
    return

Noppa()