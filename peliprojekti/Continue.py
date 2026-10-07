import Kartta

def Continue(Pelaaja):
    with open("peliprojekti/Save.txt", "r") as Admin:
        Rivit = Admin.readlines()

    # Hakee Pelaajan nimen, järjen ja rahan
    Pelaaja.Nimi = Rivit[0].strip().split(": ")[1]
    Pelaaja.Järki = Rivit[3].strip().split(": ")[1]
    Pelaaja.Raha = Rivit[4].strip().split(": ")[1]
    Pelaaja.Järki = int(Pelaaja.Järki)
    Pelaaja.Raha = int(Pelaaja.Raha)

    # Kaikki huoneet ID:n perusteella
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
    # Tiedämme jo mikä ID kullakin huoneella on, joten tarvitsemme olion kutsuma nimen eikä annettua nimeä sille
    IDee = Huone[1]
    if IDee in Huoneet:
        Pelaaja.Sijainti = Huoneet[IDee]

    # Sama käy Itemeillä, Tiedämme annetun nimen mutta ei itse olion kutsumanimeä
    Pelaaja.Invi = []
    Esineet = {"Bird": Kartta.Lintu,
        "Glass shard": Kartta.Lasi,
        "Flower": Kartta.Kukka,
        "Rock": Kartta.Kivi,
        "Bug": Kartta.Bug,
        "Fly Agaric": Kartta.Sieni,
        "Stick": Kartta.Tikku,
        "Berry": Kartta.Marja,
        "Axe": Kartta.Kirves,
        "Study book": Kartta.Kirja,
        "Rat": Kartta.Rotta,
        "Bucket of Milk": Kartta.Maito,
        "Shotgun": Kartta.Haulikko,
        "Puppy": Kartta.Pentu}

    Invi = Rivit[2].strip().split(": ")
    # Tarkistaa ettei ole tyhjä
    if len(Invi) > 1 and Invi[1]:
        Esine = Invi[1].split(", ")
        # Erotetaan kaikki itemit pilkulla kun tallennus tiedostossa ne ovat: [Bird: 0.7], [Rock: 1]
        for i in Esine:
            # Katsoo jokaisen esineen erotettuina ja lisää ne Pelaajan inventaarioon
            if i in Esineet:
                InviE = Esineet[i]
                Pelaaja.Invi.append(InviE)
                # Pidetään varma ettei esineitä yhtäkkyä synny uudelleen kun jatketaan peliä uudelleen
                if InviE.Määrä > 0:
                    InviE.Määrä -= 1

    # Jatketaan peliä normaalisti
    print(f"Loaded {Pelaaja.Nimi} at {Pelaaja.Sijainti.Nimi} with {Pelaaja.Järki} and {Pelaaja.Raha}€")
    Pelaaja.NäytäInventaario()
    Pelaaja.Liiku()
    return