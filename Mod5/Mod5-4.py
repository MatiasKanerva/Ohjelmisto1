import random

Valittuluku = random.randint(1,10)
Arvaus = int(input("Arvaa mitä lukua ajattelen: "))

while Arvaus != Valittuluku:
    if Arvaus > Valittuluku:
        Arvaus = int(input("Luku on liian iso, arvaa uudelleen: "))
    if Arvaus < Valittuluku:
            Arvaus = int(input("Luku on liian pieni, arvaa uudelleen: "))
else: print(f"Hyvää työtä, Luku oli {Valittuluku}")