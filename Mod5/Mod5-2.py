Tuuma = int(input("Anna tuuma: "))

while Tuuma > 0 and Tuuma != "":
    Sentti = 2.54
    print(f"{Tuuma} tuumaa on {Tuuma * Sentti} senttiä.")
    Tuuma = Tuuma - 1
    Tuuma = int(input("Anna uusi Tuuma: "))