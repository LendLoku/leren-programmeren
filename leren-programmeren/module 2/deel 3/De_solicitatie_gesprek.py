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

#Punten tellen 
punten = 0

if mbo4_diploma == 'ja':
    punten += 1

if rijbewijs == 'ja':
    punten += 1

if hoed == 'ja':
    punten += 1

if geslacht == 'man':
    if snor > 'ja':
        punten += 1
        if snor2 > 10 :
            punten += 1 

if geslacht == 'vrouw':
    punten += 1
    if haar == 'ja':
        punten += 1
        if haar2 > 20:
            punten +=1 

if lengte > 150 or lengte < 220:
    punten += 1

if gewicht > 90 or gewicht < 120:
    punten += 1

if certificaat == 'ja':
    punten += 1

if dieren_dresuur2 > 4:
    punten += 1

if jongleren2 > 5:
    punten += 1

if acrobatiek2 > 3:
    punten += 1

eindresultaat_positief = punten > 9
eindresultaat_negatief = punten < 9 

if eindresultaat_positief:
    print ('U bent aan genomen voor de solicitatie gesprek!')
if eindresultaat_negatief:
    print ('U bent helaas niet aangenomen voor de solicitatie gesprek.')