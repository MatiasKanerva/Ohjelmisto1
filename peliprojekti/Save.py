def Save(Player):
    # Tulostaa kaikki itemit listaan jotta on helppo tulostaa seuraavalla kerralla
    Itemit = [Item.Obj for Item in Player.Invi]
    TallennusData = (
        f"Name: {Player.Nimi}\n"
        f"{Player.Sijainti}\n"
        f"Inventory: {', '.join(Itemit)}\n"
        f"Sanity: {Player.Järki}\n"
        f"Money: {Player.Raha}")
            
    with open("peliprojekti/Save.txt", "w") as Admin:
        Admin.write(TallennusData)

    # Lopettaa pelin
    print(f"Goodbye, {Player.Nimi}!")
    exit()