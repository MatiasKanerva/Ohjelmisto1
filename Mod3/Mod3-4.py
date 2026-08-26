import math

Eka, Toka, Kolmas = input("Kerro numerot: ").split()
Eka, Toka, Kolmas = int(Eka), int(Toka), int(Kolmas)
Summa = Eka + Toka + Kolmas
print("Summa: ", Summa,
    "\nTulo: ", Eka * Toka * Kolmas,
    "\nKeskiarvo: ", round(Summa / 3, 1))