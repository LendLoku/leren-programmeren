import random
namen = []
lootjes = {}
while True:
    naam = input("Wat zijn de namen van de spelers?  ").lower()
    if naam in namen:
        print("dit heeft u al gekozen")
    else:
        namen.append(naam)
    if len(namen) >= 3:
        vraag = input("wilt u nog een naam invoeren ? ")
        if vraag == "nee":
            break
shuffle = True
while shuffle:
    namen_shuffle = random.sample(namen, len(namen))
    shuffle = False
    for i in range(len(namen)):
        if namen_shuffle[i] == namen[i]:
            shuffle = True

for i in range(len(namen)):
    lootjes.update({namen[i]: namen_shuffle[i]})

print(lootjes) 