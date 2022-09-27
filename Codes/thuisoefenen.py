from pickletools import float8
from random import choices

print('welkom bij GameShop')

game1 = 30
game2 = 20
game3 = 12, 50
game4 = 12, 50
game0 = 0

print('Wij hebben 4 games voor u die wij aan u willen voorstellen')
vraag1 = input('De 1e game is de nieuwe call of duty die iedereen wilt, wilt u deze in het winkelmandje ja/nee? : ')

if vraag1 == "ja":
   print(game1)
# elif vraag1 in ('nee'):
#     print(game0)

vraag2 = input(
    'De 2e game is een 3D game met autos waarin je tegen elkaar raced, wilt u deze in het winkelmandje ja/nee? : ')

if vraag2 in ('ja'):
    print(game2)
# elif game2 in ('nee'):
#     print(game0)

vraag3 = (input('De 3e game is mario in 2D een spel die vroeger veel gewilt was en veel gespeeld werd, wilt u deze in het winkelmandje ja/nee? : '))
if vraag3 in ('ja'):
    print(game3)
# elif game3 in ('nee'):
#     print(game0)

vraag4 = (input('De 4e game is snake een spel waarbij je steeds appels moet eten om grooter te worden tot je de max bereikt, wilt u deze in het winkelmandje ja/nee? : '))
if vraag4 in ('ja'):
    print(game4)
# elif game4 in ('nee'):
#     print(game0)


else: 
    print (game0)
totaal = (game1 + game2 + game3 + game4)
print(f'Het eind bedrag is ', {totaal})
