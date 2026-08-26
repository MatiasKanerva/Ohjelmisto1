import math

Kanta, Korkeus = input("Kerro suorakulmion kanta ja korkeus: ") .split()
Kanta, Korkeus = int(Kanta), int(Korkeus)
print("Pinta-alasi on: ", Kanta * Korkeus, "\nPiirisi on: ", (Kanta * 2) + (Korkeus * 2))