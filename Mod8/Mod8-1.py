
Kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
Vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy", "Talvi")
Luku = int(input("Kerro kuukauden numero: "))
Vuosi = Luku / 3
print(Kuukaudet[Luku - 1])
print(Vuodenajat[int(Vuosi)])