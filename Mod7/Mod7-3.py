def Converter(Bensiini):
    Litra = 3.785
    while Bensiini > 1:
        print(f"{Bensiini} galloonia on {Bensiini * Litra} litraa")
        Bensiini = float(input("Kerro kuinka paljon galoonaa bensaa sinulla on: "))
    return

Bensiini = float(input("Kerro kuinka paljon galoonaa bensaa sinulla on: "))
Converter(Bensiini)