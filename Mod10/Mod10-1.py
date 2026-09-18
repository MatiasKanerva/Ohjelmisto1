class Hissi:
    def __init__(self, AlinKerros, YlinKeros):
        self.Alinkerros = AlinKerros
        self.YlinKerros = YlinKeros
        self.Kerros = 1

    def SiirryKerrokseen(self, Kutsu):
        self.Kutsu = Kutsu
        print(Kutsu, h.Kerros)

        if Kutsu > h.Kerros:
            self.KerrosYlös()

        if Kutsu < h.Kerros:
            h.KerrosAlas()

        else: print("Olet perillä")
        return

    def KerrosYlös(self):
        while h.Kerros < h.Kutsu:
            h.Kerros += 1
            print(f"Nousit kerroksen ylemmäs: {h.Kerros}")
        return
    
    def KerrosAlas(self):
        while h.Kerros > h.Kutsu:
            h.Kerros -= 1
            print(f"Laskit kerroksen alemmas: {h.Kerros}")
        return


h = Hissi(1,8)
h.SiirryKerrokseen(6)
h.SiirryKerrokseen(3)