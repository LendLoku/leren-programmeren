import numbers
from token import NUMBER
from tokenize import Number

grootte = input('Kies de grootte: small, medium, large ')
var = 0
while var == 0:
    try:
        aantal = int(input("Hoeveel pizza's wilt u? "))
        var += 1 
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