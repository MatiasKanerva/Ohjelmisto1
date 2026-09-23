import random

class Auto:
    def __init__(self, Rekisteritunnus, Huippunopeus):
        self.Rekisteritunnus = Rekisteritunnus
        self.Huippunopeus = Huippunopeus
        self.Nopeus = 0
        self.MatkaKuljettu = 2000

    def Kiihdytä(self, Muutos):
        self.Muutos = Muutos
        self.Nopeus = self.Nopeus + Muutos
        
        if self.Nopeus > self.Huippunopeus:
            self.Nopeus = self.Huippunopeus

        if self.Nopeus < 0:
            self.Nopeus = 0

    def Kulje(self, Tuntimäärä):
        self.Tuntimäärä = Tuntimäärä
        self.MatkaKuljettu += self.Nopeus * self.Tuntimäärä

Autot = []
for i in range(1,11):
    Rekisteritunnus = f"ABC-{i}"
    Huippunopeus = random.randint(100,200)
    Autot.append(Auto(Rekisteritunnus, Huippunopeus))
    i += i

Kilpailu = True

while Kilpailu:
    for Kilpailija in Autot:
        Muutos = random.randint(-10, 15)
        Kilpailija.Kiihdytä(Muutos)
        Kilpailija.Kulje(1)
        if Kilpailija.MatkaKuljettu > 10000:
            Kilpailu = False

print(f"| {"Rekisteri":<9} | {"Huippunopeus":<12} | {"Nopeus":<10} | {"Matka (km)":<12} |\n")
for Kilpailija in Autot:
    print(f"| {Kilpailija.Rekisteritunnus:<9} | {Kilpailija.Huippunopeus:<7} km/h | {Kilpailija.Nopeus:<5} km/h | {Kilpailija.MatkaKuljettu:<9} km |")
