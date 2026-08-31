Nimi = input("Kerro nimesi: ")
Ikä = input("Mikä on ikäsi: ")

if int(Ikä) < 12:
    print("Olet alaikäinen peliin.")
    exit()

print(f"Terve, {Nimi}!\n")
Päävalikko = input(f"Mitä haluasiti tehdä?\n"
                    "1. Nukkua sängyssä\n"
                    "2. Katso ikkunasta\n"
                    "3. Kävellä ulos\n"
                    "4. Lopeta.\n")

while Päävalikko != "4" and Päävalikko != "lopeta":
    
    if Päävalikko == "1":
        print("Nukuit niin kauan että peli loppui\n")
        Päävalikko = input("")

    elif Päävalikko == "2":
        print("Lintu lensi ikkunasta läpi ja lasi räjähti naamaasi.\n")
        Päävalikko = input("")

    elif Päävalikko == "3":
        print("Kävelit ulos ja kuolit\n")
        Päävalikko = input("")

    Päävalikko = input(f"Synnyit uudelleen, Mitä haluasiti tehdä?\n"
                    "1. Nukkua sängyssä\n"
                    "2. Katso ikkunasta\n"
                    "3. Kävellä ulos\n"
                    "4. Lopeta.\n")

if Päävalikko in ("4", "lopeta"):
    print(f"Näkemiin, {Nimi}")
    exit()