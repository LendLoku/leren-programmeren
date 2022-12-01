import random

aantal_pogingen = 10
score = 0
poging = 0
while True:
    try:
        rondes = int( input("Voer in hoeveel rondes u wilt spelen (maximaal 20): "))
        if rondes <= 20 and rondes > 0:
            break
        else:
            print("Boven de 0 en onder de 20!")
    except:
        print("voer een geldig nummer in!")
print ('gok een getal tussen de 1 en 1000!')
while poging < aantal_pogingen:
    print(f"Ronde {poging}")
    geheimgetal = random.randint (0, 1000)
    aantal_gokken = 1
    while poging < aantal_pogingen:
        while True:
            try:
                gok = int(input(f'Voer hier je gok in (gok {aantal_gokken}): '))
            except:
                print ('Voer een geldig nummer in!')

            if gok == geheimgetal:
                print("goed geraden! Score + 1")
                score += 1 
                aantal_gokken += 10
                break
                
            if geheimgetal > gok:
                afstand = geheimgetal - gok
                print ('Het getal is hoger')
            elif geheimgetal < gok:
                afstand = gok - geheimgetal
                print ('Het getal is lager')

            if afstand < 50 and afstand > 20:
                print ('Je bent warm!')
            elif afstand < 20:
                print ('Je bent heel erg warm')
            aantal_gokken += 1
        print (f'Het getal was: {geheimgetal}')
        print (f'Dit was jou score: {score}')
        if rondes != poging:
            while True:
                nog_een_keer = input('Wilt u het spel nog een keer spelen? (ja of nee): ').lower()
                if nog_een_keer in ('ja', 'nee'):
                    break
            
            if nog_een_keer == 'nee':
                print (f'Uw eindscore is: {score}')
                print ('Dankuwel voor het spelen van dit spel')
                quit()
            poging += 1
print(f"Uw eindscore is: {score}")
print("Dankuwel voor het spelen van dit spel")  