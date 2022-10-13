print ('Welkom soldaat')
print ('We hebben jou nodig om de baas van het andere leger uit te schakelen!')

naam_soldaat = input ('Wat is uw naam soldaat? ')
print (f'{naam_soldaat} je gaat nu de bunker in van het andere leger.')
richting1 = input ('welke kant kies je om verder te gaan aan de linker kant staan 3 soldaten te bewaken en aan de rechterkant staat 1 soldaat (links/rechts)')

if richting1 == 'links':
    print ('U bent helaas gesneuveld')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
    exit ()
elif richting1 == 'rechts':
    print ('U hebt de soldaat dood gemaakt hij laat ze wapen vallen')
    wapen = input ('Wil je zijn wapen (ak74) op pakken (ja/nee)')
    if wapen == 'ja':
        print (f'Goed gedaan {naam_soldaat} nu heb je een wapen om je zelf te beschermen!')
    else:
        print ('Jij bent echt dom zo win je nooit')
        exit ()

print ('Je komt nu op een kruising waar je naar links kan, recht en rechtdoor')
richting2 = input ('Je komt aan de linker kant 2 soldaten tegen, rechts kom je iets tegen wat je nooit hebt gezien en rechtdoor staat er iets op je te wachten (links/rechts/rechtdoor)')
if richting2 == 'links':
    print ('U bent helaas gesneuveld')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
    exit ()

if richting2 == 'rechtdoor':
        print ('Er stonden 200 soldaten klaar om het gevecht dat buiten bezig is in te gaan')
        print ('U bent helaas gesneuveld')
        print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
        exit ()
if richting2 == 'rechts':
            print ('Je ziet een kamer met een raam en door die raam zie je camerabeelden')
            print ('Je moet de sleutel vinden om de deur te openen')
            print ('Naast de kamer met alle toegang naar de cameras ')

kamer1 = input ('Welke kamer wil je als eerste bekijken (links/rechts)')

if kamer1 == 'links':
    print ('De rechter kamer is veilig ')
    print ('Je ziet aan de linker kant van de kamer een kast en aan de rechter kant van de kamer een bureau met laatjes')
kast = input ('welke kies je als eerst (kast/bureau)')
if kast == 'kast':
    print ('Er is hier niks te vinden alleen een paar leger spullen')
elif kast == 'bureau':
    print ('Hier ligt er ook niks in alleen een paar oude stoffige boeken over het oorlog')

    if kamer1 == 'rechts':
        print ('Hier staat een soldaat in deze ligt te slapen dus je moet zo stil mogelijk naar binnen lopen')
kill1 = input ('Je loopt er heel stil naar toe, wil je hem in zijn nek steken of met je ak47 schieten. (mes/ak47)')
if kill1 == 'ak47':
    print ('Dit was een domme zet je schiet dwars door zijn hoofd maar dat schot was zo luid dat er gelijk 100 soldaten naar je toe kwamen')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
    exit ()

elif kill1 == 'mes':
        print ('Goeie zet je hebt hem dwars door zijn nek gestoken zonder enige geluid')
        if kamer1:
            print ('Je ziet recht voor je tegen de muur een sleutelhanger liggen. Dat zijn de sleutels voor de kamer met de camerabeelden!')

camerakamer = print ('Je opent nu de deur')
print ('Je kan op de cameras 4 kamers zien en je ziet op een van de kamers de leider van de vijanden.')
print ('Maar je ziet ook dat je nog 4 kamers langs moet om bij hem te komen die zwaar bewaakt zijn.')
print ('Je zag dat links vrij is maar er is kans dat daar niks is, je kan rechts kiezen staan 4 soldaten maar skip je gelijk 1 kamer. of rechtdoor wat nog een verassing is')
richting3 = input ('Je kan kiezen tussen 3 richtingen rechtdoor, links of rechts. (links/rechtdoor/rechts)')

if richting3 == 'links':
    print ('Je loopt een hele eind door en gaat naar links. Maar aan het einde kom je in de slaapkamer van de soldaten waar 300 soldaten nu zijn.')
    print ('Je besluit dus om nu snel terug te rennen en een andere kant kiezen')
