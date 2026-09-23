import random

class Item:
    def __init__(self, Obj:str, Paino:float):
        self.Obj = Obj
        self.Paino= Paino

    def __repr__(self):
        return f"{self.Obj}: {self.Paino}kg"

class Huone:
    def __init__(self, Nimi:str):
        self.Nimi = Nimi
        self.Mahd_Esine: list[Item] = []

    def __repr__(self):
        return f"{self.Nimi}: {self.Mahd_Esine}"

class Pelaaja:
    def __init__(self, Nimi:str, Sijainti: Huone = None):
        self.Nimi = Nimi
        self.Sijainti = Sijainti
        self.Invi: list[Item] = []

    def Liiku(self):
        def ShutDown():
            print(f"Näkemiin, {self.Nimi}!")
            exit()
            return
        
        if self.Sijainti == Makuuhuone:
            Input = input(f"Mitä haluasiti tehdä?\n"
                "1. Nukkua sängyssä\n"
                "2. Katso ikkunasta\n"
                "3. Kävellä ulos\n"
                "4. Katso Inventaariosi.\n"
                "5. Lopeta\n")
            if Input == "1":
                    print("Menit nukkumaan...\n")
                    Painajainen()
            if Input == "2":
                print("Lintu lensi ikkunasta läpi ja lasi räjähti lattiallesi.\n")
                Player.Sijainti = Ikkuna
            if Input == "3":
                print("Kävelit ulos ja näet kukkia, hiekkaa ja ötökän etupihaltasi.\n")
                Player.Sijainti = Etupiha
            if Input == "4":
                Player.NäytäInventaario()
            if Input == "5":
                ShutDown()
            return self.Liiku()
        
        if self.Sijainti == Ikkuna:
            Input = input("1. Nosta lintu\n"
                        "2. Nosta lasin siru\n"
                        "3. Takaisin\n")
            if Input == "1":
                Player.Collect(Lintu)
                print("Lintu on lisätty inventaarioosi.\n")
                self.Sijainti = Makuuhuone
            if Input == "2":
                Player.Collect(Lasi)
                print("Lasin siruja ollaan lisätty inventaarioosi.\n")
                self.Sijainti = Makuuhuone
            if Input == "3":
                self.Sijainti = Makuuhuone
                print("Kävelit takaisin Makuuhuoneeseen.\n")
            return self.Liiku()

        if self.Sijainti == Etupiha:
            Input = input("1. Nosta kukkia\n" \
                        "2. Nosta kivi\n"
                        "3. Nosta ötökkä\n"
                        "4. Koti\n"
                        "5. Lopeta\n")
            if Input == "1":
                Player.Collect(Kukka)
                print("Kukka on lisätty inventaarioosi\n")
            if Input == "2":
                Player.Collect(Kivi)
                print("Kivi on lisätty inventaarioosi\n")
            if Input == "3":
                Player.Collect(Bug)
                print("Ötökkä on lisätty inventaarioosi\n")
            if Input == "4":
                self.Sijainti = Makuuhuone
                print("Kävelit takaisin Makuuhuoneeseen.\n")
            if Input == "5":
                ShutDown()
            return self.Liiku()
        return

    def Collect(self, Esine: Item):
        self.Invi.append(Esine)
        return
    
    def NäytäInventaario(self):
        print(f"Tässä on Inventiaariosi: {self.Invi}\n")
        return

# Minipeli nukkumisesta
def Painajainen():
    print("Heräät painajaisessa. Katsot ympärille ja huomaat olevana pitkässä käytävässä\n"
          "Kuulet jättiläis hirvion sinun takanasi lähestyvän kohti ja edessäsi näet hohtavan oven\n"
          "Hettämällä noppaa liikut eteenpäin. Hirviö lähestyy hölkkäys nopeudella:\n" 
          "1 Kompastut\n"
          "2,3,4 Kävelet\n"
          "5,6 Juokset")
    PelaajanMatka = 0
    Nopeus = 0
    HirvionMatka = 5

    Vuoro = input("Heitä noppaa: ")
    while Vuoro == "" or Vuoro != "":
        Noppa = random.randint(1,6)
        if Noppa == 1:
            Nopeus = 1
            print(f"\nHeitit: {Noppa}\nKompastuit! Etenet hitaasti...")
        elif 1 < Noppa < 5:
            Nopeus = 2
            print(f"\nHeitit: {Noppa}\nKävelet reippaasti eteenpäin.")
        elif 4 < Noppa:
            Nopeus = 4
            print(f"\nHeitit: {Noppa}\nJuokset täysillä kohti ovea!")
        HirvionMatka -= 1
        PelaajanMatka = PelaajanMatka + Nopeus

        if PelaajanMatka >= 13:
            print("\nPääsit painajaisesta pois ja heräät huoneessasi.")
            return

        if HirvionMatka < 1:
            print("\nPeli loppui. Kuolit hirviölle.")
            exit()
        Vuoro = input("Heitä noppaa uudelleen painamalla 1: ")

# Huoneiden luonti
Makuuhuone = Huone("Makuuhuone")
Ikkuna = Huone("Ikkuna")
Etupiha = Huone("Etupiha")

# Esineiden luonti
Lintu = Item("Lintu", 0.7)
Lasi = Item("Lasin siru", 0.1)
Kukka = Item("Kukka", 0.1)
Kivi = Item("Kivi", 1)
Bug = Item("Bug", 0.1)

# Esineiden Siirto huoneisiin
Ikkuna.Mahd_Esine.extend([Lintu, Lasi])
Etupiha.Mahd_Esine.extend([Kukka, Kivi, Bug])

# Pelin Aloitus
Nimi = input("Kerro nimesi: ")
Ikä = input("Mikä on ikäsi: ")

Player = Pelaaja(Nimi, Makuuhuone)

if int(Ikä) < 12:
    print("Olet alaikäinen peliin.")
    exit()
else: print(f"Terve, {Nimi}!\n")

Player.Liiku()