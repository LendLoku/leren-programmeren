from gamefunction import *
from tekst import *
print ('Welkom soldaat')
print ('We hebben jou nodig om de baas van het andere leger uit te schakelen!\n')
naam_soldaat = naam()
print (f'{naam_soldaat} je gaat nu de bunker in van het andere leger.')

richting1 = vraag_richting1()

if richting1 == 'links':
    Beindigt_spel(naam_soldaat)
elif richting1 == 'rechts':
    print ('U hebt de soldaat dood gemaakt hij laat ze wapen vallen')

wapen = vraag_wapen()
if wapen == 'ja':
    print (f'Goed gedaan {naam_soldaat} nu heb je een wapen om je zelf te beschermen!')

else:
    Beindigt_spel(naam_soldaat)

print ('Je komt nu op een kruising waar je naar links kan, recht en rechtdoor')
richting2 = vraag_richting2()
if richting2 == 'links':
     Beindigt_spel(naam_soldaat)
if richting2 == 'rechtdoor':
     Beindigt_spel(naam_soldaat)
if richting2 == 'rechts':
     print = richting2_rechts

kamer1 = input ('Welke kamer wil je als eerste bekijken, in de linker kamer staan 10 soldaten te bewaken en rechts kan je niet goed zien want het is heel donker. (links/rechts)\n')

if kamer1 == 'links':
         Beindigt_spel(naam_soldaat)

if kamer1 == 'rechts': print (kamer1_tekst)
kill1 = input ('Je loopt er heel stil naar toe, wil je hem in zijn nek steken of met je ak47 schieten. (mes/ak47)\n')

if kill1 == 'ak47':
    Beindigt_spel(naam_soldaat)

elif kill1 == 'mes':
        print ('Goeie zet je hebt hem dwars door zijn nek gestoken zonder enige geluid\n')
        if kamer1:
            print ('Je ziet recht voor je tegen de muur een sleutelhanger liggen. Dat zijn de sleutels voor de kamer met de camerabeelden!\n')

camerakamer = print(camera_kamer_tekst)

richting3 = vraag_richting3()

richting4 = input ('Kies je rechtdoor of rechts')

if richting3 == 'rechtdoor' or richting4 == 'rechtdoor':
    print (VoorHeteinde)
elif richting3 == 'rechts' or richting4 == 'rechtdoor':
    print (einde)
