import Game

def Save():
    Nimet = [Game.Item.Obj for Game.Item in Game.Player.Invi]
    TallennusData = (
        f"Name: {Game.Player.Nimi}\n"
        f"{Game.Player.Sijainti.ID}\n"
        f"Inventory: {', '.join(Nimet)}")
            
    with open("peliprojekti/Save.txt", "w") as Admin:
        Admin.write(TallennusData)
    return