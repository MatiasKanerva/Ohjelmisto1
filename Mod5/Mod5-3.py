Syöte = input("Anna luku: ")
Pieni = int(Syöte)
Suurin = int(Syöte)

while Syöte != "":
    Syöte = input("Anna uusi luku: ")
    if Syöte == "":
        break

    luku = int(Syöte)
    if luku < Pieni:
        Pieni = luku

    if luku > Suurin:
        Suurin = luku

print(f"Suurin {Suurin}\nPienin {Pieni}")