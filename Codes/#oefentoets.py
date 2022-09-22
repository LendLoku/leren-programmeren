#oefentoets
iphone = int (input ('hoe duur is de Iphone 13 in euros? : '))
samsung = int (input ('hoe duur is de Samsung Galaxy 22 in euros? : '))   

max1 = iphone - samsung
max2 = samsung - iphone 


if (iphone > 900 and samsung > 900 ):
    print ('Het advies is dus  geen telefoon te kopen, ze zijn te duur.')
    exit()

if max1 > 50:
    print (f'''de iphone is duurder dan de samsung
de iphone kost €{iphone}
de goedkoopste is de samsung die kost €{samsung}
het advies is dus om de samsung te kopen. Deze is namelijk {max1} euro goedkoper dan de iphone''')

elif max2 < 50:
    print (f'''de iphone is duurder dan de samsung
de iphone kost €{iphone}
de goedkoopste is de samsung die kost €{samsung}
het advies is dus om de iphone te kopen. Deze is namelijk {max1} euro goedkoper dan de iphone''')

elif samsung > iphone: 
    print (f'''de samsung is duurder dan de iphone    
de samsung is het duurst de telefoon kost €{samsung}
de goedkoopste is de iphone die kost €{iphone}
het advies is dus om de iphone te kopen. Deze is namelijk {max2} euro goedkoper dan de samsung''')


elif samsung == iphone:
     input ('de telefoons zijn even duur dus het maakt niet uit welke u wilt kiezen')   

