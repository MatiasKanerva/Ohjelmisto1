def Lista(Kaikki: list):
    for x in Kaikki:
        if x % 2 == 0:
            Parilliset.append(x)
    return Kaikki

Parilliset = []
lista = Lista([1,2,3,4,5,6,7,8,9,10])
print(f"Kaikki luvut: {lista}\nParilliset: {Parilliset}")