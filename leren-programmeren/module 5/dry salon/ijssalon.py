from functions import *

nogEen = True

lst = [{'name': 'bolletje', 'aantal': 0, 'prijs': 1.10},
        {'name': 'hoorntje', 'aantal': 0, 'prijs': 1.25},
        {'name': 'bakje', 'aantal': 0, 'prijs': 0.75}]

smaakLstZakelijk = [{'name': 'l. aardbei', 'aantal': 0, 'prijs': 9.80, 'key': 'a'},
                     {'name': 'l. chocolade', 'aantal': 0, 'prijs': 9.80, 'key': 'b'},
                     {'name': 'l. munt', 'aantal': 0, 'prijs': 9.80, 'key': 'c'},
                     {'name': 'l. vanille', 'aantal': 0, 'prijs': 9.80, 'key': 'd'}]

smaakLstKlant = [{'name': 'b. aardbei', 'aantal': 0, 'prijs': 0.95, 'key': 'a'},
             {'name': 'b. chocolade', 'aantal': 0, 'prijs': 0.95, 'key': 'b'},
             {'name': 'b. vanille', 'aantal': 0, 'prijs': 0.95, 'key': 'c'}]

toppingLst = [{'name': 'geen', 'aantal': 0, 'prijs': 0, 'key': 'a'},
             {'name': 'slagroom', 'aantal': 0, 'prijs': 0.50, 'key': 'b'},
             {'name': 'sprinkels', 'aantal': 0, 'prijs': 0.30, 'key': 'c'},
             {'name': 'caramel saus', 'aantal': 0, 'prijs': 0, 'key': 'd'}]

smaakTekstZakelijk = f"Welke smaak wilt u? A) Aardbei, B) Chocolade, C) Munt of D) Vanille?\n "
smaakTekstKlant = f"Welke smaak wilt u voor uw bolletje? A) Aardbei, B) Chocolade, C) Munt of D) Vanille?\n "
toppingTekst = "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?\n "

# Hier begint de code

print("Welkom bij Papi Gelato.")
while True:
    particOfZakelijk = input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ")
    if particOfZakelijk in ("1", "2"):
        break
    else:
        print("Sorry dat is geen optie die we aanbieden...")

while nogEen:
    if particOfZakelijk == '1': # Particulier
        aantal = aantalBolletjesOfLiter(particOfZakelijk)

        keuze = bakjeOfHoorntje(aantal)

        smaakEnTopping(aantal, smaakLstKlant, smaakTekstKlant) # Smaak

        smaakEnTopping(aantal, toppingLst, toppingTekst) # Topping

        nogEen = meerBestellen()  

        # tempLst = bolletjesEnKeuzeBerekening(aantal, keuze, lst)

        bolletjesEnKeuzeBerekening(aantal, keuze, lst)
    elif particOfZakelijk == '2': # Zakelijk
        aantalLiter = aantalBolletjesOfLiter(particOfZakelijk)

        smaakEnTopping(aantalLiter, smaakLstZakelijk, smaakTekstZakelijk)
        nogEen = False

if particOfZakelijk == '1':
    bon(lst, smaakLstKlant, toppingLst, particOfZakelijk)
else:
    bon(lst, smaakLstZakelijk, toppingLst, particOfZakelijk)