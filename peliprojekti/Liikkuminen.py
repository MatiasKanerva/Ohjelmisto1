import Continue
import Save
import Kartta
import Nightmare

def Start(Pelaaja):
    Input = input("1. New game\n"
                  "2. Continue\n"
                  "3. Quit\n")
    if Input == "1":

        Nimi = input("What's your name?: ")
        Ikä = input("How old are you?: ")

        if int(Ikä) < 12:
            print("You are underaged to play this game, BANISHED!")
            exit()
        else: print(f"\nHello, {Nimi}!\n")

        Pelaaja.Nimi = Nimi
        Pelaaja.Sijainti = Kartta.Makuuhuone

    elif Input == "2":
        Continue.Continue()
        
    elif Input == "3":
        Save.Save()

def Bedroom(Pelaaja):
    Input = input(f"You are in *{Pelaaja.Sijainti.Nimi}*. Would you like to do?\n"
                    "1. Sleep in Bed\n"
                    f"2. Walk to *{Kartta.Ikkuna.Nimi}*\n"
                    f"3. Walk to *{Kartta.Etupiha.Nimi}*\n"
                    "\n4. Show Inventory\n"
                    "5. Save & Quit\n")
    
    if Input == "1":
            print("You went to sleep...\n")
            Nightmare.Painajainen()

    elif Input == "2":
        Pelaaja.Sijainti = Kartta.Ikkuna
        print(f"*{Kartta.Lintu.Obj}* flew at your *{Kartta.Ikkuna.Nimi}*, breaking the glass into *{Kartta.Lasi.Obj}* and dying on the spot\n")
        

    elif Input == "3":
        Pelaaja.Sijainti = Kartta.Etupiha
        print(f"You walked *{Pelaaja.Sijainti.Nimi}*, you see a bunch of *{Kartta.Kukka.Obj}*, heavy looking *{Kartta.Kivi.Obj}* and a small colorful *{Kartta.Bug.Obj}*\n")

    elif Input == "4":
        Pelaaja.NäytäInventaario()

    elif Input == "5":
        Save.Save()

def Window(Pelaaja):
    Input = input(f"1. Pick up *{Kartta.Lintu.Obj}*\n"
                    f"2. Pick up *{Kartta.Lasi.Obj}*\n"
                    f"3. Walk Back to *{Kartta.Makuuhuone.Nimi}*\n"
                    f"\n4. Show Inventory\n")
                    
    if Input == "1":
        if Kartta.Lintu in Kartta.Ikkuna.Mahd_Esine:
            if Kartta.Lintu.Määrä > 0:
                Kartta.Lintu.Määrä -= 1
                Pelaaja.Collect(Kartta.Lintu)
                print(f"*{Kartta.Lintu.Obj}* has been added to your Inventory\n")
                Pelaaja.Sijainti = Kartta.Makuuhuone
            else: Kartta.Ikkuna.Mahd_Esine.remove(Kartta.Lintu)
        else: print("There was only one bird to pick...\n")
            

    elif Input == "2":
        if Kartta.Lasi in Kartta.Ikkuna.Mahd_Esine:
            if Kartta.Lasi.Määrä > 0:
                Pelaaja.Collect(Kartta.Lasi)
                Kartta.Lasi.Määrä -= 1
                print(f"*{Kartta.Lasi.Obj}* has been added to your Inventory\n")
                Pelaaja.Sijainti = Kartta.Makuuhuone
            else: Kartta.Ikkuna.Mahd_Esine.remove(Kartta.Lasi)
        else: print("You've picked up every single shard\n")

    elif Input == "3":
        Pelaaja.Sijainti = Kartta.Makuuhuone
        print(f"You walked back to *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "4":
        Pelaaja.NäytäInventaario()

def Front_Door(Pelaaja):
    Input = input("1. Pick up flowers\n" \
                    "2. Pick up a rock\n"
                    "3. Pick up bugs\n"
                    "4. Walk to Mainroad\n"
                    "5. Go Home\n"
                    "\n6. Show Inventory\n"
                    "7. Save & Quit\n")
                    
    if Input == "1":
        if Kartta.Kukka in Kartta.Etupiha.Mahd_Esine:
            if Kartta.Kukka.Määrä > 0:
                Pelaaja.Collect(Kartta.Kukka)
                Kartta.Kukka.Määrä -= 1
                print(f"*{Kartta.Kukka.Obj}* has been added to your Inventory\n")
            else: Kartta.Etupiha.Mahd_Esine.remove(Kartta.Kukka)
        else: print(f"You couldn't find anymore *{Kartta.Kukka.Obj}* in the garden\n")

    elif Input == "2":
        if Kartta.Kivi in Kartta.Etupiha.Mahd_Esine:
            if Kartta.Kivi.Määrä > 0:
                Pelaaja.Collect(Kartta.Kivi)
                Kartta.Kivi.Määrä -= 1
                print(f"*{Kartta.Kivi.Obj}* has been added to your Inventory\n")
            else: Kartta.Etupiha.Mahd_Esine.remove(Kartta.Kivi)
        else: print(f"You couldn't find any more *{Kartta.Kivi.Obj}*\n")

    elif Input == "3":
        if Kartta.Bug in Kartta.Etupiha.Mahd_Esine:
            if Kartta.Bug.Määrä > 0:
                Pelaaja.Collect(Kartta.Bug)
                Kartta.Bug.Määrä -= 1
                print(f"*{Kartta.Bug.Obj}* has been added to your Inventory\n")
            else: Kartta.Etupiha.Mahd_Esine.remove(Kartta.Bug)
        else: print(f"You couldn't find any more cool *{Kartta.Bug.Obj}* to pick\n")

    elif Input == "4":
        Pelaaja.Sijainti = Kartta.Katu
        print(f"You walked to *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "5":
        Pelaaja.Sijainti = Kartta.Makuuhuone
        print(f"You walked back inside to your *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "6":
        Pelaaja.NäytäInventaario()

    elif Input == "7":
        Save.Save()

def Mainroad(Pelaaja):
    Input = input(f"1. Walk to *{Kartta.Koulu.Nimi}*\n"
                    f"2. Explore *{Kartta.Metsä.Nimi}*\n"
                    f"3. Walk to *{Kartta.Kuja.Nimi}*\n"
                    "\n4. Show Inventory\n"
                    "5. Save & Quit\n")
                    
    if Input == "1":
        Pelaaja.Sijainti = Kartta.Koulu
        print(f"You walked inside your *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "2":
        Pelaaja.Sijainti = Kartta.Metsä
        print(f"You forced your way into *{Pelaaja.Sijainti.Nimi}* through the thick foliage\n")

    elif Input == "3":
        Pelaaja.Sijainti = Kartta.Kuja
        print(f"You walked into the gloomy and wet *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "4":
        Pelaaja.NäytäInventaario()

    elif Input == "5":
        Save.Save()

def Forest(Pelaaja):
    Input = input("1. Pick up Mushrooms\n"
                    "2. Pick up Sticks\n"
                    "3. Pick up Berries\n"
                    "4. Walk to Cabin\n"
                    "5. Walk to Mainroad\n"
                    "\n6. Show Inventory\n"
                    "7. Save & Quit\n")
    
    if Input == "1":
        if Kartta.Sieni in Kartta.Metsä.Mahd_Esine and Kartta.Sieni.Määrä > 0:
            Pelaaja.Collect(Kartta.Sieni)
            Kartta.Sieni.Määrä -= 1
            print(f"*{Kartta.Sieni.Obj}* has been added to your Inventory\n")
            if Kartta.Sieni.Määrä == 0:
                Kartta.Metsä.Mahd_Esine.remove(Kartta.Sieni)
        else: print(f"I think you got the whole *{Kartta.Sieni.Obj}* cluster\n")

    elif Input == "2":
        if Kartta.Tikku in Kartta.Metsä.Mahd_Esine and Kartta.Tikku.Määrä > 0:
            Pelaaja.Collect(Kartta.Tikku)
            Kartta.Tikku.Määrä -= 1
            print(f"*{Kartta.Tikku.Obj}* has been added to your Inventory\n")
            if Kartta.Tikku.Määrä == 0:
                Kartta.Metsä.Mahd_Esine.remove(Kartta.Tikku)
        else: print("You took all the sticks nearby\n")

    elif Input == "3":
        if Kartta.Marja in Kartta.Metsä.Mahd_Esine and Kartta.Marja.Määrä > 0:
            Pelaaja.Collect(Kartta.Marja)
            Kartta.Marja.Määrä -= 1
            print(f"*{Kartta.Marja.Obj}* has been added to your Inventory\n")
            if Kartta.Marja.Määrä == 0:
                Kartta.Metsä.Mahd_Esine.remove(Kartta.Marja)
        else: print("You got all the berries from the bush\n")

    elif Input == "4":
        Pelaaja.Sijainti = Kartta.Mökki
        print(f"You walk inside *{Pelaaja.Sijainti.Nimi}*, it looks vintage and cozy. The fireplace is cracking with fire\n")

    elif Input == "5":
        Pelaaja.Sijainti = Kartta.Katu
        print(f"You walked back to *{Pelaaja.Sijainti.Nimi}* through the dense foliage again\n")

    elif Input == "6":
        Pelaaja.NäytäInventaario()

    elif Input == "7":
        Save.Save()

def Cabin(Pelaaja):
    Input = input("1. Pick up Axe\n"
                    "2. Walk to Forest\n"
                    "\n3. Show Inventory\n"
                    "4. Save & Quit\n")
    if Input == "1":
        if Kartta.Kirves in Kartta.Mökki.Mahd_Esine and Kartta.Kirves.Määrä > 0:
            Pelaaja.Collect(Kartta.Kirves)
            Kartta.Kirves.Määrä -= 1
            print(f"*{Kartta.Kirves.Obj}* has been added to your Inventory\n")
            if Kartta.Kirves.Määrä == 0:
                Kartta.Mökki.Mahd_Esine.remove(Kartta.Kirves)
        else: print(f"I think that was the only *{Kartta.Kirves.Obj}* around\n")

    elif Input == "2":
        Pelaaja.Sijainti = Kartta.Metsä
        print(f"You walked back to the open *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "3":
        Pelaaja.NäytäInventaario()

    elif Input == "4":
        Save.Save()

def School(Pelaaja):
    Input = input(f"1. Find your *{Kartta.Luokka.Nimi}*\n"
                    f"2. Walk to *{Kartta.Katu.Nimi}*\n"
                    "\n3. Show Inventory\n"
                    "4. Save & Quit\n")
                    
    if Input == "1":
        Pelaaja.Sijainti = Kartta.Luokka
        print(f"You found your way into *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "2":
        Pelaaja.Sijainti = Kartta.Katu
        print(f"You walked back to *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "3":
        Pelaaja.NäytäInventaario()

    elif Input == "4":
        Save.Save()

def Classroom(Pelaaja):
    Valikko = (f"1. Pick up *{Kartta.Kirja.Obj}*\n"
                    f"2. Get out of *{Pelaaja.Sijainti.Nimi}*\n"
                    "\n3. Show Inventory\n"
                    "4. Save & Quit\n")

    if Kartta.Kirja in Pelaaja.Invi:
        Valikko = f"0. Study with *{Kartta.Kirja.Obj}*\n" + Valikko
        
    Input = input(Valikko)

    if Input == "0" and Kartta.Kirja in Pelaaja.Invi:
        print("-" * 30)
        print(f"Scholar ending: You study *{Kartta.Kirja.Obj}* and your grades improve\n")
        print("-" * 30)
        Save.Save()
    else: print(f"You don't have *{Kartta.Kirja.Obj}* to study with")
                    
    if Input == "1" and Kartta.Kirja not in Pelaaja.Invi:
        if Kartta.Kirja in Kartta.Luokka.Mahd_Esine and Kartta.Kirja.Määrä > 0:
            Pelaaja.Collect(Kartta.Kirja)
            Kartta.Kirja.Määrä -= 1
            print(f"*{Kartta.Kirja.Obj}* has been added to your Inventory, You can now study\n")
            if Kartta.Kirja.Määrä == 0:
                Kartta.Luokka.Mahd_Esine.remove(Kartta.Kirja)
        else: print(f"You already own *{Kartta.Kirja.Obj}* for studying\n")

    elif Input == "2":
        Pelaaja.Sijainti = Kartta.Koulu
        print(f"You walked into the hallway of *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "3":
        Pelaaja.NäytäInventaario()

    elif Input == "4":
        Save.Save()

def Alleyway(Pelaaja):
    Input = input("1. Pick up Rat\n"
                    "2. Walk to Farm\n"
                    "3. Search Dumpsters\n"
                    "\n4. Show Inventory\n"
                    "5. Save & Quit\n")
    
    if Input == "1":
        if Kartta.Rotta in Kartta.Kuja.Mahd_Esine and Kartta.Rotta.Määrä > 0:
            Pelaaja.Collect(Kartta.Rotta)
            Kartta.Rotta.Määrä -= 1
            print(f"*{Kartta.Rotta.Obj}* has been added to your Inventory. Don't catch a plaque though, ew\n")
            if Kartta.Rotta.Määrä == 0:
                Kartta.Kuja.Mahd_Esine.remove(Kartta.Rotta)
        else: print("You took the whole family. What are you gonna do with more? Colonize them?\n")

    elif Input == "2":
        Pelaaja.Sijainti = Kartta.Maatila
        print(f"You walked a long road heading to *{Pelaaja.Sijainti.Nimi}*, I wonder what there will be?\n")

    elif Input == "3":
        Pelaaja.Search(Kartta.Kuja)

    elif Input == "4":
        Pelaaja.NäytäInventaario()

def Farm(Pelaaja):
    Valikko = ("1. Pick up Shotgun\n"
                "2. Pick up Milk\n"
                "3. Walk to Kennel\n"
                "4. Walk to Alleyway\n"
                "\n5. Show Inventory\n"
                "6. Save & Quit\n")
    
    if Kartta.Maito in Pelaaja.Invi:
        Valikko = f"0. Work in the *{Pelaaja.Sijainti.Nimi}*\n" + Valikko

    Input = input(Valikko)

    if Input == "0" and Kartta.Maito in Pelaaja.Invi:
        print("-" * 30)
        print("Farmer Ending: You helped the citys agriculture and processing more foods for the people")
        print("-" * 30)
        Save.Save()
    else: print(f"You don't have guts to work in the *{Pelaaja.Sijainti.Nimi}*")

    if Input == "1":
        if Kartta.Haulikko in Kartta.Maatila.Mahd_Esine and Kartta.Haulikko.Määrä > 0:
            Pelaaja.Collect(Kartta.Haulikko)
            Kartta.Haulikko.Määrä -= 1
            print(f"*{Kartta.Haulikko.Obj}* has been added to your Inventory\n")
            if Kartta.Haulikko.Määrä == 0:
                Kartta.Maatila.Mahd_Esine.remove(Kartta.Haulikko)
        else: print("No. You can't dual wield them.\n")

    elif Input == "2":
        if Kartta.Maito in Kartta.Maatila.Mahd_Esine and Kartta.Maito.Määrä > 0:
            Pelaaja.Collect(Kartta.Maito)
            Kartta.Maito.Määrä -= 1
            print(f"*{Kartta.Maito.Obj}* was added to your Inventory\n")
            if Kartta.Maito == 0:
                Kartta.Maatila.Mahd_Esine.remove(Kartta.Maito)
        else: print(f"You don't have a third arm for another bucket of *{Kartta.Maito.Obj}*")

    elif Input == "3":
        Pelaaja.Sijainti = Kartta.KoiraTarha
        print(f"You walk to *{Pelaaja.Sijainti.Nimi}*, you can hear lots of barking and growling\n")

    elif Input == "4":
        Pelaaja.Sijainti = Kartta.Kuja
        print("You walk back the long path until you reach Alleyway\n")

    elif Input == "5":
        Pelaaja.NäytäInventaario()

    elif Input == "6":
        Save.Save()

def Kennel(Pelaaja):
    Input = input("1. Pick up Puppy\n"
                    "2. Pat a Dog\n"
                    "3. Walk to Farm\n"
                    "\n4. Show Inventory\n"
                    "5. Save & Quit\n")
    
    if Input == "1":
        if Kartta.Pentu in Kartta.KoiraTarha.Mahd_Esine and Kartta.Pentu.Määrä > 0:
            Pelaaja.Collect(Kartta.Pentu)
            Kartta.Pentu.Määrä -= 1
            print(f"{Kartta.Pentu.Obj}* has been added to your Inventoryn, Cute little fucker ain't ya\n")
            if Kartta.Pentu.Määrä == 0:
                Kartta.KoiraTarha.Mahd_Esine.remove(Kartta.Pentu)
        else: print("Mhehe, stole em all!\n")

    elif Input == "2":
        print(f"You walk up to *{Kartta.Pentu.Obj}* and start petting their head, squishing their cheeks and scratching their backs\n")

    elif Input == "3":
        Pelaaja.Sijainti = Kartta.Maatila
        print(f"You walk back to *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "4":
        Pelaaja.NäytäInventaario()

    elif Input == "5":
        Save.Save()