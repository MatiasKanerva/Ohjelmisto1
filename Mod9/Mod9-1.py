class Auto:
    def __init__(self, Rekisteritunnus, Huippunopeus):
        self.Rekisteritunnus = Rekisteritunnus
        self.Huippunopeus = Huippunopeus
        self.Nopeus = 0
        self.MatkaKuljettu = 0

Honda = Auto("ABC-123", "142 KM/H")
print(f"Rekisteritunnus: {Honda.Rekisteritunnus}\nHuippunopeus: {Honda.Huippunopeus}\nTämän hetkinen nopeus: {Honda.Nopeus} KM/H,\nKilometri mittarin lukema: {Honda.MatkaKuljettu} KM")
