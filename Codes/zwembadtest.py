lengte = float(input('lengte? '))
breedte = float (input('breedt? '))
hoogte = float (input('hoogte? '))

m3 = lengte * breedte * hoogte 
KostenPerM3 = 32.50 * m3 
KostenUitgraven = 25 * m3 
totaalkosten = KostenPerM3 + KostenUitgraven

print (f'Uitgraven:          €{KostenUitgraven}')
print (f'Afvoeren grond:     €{KostenPerM3}')
print (f'Totaal:             €{totaalkosten}')