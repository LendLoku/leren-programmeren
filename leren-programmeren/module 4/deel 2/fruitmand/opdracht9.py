from fruitmand import fruitmand

for index in range (len(fruitmand)):
    if fruitmand [index] ['name'] == 'druif':
        fruitmand.pop(index)
        break

for color in range (len(fruitmand)):
    print (fruitmand[color]['color'])

kleuren = []
for fruit in fruitmand:
    if not fruit['color'] in kleuren:
        kleuren.append (fruit['color'])

print (kleuren)