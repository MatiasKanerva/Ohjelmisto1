Luku = input("Anna numero: ")
Lista = []

while Luku != "":
    Lista.append(int(Luku))
    Lista.sort(reverse=True)

    Luku = input("Anna uusi numero: ")

print(f"Viisi suurinta lukua: {Lista[:5]}")