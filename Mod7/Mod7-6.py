import math

def Pizza(Halkasija, Hinta):
    PizzaKoko = math.pi * Halkasija**2 / 4
    PizzaHinta = round(PizzaKoko / Hinta, 1)
    Hinnat.append(PizzaHinta)
    return

Hinnat = []
for x in range(2):
    PizzaHalk, PizzaEuro = input("Kerro pizzan halkaisija ja hinta: ").split()
    PizzaHalk, PizzaEuro = int(PizzaHalk), int(PizzaEuro)
    Pizza(PizzaHalk,PizzaEuro)

if Hinnat[0] < Hinnat[1]:
    print(f"Ensimmäinen pitsa on halvempi: {Hinnat[0]}€")
else: print(f"Toinen pitsa on halvempi:  {Hinnat[1]}€")