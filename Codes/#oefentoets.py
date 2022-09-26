#oefentoets
iphone = int (input ('hoe duur is de Iphone 13 in euros? : '))
samsung = int (input ('hoe duur is de Samsung Galaxy 22 in euros? : '))   


if (iphone > 900 and samsung > 900 ):
    print ('Het advies is dus  geen telefoon te kopen, ze zijn te duur.')
    exit()

if (iphone - samsung) > 50:
    print (f'''de iphone is meer dan €50 duurder dan de samsung
de iphone kost €{iphone}
de goedkoopste is de samsung die kost €{samsung}
het advies is dus om de samsung te kopen. Deze is namelijk {iphone - samsung} euro goedkoper dan de iphone''')

elif (iphone > samsung):
    print (f'''de iphone is duurder dan de samsung
de iphone kost €{iphone}
de goedkoopste is de samsung die kost €{samsung}
het advies is dus om de iphone te kopen. Het verschil is namelijk €{iphone - samsung} met de samsung''')

elif samsung > iphone: 
    print (f'''de samsung is duurder dan de iphone    
de samsung is het duurst de telefoon kost €{samsung}
de goedkoopste is de iphone die kost €{iphone}
het advies is dus om de iphone te kopen. Deze is namelijk {samsung - iphone} euro goedkoper dan de samsung''')


elif samsung == iphone:
     input ('de telefoons zijn even duur dus het advies is om de iphone te kiezen')