import math

LeiviskäKPL, NaulaKPL, LuodiKPL = input(" Kerro kuinka monta Leiveskää, Nauloja ja Luoteja sinulla on: ").split()
LeiviskäKPL, NaulaKPL, LuodiKPL = float(LeiviskäKPL), float(NaulaKPL), float(LuodiKPL)  

LuotiMassa = 13.3
NaulaMassa = LuotiMassa * 32
LeiviskäMassa = NaulaMassa * 20

LuoditG = LuotiMassa * LuodiKPL
NaulatG = NaulaMassa * NaulaKPL
LeiviskäG = LeiviskäMassa * LeiviskäKPL

Yhteensä = LuoditG + NaulatG + LeiviskäG
Gramma = round(Yhteensä % 1000,2)
Kilo = Yhteensä // 1000
print("Massa nykymittojen mukaan:\n", Kilo, " Kilogrammaa ja ", Gramma, " grammaa.")