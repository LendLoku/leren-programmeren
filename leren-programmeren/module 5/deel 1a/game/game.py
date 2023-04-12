from gamefunction import *
print ('Welkom soldaat')
print ('We hebben jou nodig om de baas van het andere leger uit te schakelen!\n')
naam_soldaat = naam()
print ('je gaat nu de bunker in van het andere leger.')
while True:
    richting1 = input ('welke kant kies je om verder te gaan aan de linker kant staan 3 soldaten te bewaken en aan de rechterkant staat 1 soldaat (links/rechts)\n')
    if richting1 in ['links','rechts']:
        break

if richting1 == dead():
    exit()
elif richting1 == 'rechts':
    print ('U hebt de soldaat dood gemaakt hij laat ze wapen vallen')

    while True:
        wapen = input ('Wil je zijn wapen (ak74) op pakken (ja/nee) \n')
        if wapen in ['ja','nee']:
            break
    if wapen == 'ja':
        print (f'Goed gedaan nu heb je een wapen om je zelf te beschermen!')

    else:
        dead()
        exit ()

print ('Je komt nu op een kruising waar je naar links kan, recht en rechtdoor')
while True:
    richting2 = input ('Je komt aan de linker kant 2 soldaten tegen, rechts kom je iets tegen wat je nooit hebt gezien en rechtdoor staat er iets op je te wachten (links/rechts/rechtdoor) \n')
    if richting2 in ['links','rechts', 'rechtdoor']:
        break
if richting2 == left():
     exit()

if richting2 == rechtdoor():
        exit ()
if richting2 == 'rechts':
            print ('Je ziet een kamer met een raam en door die raam zie je camerabeelden')
            print ('Je moet de sleutel vinden om de deur te openen')
            print ('Naast de kamer met alle toegang naar de cameras \n')

kamer1 = input ('Welke kamer wil je als eerste bekijken, in de linker kamer staan 10 soldaten te bewaken en rechts kan je niet goed zien want het is heel donker. (links/rechts)\n')

if kamer1 == left():
     exit()

if kamer1 == 'rechts':
        print ('Je bent nu in het rechter kamer') 
        print ('Hier staat een soldaat, deze soldaat ligt te slapen dus je moet zo stil mogelijk naar binnen lopen')
kill1 = input ('Je loopt er heel stil naar toe, wil je hem in zijn nek steken of met je ak47 schieten. (mes/ak47)\n')

if kill1 == ak47():
    exit ()

elif kill1 == 'mes':
        print ('Goeie zet je hebt hem dwars door zijn nek gestoken zonder enige geluid\n')
        if kamer1:
            print ('Je ziet recht voor je tegen de muur een sleutelhanger liggen. Dat zijn de sleutels voor de kamer met de camerabeelden!\n')

camerakamer = print ('Je opent nu de deur')
print ('Je kan op de cameras 4 kamers zien en je ziet op een van de kamers de leider van de vijanden.')
print ('Maar je ziet ook dat je nog 4 kamers langs moet om bij hem te komen die zwaar bewaakt zijn.')
print ('Je zag dat links vrij is maar er is kans dat daar niks is, je kan rechts kiezen staan 4 soldaten maar skip je gelijk 1 kamer. of rechtdoor wat nog een verassing is\n')
richting3 = input ('Je kan kiezen tussen 3 richtingen rechtdoor, links of rechts. (links/rechtdoor/rechts)\n')
while True:
    if richting3 == 'links':    
        print ('Je loopt een hele eind door en gaat naar links. Maar aan het einde kom je in de slaapkamer van de soldaten waar 300 soldaten nu zijn.')
        print ('Je besluit dus om nu snel terug te rennen en een andere kant kiezen')
        terug = input ('Wil je terug rennen (ja/nee)')
        if terug == 'nee':
            print ('Maar een van de 300 soldaten zag jou en rent nu achter jou aan met 60 man en schieten jou dood')
        dead()
        exit ()
    break
richting4 = input ('Kies je rechtdoor of rechts')

if richting3 == 'rechtdoor' or richting4 == 'rechtdoor':
    VoorHetEinde()
    exit ()
elif richting3 == 'rechts' or richting4 == 'rechtdoor':
    einde()
    exit ()