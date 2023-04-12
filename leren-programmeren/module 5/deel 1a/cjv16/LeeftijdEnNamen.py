def NaamEnLeeftijd():
    namen = []
    leeftijd = []

    while True:
        VraagNaam = input ('vull een naam in. Typ (stop) als je wilt stoppen: ')
        if VraagNaam == 'stop':
            break
        VraagLeeftijd = input ('vull een leeftijd in. Typ (stop) als je wilt stoppen: ')
        if VraagLeeftijd == 'stop':
            break
        namen.append(VraagNaam)
        leeftijd.append(VraagLeeftijd)
    x = zip(namen, leeftijd)
    return x

for naam, leeftijd in NaamEnLeeftijd():
    print (f'{naam} is {leeftijd} jaar oud')