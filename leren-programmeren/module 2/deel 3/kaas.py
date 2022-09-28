geel = input('Is de kaas geel? y/n ')

if geel == 'y':
    gaten = input('Zitten er gaten in? y/n ')
    
    if gaten == "y":
        duur = input('Is de kaas belachelijk duur? y/n ')
        
        if duur == 'y':
            print('Emmenthaler')
        
        else:
            print('Leerdammer')

        
    if gaten == 'n':
        hardekaas = input('Is de kaas hard als steen? y/n ')
    
        if hardekaas == 'n':
            print('Goudse Kaas')
        else: 
            print('Parmigiano Reggiano')

if geel == 'n':
    schimmel = input('Heeft de kaas blauweschimmel? y/n ')
    if schimmel == 'y':
        korst = input('Heeft de kaas een korst? y/n ')
        
        if korst == 'y':
            print('Blue de Rochbaron')
        else:
            print("Foume d' Ambert")

    if schimmel == 'n':
        korst2 = input('Heeft de kaas een korst? y/n ')
                
        if korst2 == 'y':
            print('Camembert')   
        else:
            print('Mozzarella')