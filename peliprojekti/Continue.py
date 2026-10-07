import Kartta
import Game

def Continue():
    with open("peliprojekti/Save.txt", "r") as Admin:
        Rivit = Admin.readlines()

    Game.Player.Nimi = Rivit[0].strip().split(": ")[1]
    
    Huoneet = {"1": Kartta.Aloitus,
                "2": Kartta.Makuuhuone,
                "3": Kartta.Ikkuna,
                "4": Kartta.Etupiha,
                "5": Kartta.Katu,
                "6": Kartta.Metsä,
                "7": Kartta.Mökki,
                "8": Kartta.Koulu,
                "9": Kartta.Luokka,
                "10": Kartta.Kuja,
                "11": Kartta.Maatila,
                "12": Kartta.KoiraTarha}
    Huone = Rivit[1].strip().split(": ")
    IDee = Huone[1]

    if IDee in Huoneet:
        Game.Player.Sijainti = Huoneet[IDee]

    Game.Player.Invi = []
    Esineet = {"Bird": Kartta.Lintu,
        "Glass shard": Kartta.Lasi,
        "Flower": Kartta.Kukka,
        "Rock": Kartta.Kivi,
        "Bug": Kartta.Bug,
        "Fly Agaric": Kartta.Sieni,
        "Stick": Kartta.Tikku,
        "Berry": Kartta.Marja,
        "Axe": Kartta.Kirves,
        "Teacher": Kartta.Opettaja,
        "Rat": Kartta.Rotta,
        "Bucket of Milk": Kartta.Maito,
        "Shotgun": Kartta.Haulikko,
        "Puppy": Kartta.Pentu}

    Invi = Rivit[2].strip().split(": ")
    if len(Invi) > 1 and Invi[1]:
        Esine = Invi[1].split(", ")
        for i in Esine:
            if i in Esineet:
                InviE = Esineet[i]
                Game.Player.Invi.append(InviE)
                if InviE.Määrä > 0:
                    InviE.Määrä -= 1

    print(f"Loaded {Game.Player.Nimi} at {Game.Player.Sijainti}")
    Game.Player.NäytäInventaario()
    Game.Player.Liiku()
    return