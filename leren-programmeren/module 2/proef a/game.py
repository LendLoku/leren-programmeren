print ('Welkom soldaat')
print ('We hebben jou nodig om de baas van het andere leger uit te schakelen!\n')
naam_soldaat = input ('Wat is uw naam soldaat?\n')
print (f'{naam_soldaat} je gaat nu de bunker in van het andere leger.')
while True:
    richting1 = input ('welke kant kies je om verder te gaan aan de linker kant staan 3 soldaten te bewaken en aan de rechterkant staat 1 soldaat (links/rechts)\n')
    if richting1 in ['links','rechts']:
        break

if richting1 == 'links':
    print ('U bent helaas gesneuveld')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
    exit ()
elif richting1 == 'rechts':
    print ('U hebt de soldaat dood gemaakt hij laat ze wapen vallen')

    while True:
        wapen = input ('Wil je zijn wapen (ak74) op pakken (ja/nee) \n')
        if wapen in ['ja','nee']:
            break
    if wapen == 'ja':
        print (f'Goed gedaan {naam_soldaat} nu heb je een wapen om je zelf te beschermen!')

    else:
        print ('Jij bent echt dom zo win je nooit')
        exit ()

print ('Je komt nu op een kruising waar je naar links kan, recht en rechtdoor')
while True:
    richting2 = input ('Je komt aan de linker kant 2 soldaten tegen, rechts kom je iets tegen wat je nooit hebt gezien en rechtdoor staat er iets op je te wachten (links/rechts/rechtdoor) \n')
    if richting2 in ['links','rechts', 'rechtdoor']:
        break
if richting2 == 'links':
    print ('U bent helaas gesneuveld')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven. \n') 
    exit ()

if richting2 == 'rechtdoor':
        print ('Er stonden 200 soldaten klaar om het gevecht dat buiten bezig is in te gaan')
        print ('U bent helaas gesneuveld')
        print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
        exit ()
if richting2 == 'rechts':
            print ('Je ziet een kamer met een raam en door die raam zie je camerabeelden')
            print ('Je moet de sleutel vinden om de deur te openen')
            print ('Naast de kamer met alle toegang naar de cameras \n')

kamer1 = input ('Welke kamer wil je als eerste bekijken, in de linker kamer staan 10 soldaten te bewaken en rechts kan je niet goed zien want het is heel donker. (links/rechts)\n')


if kamer1 == 'links':
         print ('Die 10 soldaten hebben je vol door je hoofd heen geschoten ze hoorde je voet stappen.')
         print ('U bent helaas gesneuveld')
         print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
         exit ()

if kamer1 == 'rechts':
        print ('Je bent nu in het rechter kamer') 
        print ('Hier staat een soldaat, deze soldaat ligt te slapen dus je moet zo stil mogelijk naar binnen lopen')
kill1 = input ('Je loopt er heel stil naar toe, wil je hem in zijn nek steken of met je ak47 schieten. (mes/ak47)\n')

if kill1 == 'ak47':
    print ('Dit was een domme zet je schiet dwars door zijn hoofd maar dat schot was zo luid dat er gelijk 100 soldaten naar je toe kwamen')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.\n') 
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
            print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.\n') 
        exit ()
    break
richting4 = input ('Kies je rechtdoor of rechts')

if richting3 == 'rechtdoor' or richting4 == 'rechtdoor':
    print ('Je loopt rechtdoor het word helemaal donker in de lange gang waar je nu in loopt en je hebt geen zaklamp of iets dat licht geeft')
    print ('Je ziet licht aan het einde en rent er snel naar toe')
    print ('Je bent er eindelijk en is het een van de 400 leger autos die aan staan waar 400 soldaten in staan')
    print ('Je word nu vol door je hoofd heen geschoten door de bewakers die daar staan')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.\n') 
    exit ()
elif richting3 == 'rechts' or richting4 == 'rechtdoor':
    print ('Je schiet de 4 soldaten neer en je werd in je been geraakt.')
    print ('Je loopt nu mank maar je komt de leider tegen die je dood wou hebben')
    print ('Je hebt de leider dood geschoten waardoor de tegenstanders zich moeten overgeven aan jou land.')
    print ('Je bloed nu langzaam dood maar hebt wel de leider dood')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
    exit ()