#De vragen
mbo4_diploma = input ('Bent u bezit van een mbo 4 diploma? (ja/nee) ')
rijbewijs = input ('Bent u in bezit van een geldig vrachtwagen rijbewijs (ja/nee) ')
hoed = input ('Bent u in bezit van een hoge hoed (ja/nee) ')
geslacht = input ('Bent u een man of een vrouw? (vrouw/man) ')
if geslacht == 'man':
    snor = input ('heeft u een snor? (ja/nee) ')
    if snor == 'ja':
       snor2 = int (input ('Hoe lang is uw snor? (IN CM) '))
if geslacht == 'vrouw':
    haar = input ('is uw haar lang en rood krullend? (ja/nee) ')
    haar == 'ja'
    haar2 = int (input ('Hoelang is uw haar? (IN CM) '))
lengte = int (input ('Hoelang bent u? (IN CM) '))
gewicht = int (input('Hoe zwaar bent u? (IN KG) '))
certificaat = input ('Bent u in bezit van een Certificaat “Overleven met gevaarlijk personeel “? (ja/nee) ')
dieren_dresuur = input ('Heeft u praktijkervaring met dieren-dressuur? (ja/nee) ')
if dieren_dresuur == 'ja':
   dieren_dresuur2 = int (input ('Hoeveel jaar ervaring heeft u dan met dieren-dressuur? '))
jongleren = input ('Heeft u ervaring met jongleren? (ja/nee) ')
if jongleren == 'ja':
    jongleren2 = int (input ('Hoeveel jaar ervaring heeft u met jongleren? '))
acrobatiek = input ('Heeft u praktijkervaring met acrobatiek? (ja/nee) ')
if acrobatiek == 'ja':
    acrobatiek2 = int (input ('Hoeveel jaar ervaring heeft u met acrobatiek? '))

if mbo4_diploma == 'ja' and rijbewijs == 'ja' and hoed == 'ja' and (geslacht == 'man' and snor2 > 9) or (geslacht == 'vrouw' and haar2 > 19) and lengte >149 and (gewicht > 90 or gewicht) < 120 and certificaat == 'ja' and dieren_dresuur == 'ja' and dieren_dresuur2 >= 4 and jongleren == 'ja' and jongleren2 >= 5 and acrobatiek == 'ja' and acrobatiek2 >= 3:
    print ('U bent aangenomen voor de solicitatie gesprek!')
else:
    print ('U voldoet niet aan de eisen.') 