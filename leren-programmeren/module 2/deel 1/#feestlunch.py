#feestlunch
#begin van de bestelling
print('Hallo, typ uw besteling in')

#croissantjes
croissantjes = int(input('hoeveel croissantjes wilt u? : '))
crtotaal = croissantjes * 0.39

#stokbrooden
stokbrood = int(input('hoeveel stokbrood wilt u? : '))
stoktotaal = stokbrood * 2.78

#kortingsbonnen
aantal_kortingsbonnen = int(input('hoeveel kortings bonnen heeft uw? : '))
korting = int(input('hoeveel cent zijn ze waard? : '))
korting_total = aantal_kortingsbonnen * korting / 100

#totale prijs
totaal= stoktotaal + crtotaal - korting_total
print({totaal},'euro')