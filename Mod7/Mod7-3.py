def Converter():
    Litra = 3.785
    Gallon = float(input("Kerro kuinka paljon galoonaa bensaa sinulla on: "))
    while Gallon > 1:
        print(f"{Gallon} galloonia on {Gallon * Litra} litraa")
        Gallon = float(input("Kerro kuinka paljon galoonaa bensaa sinulla on: "))
    return

Converter()