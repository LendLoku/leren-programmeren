import random
kleuren = ['oranje', 'blauw', 'groen', 'bruin']
Hoeveel_mms = int(input('hoeveel m&ms wilt u in het zakje?: '))
zakje = []

for x in range (Hoeveel_mms):
    zakje += random.choices (kleuren)

print (zakje)