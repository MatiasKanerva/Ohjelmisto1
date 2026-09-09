import random

Nimi = input("Kerro nimesi: ")
Ikä = input("Mikä on ikäsi: ")

if int(Ikä) < 12:
    print("Olet alaikäinen peliin.")
    exit()
else: print(f"Terve, {Nimi}!\n")

Inventaario = []

def NäytäInventaario():
    print(f"Tässä on Inventiaariosi: {Inventaario}\n")
    return

def Valinta(valinta):
    if valinta == 2:
        Input = input("1. Nosta lintu\n"
                          "2. Nosta lasin siru\n")
        if Input == "1":
            Inventaario.append("Lintu")
            print("Lintu on lisätty inventaarioosi.")
        if Input == "2":
            Inventaario.append("Lasin siru")
            print("Lasin siruja ollaan lisätty inventaarioosi.")

    if valinta == 3:
        Input = input("1. Nosta kukkia\n" \
                          "2. Nosta hiekkaa\n"
                          "3. Nosta ötökkä\n")
        if Input == "1":
            Inventaario.append("Kukka")
            print("Kukka on lisätty inventaarioosi")
        if Input == "2":
            Inventaario.append("Hiekkaa")
            print("Hiekka on lisätty inventaarioosi")
        if Input == "3":
            Inventaario.append("Ötökkä")
            print("Ötökkä on lisätty inventaarioosi")

    return

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

    Vuoro = input("Heitä noppaa painamalla 1: ")
    while Vuoro != "":
        Noppa = random.randint(1,6)
        print(Noppa)
        if Noppa == 1:
            Nopeus = 1
            print("Kompastuit! Etenet hitaasti...")
        elif 1 < Noppa < 5:
            Nopeus = 2
            print("Kävelet reippaasti eteenpäin.")
        elif 4 < Noppa:
            Nopeus = 4
            print("Juokset täysillä kohti ovea!")
        HirvionMatka =- 1
        PelaajanMatka = PelaajanMatka + Nopeus
        print(f"Matka: {PelaajanMatka}, Nopeus: {Nopeus}")

        if PelaajanMatka >= 15:
            print("Pääsit painajaisesta pois ja heräät huoneessasi.")
            return

        if HirvionMatka > 1:
            print("Peli loppui. Kuolit hirviölle.")
            exit()
        Vuoro = input("Heitä noppaa uudelleen painamalla 1: ")

Päävalikko = input(f"Mitä haluasiti tehdä?\n"
                    "1. Nukkua sängyssä\n"
                    "2. Katso ikkunasta\n"
                    "3. Kävellä ulos\n"
                    "4. Lopeta.\n"
                    "5. Katso inventaariosi\n")

while Päävalikko != "4" and Päävalikko != "lopeta":
    
    if Päävalikko == "1":
        print("Menit nukkumaan...\n")
        Painajainen()
        Päävalikko = input("")

    elif Päävalikko == "2":
        print("Lintu lensi ikkunasta läpi ja lasi räjähti lattiallesi.\n")
        Valinta(valinta=2)
        Päävalikko = input("")

    elif Päävalikko == "3":
        print("Kävelit ulos ja näet kukkia, hiekkaa ja ötökän etupihaltasi.\n")
        Valinta(valinta=3)
        Päävalikko = input("")

    elif Päävalikko == "5":
        print(Inventaario)
        Päävalikko = input("")

    Päävalikko = input(f"Mitä haluasiti tehdä?\n"
                    "1. Nukkua sängyssä\n"
                    "2. Katso ikkunasta\n"
                    "3. Kävellä ulos\n"
                    "4. Lopeta.\n"
                    "5. Katso inventaariosi\n")

if Päävalikko in ("4", "lopeta"):
    print(f"Näkemiin, {Nimi}")
    exit()