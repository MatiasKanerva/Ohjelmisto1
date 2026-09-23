class Auto:
    def __init__(self, Rekisteritunnus, Huippunopeus):
        self.Rekisteritunnus = Rekisteritunnus
        self.Huippunopeus = Huippunopeus
        self.Nopeus = 0
        self.MatkaKuljettu = 0

    def Kiihdytä(self, Muutos):
        self.Muutos = Muutos
        self.Nopeus = self.Nopeus + Muutos
        if Muutos < 0:
            print(f"Hidastat autoa {Muutos} KM/H ja ajat nopeudella {self.Nopeus} KM/H")
        elif self.Nopeus > self.Huippunopeus:
            self.Nopeus = self.Huippunopeus
            print(f"Kiihdytit {Muutos} KM/H, mutta olet jo maksimi nopeudella {self.Huippunopeus} KM/H")
        elif self.Nopeus < 0:
            self.Nopeus = 0
            print(f"Auto pysähtyi.")
        else: print(f"Kiihdytit {Muutos} KM/H ja ajat nopeudella {self.Nopeus} KM/H")



Honda = Auto("ABC-123", 142)
print(f"Rekisteritunnus: {Honda.Rekisteritunnus}\nHuippunopeus: {Honda.Huippunopeus}\nTämän hetkinen nopeus: {Honda.Nopeus} KM/H,\nKilometri mittarin lukema: {Honda.MatkaKuljettu} KM")
Honda.Kiihdytä(30)
Honda.Kiihdytä(70)
Honda.Kiihdytä(50)
Honda.Kiihdytä(-200)
