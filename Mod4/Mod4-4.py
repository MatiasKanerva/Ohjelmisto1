Vuosi = int(input("Anna vuosi: "))

Karkavuosi = Vuosi // int(4)

if Karkavuosi != Vuosi / 4:
    print(f"Vuosi {Vuosi} ei ole karkausvuosi")

else: print(f"Vuosi {Vuosi} on kaurkaus vuosi")