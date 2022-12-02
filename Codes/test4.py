import random

AANTALRONDES = 20
AANTALPOGINGEN = 10
ronde = 0
score = 0
poging = 0
while ronde < AANTALRONDES:
    ronde+=1
    while True:
        meeDoen = input("zou je een getal tussen 1 en 1000 willen raden? ja/nee  ").lower()
        if meeDoen in ['ja','nee']:
            break
        else:
            print('vul ja of nee in')

    if meeDoen == "nee":
        print("einde")
        break
    print(f'dit is ronde: {ronde}')
    raadGetal = random.randint(1, 1000) #randint staat voor een random int getal.
    print(raadGetal)

    poging=0

    while poging < AANTALPOGINGEN:
        while True:
            try:
                antwoord = int(input('raad het getal: '))
                break
            except ValueError: #dit betekent dat als je iets andres dan een getal invoert moet je dan iets opnieuwe in vullen
                print('je mag alleen cijfers')

        if raadGetal == antwoord:
            print('je hebt het getal goed geraden!')
            score+=1
            break
        else:      #De absolute waarde houdt zich bezig met de waarde of omvang van een getal in plaats van het teken dat aan het getal is gekoppeld
            verschil = abs(antwoord - raadGetal)
            if verschil <= 20:  # berekent hier of het heel dichtbij is of dichtbij
                print("Je bent heel dichtbij!")
            elif verschil <= 50 and verschil >= 20:
                print("Je bent dichtbij!")

            if antwoord > raadGetal:
                print('gok lager')
            elif antwoord < raadGetal:
                print('gok hoger!')
        poging += 1

    print(f"jou eind score is{score} ")

print(f"Jou eind score is {score} van de {AANTALRONDES} punten!")