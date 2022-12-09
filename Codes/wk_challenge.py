wedstrijd_gewonnnen = 3
wedstrijd_verloren = 0
puntenTotaal1 = 0
puntenTotaal2 = 0
puntenTotaal3 = 0
land1 = input ('welke land speelt eerst in groep A? ')
land2 = input ('welke land speelt als tweede in groep A? ')
land3 = input ('welke land speelt als derde in groep A? ')
groepA = [land1,land2,land3]
print (f'''
wedstrijden     thuis       uit         Doelpunten1         Doelpunten2         winnaar
1               {land1}     {land2}
2               {land2}     {land3}
3               {land1}     {land3}''')


doelsaldo1 = int(input(f'hoeveel doelpunten heeft {land1} gemaakt? '))
doelsaldo2 = int(input(f'hoeveel doelpunten heeft {land2} gemaakt? '))
if doelsaldo1 > doelsaldo2:
    print(f'de winnaar is {land1}')
    puntenTotaal1 += wedstrijd_gewonnnen
elif doelsaldo1 < doelsaldo2:
    print(f'de winnaar is {land2}')
    puntenTotaal2 += wedstrijd_verloren
print(f''' 
Land        Doelsaldo       Puntentotaal
{land1}         {doelsaldo1}                        {puntenTotaal1}
{land2}         {doelsaldo2}                        {puntenTotaal2}
{land3}
''')
