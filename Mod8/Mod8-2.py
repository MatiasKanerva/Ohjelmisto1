Nimi = input("Kerro nimiä: ")
KerrotutNimet = set()
AnnettuNimi = []
Sama = 0

while Nimi != "":
    for i in range(len(AnnettuNimi)):
        Sama = 0
        if Nimi == AnnettuNimi[i]:
            Sama += 1
            print("Annoit jo tämän nimen")
            break
        i += i
        
    if Sama == 0:
        KerrotutNimet.add(Nimi)
        print("Uusi nimi tallenettu")
        for i in KerrotutNimet:
            print(i)

    AnnettuNimi.append(Nimi)
    Nimi = input("\nKerro uusi nimi: ")