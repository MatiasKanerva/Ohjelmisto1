import random
import Kartta
import Liikkuminen

class Pelaaja:
    def __init__(self, Nimi:str, Sijainti: Kartta.Huone):
        self.Nimi = Nimi
        self.Sijainti = Sijainti
        self.Invi: list[Kartta.Item] = []

        # Pelaajan "Health point"
        self.Järki = 100
        self.Raha = 5

    # Tämä siirtää pelaajan huoneesta huoneeseen
    def Liiku(self):
        # Kaikki huoneet Joukossa jotta ei tarvitsisi laittaa kaikkia putkeen elif muodossa
        Huoneet = {
            Kartta.Aloitus: Liikkuminen.Start,
            Kartta.Makuuhuone: Liikkuminen.Bedroom,
            Kartta.Ikkuna: Liikkuminen.Window,
            Kartta.Etupiha: Liikkuminen.Front_Door,
            Kartta.Katu: Liikkuminen.Mainroad,
            Kartta.Koulu: Liikkuminen.School,
            Kartta.Luokka: Liikkuminen.Classroom,
            Kartta.Metsä: Liikkuminen.Forest,
            Kartta.Mökki: Liikkuminen.Cabin,
            Kartta.Kuja: Liikkuminen.Alleyway,
            Kartta.Maatila: Liikkuminen.Farm,
            Kartta.KoiraTarha: Liikkuminen.Kennel
    }

        # Sijoittaa pelaajan sijainnin ja liikuttaa sen oikeaan huoneeseen listasta
        while True:
            Siirry = Huoneet.get(self.Sijainti)
            if Siirry:
                Siirry(self)


    # Etsiä sijainnista variableja, tällä hetkellä käytössä kujalla mutta voi lisätä useampia
    def Search(self, Paikka):
        Paikka = self.Sijainti
        if Paikka == Kartta.Kuja:
            Chance = random.randint(0,2)
            if Chance == 1:
                Lisä = random.randint(1,5)
                self.Raha += Lisä
                print(f"You found {Lisä}€, you now have {self.Raha}€\n")
            elif Chance == 2:
                JärkiRand = random.randint(-5,3)
                self.Järki += JärkiRand
                if JärkiRand < 0:
                    print(f"You saw something you shouldn't have. It stares right back at you. Lost {JärkiRand} Sanity\n")
                else: print(f"You found something cool, but can't take with you. {JärkiRand} Sanity\n")
            else: print("You found nothing\n")

    # Kerää Itemin Pelaajan inventaarioon
    def Collect(self, Esine: Kartta.Item):
        self.Invi.append(Esine)

    # Näyttää inventaarion
    def NäytäInventaario(self):
        print(f"Your inventory: {self.Invi}\n")
        print(f"Sanity: {self.Järki} | Money: {self.Raha}")

# Pelin Aloitus
with open("peliprojekti/Ohjeet.txt", "r") as OTied:
    Ohje = OTied.read()
with open("peliprojekti/Intro.txt", "r") as ITied:
    Intro = ITied.read()
print(f"{Ohje}\n{Intro}")

Player = Pelaaja("", Kartta.Aloitus)
Player.Liiku()
