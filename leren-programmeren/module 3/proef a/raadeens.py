import random
DICHTBIJ_HET_GETAL = 50
HEEL_DICHT_BIJ_GETAL = 20
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
    raadGetal = random.randint(1, 1000) 

    poging = 0
    while poging < AANTALPOGINGEN:
        while True:
            try:
                antwoord = int(input('raad het getal: '))
                break
            except ValueError: 
                print('Voer een getal in')

        if raadGetal == antwoord:
            print('je hebt het getal goed geraden!')
            score+=1
            break
        else:      
            verschil = abs(antwoord - raadGetal)
            if verschil <= HEEL_DICHT_BIJ_GETAL:
                print("Je bent heel dichtbij!")
            elif verschil <= DICHTBIJ_HET_GETAL and verschil >= HEEL_DICHT_BIJ_GETAL:
                print("Je bent dichtbij!")

            if antwoord > raadGetal:
                print('gok lager')
            elif antwoord < raadGetal:
                print('gok hoger!')
        poging += 1

    print(f"jou eind score is {score} ")

print(f"Jou eind score is {score} van de {AANTALRONDES} punten!")