def Save(Player):
    Nimet = [Item.Obj for Item in Player.Invi]
    TallennusData = (
        f"Name: {Player.Nimi}\n"
        f"{Player.Sijainti}\n"
        f"Inventory: {', '.join(Nimet)}")
            
    with open("peliprojekti/Save.txt", "w") as Admin:
        Admin.write(TallennusData)

    print(f"Goodbye, {Player.Nimi}!")
    exit()