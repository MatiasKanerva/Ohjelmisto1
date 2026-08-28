Sukupuoli = input("Oletko mies vai nainen? ")
Hemo = int(input("Mikä on hemoglobaaniarvosi? "))

if Sukupuoli == "Mies":
    if 134 > Hemo < 195:
        print("Hemoglobaani arvo on sopiva")
    elif Hemo < 134:
        print("Hemoglobaani arvo on liian alhainen miehelle")

    else: print("Hemoglobaani arvo on liian korkea miehelle")

elif Sukupuoli == "Nainen":
    if 117 > Hemo <= 175:
        print("Hemoglobaani arvo on sopiva")
    elif Hemo < 117:
        print("Hemoglobaani arvo on liian alhainen naiselle")

    else: print("Hemoglobaani arvo on liian korkea naiselle")