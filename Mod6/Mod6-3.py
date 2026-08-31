Alkunumero = int(input("Kirjoita numero katsoakseen onko se alkunumero: "))

Alkuluku = 1

for x in range(2, Alkunumero - 1):
    x = x + 1
    Jako = Alkunumero / x
    if Alkunumero % x == 0:
        print("ei ole alkunumero")
        Alkuluku = 0
        break

if Alkuluku != 0:
    print("On alkunumero")