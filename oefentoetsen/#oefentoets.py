#oefentoets

iphone = input ('hoe duur is de Iphone 13 in euros? : ')
iphone = int (iphone)

samsung = input ('hoe duur is de Samsung Galaxy 22 in euros? : ')
samsung = int (samsung)

evenduur = samsung == iphone
iphoneduurder = iphone > samsung 
samsungduurder = samsung > iphone 

if iphoneduurder:
    input (f'''de iphone is duurder dan de samsung 
de iphone kost €{iphone}
de goedkoopste is de samsung die kost €{samsung}
het advies is dus om de samsung te kopen. Deze is namelijk {iphone - samsung} euro goedkoper dan de iphone''')

if samsungduurder:
    input (f'''de samsung is duurder dan de iphone
de samsung is het duurst de telefoon kost €{samsung}
de goedkoopste is de iphone die kost €{iphone}
het advies is dus om de iphone te kopen. Deze is namelijk {samsung - iphone} euro goedkoper dan de samsung''')

elif evenduur: 
    input ('de telefoons zijn even duur dus het maakt niet uit welke u wilt kiezen')   