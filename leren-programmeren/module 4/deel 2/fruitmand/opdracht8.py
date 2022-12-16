from fruitmand import fruitmand
fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 1500,
    'color' : 'lime',
    'round' : True
})
totaal_gewicht = 0
for fruit in fruitmand:
    totaal_gewicht = totaal_gewicht + fruit["weight"]
print(totaal_gewicht)