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
        return f"{self.Nimi}"

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
        elif "Mainroad" in Sij:
            self.Sijainti = Katu
        elif "Forest" in Sij:
            self.Sijainti = Metsä
        elif "Cabin" in Sij:
            self.Sijainti = Mökki
        elif "School" in Sij:
            self.Sijainti = Koulu
        elif "Classroom" in Sij:
            self.Sijainti = Luokka
        elif "Alleyway" in Sij:
            self.Sijainti = Kuja
        elif "Farm" in Sij:
            self.Sijainti = Maatila
        elif "Kennel" in Sij:
            self.Sijainti = KoiraTarha
        else: self.Sijainti = Aloitus

        self.Invi = []
        Esineet = {"Bird": Lintu,
            "Glass shard": Lasi,
            "Flower": Kukka,
            "Rock": Kivi,
            "Bug": Bug,
            "Fly Agaric": Sieni,
            "Stick": Tikku,
            "Berry": Marja,
            "Axe": Kirves,
            "Teacher": Opettaja,
            "Rat": Rotta,
            "Bucket of Milk": Maito,
            "Shotgun": Haulikko,
            "Puppy": Pentu}

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

                    Nimi = input("What's your name?: ")
                    Ikä = input("How old are you?: ")

                    if int(Ikä) < 12:
                        print("You are underaged to play this game, BANISHED!")
                        exit()
                    else: print(f"Hello, {Nimi}!\n")

                    self.Nimi = Nimi
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
                    "4. Show Inventory\n"
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
                            "3. Walk Back\n"
                            "4. Show Inventory\n")
                
                if Input == "1":
                    if Lintu.Määrä > 0:
                        self.Collect(Lintu)
                        Lintu.Määrä -= 1
                        print(f"*{Lintu.Obj}* has been added to your Inventory\n")
                        self.Sijainti = Makuuhuone
                    else: print("There was only one bird to pick...\n")

                elif Input == "2":
                    if Lasi.Määrä > 0:
                        self.Collect(Lasi)
                        Lasi.Määrä -= 1
                        print(f"*{Lasi.Obj}* has been added to your Inventory\n")
                        self.Sijainti = Makuuhuone
                    else: print("You've picked up every single shard\n")

                elif Input == "3":
                    self.Sijainti = Makuuhuone
                    print("You walked back to your bedroom\n")

                elif Input == "4":
                    self.NäytäInventaario()


            elif self.Sijainti == Etupiha:
                Input = input("1. Pick up flowers\n" \
                            "2. Pick up a rock\n"
                            "3. Pick up bugs\n"
                            "4. Walk to Mainroad\n"
                            "5. Go Home\n"
                            "6. Show Inventory\n"
                            "7. Save & Quit\n")
                
                if Input == "1":
                    if Kukka.Määrä > 0:
                        self.Collect(Kukka)
                        Kukka.Määrä -= 1
                        print(f"*{Kukka.Obj}* has been added to your Inventory\n")
                    else: print("You couldn't find anymore Flowers since you ruined the garden\n")

                elif Input == "2":
                    if Kivi.Määrä > 0:
                        self.Collect(Kivi)
                        Kivi.Määrä -= 1
                        print(f"*{Kivi.Obj}* has been added to your Inventory\n")
                    else: print("You couldn't find any more Rocks\n")

                elif Input == "3":
                    if Bug.Määrä > 0:
                        self.Collect(Bug)
                        Bug.Määrä -= 1
                        print(f"*{Bug.Obj}* has been added to your Inventory\n")
                    else: print("You couldn't find any more of cool bugs to pick\n")

                elif Input == "4":
                    self.Sijainti = Katu
                    print("You walked to the Mainroad\n")

                elif Input == "5":
                    self.Sijainti = Makuuhuone
                    print("You walked back inside, to your room\n")

                elif Input == "6":
                    self.NäytäInventaario()

                elif Input == "7":
                    Shutdown()


            elif self.Sijainti == Katu:
                Input = input("1. Walk to School\n"
                              "2. Explore the Forest\n"
                              "3. Walk to Alleyway\n"
                              "4. Show Inventory\n")
                
                if Input == "1":
                    self.Sijainti = Koulu
                    print("You walked inside your school\n")

                elif Input == "2":
                    self.Sijainti = Metsä
                    print("You forced your way into the forest through the thick foliage\n")

                elif Input == "3":
                    self.Sijainti = Kuja
                    print("You walked into the gloomy and wet Alleywey\n")

                elif Input == "4":
                    self.NäytäInventaario()


            elif self.Sijainti == Koulu:
                Input = input("1. Find your Classroom\n"
                              "2. Walk to Mainroad\n"
                              "3. Show Inventory\n")
                
                if Input == "1":
                    self.Sijainti = Luokka
                    print("You found your way into your class\n")

                elif Input == "2":
                    self.Sijainti = Katu
                    print("You walked back to the Main road\n")

                elif Input == "3":
                    self.NäytäInventaario()


            elif self.Sijainti == Luokka:
                Input = input("1. Steal the Teacher\n"
                              "2. Get out of Class\n"
                              "3. Show Inventory\n")
                
                if Input == "1":
                    if Opettaja.Määrä > 0:
                        self.Collect(Opettaja)
                        Opettaja.Määrä -= 1
                        print(f"*{Opettaja.Obj}* has been added to your Inventory, somehow?...\n")
                    else: print("You already kidnapped a person, and you're ASKIN MORE!?!?\n")

                elif Input == "2":
                    self.Sijainti = Koulu
                    print("You walked back to the hallway\n")

                elif Input == "3":
                    self.NäytäInventaario()


            elif self.Sijainti == Metsä:
                Input = input("1. Pick up Mushrooms\n"
                              "2. Pick up Sticks\n"
                              "3. Pick up Berries\n"
                              "4. Walk to Cabin\n"
                              "5. Walk to Mainroad\n"
                              "6. Show Inventory\n")

                if Input == "1":
                    if Sieni.Määrä > 0:
                        self.Collect(Sieni)
                        Sieni.Määrä -= 1
                        print(f"*{Sieni.Obj}* has been added to your Inventory\n")
                    else: print("I think you got the whole cluster\n")

                elif Input == "2":
                    if Tikku.Määrä > 0:
                        self.Collect(Tikku)
                        Tikku.Määrä -= 1
                        print(f"*{Tikku.Obj}* has been added to your Inventory\n")
                    else: print("You took all the sticks nearby\n")

                elif Input == "3":
                    if Marja.Määrä > 0:
                        self.Collect(Marja)
                        Marja.Määrä -= 1
                        print(f"*{Marja.Obj}* has been added to your Inventory\n")
                    else: print("You got all the berries from the bush\n")

                elif Input == "4":
                    self.Sijainti = Mökki
                    print("You walk inside Cabin, it looks vintage and cozy. The fireplace is cracking with fire\n")

                elif Input == "5":
                    self.Sijainti = Katu
                    print("You walked back to Mainroad through the dense foliage again\n")

                elif Input == "6":
                    self.NäytäInventaario()


            elif self.Sijainti == Mökki:
                Input = input("1. Pick up Axe\n"
                              "2. Walk to Forest\n"
                              "3. Show Inventory\n"
                              "4. Save & Quit\n")

                if Input == "1":
                    if Kirves.Määrä > 0:
                        self.Collect(Kirves)
                        Kirves.Määrä -= 1
                        print(f"*{Kirves.Obj}* has been added to your Inventory\n")
                    else: print("I think that was the only Axe around\n")

                elif Input == "2":
                    self.Sijainti = Metsä
                    print("You walked back to the open Forest\n")

                elif Input == "3":
                    self.NäytäInventaario()

                elif Input == "4":
                    Shutdown()


            elif self.Sijainti == Kuja:
                Input = input("1. Pick up Rat\n"
                              "2. Walk to Farm\n"
                              "3. Show Inventory\n")

                if Input == "1":
                    if Rotta.Määrä > 0:
                        self.Collect(Rotta)
                        Rotta.Määrä -= 1
                        print(f"*{Rotta.Obj}* has been added to your Inventory. Don't catch a plaque though, ew\n")
                    else: print("You took the whole family. What are you gonna do with more? Colonize them?\n")

                elif Input == "2":
                    self.Sijainti = Maatila
                    print("You walked a long road heading to the Farms, I wonder what there will be?\n")

                elif Input == "3":
                    self.NäytäInventaario()


            elif self.Sijainti == Maatila:
                Input = input("1. Pick up Shotgun\n"
                              "2. Pick up Milk\n"
                              "3. Walk to Kennel\n"
                              "4. Walk to Alleyway\n"
                              "5. Show Inventory\n"
                              "6. Save & Quit\n")
                
                if Input == "1":
                    if Haulikko.Määrä > 0:
                        self.Collect(Haulikko)
                        Haulikko.Määrä -= 1
                        print(f"*{Haulikko.Obj}* has been added to your Inventory\n")
                    else: print("No. You can't dual wield them.\n")

                elif Input == "2":
                    if Maito.Määrä > 0:
                        self.Collect(Maito)
                        Maito.Määrä -= 1
                        print(f"*{Maito.Obj}* was added to your Inventory\n")
                    else: print("You don't have a third arm for another bucket")

                elif Input == "3":
                    self.Sijainti = KoiraTarha
                    print("You walk to Kennel, you can hear lots of barking and growling\n")

                elif Input == "4":
                    self.Sijainti = Kuja
                    print("You walk back the long path until you reach Alleyway\n")

                elif Input == "5":
                    self.NäytäInventaario()

                elif Input == "6":
                    Shutdown()


            elif self.Sijainti == KoiraTarha:
                Input = input("1. Pick up Puppy\n"
                              "2. Pat a Dog\n"
                              "3. Walk to Farm\n"
                              "4. Show Inventory\n")

                if Input == "1":
                    if Pentu.Määrä > 0:
                        self.Collect(Pentu)
                        Pentu.Määrä -= 1
                        print(f"{Pentu.Obj}* has been added to your Inventoryn, Cute little fucker ain't ya\n")
                    else: print("Mhehe, stole em all!\n")

                elif Input == "2":
                    print("You walk up to a dog and start petting their head, squishing their cheeks and scratching their backs\n")

                elif Input == "3":
                    self.Sijainti = Maatila
                    print("You walk back to Farm field\n")

                elif Input == "4":
                    self.NäytäInventaario()


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
Katu = Huone("Mainroad")
Metsä = Huone("Forest")
Mökki = Huone("Cabin")
Koulu = Huone("School")
Luokka = Huone("Classroom")
Kuja = Huone("Alleyway")
Maatila = Huone("Farm")
KoiraTarha = Huone("Kennel")

# Esineiden luonti
Lintu = Item("Bird", 0.7, 1)
Lasi = Item("Glass shard", 0.1, 10)
Kukka = Item("Flower", 0.1, 6)
Kivi = Item("Rock", 1, 3)
Bug = Item("Bug", 0.1, 2)
Sieni = Item("Fly Agaric", 0.3, 4)
Tikku = Item("Stick", 0.7, 10)
Marja = Item("Berry", 0.1, 20)
Kirves = Item("Axe", 2, 1)
Opettaja = Item("Teacher", 93, 1)
Rotta = Item("Rat", 0.6, 3)
Maito = Item("Bucket of Milk", 10, 2)
Haulikko = Item("Shotgun", 3, 1)
Pentu = Item("Puppy", 0.8, 1)

# Esineiden Siirto huoneisiin
Ikkuna.Mahd_Esine.extend([Lintu, Lasi])
Etupiha.Mahd_Esine.extend([Kukka, Kivi, Bug])
Katu.Mahd_Esine.extend([None])
Metsä.Mahd_Esine.extend([Sieni, Tikku, Marja])
Mökki.Mahd_Esine.extend([Kirves])
Koulu.Mahd_Esine.extend([None])
Luokka.Mahd_Esine.extend([Opettaja])
Kuja.Mahd_Esine.extend([Rotta])
Maatila.Mahd_Esine.extend([Maito, Haulikko])
KoiraTarha.Mahd_Esine.extend([Pentu])

# Pelin Aloitus
with open("peliprojekti/Ohjeet.txt", "r") as OTied:
    Ohje = OTied.read()
with open("peliprojekti/Intro.txt", "r") as ITied:
    Intro = ITied.read()
print(f"{Ohje}\n{Intro}")

Player = Pelaaja("", Aloitus)
Player.Liiku()