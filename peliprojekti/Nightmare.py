import random
import Save

def Painajainen(Pelaaja):
    # Lore dump ja minipelin säännöt, amazing writing 10/10, +1 piste projektiin!
    print("You wake up in a nightmare, you look around your surroundings, standing in the middle of a long and dark hallway\n"
          "You hear a low growl and heavy footsteps coming from behind\n"
          "Instinctivly you start running the opposite direction where you see a glowing white door\n"
          "Throwing the dice you move forward with various speeds while the Monster is after you.\n" 
          "1 Stumble\n"
          "2,3,4 Walk\n"
          "5,6 Run")
    PelaajanMatka = 0
    Nopeus = 0
    # Pelaajalla on 5 vuoroa ennen kuin hirviö saa kiinni
    HirvionMatka = 5

    Vuoro = input("Throw a dice: ")
    while Vuoro == "" or Vuoro != "":
        Noppa = random.randint(1,6)
        if Noppa == 1:
            Nopeus = 1
            Pelaaja.Järki -= 15
            print(f"\nYou threw: {Noppa}\nYou stumbled slowly forward...\nYou lost 15 sanity\nSanity: {Pelaaja.Järki}")
        elif 1 < Noppa < 5:
            Nopeus = 2
            Pelaaja.Järki -= 10
            print(f"\nYou threw: {Noppa}\nYou walk forward in a quick pace\nYou lost 10 sanity\nSanity: {Pelaaja.Järki}")
        elif 4 < Noppa:
            Nopeus = 4
            Pelaaja.Järki -= 5
            print(f"\nYou threw: {Noppa}\nYou ran forward as fast as you could!\nYou lost 5 sanity\nSanity: {Pelaaja.Järki}")
        HirvionMatka -= 1
        PelaajanMatka = PelaajanMatka + Nopeus

        if PelaajanMatka >= 13:
            print("\nYou managed to escape the nightmare, you're awake in your room\n")
            return

        # Tätä lopetusta voi tietenkin muuttaa jos olisi enemmän aikaa ja olisi toisia minipelejä kun menee nukkumaan.
        if HirvionMatka < 1:
            print("-" * 30)
            print("\nNightmare Ending: The Monster cought up to you, you weren't fast enough...\n")
            print("-" * 30)
            Save.Save(Pelaaja)
            break
        Vuoro = input("Throw the dice again to proceed\n")