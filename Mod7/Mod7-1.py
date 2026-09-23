import random

def Noppa():
    return random.randint(1,6)

Luku = 0
while Luku != 6:
    Luku = Noppa()
    print(Luku)