import random

Summa = 0
List = []

for X in range(3):
    Noppa = random.randint(1,10)
    Summa = Summa + Noppa
    List.append(Noppa)

print(f"Noppien kolmen arvo ovat {List} ja summa yhteensä on {Summa}")