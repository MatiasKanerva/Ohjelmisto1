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
        Continue.Continue(Pelaaja)
        
    elif Input == "3":
        Save.Save(Pelaaja)

# Esimerkit täällä joka soveltuu kaikkille funktioille
def Bedroom(Pelaaja):
    # Antaa pelaajalle valinnan, myös kertoo missä sijainnissa ollaan tällä hetkellä ja kohottaa Itemit ja Huoneet
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input("1. Sleep in Bed\n"
                    f"2. Walk to *{Kartta.Ikkuna.Nimi}*\n"
                    f"3. Walk to *{Kartta.Etupiha.Nimi}*\n"
                    "\n4. Show Inventory\n"
                    "5. Save & Quit\n")
    
    if Input == "1":
            # Vie painajaisiin, myöhemmin jos tätä jatketaan tämä painajainen tapahtuisi enemmän sitä vähemmän järkeä pelaajalla on
            print("You went to sleep...\n")
            Nightmare.Painajainen(Pelaaja)

    elif Input == "2":
        # Vaihtaa pelaajan sijaintia ja Liiku() tekee siirtämisen
        Pelaaja.Sijainti = Kartta.Ikkuna
        print(f"*{Kartta.Lintu.Obj}* flew at your *{Kartta.Ikkuna.Nimi}*, breaking the glass into *{Kartta.Lasi.Obj}* and dying on the spot\n")
        

    elif Input == "3":
        Pelaaja.Sijainti = Kartta.Etupiha
        print(f"You walked *{Pelaaja.Sijainti.Nimi}*, you see a bunch of *{Kartta.Kukka.Obj}*, heavy looking *{Kartta.Kivi.Obj}* and a small colorful *{Kartta.Bug.Obj}*\n")

    elif Input == "4":
        Pelaaja.NäytäInventaario()

    elif Input == "5":
        Save.Save(Pelaaja)

def Window(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input(f"1. Pick up *{Kartta.Lintu.Obj}*\n"
                    f"2. Pick up *{Kartta.Lasi.Obj}*\n"
                    f"3. Walk Back to *{Kartta.Makuuhuone.Nimi}*\n"
                    f"\n4. Show Inventory\n"
                    "5. Save & Quit\n")
                    
    if Input == "1" and Kartta.Lintu in Kartta.Ikkuna.Mahd_Esine:
        Pelaaja.Collect(Kartta.Lintu)
        Kartta.Lintu.Määrä -= 1
        print(f"*{Kartta.Lintu.Obj}* has been added to your Inventory\n")
        Pelaaja.Sijainti = Kartta.Makuuhuone
        if Kartta.Lintu.Määrä == 0:
            Kartta.Ikkuna.Mahd_Esine.remove(Kartta.Lintu)
    else: print("There was only one bird to pick...\n")
            

    if Input == "2":
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

    elif Input == "5":
        Save.Save(Pelaaja)

def Front_Door(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input(f"1. Pick up *{Kartta.Kukka.Obj}*\n"
                    f"2. Pick up *{Kartta.Kivi.Obj}*\n"
                    f"3. Pick up *{Kartta.Bug.Obj}*\n"
                    f"4. Walk to *{Kartta.Katu.Nimi}*\n"
                    f"5. Go back to *{Kartta.Makuuhuone.Nimi}*\n"
                    "\n6. Show Inventory\n"
                    "7. Save & Quit\n")
                    
    if Input == "1":
        if Kartta.Kukka in Kartta.Etupiha.Mahd_Esine:
            Pelaaja.Collect(Kartta.Kukka)
            print(f"*{Kartta.Kukka.Obj}* has been added to your Inventory\n")

    elif Input == "2":
        if Kartta.Kivi in Kartta.Etupiha.Mahd_Esine:
            Pelaaja.Collect(Kartta.Kivi)              
            print(f"*{Kartta.Kivi.Obj}* has been added to your Inventory\n")

    elif Input == "3":
        if Kartta.Bug in Kartta.Etupiha.Mahd_Esine:
            Pelaaja.Collect(Kartta.Bug)
            print(f"*{Kartta.Bug.Obj}* has been added to your Inventory\n")

    elif Input == "4":
        Pelaaja.Sijainti = Kartta.Katu
        print(f"You walked to *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "5":
        Pelaaja.Sijainti = Kartta.Makuuhuone
        print(f"You walked back inside to your *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "6":
        Pelaaja.NäytäInventaario()

    elif Input == "7":
        Save.Save(Pelaaja)

def Mainroad(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input(f"1. Walk to *{Kartta.Koulu.Nimi}*\n"
                    f"2. Explore *{Kartta.Metsä.Nimi}*\n"
                    f"3. Walk to *{Kartta.Kuja.Nimi}*\n"
                    f"4. Walk to *{Kartta.Etupiha.Nimi}\n*"
                    "\n5. Show Inventory\n"
                    "6. Save & Quit\n")
                    
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
            Pelaaja.Sijainti = Kartta.Etupiha
            print(f"You walked to *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "5":
        Pelaaja.NäytäInventaario()

    elif Input == "6":
        Save.Save(Pelaaja)

def Forest(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input(f"1. Pick up *{Kartta.Sieni.Obj}*\n"
                    f"2. Pick up *{Kartta.Tikku.Obj}*\n"
                    f"3. Pick up *{Kartta.Marja.Obj}*\n"
                    f"4. Walk to *{Kartta.Mökki.Nimi}*\n"
                    f"5. Walk to *{Kartta.Katu.Nimi}*\n"
                    "\n6. Show Inventory\n"
                    "7. Save & Quit\n")
    
    if Input == "1":
        if Kartta.Sieni in Kartta.Metsä.Mahd_Esine:
            Pelaaja.Collect(Kartta.Sieni)
            print(f"*{Kartta.Sieni.Obj}* has been added to your Inventory\n")

    elif Input == "2":
        if Kartta.Tikku in Kartta.Metsä.Mahd_Esine:
            Pelaaja.Collect(Kartta.Tikku)
            print(f"*{Kartta.Tikku.Obj}* has been added to your Inventory\n")

    elif Input == "3":
        if Kartta.Marja in Kartta.Metsä.Mahd_Esine:
            Pelaaja.Collect(Kartta.Marja)
            print(f"*{Kartta.Marja.Obj}* has been added to your Inventory\n")

    elif Input == "4":
        Pelaaja.Sijainti = Kartta.Mökki
        print(f"You walk inside *{Pelaaja.Sijainti.Nimi}*, it looks vintage and cozy. The fireplace is cracking with fire\n")

    elif Input == "5":
        Pelaaja.Sijainti = Kartta.Katu
        print(f"You walked back to *{Pelaaja.Sijainti.Nimi}* through the dense foliage again\n")

    elif Input == "6":
        Pelaaja.NäytäInventaario()

    elif Input == "7":
        Save.Save(Pelaaja)

def Cabin(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input(f"1. Pick up *{Kartta.Kirja.Obj}*\n"
                    f"2. Walk to *{Kartta.Metsä.Nimi}*\n"
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
        Save.Save(Pelaaja)

def School(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
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
        Save.Save(Pelaaja)

# Esimerkki jos tietty Itemi on Pelaajan Inventaariossa
#Scholar ending sijaitsee täällä AKA. 4. Hyvä koulutus!
def Classroom(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    # Laitetaan valikoima listaan jotta voidaan muokata haluttaessa
    Valikko = (f"1. Pick up *{Kartta.Kirja.Obj}*\n"
                f"2. Get out of *{Pelaaja.Sijainti.Nimi}*\n"
                "\n3. Show Inventory\n"
                "4. Save & Quit\n")
    
    # Katsoo jos Kirja on Pelaajan inventaariossa ja lisää listalle uuden vaihtoehdon
    if Kartta.Kirja in Pelaaja.Invi:
        Valikko = f"0. Study with *{Kartta.Kirja.Obj}*\n" + Valikko

    # Input vasta uusien valintojen tarkistamisen jälkeen jotta extra valinnat eivät tule esille heti
    Input = input(Valikko)

    # Estää pelaajan pelaajan kirjoittamaan "0" ennen ottamatta kirjaa
    if Input == "0" and Kartta.Kirja in Pelaaja.Invi:
        print("-" * 30)
        print(f"Scholar ending: You study *{Kartta.Kirja.Obj}* and your grades improve\n")
        print("-" * 30)
        Save.Save(Pelaaja)
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
        Save.Save(Pelaaja)

def Alleyway(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input(f"1. Pick up *{Kartta.Rotta.Obj}*\n"
                    f"2. Walk to *{Kartta.Maatila.Nimi}*\n"
                    f"3. Walk to *{Kartta.Katu.Nimi}*\n"
                    f"4. Search Dumpsters\n"
                    "\n5. Show Inventory\n"
                    "6. Save & Quit\n")
    
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
            Pelaaja.Sijainti = Kartta.Katu
            print(f"Walked to *{Pelaaja.Sijainti.Nimi}*\n")

    elif Input == "4":
        Pelaaja.Search(Kartta.Kuja)

    elif Input == "5":
        Pelaaja.NäytäInventaario()

    elif Input == "6":
        Save.Save(Pelaaja)

# Farmer ending sijaitsee täällä AKA. 15. Maanpäällinen Elämä
def Farm(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Valikko = (f"1. Pick up *{Kartta.Haulikko.Obj}*\n"
                f"2. Pick up *{Kartta.Maito.Obj}*\n"
                f"3. Walk to *{Kartta.KoiraTarha.Nimi}*\n"
                f"4. Walk to *{Kartta.Kuja.Nimi}*\n"
                "\n5. Show Inventory\n"
                "6. Save & Quit\n")
    
    if Kartta.Maito in Pelaaja.Invi:
        Valikko = f"0. Work in the *{Pelaaja.Sijainti.Nimi}*\n" + Valikko

    Input = input(Valikko)

    if Input == "0" and Kartta.Maito in Pelaaja.Invi:
        print("-" * 30)
        print("Farmer Ending: You helped the citys agriculture and processing more foods for the people")
        print("-" * 30)
        Save.Save(Pelaaja)
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
        Save.Save(Pelaaja)

def Kennel(Pelaaja):
    print(f"You are at *{Pelaaja.Sijainti.Nimi}*. What would you like to do?\n")
    Input = input(f"1. Pick up *{Kartta.Pentu.Obj}*\n"
                    "2. Pat a Dog\n"
                    f"3. Walk to *{Kartta.Maatila.Nimi}*\n"
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
        Save.Save(Pelaaja)