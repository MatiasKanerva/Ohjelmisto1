class Item:
    def __init__(self, Obj:str, Paino:float, Määrä:int):
        self.Obj = Obj
        self.Paino = Paino
        self.Määrä = Määrä

    # Tulostaa pelkän Nimen ja Painon eikä Määrää, Pelaajan ei tarvitse tietää summaa tallennus tiedostossa.
    def __repr__(self):
        return f"{self.Obj}: {self.Paino}kg"

class Huone:
    def __init__(self, Nimi:str, ID:int):
        self.Nimi = Nimi
        self.ID = ID
        self.Mahd_Esine: list[Item] = []

    # Tulostaa pelkän Nimen ja ID eikä Mahdollista Esinettä, emme halua että pelaaja näkee sitä tallennus tiedostossa.
    def __repr__(self):
        return f"{self.Nimi}: {self.ID}"
    
# Huoneiden luonti
Aloitus = Huone("Start",1)
Makuuhuone = Huone("Bedroom",2)
Ikkuna = Huone("Window",3)
Etupiha = Huone("Front Door",4)
Katu = Huone("Mainroad",5)
Metsä = Huone("Forest",6)
Mökki = Huone("Cabin",7)
Koulu = Huone("School",8)
Luokka = Huone("Classroom",9)
Kuja = Huone("Alleyway",10)
Maatila = Huone("Farm",11)
KoiraTarha = Huone("Kennel",12)

# Esineiden luonti
# None viittaa loputtomaan määrään
Lintu = Item("Bird", 0.7, 1)
Lasi = Item("Glass shard", 0.1, 10)
Kukka = Item("Flower", 0.1, None)
Kivi = Item("Rock", 1, None)
Bug = Item("Bug", 0.1, None)
Sieni = Item("Fly Agaric", 0.3, None)
Tikku = Item("Stick", 0.7, None)
Marja = Item("Berry", 0.1, None)
Kirves = Item("Axe", 2, 1)
Kirja = Item("Study book", 0.8, 1)
Rotta = Item("Rat", 0.6, 3)
Maito = Item("Bucket of Milk", 10, 2)
Haulikko = Item("Shotgun", 3, 1)
Pentu = Item("Puppy", 0.8, 1)

# Esineiden Siirto huoneisiin
# None viittaa ettei sieltä voi saada tavaroita.
Ikkuna.Mahd_Esine.extend([Lintu, Lasi])
Etupiha.Mahd_Esine.extend([Kukka, Kivi, Bug])
Katu.Mahd_Esine.extend([None])
Metsä.Mahd_Esine.extend([Sieni, Tikku, Marja])
Mökki.Mahd_Esine.extend([Kirves])
Koulu.Mahd_Esine.extend([None])
Luokka.Mahd_Esine.extend([Kirja])
Kuja.Mahd_Esine.extend([Rotta])
Maatila.Mahd_Esine.extend([Maito, Haulikko])
KoiraTarha.Mahd_Esine.extend([Pentu])