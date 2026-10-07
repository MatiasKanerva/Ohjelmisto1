import random
import Kartta
import Liikkuminen

class Pelaaja:
    def __init__(self, Nimi:str, Sijainti: Kartta.Huone):
        self.Nimi = Nimi
        self.Sijainti = Sijainti
        self.Invi: list[Kartta.Item] = []
        self.Järki = 100
        self.Raha = 5

    def Liiku(self):
        while True:
            if self.Sijainti == Kartta.Aloitus:
                Liikkuminen.Start(self)

            elif self.Sijainti == Kartta.Makuuhuone:
                Liikkuminen.Bedroom(self)
            
            elif self.Sijainti == Kartta.Ikkuna:
                Liikkuminen.Window(self)

            elif self.Sijainti == Kartta.Etupiha:
                Liikkuminen.Front_Door(self)

            elif self.Sijainti == Kartta.Katu:
                Liikkuminen.Mainroad(self)

            elif self.Sijainti == Kartta.Koulu:
                Liikkuminen.School(self)

            elif self.Sijainti == Kartta.Luokka:
                Liikkuminen.Classroom(self)

            elif self.Sijainti == Kartta.Metsä:
                Liikkuminen.Forest(self)  

            elif self.Sijainti == Kartta.Mökki:
                Liikkuminen.Cabin(self)

            elif self.Sijainti == Kartta.Kuja:
                Liikkuminen.Alleyway(self)

            elif self.Sijainti == Kartta.Maatila:
                Liikkuminen.Farm(self)

            elif self.Sijainti == Kartta.KoiraTarha:
                Liikkuminen.Kennel(self)

    # Etsiä sijainnista 
    def Search(self, Paikka):
        Paikka = self.Sijainti
        if Paikka == Kartta.Kuja:
            Chance = random.randint(0,2)
            if Chance == 1:
                Lisä = random.randint(1,5)
                self.Raha += Lisä
                print(f"You found {Lisä}€, you now have {self.Raha}€\n")
            elif Chance == 2:
                JärkiC = self.Järki
                self.Järki += random.randint(-5,3)
                if JärkiC > self.Järki:
                    print(f"You saw something you shouldn't have. It stares right back at you. Lost {JärkiC} Sanity\n")
                else: print(f"You found something cool, but can't take with you. Gained {JärkiC} Sanity\n")
            else: print("You found nothing\n")

    # Kerätä Itemi Pelaajan inventaarioon
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

# Pelin alkaminen
Player = Pelaaja("", Kartta.Aloitus)

try:
    import Liikkuminen
    print("Liikkumisesta löytyvät funktiot:", [x for x in dir(Liikkuminen) if not x.startswith("__")])
except Exception as e:
    print("Virhe Liikkuminen.py lennossa:", e)
    
Player.Liiku()
