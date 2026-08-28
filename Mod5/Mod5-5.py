Käyttäjätunnus = "Python"
Salasana = "rules"
Yrityksiä = 1

YritysK, YritysS = input("Kirjoita käyttäjätunnus ja salasana: ").split()

while YritysK != Käyttäjätunnus and YritysS != Salasana:
    YritysK, YritysS = input("Käyttäjätunnus tai salasana ovat väärin, kirjoita uudelleen: ").split()
    Yrityksiä = Yrityksiä + 1
    print(Yrityksiä)
    if Yrityksiä >= 5:
        print("Pääsy evätty")
        break
else: print(f"Tervetuloa {Käyttäjätunnus}")