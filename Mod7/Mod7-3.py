def Converter(Gallon):
    return Gallon * 3.785

Bensiini = float(input("Kerro kuinka paljon galoonaa bensaa sinulla on: "))
Converter(Bensiini)
print(f"{Bensiini} galloonia on {round(Converter(Bensiini),2)} litraa")