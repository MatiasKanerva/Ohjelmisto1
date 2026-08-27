
Kuha = float(input("Kuinka pitkän kuhan nappasit?: "))


if Kuha < 37:
    alisentti = 37 - Kuha
    print("Anteeksi, mutta kuhasi on", alisentti ,"senttiä liian pieni, palautathan kuhan jokeen, kiitos")

else:
    print("Vau! Nappasit ison kuhan!")