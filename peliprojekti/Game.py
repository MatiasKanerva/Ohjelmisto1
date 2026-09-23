import random

class Item:
    def __init__(self, Obj:str, Paino:float, Määrä:int):
        self.Obj = Obj
        self.Paino = Paino
        self.Määrä = Määrä

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

    def Save(self):
        Nimet = [esine.Obj for esine in self.Invi]
        TallennusData = (
            f"Name: {self.Nimi}\n"
            f"Location: {self.Sijainti.Nimi}\n"
            f"Inventory: {', '.join(Nimet)}")
                
        with open("peliprojekti/Save.txt", "w") as Admin:
            Admin.write(TallennusData)
        return

    def Continue(self):
        with open("peliprojekti/Save.txt", "r") as Admin:
            Rivit = Admin.readlines()

        self.Nimi = Rivit[0].strip().split(": ")[1]
        Sij = Rivit[1].strip().split(": ")[1]
        if "Bedroom" in Sij:
            self.Sijainti = Makuuhuone
        elif "Window" in Sij:
            self.Sijainti = Ikkuna
        elif "Front Door" in Sij:
            self.Sijainti = Etupiha
        else:
            self.Sijainti = Makuuhuone

        self.Invi = []
        Esineet = {"Bird": Lintu,
            "Glass shard": Lasi,
            "Flower": Kukka,
            "Rock": Kivi,
            "Bug": Bug}

        Invi = Rivit[2].strip().split(": ")
        if len(Invi) > 1 and Invi[1]:
            Esine = Invi[1].split(", ")
            for ENimi in Esine:
                if ENimi in Esineet:
                    InviE = Esineet[ENimi]
                    self.Invi.append(InviE)
                    if InviE.Määrä > 0:
                        InviE.Määrä -= 1

        print(f"Loaded {self.Nimi} at {self.Sijainti}")
        self.NäytäInventaario()
        self.Liiku()

    def Liiku(self):

        def Shutdown(): 
            self.Save()
            print(f"Goodbye, {self.Nimi}!")
            exit()
            return

        while True:
            if self.Sijainti == Aloitus:
                Input = input("1. New game\n"
                              "2. Continue\n"
                              "3. Quit\n")
                if Input == "1":
                    self.Sijainti = Makuuhuone
                if Input == "2":
                    self.Continue()
                if Input == "3":
                    Shutdown()


            elif self.Sijainti == Makuuhuone:
                Input = input(f"What would you like to do?\n"
                    "1. Sleep in your bed\n"
                    "2. Go to the window\n"
                    "3. Walk outside\n"
                    "4. Inventory\n"
                    "5. Save & Quit\n")
                
                if Input == "1":
                        print("You went to sleep...\n")
                        Painajainen()

                if Input == "2":
                    print("A bird flew at your window, breaking the glass into shards and dying \n")
                    self.Sijainti = Ikkuna

                if Input == "3":
                    print("You walked outside, you see a bunch of flowers, a heavy looking rock and a small colorful bug\n")
                    self.Sijainti = Etupiha

                if Input == "4":
                    self.NäytäInventaario()

                if Input == "5":
                    Shutdown()

            
            elif self.Sijainti == Ikkuna:
                Input = input("1. Pick up the dead bird\n"
                            "2. Pick up glass shards\n"
                            "3. Back\n")
                
                if Input == "1":
                    if Lintu.Määrä > 0:
                        self.Collect(Lintu)
                        Lintu.Määrä -= 1
                        print("*Bird* has been added to your inventory\n")
                        self.Sijainti = Makuuhuone
                    else: print("There was only one bird to pick...")

                elif Input == "2":
                    if Lasi.Määrä > 0:
                        self.Collect(Lasi)
                        Lasi.Määrä -= 1
                        print("*Glass shards* has been added to your inventory\n")
                        self.Sijainti = Makuuhuone
                    else: print("You've picked up every single shard")

                elif Input == "3":
                    self.Sijainti = Makuuhuone
                    print("You walked back to your bedroom\n")


            elif self.Sijainti == Etupiha:
                Input = input("1. Pick up flowers\n" \
                            "2. Pick up a rock\n"
                            "3. Pick up a bug\n"
                            "4. Home\n"
                            "5. Save & Quit\n")
                
                if Input == "1":
                    if Kukka.Määrä > 0:
                        self.Collect(Kukka)
                        Kukka.Määrä -= 1
                        print("*Flower* has been added to your inventory\n")
                    else: print("You couldn't find anymore Flowers since you ruined the garden")

                elif Input == "2":
                    if Kivi.Määrä > 0:
                        self.Collect(Kivi)
                        Kivi.Määrä -= 1
                        print("*Rock* has been added to your inventory\n")
                    else: print("You couldn't find any more Rocks")

                elif Input == "3":
                    if Bug.Määrä > 0:
                        self.Collect(Bug)
                        Bug.Määrä -= 1
                        print("*Bug* has been added to your inventory\n")
                    else: print("You couldn't find any more of cool bugs to pick")

                elif Input == "4":
                    self.Sijainti = Makuuhuone
                    print("You walked back inside, to your room\n")

                elif Input == "5":
                    Shutdown()

    def Collect(self, Esine: Item):
        self.Invi.append(Esine)
    
    def NäytäInventaario(self):
        print(f"Your inventory: {self.Invi}\n")

# Minipeli nukkumisesta
def Painajainen():
    print("You wake up in a nightmare, you look around your surroundings, standing in the middle of a long and dark hallway\n"
          "You hear a low growl and heavy footsteps coming from behind\n"
          "Instinctivly you start running the opposite direction where you see a glowing white door\n"
          "Throwing the dice you move forward with various speeds while the Monster is after you.\n" 
          "1 Stumble\n"
          "2,3,4 Walk\n"
          "5,6 Run")
    PelaajanMatka = 0
    Nopeus = 0
    HirvionMatka = 5

    Vuoro = input("Throw a dice: ")
    while Vuoro == "" or Vuoro != "":
        Noppa = random.randint(1,6)
        if Noppa == 1:
            Nopeus = 1
            print(f"\n You threw: {Noppa}\nYou stumbled slowly forward...")
        elif 1 < Noppa < 5:
            Nopeus = 2
            print(f"\nYou threw: {Noppa}\nYou walk forward in a quick pace")
        elif 4 < Noppa:
            Nopeus = 4
            print(f"\nYou threw: {Noppa}\nYou ran forward as fast as you could!")
        HirvionMatka -= 1
        PelaajanMatka = PelaajanMatka + Nopeus

        if PelaajanMatka >= 13:
            print("\nYou managed to escape the nightmare, you're awake in your room")
            return

        if HirvionMatka < 1:
            print("\nYou died to the Monster...")
            exit()
        Vuoro = input("Throw the dice again to proceed")

# Huoneiden luonti
Aloitus = Huone("Aloitus")
Makuuhuone = Huone("Bedroom")
Ikkuna = Huone("Window")
Etupiha = Huone("Front Door")

# Esineiden luonti
Lintu = Item("Bird", 0.7, 1)
Lasi = Item("Glass shard", 0.1, 10)
Kukka = Item("Flower", 0.1, 6)
Kivi = Item("Rock", 1, 3)
Bug = Item("Bug", 0.1, 2)

# Esineiden Siirto huoneisiin
Ikkuna.Mahd_Esine.extend([Lintu, Lasi])
Etupiha.Mahd_Esine.extend([Kukka, Kivi, Bug])

# Pelin Aloitus
with open("peliprojekti/Ohjeet.txt", "r") as OTied:
    Ohje = OTied.read()

with open("peliprojekti/Intro.txt", "r") as ITied:
    Intro = ITied.read()

print(f"{Ohje}\n{Intro}")

Nimi = input("What's your name?: ")
Ikä = input("How old are you?: ")

Player = Pelaaja(Nimi, Aloitus)

if int(Ikä) < 12:
    print("You are underaged to play this game, BANISHED!")
    exit()
else: print(f"Hello, {Nimi}!\n")
Player.Liiku()