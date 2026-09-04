Kaikki = []
Parittomat = []

def Lista():
    Luku = input("Kirjoita numero: ")
    while Luku != "":
        Luku = int(Luku)
        Kaikki.append(Luku)
        if Luku % 2:
            Parittomat.append(Luku)
        Luku = input("Kirjoita numero: ")
    print(f"Kaikki luvut: {Kaikki}\nParittomat luvut {Parittomat}")
    return

Lista()