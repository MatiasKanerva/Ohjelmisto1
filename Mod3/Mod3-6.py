import random

Koodi1 = []
Koodi2 = []

for X in range(3):
    Koodi1.append(random.randint(0,9))

for X in range(4):
    Koodi2.append(random.randint(1,6))

print("Kolminumeroinen koodisi on: ", Koodi1, "\nNelinumeroinen koodisi on: ", Koodi2)