class Lehti:
    def __init__(self, Nimi, Kirjailija):
        self.Nimi = Nimi
        self.Kirjailija = Kirjailija

    def TulostaTiedot(self):
        print(f"Lehden nimi: {lehti.Nimi}, Päätoimittaja: {lehti.Kirjailija}")

class Kirja(Lehti):
    def __init__(self, Nimi, Kirjailija, Sivut):
        super().__init__(Nimi, Kirjailija)
        self.Sivut = Sivut

    def TulostaTiedot(self):
        super().TulostaTiedot()
        print(f"Kirjan nimi: {self.Nimi}, Kirjailija: {self.Kirjailija}, Sivuja kirjassa on {self.Sivut}")

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
kirja.TulostaTiedot()