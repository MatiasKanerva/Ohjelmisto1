import Game

def Continue():
    with open("peliprojekti/Save.txt", "r") as Admin:
        Rivit = Admin.readlines()

    Game.Player.Nimi = Rivit[0].strip().split(": ")[1]
    
    Huoneet = {"1": Game.Aloitus,
                "2": Game.Makuuhuone,
                "3": Game.Ikkuna,
                "4": Game.Etupiha,
                "5": Game.Katu,
                "6": Game.Metsä,
                "7": Game.Mökki,
                "8": Game.Koulu,
                "9": Game.Luokka,
                "10": Game.Kuja,
                "11": Game.Maatila,
                "12": Game.KoiraTarha}
    Idee = Rivit[1].strip()
    if Idee in Huoneet:
        Game.Player.Sijainti = Huoneet[Idee]

    Game.Player.Invi = []
    Esineet = {"Bird": Game.Lintu,
        "Glass shard": Game.Lasi,
        "Flower": Game.Kukka,
        "Rock": Game.Kivi,
        "Bug": Game.Bug,
        "Fly Agaric": Game.Sieni,
        "Stick": Game.Tikku,
        "Berry": Game.Marja,
        "Axe": Game.Kirves,
        "Teacher": Game.Opettaja,
        "Rat": Game.Rotta,
        "Bucket of Milk": Game.Maito,
        "Shotgun": Game.Haulikko,
        "Puppy": Game.Pentu}

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