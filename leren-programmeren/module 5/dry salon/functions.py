def aantalBolletjesOfLiter(particOfZakelijk):
    while True:
        try:
            if particOfZakelijk == '1':
                aantal = int(input("Hoeveel bolletjes wilt u? "))
                if aantal > 8:
                    print("Sorry, zulke grote bakken hebben we niet ")
                else:
                    return aantal
            elif particOfZakelijk == '2':
                aantalLiter = int(input("Hoeveel liter ijs wilt u? "))
                return aantalLiter
        except:
            print("Sorry dat is geen optie die we aanbieden...")

def bakjeOfHoorntje(aantal):
    keuzeBoolean = True
    if aantal >= 1 and aantal <= 3:
        while keuzeBoolean:
            keuze = input(f"Wil u deze {aantal} bolletje(s) in een hoorntje of een bakje? ").lower()
            if keuze in ("hoorntje", "bakje"):
                keuzeBoolean = False
            else:
                print("Sorry dat is geen optie die we aanbieden...")
    elif aantal >= 4 and aantal <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes ")
        keuze = "bakje"

    
    return keuze

def smaakEnTopping(aantal, lst, tekst):
    keuzeBoolean = True
    
    for index in range(aantal):
        while keuzeBoolean:
            keuze = input(tekst).lower()
            if keuze == 'a':
                keuze = lst[0]['name']
                keuzeBoolean = False
            elif keuze == 'b':
                keuze = lst[1]['name']
                keuzeBoolean = False
            elif keuze == 'c':
                keuze = lst[2]['name']
                keuzeBoolean = False
            elif keuze == 'd':
                keuze = lst[3]['name']
                keuzeBoolean = False
            else:
                print("Sorry dat is geen optie die we aanbieden...")

            for item in lst:
                if keuze == item['name']:
                    item['aantal'] += 1
            
        keuzeBoolean = True
    return lst
        

def meerBestellen():
    while True:
        meer = input("Wilt u nog meer bestellen? ")
        if meer == "y":
            return True
        elif meer == "n":
            return False
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def bolletjesEnKeuzeBerekening(aantal, keuze, lst):
    lst[0]['aantal'] += aantal

    for item in lst:
        if keuze == item['name']:
            item['aantal'] += 1

    return lst

def bon(lst, smaakLst, toppings, particOfZakelijk):
    BTW = 0.06
    totaalPrijs = 0
    totaalPrijsToppings = 0
    lst.extend(smaakLst)

    print('--------["Papi Gelato"]--------')
    for index in lst[1:]:
        if index['aantal']:
            print(f"{index['name']} {index['aantal']} x € {'%.2f' % (index['prijs'])} = € {'%.2f' % (index['aantal'] * index['prijs'])}")
        totaalPrijs += index['aantal'] * index['prijs']

    if lst[2]['aantal'] > 0:
        toppings[3]['prijs'] = 0.9
    elif lst[3]['aantal'] > 0:
        toppings[3]['prijs'] = 0.6
    
    for item in toppings:
        totaalPrijsToppings += item['aantal'] * item['prijs']   

    totaalPrijs += totaalPrijsToppings

    btw = BTW * totaalPrijs
    
    if totaalPrijsToppings:
        print(f"toppings              € {'%.2f' % totaalPrijsToppings}\n")
    print("-------------------------------")
    print(f"totaal                 € {'%.2f' % totaalPrijs}")
    if particOfZakelijk == "2":
        print(f"btw ({BTW}%)               € {'%.2f' % btw}")
    print("Bedankt en tot ziens! ")