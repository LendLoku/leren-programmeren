grootte = input('Kies de grootte: small, medium, large ')
juisteaantalingevoerd = 'nee'
while juisteaantalingevoerd == 'nee':
    try:
        aantal = int(input("Hoeveel pizza's wilt u? "))
        juisteaantalingevoerd = 'ja' 
    except:
        print("Nee dat is niet de juiste eenheid. Voer een nummer in!")
if grootte in("s","small","Small","S"):
    prijs = 6.99
if grootte in("m","medium","Medium","M"):
    prijs = 8.99
if grootte in("l","large","Large","L"):
    prijs = 10.99

totaalprijs = aantal * prijs

print(f"""
    BON
    -------------------------------------
    {aantal} {grootte} pizza's       {aantal}x {prijs},- €
    
    -------------------------------------
    Totaal prijs:           {totaalprijs},- €
    """)