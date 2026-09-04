import math

def Pizza():
    PizzaHalk1, PizzaEuro1 = input("Kerro pizzan halkaisija ja hinta: ").split()
    PizzaHalk1, PizzaEuro1 = int(PizzaHalk1), float(PizzaEuro1)
    PizzaHalk2, PizzaEuro2 = input("Kerro toisen pizzan halkaisija ja hinta: ").split()
    PizzaHalk2, PizzaEuro2 = int(PizzaHalk2), float(PizzaEuro2)

    PizzaKoko1 = math.pi * PizzaHalk1**2 / 4
    PizzaHinta1 = round(PizzaKoko1 / PizzaEuro1, 1)

    PizzaKoko2 = math.pi * PizzaHalk2**2 / 4
    PizzaHinta2 = round(PizzaKoko2 / PizzaEuro2, 1)

    if PizzaHinta1 < PizzaHinta2:
        print(f"Pizza 1 on halvempi ja maksaa {PizzaHinta1}€")
    else: print(f"Pizza 2 on halvempi ja maksaa {PizzaHinta2}€")

Pizza()