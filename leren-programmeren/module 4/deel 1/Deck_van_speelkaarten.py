import random
deck = []
kleuren = ("harten", "klaveren", "schoppen", "ruiten")
nummers_en_personages = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")

for kleur in kleuren(0, 4):
    for soort in nummers_en_personages(0, 13):
        deck.append(kleur + " " + soort)

deck.append("joker")
deck.append("joker")
random.shuffle(deck)
print (deck)
for inhoudsopgave in range(7):
    print(f"kaart {inhoudsopgave+1}: ", deck[0])
    deck.pop (0)

print (deck)